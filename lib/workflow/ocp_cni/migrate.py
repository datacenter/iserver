import os
import json
import copy
import time
import yaml
from lib.k8s import output as k8s_output
from lib import file_helper
from lib import filter_helper
from lib import ip_helper
from lib import output_helper
from lib.workflow.ocp_cni import common as local_common
from lib.workflow import ocp_common as global_common
from lib.workflow.ocp_cilium_cli import install as cli_install
from lib.workflow.ocp_node import reload
from menu.common import get_confirmation


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'cidr' not in params:
        return None, 'Target cilium cni cluster network cidr required'

    if not ip_helper.is_valid_ipv4_cidr(params['cidr']):
        return None, 'Invalid cluster network cidr'
    
    if 'host_prefix' not in params:
        return None, 'Target cilium cni host prefix length required'

    if not isinstance(params['host_prefix'], int):
        return None, 'host_prefix param must be int'

    if params['host_prefix'] < 16 or params['host_prefix'] > 26:
        return None, 'host_prefix invalid'
    
    if int(params['cidr'].split('/')[1]) >= params['host_prefix']:
        return None, 'Host prefix invalid for cidr network'

    if 'manifest' not in params:
        return None, 'Manifest directory required'

    if not os.path.isdir(params['manifest']):
        return None, 'Manifest directory does not exist'
    
    if not os.path.isabs(params['manifest']):
        return None, 'Manifest directory must be absolute (not relative)'

    manifests = file_helper.get_files_text(params['manifest'])
    if get_cilium_config_filename(manifests) is None:
        return None, 'Does not look like cilium manifests'
    
    if get_cilium_manifests_type(manifests) != 'clife':
        return None, 'Migration restricted to Cilium EE with clife manifests'

    supported_kinds = [
        'CustomResourceDefinition',
        'Deployment',
        'CiliumConfig',
        'OperatorGroup',
        'ClusterRoleBinding',
        'ClusterRole',
        'RoleBinding',
        'Role',
        'Subscription',
        'Namespace',
        'ServiceAccount',
        'Service'
    ]

    for key in manifests:
        body = yaml.safe_load(manifests[key])
        if body['kind'] not in supported_kinds:
            return None, 'Unsupported manifest file: %s' % (key)

    if 'start' not in params:
        params['start'] = 1

    if not isinstance(params['start'], int):
        return None, 'start param must be int'

    if params['start'] < 1:
        return None, 'start must be ge 1'

    if 'stop' not in params:
        params['stop'] = 10

    if not isinstance(params['stop'], int):
        return None, 'stop param must be int'

    if params['stop'] < 1:
        return None, 'step must be ge 1'

    if params['stop'] < params['start']:
        return None, 'stop must be gt start'

    if 'reload' not in params:
        params['reload'] = False

    if not isinstance(params['reload'], bool):
        return None, 'reboot param must be true or false'
    
    if 'confirmation' not in params:
        params['confirmation'] = False

    if not isinstance(params['confirmation'], bool):
        return None, 'confirmation param must be true or false'
    
    if 'check-verbose' not in params:
        params['check-verbose'] = True

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'
    
    allowed_keys = [
        'cluster',
        'cidr',
        'host_prefix',
        'manifest',
        'start',
        'stop',
        'reload',
        'confirmation',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def get_cilium_config_filename(manifests):
    for key in manifests:
        content = yaml.safe_load(manifests[key])
        if content is not None:
            if 'kind' in content:
                if content['kind'] == 'CiliumConfig':
                    return key
    return None


def get_cilium_config(manifests):
    for key in manifests:
        content = yaml.safe_load(manifests[key])
        if content is not None:
            if 'kind' in content:
                if content['kind'] == 'CiliumConfig':
                    return content
    return None


def get_cilium_manifests_type(manifests):
    cilium_config = get_cilium_config(manifests)
    if cilium_config is None:
        return None

    label = filter_helper.get_attr(
        cilium_config, 'metadata:labels:app.kubernetes.io/name'
    )
    if label is not None and label == 'clife':
        return 'clife'

    return 'olm'


def check_cluster_before(params, my_output):
    my_output.default('Collect Cluster Operators', before_newline=True, underline=True)
    before_cluster_operators = params['k8s_handler'].get_cluster_operators(cache_enabled=False)
    if before_cluster_operators is None:
        my_output.error('rest api failed')
        return False
    
    for cluster_operator in before_cluster_operators:
        my_output.default('- %s [%s]' % (cluster_operator['name'], cluster_operator['available']))
        if not cluster_operator['available']:
            my_output.error('All cluster operators must be available before migration')
            return False
        
    return True


def disable_network_operator_management(params, my_output):
    success = params['k8s_handler'].disable_network_operator_management(
        confirmation=params['confirmation'],
        my_output=my_output
    )
    if not success:
        return False
    return True


def scale_down_network_operator(params, my_output, k8s_output_handler):
    my_output.default('Network Operator', underline=True, before_newline=True)
    deployment = params['k8s_handler'].get_deployment('openshift-network-operator', 'network-operator', cache_enabled=False)
    if deployment is None:
        my_output.error('Network operator deployment not found')
        return False

    k8s_output_handler.print_deployments([deployment])

    replica_set = params['k8s_handler'].get_replica_set_deployment('openshift-network-operator', 'network-operator', cache_enabled=False)
    if replica_set is None:
        my_output.error('Network operator replica set not found')
        return False

    k8s_output_handler.print_replica_sets([replica_set])

    pods = params['k8s_handler'].get_pods_replica_set(replica_set['namespace'], replica_set['name'], cache_enabled=False)
    if pods is None:
        my_output.error('Network operator pods not found')
        return False

    k8s_output_handler.print_pods_state(pods)

    success = params['k8s_handler'].set_deployment_replicas(
        'openshift-network-operator', 
        'network-operator',
        0,
        confirmation=params['confirmation'],
        my_output=my_output,
        wait=True
    )
    if not success:
        return False

    return True


def pause_mcp(params, my_output):
    success = params['k8s_handler'].set_machine_config_pool_pause(
        'master',
        True,
        confirmation=params['confirmation'],
        my_output=my_output,
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].set_machine_config_pool_pause(
        'worker',
        True,
        confirmation=params['confirmation'],
        my_output=my_output,
        wait=True
    )
    if not success:
        return False

    return True


def get_upstream_interface(params, my_output):
    success, output, error = params['ssh_handler'].run_cmd('sudo ovs-vsctl list-ports br-ex')
    if not success:
        my_output.error('Failed to get ovs switch information')
        return None
    
    upstream_interface = None
    for line in output.split('\n'):
        if line.startswith('patch-'):
            continue
        if len(line) == 0:
            continue
        upstream_interface = line
 
    if upstream_interface is None:
        my_output.error('Failed to get ovs switch information')
        return None
    
    params['upstream'] = upstream_interface
    return params


def fixup_manifests(params, my_output):
    my_output.default('Cilium Manifests Fixup', before_newline=True, underline=True)

    manifests = file_helper.get_files_text(params['manifest'])
    cilium_config_filename = get_cilium_config_filename(manifests)
    cilium_config = yaml.safe_load(manifests[cilium_config_filename])
    cilium_config['spec']['ipam']['operator'] = {}
    cilium_config['spec']['ipam']['operator']['clusterPoolIPv4PodCIDRList'] = [params['cidr']]
    cilium_config['spec']['ipam']['operator']['clusterPoolIPv4MaskSize'] = params['host_prefix']
    cilium_config['spec']['tunnelPort'] = 4789
    cilium_config['spec']['kubeProxyReplacement'] = 'QUOTEtrueQUOTE'
    cilium_config['spec']['devices'] = 'br-ex,%s' % (params['upstream'])

    if params['k8s_handler'].get_node_count() == 1:
        cilium_config['spec']['operator']['replicas'] = 1

    config_mo = params['k8s_handler'].get_infrastructure_cluster_config(return_mo=True, cache_enabled=False)
    if config_mo is None:
        my_output.error('Failed to get cluster infrastructure config')
        return None
    
    try:
        internal_url = config_mo['status']['apiServerInternalURI']
        cilium_config['spec']['k8sServiceHost'] = 'QUOTE%sQUOTE' % (internal_url.split('https://')[1].split(':')[0])
        cilium_config['spec']['k8sServicePort'] = int(internal_url.split(':')[2])
    except BaseException:
        my_output.error('Failed to get or parse apiServerInternalURI from cluster infrastructure config')
        return None
    
    manifests[cilium_config_filename] = yaml.dump(cilium_config).replace('QUOTE', '"')
    my_output.default(manifests[cilium_config_filename], before_newline=True, wrap='~~~')

    deployment_filename = None
    for key in manifests:
        if os.path.basename(key) == 'apps_v1_deployment_clife-controller-manager.yaml':
            deployment_filename = key

    if deployment_filename is None:
        my_output.error('Manifest not found: apps_v1_deployment_clife-controller-manager.yaml')
        return None
    
    deployment_config = yaml.safe_load(manifests[deployment_filename])
    try:
        env_mo = {}
        env_mo['name'] = 'KUBERNETES_SERVICE_HOST'
        env_mo['value'] = cilium_config['spec']['k8sServiceHost']
        deployment_config['spec']['template']['spec']['containers'][0]['env'].append(env_mo)

        env_mo = {}
        env_mo['name'] = 'KUBERNETES_SERVICE_PORT'
        env_mo['value'] = 'QUOTE%sQUOTE' % (str(cilium_config['spec']['k8sServicePort']))
        deployment_config['spec']['template']['spec']['containers'][0]['env'].append(env_mo)
    except BaseException:
        my_output.error('Failed to change clife-controller-manager deployment')
        return None

    manifests[deployment_filename] = yaml.dump(deployment_config).replace('QUOTE', '"')
    my_output.default(manifests[deployment_filename], before_newline=True, wrap='~~~')

    if params['confirmation']:
        if not get_confirmation():
            return None
        
    return manifests


def apply_manifests(params, manifests, my_output):
    my_output.default('Apply manifests', before_newline=True, underline=True)

    for key in manifests:
        body = yaml.safe_load(manifests[key])
        if body['kind'] == 'CustomResourceDefinition':
            my_output.default('- %s:%s' % (body['kind'], body['metadata']['name']))
            if not params['k8s_handler'].is_custom_resource_definition(body['metadata']['name'], cache_enabled=False):
                success = params['k8s_handler'].create_custom_resource_definition_mo(body)
                if not success:
                    my_output.error('rest api failed')
                    return False

    for key in manifests:
        body = yaml.safe_load(manifests[key])
        if body['kind'] == 'Namespace':
            my_output.default('- %s:%s' % (body['kind'], body['metadata']['name']))
            if not params['k8s_handler'].is_namespace(body['metadata']['name'], cache_enabled=False):
                success = params['k8s_handler'].create_namespace_mo_from_body(body)
                if not success:
                    my_output.error('rest api failed')
                    return False

    for key in manifests:
        body = yaml.safe_load(manifests[key])
        if body['kind'] == 'ServiceAccount':
            my_output.default('- %s:%s' % (body['kind'], body['metadata']['name']))
            if not params['k8s_handler'].is_service_account(body['metadata']['namespace'], body['metadata']['name']):
                success = params['k8s_handler'].create_service_account_mo(body)
                if not success:
                    my_output.error('rest api failed')
                    return False

    for key in manifests:
        body = yaml.safe_load(manifests[key])
        if body['kind'] == 'OperatorGroup':
            my_output.default('- %s:%s' % (body['kind'], body['metadata']['name']))
            if not params['k8s_handler'].is_operator_group(body['metadata']['namespace'], body['metadata']['name']):
                success = params['k8s_handler'].create_operator_group_mo(body)
                if not success:
                    my_output.error('rest api failed')
                    return False

    for key in manifests:
        body = yaml.safe_load(manifests[key])        
        if body['kind'] == 'Role':
            my_output.default('- %s:%s' % (body['kind'], body['metadata']['name']))
            if not params['k8s_handler'].is_role(body['metadata']['namespace'], body['metadata']['name']):
                success = params['k8s_handler'].create_role_mo(body)
                if not success:
                    my_output.error('rest api failed')
                    return False

    for key in manifests:
        body = yaml.safe_load(manifests[key])        
        if body['kind'] == 'RoleBinding':
            my_output.default('- %s:%s' % (body['kind'], body['metadata']['name']))
            if not params['k8s_handler'].is_role_binding(body['metadata']['namespace'], body['metadata']['name']):
                success = params['k8s_handler'].create_role_binding_mo(body)
                if not success:
                    my_output.error('rest api failed')
                    return False
            
    for key in manifests:
        body = yaml.safe_load(manifests[key])        
        if body['kind'] == 'ClusterRole':
            my_output.default('- %s:%s' % (body['kind'], body['metadata']['name']))
            if not params['k8s_handler'].is_cluster_role(body['metadata']['name'], cache_enabled=False):
                success = params['k8s_handler'].create_cluster_role_mo(body)
                if not success:
                    my_output.error('rest api failed')
                    return False
              
    for key in manifests:
        body = yaml.safe_load(manifests[key])        
        if body['kind'] == 'ClusterRoleBinding':
            my_output.default('- %s:%s' % (body['kind'], body['metadata']['name']))
            if not params['k8s_handler'].is_cluster_role_binding(body['metadata']['name'], cache_enabled=False):
                success = params['k8s_handler'].create_cluster_role_binding_mo(body)
                if not success:
                    my_output.error('rest api failed')
                    return False

    for key in manifests:
        body = yaml.safe_load(manifests[key])        
        if body['kind'] == 'Service':
            my_output.default('- %s:%s' % (body['kind'], body['metadata']['name']))
            if not params['k8s_handler'].is_service(body['metadata']['namespace'], body['metadata']['name']):
                success = params['k8s_handler'].create_service_mo(body)
                if not success:
                    my_output.error('rest api failed')
                    return False

    for key in manifests:
        body = yaml.safe_load(manifests[key])        
        if body['kind'] == 'Subscription':
            my_output.default('- %s:%s' % (body['kind'], body['metadata']['name']))
            if not params['k8s_handler'].is_subscription(body['metadata']['namespace'], body['metadata']['name']):
                success = params['k8s_handler'].create_resource(body)
                if not success:
                    my_output.error('rest api failed')
                    return False

    for key in manifests:
        body = yaml.safe_load(manifests[key])        
        if body['kind'] == 'CiliumConfig':
            my_output.default('- %s:%s' % (body['kind'], body['metadata']['name']))
            if params['k8s_handler'].is_cilium_config(name=body['metadata']['name']):
                cilium_config_mo = params['k8s_handler'].get_cilium_config(name=body['metadata']['name'], cache_enabled=False, return_mo=True)
                if cilium_config_mo is not None:
                    body['metadata']['resourceVersion'] = cilium_config_mo['metadata']['resourceVersion']

                success = params['k8s_handler'].replace_resource(body)
                if not success:
                    my_output.error('rest api failed')
                    return False
            else:
                success = params['k8s_handler'].create_resource(body)
                if not success:
                    my_output.error('rest api failed')
                    return False
                                            
    for key in manifests:
        body = yaml.safe_load(manifests[key])        
        if body['kind'] == 'Deployment':
            my_output.default('- %s:%s' % (body['kind'], body['metadata']['name']))
            if not params['k8s_handler'].is_deployment(body['metadata']['namespace'], body['metadata']['name']):
                success = params['k8s_handler'].create_resource(body)
                if not success:
                    my_output.error('rest api failed')
                    return False

    return True


def update_multus(params, my_output):
    my_output.default('Multus Update', before_newline=True, underline=True)

    config_map_mo = params['k8s_handler'].get_config_map(
        'openshift-multus', 
        'multus-daemon-config', 
        cache_enabled=False, 
        return_mo=True
    )
    if config_map_mo is None:
        my_output.error('Multus config map not found: openshift-multus/multus-daemon-config')
        return False

    data_mo = filter_helper.get(config_map_mo, 'data:daemon-config.json')
    if data_mo is None:
        my_output.error('Unsupported config map body - no daemon-config.json')
        return False

    try:
        data_json = json.loads(data_mo)
    except BaseException:
        my_output.error('Unsupported config map body - json expected')
        return False

    data_json['readinessindicatorfile'] = '/host/run/multus/cni/net.d/05-cilium.conflist'

    cm_data = {}
    cm_data['daemon-config.json'] = json.dumps(data_json, indent=4)

    success = params['k8s_handler'].set_config_map_data(
        'openshift-multus', 
        'multus-daemon-config',
        cm_data,
        confirmation=params['confirmation'],
        my_output=my_output
    )
    if not success:
        return False
    
    return True


def wait_cilium_resources(params, my_output, k8s_output_handler):
    my_output.default('Wait for Cilium resources', before_newline=True, underline=True)

    my_output.default('Take a nap...', before_newline=True, after_newline=True)
    time.sleep(60)

    deployments = params['k8s_handler'].get_deployments(
        object_filter=['namespace:cilium'],
        cache_enabled=False
    )
    if deployments is None:
        my_output.error('Failed to get deployments')
        return False
    
    if len(deployments) == 0:
        my_output.error('Unexpected no deployments in cilium namespace')
        return False
    
    pods = params['k8s_handler'].get_pods(
        object_filter=['namespace:cilium'],
        cache_enabled=False
    )
    if pods is None:
        my_output.error('Failed to get pods')
        return False
    
    if len(pods) == 0:
        my_output.error('Unexpected no pods in cilium namespace')
        return False
    
    for pod in pods:
        my_output.default('- pod: %s' % (pod['name']))
        success = params['k8s_handler'].wait_pod_phase(
            'cilium', 
            pod['name'], 
            'Running', 
            max_time=360
        )
        if not success:
            my_output.default('Timed out... check whats the status...')
            if not get_confirmation():
                return False

    for deployment in deployments:
        my_output.default('- deployment: %s' % (deployment['name']))
        success = params['k8s_handler'].wait_deployment_ready_state(
            'cilium', 
            deployment['name']
        )
        if not success:
            my_output.default('Timed out... check whats the status...')
            if not get_confirmation():
                return False

    deployments = params['k8s_handler'].get_deployments(
        object_filter=['namespace:cilium'],
        cache_enabled=False
    )
    if deployments is None:
        my_output.error('Failed to get deployments')
        return False
    
    k8s_output_handler.print_deployments(deployments)

    pods = params['k8s_handler'].get_pods(
        object_filter=['namespace:cilium'],
        cache_enabled=False
    )
    if pods is None:
        my_output.error('Failed to get pods')
        return False

    k8s_output_handler.print_pods_state(pods)
    return True


def delete_api_server_pods(params, my_output, k8s_output_handler):
    my_output.default('Delete kube API server pods', before_newline=True, underline=True)

    pods = params['k8s_handler'].get_pods(
        object_filter=['label:apiserver:true', 'namespace:openshift-kube-apiserver'],
        cache_enabled=False
    )
    if pods is None:
        my_output.error('failed to find pods')
        return False
    
    if len(pods) != params['k8s_handler'].get_node_count(cache_enabled=False):
        my_output.error('unexpected pod count')
        return False
    
    k8s_output_handler.print_pods_state(pods)

    my_output.default('Delete', before_newline=True)
    for pod in pods:
        my_output.default('- %s' % (pod['name']))
        success = params['k8s_handler'].delete_pod_mo(
            pod['namespace'],
            pod['name']
        )
        if not success:
            my_output.error('rest api failed')
            return False
        
    return True


def get_machine_config_resources(params, my_output):
    deployments_a = params['k8s_handler'].get_deployments(
        object_filter=['namespace:openshift-machine-config-operator', 'name:machine-config-controller'],
        cache_enabled=False
    )
    if deployments_a is None:
        my_output.error('Failed to get machine config operator deployments')
        return None, None
    
    if len(deployments_a) != 1:
        my_output.error('Unexpected machine config operator deployments count')
        return None, None

    pods_a = params['k8s_handler'].get_pods(
        object_filter=['namespace:openshift-machine-config-operator', 'label:k8s-app:machine-config-controller'],
        cache_enabled=False
    )

    if pods_a is None:
        my_output.error('Failed to get machine config operator pods')
        return None, None
    
    if len(pods_a) != 1:
        my_output.error('Unexpected machine config operator pods count')
        return None, None

    deployments_b = params['k8s_handler'].get_deployments(
        object_filter = ['namespace:openshift-machine-config-operator', 'name:machine-config-operator'],
        cache_enabled=False
    )
    if deployments_b is None:
        my_output.error('Failed to get machine config controller deployments')
        return None, None
    
    if len(deployments_b) != 1:
        my_output.error('Unexpected machine config controller deployments count')
        return None, None

    pods_b = params['k8s_handler'].get_pods(
        object_filter=['namespace:openshift-machine-config-operator', 'label:k8s-app:machine-config-operator'],
        cache_enabled=False
    )

    if pods_b is None:
        my_output.error('Failed to get machine config operator pods')
        return None, None
    
    if len(pods_b) != 1:
        my_output.error('Unexpected machine config operator pods count')
        return None, None
    
    deployments = deployments_a + deployments_b
    pods = pods_a + pods_b
    return deployments, pods


def restart_machine_config(params, my_output, k8s_output_handler):
    my_output.default('Delete machine config deployments', before_newline=True, underline=True)

    deployments, pods = get_machine_config_resources(params, my_output)
    if deployments is None or pods is None:
        return False

    k8s_output_handler.print_deployments(deployments)
    k8s_output_handler.print_pods_state(pods)

    my_output.default('Rollout restart', before_newline=True)
    for deployment in deployments:
        print('- %s/%s' % (deployment['namespace'], deployment['name']))
        success = params['k8s_handler'].restart_deployment(
            deployment['namespace'], 
            deployment['name']
        )
        if not success:
            my_output.error('rest api failed')
            return False
        
    my_output.default('Take a nap...', before_newline=True, after_newline=True)
    time.sleep(10)

    my_output.default('Wait for deployment ready', before_newline=True)
    for deployment in deployments:
        print('- %s/%s' % (deployment['namespace'], deployment['name']))
        success = params['k8s_handler'].wait_deployment_ready_state(
            deployment['namespace'], 
            deployment['name']
        )
        if not success:
            my_output.error('rest api failed')
            return False

    deployments, pods = get_machine_config_resources(params, my_output)
    if deployments is None or pods is None:
        return False

    k8s_output_handler.print_deployments(deployments)
    k8s_output_handler.print_pods_state(pods)

    return True


def scale_up_network_operator(params, my_output, k8s_output_handler):
    my_output.default('Network Operator', underline=True, before_newline=True)
    deployment = params['k8s_handler'].get_deployment('openshift-network-operator', 'network-operator', cache_enabled=False)
    if deployment is None:
        my_output.error('Network operator deployment not found')
        return False

    k8s_output_handler.print_deployments([deployment])

    success = params['k8s_handler'].set_deployment_replicas(
        'openshift-network-operator', 
        'network-operator',
        1,
        confirmation=params['confirmation'],
        my_output=my_output,
        wait=True
    )
    if not success:
        return False

    replica_set = params['k8s_handler'].get_replica_set_deployment('openshift-network-operator', 'network-operator', cache_enabled=False)
    if replica_set is None:
        my_output.error('Network operator replica set not found')
        return False

    k8s_output_handler.print_replica_sets([replica_set])

    pods = params['k8s_handler'].get_pods_replica_set(replica_set['namespace'], replica_set['name'], cache_enabled=False)
    if pods is None:
        my_output.error('Network operator pods not found')
        return False

    k8s_output_handler.print_pods_state(pods)

    return True


def enable_network_operator_management(params, my_output):
    success = params['k8s_handler'].enable_network_operator_management(
        confirmation=params['confirmation'],
        my_output=my_output
    )
    if not success:
        return False
    
    return True


def unpause_mcp(params, my_output):
    success = params['k8s_handler'].set_machine_config_pool_pause(
        'worker',
        False,
        confirmation=False,
        my_output=my_output,
        wait=False
    )
    if not success:
        return False

    success = params['k8s_handler'].set_machine_config_pool_pause(
        'master',
        False,
        confirmation=False,
        my_output=my_output,
        wait=False
    )
    if not success:
        return False

    return True


def mcp_restart_cluster(params, my_output, k8s_output_handler, log_id):
    nodes = params['k8s_handler'].get_nodes(cache_enabled=False)
    if nodes is not None:
        k8s_output_handler.print_nodes_state(nodes)

    if not unpause_mcp(params, my_output):
        return False
    
    success, failed_nodes = params['k8s_handler'].wait_mcp_cluster_restart(nodes, my_output=my_output)
    if not success:
        if not params['reload']:
            my_output.default('Waiting for automatic node restart timed out')
            my_output.default('- node: %s' % (','.join(failed_nodes)))
            my_output.default('- check what blocks that')
            my_output.default('- consider reboot')
            my_output.default('- press Y once all nodes restarted or N to break the workflow')
            if not get_confirmation():
                return False
        else:
            my_output.default('Triggering graceful reload of nodes that failed mcp-triggered restart')
            my_output.default('- node: %s' % (','.join(failed_nodes)))

            child_params = {}
            child_params['cluster'] = params['cluster']
            child_params['pre'] = False
            child_params['post'] = False
            child_params['confirmation'] = False
            child_params['verbose'] = True
            child_params['check-verbose'] = False
            success = reload.run(child_params, log_id=log_id)
            if not success:
                return False
            
    my_output.default('Wait for kubernetes api [30min]...')
    success = params['k8s_handler'].wait_api(max_time=1800)
    if not success:
        my_output.default('Waiting for k8s api timed out')
        my_output.default('- check what blocks that')
        my_output.default('- press Y once k8s api works or N to break the workflow')
        if not get_confirmation():
            return False

    return True


def wait_cluster_ready(params, my_output, k8s_output_handler):
    my_output.default('Wait nodes ready [30min]...')
    success = params['k8s_handler'].wait_nodes_ready(max_time=1800)
    if not success:
        my_output.default('Check what prevents nodes from being ready...')
        if not get_confirmation():
            return False
    
    nodes = params['k8s_handler'].get_nodes(cache_enabled=False)
    if nodes is not None:
        k8s_output_handler.print_nodes_state(nodes)

    my_output.default('Wait machine config pool ready [1hr]...', before_newline=True)
    success = params['k8s_handler'].wait_machine_config_pool_ready()
    if not success:
        my_output.default('Check what prevents mcp from being ready...')
        if not get_confirmation():
            return False

    mcp = params['k8s_handler'].get_machine_config_pools(cache_enabled=False)
    if mcp is not None:
        k8s_output_handler.print_machine_config_pools(mcp)

    my_output.default('Wait Cluster Operators', before_newline=True)
    before_cluster_operators = params['k8s_handler'].get_cluster_operators(cache_enabled=False)
    if before_cluster_operators is None:
        my_output.error('rest api failed')
        return False
    
    for cluster_operator in before_cluster_operators:
        my_output.default('- wait for %s available' % (cluster_operator['name']))
        success = params['k8s_handler'].wait_cluster_operator_available(cluster_operator['name'])
        if not success:
            my_output.default('Check what prevents all cluster operators from being ready...')
            if not get_confirmation():
                return False
            
    my_output.default('Check Cluster Operators', before_newline=True, underline=True)
    cluster_operators = params['k8s_handler'].get_cluster_operators(cache_enabled=False)
    if cluster_operators is None:
        my_output.error('rest api failed')
        return False
    
    k8s_output_handler.print_cluster_operators(cluster_operators)
        
    return True


def update_cilium_config_device(params, my_output, k8s_output_handler):
    my_output.default('Remove device from cilium config')
    cilium_config_mo = params['k8s_handler'].get_cilium_config(cache_enabled=False, return_mo=True)
    if cilium_config_mo is None:
        my_output.error('Failed to get CiliumConfig CRD')
        return False
    
    if 'devices' not in cilium_config_mo['spec']:
        my_output.default('- already removed')
        return True
    
    cilium_spec = copy.deepcopy(cilium_config_mo['spec'])
    del cilium_spec['devices']

    body = {}
    body['apiVersion'] = cilium_config_mo['apiVersion']
    body['kind'] = cilium_config_mo['kind']
    body['metadata'] = {}
    body['metadata']['name'] = cilium_config_mo['metadata']['name']
    body['metadata']['labels'] = cilium_config_mo['metadata']['labels']
    body['metadata']['resourceVersion'] = cilium_config_mo['metadata']['resourceVersion']
    body['spec'] = copy.deepcopy(cilium_spec)

    success = params['k8s_handler'].replace_resource(body)
    if not success:
        my_output.error('rest api failed')
        return False
    
    my_output.default('- patched')

    if not params['k8s_handler'].restart_deployment('cilium', 'cilium-operator', my_output=my_output):
        return False

    if not params['k8s_handler'].restart_daemon_set('cilium', 'cilium', my_output=my_output):
        return False

    if not wait_cilium_resources(params, my_output, k8s_output_handler):
        return False
    
    return True


def prepare_kubeconfig(params, my_output):
    my_output.default('Prepare kubeconfig', before_newline=True)

    if not params['ssh_handler'].is_directory('.kube', path_fixup=False):
        success = params['ssh_handler'].create_directory('.kube', path_fixup=False)
        if not success:
            my_output.error('Failed to create .kube directory')
            return False
        
        my_output.default('.kube directory created')
    else:
        my_output.default('.kube directory already exists')

    success = params['ssh_handler'].scp_file(
        params['kubeconfig_filename'], 
        '.kube/config'
    )
    if not success:
        my_output.error('Failed to upload kubeconfig')
        return False
    
    my_output.default('kubeconfig uploaded')

    return True


def install_cilium_cli(params, my_output, log_id):
    success, output, error = params['ssh_handler'].run_cmd('cilium --help')
    if success:
        my_output.default('Cilium cli already installed', before_newline=True)
        return True

    install_params = {}
    install_params['cluster'] = params['cluster']
    install_params['confirmation'] = params['confirmation']
    install_params['check_verbose'] = False

    success = cli_install.run(install_params, log_id)
    if not success:
        return False
    
    return True


def approve_installplan(params, my_output):
    my_output.default('Approve cilium install plan', before_newline=True)

    info = params['k8s_handler'].get_installplans(
        object_filter=['namespace:cilium'],
        return_mo=True,
        cache_enabled=False
    )
    if info is None:
        my_output.error('Failed to get installplan')
        return False
    
    if len(info) != 1:
        my_output.error('Unexpected installplan count: %s' % (len(info)))
        return False
    
    if info[0]['spec']['approved']:
        my_output.default('- installplan cilium/%s already approved' % (info[0]['metadata']['name']))
        return True
    
    my_output.default('- installplan cilium/%s will be approved' % (info[0]['metadata']['name']))

    success = params['k8s_handler'].approve_installplan(
        'cilium',
        info[0]['metadata']['name']
    )
    if not success:
        my_output.error('rest api failed')
        return False
    
    my_output.default('- patched (approved)')
    return True


def remove_ovn(params, my_output):
    my_output.default('Remove ovn-kubernetes namespace', before_newline=True)

    if not params['k8s_handler'].is_namespace('openshift-ovn-kubernetes'):
        my_output.default('- already removed')
        return True
    
    used = params['k8s_handler'].check_namespace_usage_and_state(
        'openshift-ovn-kubernetes', 
        my_output=my_output, 
        show_details=True, 
        underline=False, 
        before_newline=True
    )
    if used:
        my_output.default('Clean up unexpected resources in openshift-ovn-kubernetes manually first')
        if params['confirmation']:
            if not get_confirmation():
                return False        

    success = params['k8s_handler'].delete_namespace(
        'openshift-ovn-kubernetes',
        my_output=None,
        wait=True
    )
    if not success:
        my_output.error('Namespace delete failed')
        return False
    
    my_output.default('Namespace deleted')
    return True


def reload_cluster_nodes(params, my_output, k8s_output_handler, log_id):
    my_output.default('Reload nodes', before_newline=True)
    handlers = global_common.get_nodes_ssh_handler(
        params['cluster'], 
        params['k8s_handler'], 
        log_id=log_id
    )
    for node_name in handlers:
        my_output.default('- %s' % (node_name))

        success, output, error = handlers[node_name].run_cmd('sudo reboot')
        if not success:
            my_output.default('sudo reboot failed')
            return False

    my_output.default('Wait for no kubernetes api [10min]...')
    success = params['k8s_handler'].wait_no_api(max_time=600)
    if not success:
        my_output.default('Check what prevents all nodes from reload')
        if not get_confirmation():
            return False

    my_output.default('Wait for kubernetes api [30min]...')
    success = params['k8s_handler'].wait_api(max_time=1800)
    if not success:
        my_output.default('Check what prevents kubernetes api from working...')
        if not get_confirmation():
            return False

    if not wait_cluster_ready(params, my_output, k8s_output_handler):
        return False

    if not wait_cilium_resources(params, my_output, k8s_output_handler):
        return False

    success, output, error = params['ssh_handler'].run_cmd('cilium status -n cilium')
    if not success:
        my_output.default('Failed to get cilium status')
        return False
    
    my_output.default(output, wrap='~~~', before_newline=True)

    return True


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - Cilium CNI - Migration', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if params is None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id, mgmt_required=True)
    if params is None:
        return False
    
    if params['start'] <= 1 and params['stop'] >= 1:
        my_output.default('Step 1: Check cluster state and input parameters', before_newline=True, after_newline=True, double_underline=True)

        cluster_network = params['k8s_handler'].get_cluster_network()
        if cluster_network is None:
            my_output.error('Failed to get cluster network information')
            return False
        
        k8s_output_handler.print_network(cluster_network)

        if not params['k8s_handler'].is_cluster_network_ovn():
            my_output.error('Expected starting cni is ovn')
            return False

        if ip_helper.is_subnet_overlap(cluster_network['cluster_network'], params['cidr']):
            my_output.error('Target cluster network overlaps with ovn cluster network')
            return False
        
        my_output.default('Target cluster network does not overlap with ovn cluster network')

        params = get_upstream_interface(params, my_output)
        if params is None:
            return False
        
        my_output.default('Upstream interface of OVS switch: %s' % (params['upstream']))

        if not check_cluster_before(params, my_output):
            return False
    
    if params['start'] <= 2 and params['stop'] >= 2:
        my_output.default('Step 2: Disable cluster network operator', before_newline=True, after_newline=True, double_underline=True)

        if not disable_network_operator_management(params, my_output):
            return False
        
        if not scale_down_network_operator(params, my_output, k8s_output_handler):
            return False

        success = params['k8s_handler'].delete_config_map(
            'openshift-network-operator',
            'applied-cluster',
            my_output=my_output,
            wait=True
        )
        if not success:
            return False

        if not pause_mcp(params, my_output):
            return False
        
    if params['start'] <= 3 and params['stop'] >= 3:
        my_output.default('Step 3: Change default CNI', before_newline=True, after_newline=True, double_underline=True)

        success = params['k8s_handler'].set_cluster_network_type(
            'Cilium', 
            params['cidr'], 
            params['host_prefix'], 
            confirmation=params['confirmation'], 
            my_output=my_output
        )
        if not success:
            return False
        
        success = params['k8s_handler'].set_cluster_network_operator_type(
            'Cilium', 
            params['cidr'], 
            params['host_prefix'], 
            confirmation=params['confirmation'], 
            my_output=my_output
        )
        if not success:
            return False

    if params['start'] <= 4 and params['stop'] >= 4:
        my_output.default('Step 4: Deploy Cilium', before_newline=True, after_newline=True, double_underline=True)

        if 'upstream' not in params:
            params = get_upstream_interface(params, my_output)
            if params is None:
                return False
            
        manifests = fixup_manifests(params, my_output)
        if manifests is None:
            return False
        
        if not apply_manifests(params, manifests, my_output):
            return False
        
        if not update_multus(params, my_output):
            return False

        if not wait_cilium_resources(params, my_output, k8s_output_handler):
            return False
    
    if params['start'] <= 5 and params['stop'] >= 5:
        my_output.default('Step 5: Re-enable OpenShift operator management', before_newline=True, after_newline=True, double_underline=True)

        if not delete_api_server_pods(params, my_output, k8s_output_handler):
            return False
        
        if not restart_machine_config(params, my_output, k8s_output_handler):
            return False

        if not scale_up_network_operator(params, my_output, k8s_output_handler):
            return False

        if not enable_network_operator_management(params, my_output):
            return False

    if params['start'] <= 6 and params['stop'] >= 6:
        my_output.default('Step 6: Restart cluster', before_newline=True, after_newline=True, double_underline=True)

        if not mcp_restart_cluster(params, my_output, k8s_output_handler, log_id):
            return False

    if params['start'] <= 7 and params['stop'] >= 7:
        my_output.default('Step 7: Wait cluster ready', before_newline=True, after_newline=True, double_underline=True)

        if not wait_cluster_ready(params, my_output, k8s_output_handler):
            return False

        if not wait_cilium_resources(params, my_output, k8s_output_handler):
            return False

    if params['start'] <= 8 and params['stop'] >= 8:
        my_output.default('Step 8: Post migration', before_newline=True, after_newline=True, double_underline=True)

        if not update_cilium_config_device(params, my_output, k8s_output_handler):
            return False
        
        if not approve_installplan(params, my_output):
            return False
            
        if not remove_ovn(params, my_output):
            return False

        if not prepare_kubeconfig(params, my_output):
            return False

        if not install_cilium_cli(params, my_output, log_id):
            return False

        success, output, error = params['ssh_handler'].run_cmd('cilium status -n cilium')
        if not success:
            my_output.default('Failed to get cilium status')
            return False
        
        my_output.default(output, wrap='~~~', before_newline=True)

    if params['start'] <= 9 and params['stop'] >= 9:
        my_output.default('Step 9: Cluster Restart', before_newline=True, after_newline=True, double_underline=True)

        if not reload_cluster_nodes(params, my_output, k8s_output_handler, log_id):
            return False
        
    return True
