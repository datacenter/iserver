import os
import time
import yaml
from lib import file_helper
from lib import output_helper
from lib.workflow import ocp_common as workflow_common
from lib.workflow.ocp_cilium_cli import task as cilium_cli_workflow
from lib.workflow.ocp_fabric import bgp


def apply_files(user_settings, ssh_handler, my_output):
    directory = os.path.join(
        user_settings['directory'],
        'files'
    )
    if not os.path.isdir(directory):
        my_output.default('- directory with files to apply not found')
        return True

    my_output.default('Kubernetes files', before_newline=True, underline=True)
    for file_basename in os.listdir(directory):
        destination_filename = '/tmp/%s' % (file_basename)
        source_filename = os.path.join(
            directory,
            file_basename
        )
        my_output.default('File: %s' % (source_filename))

        yaml_content = file_helper.get_file_yaml(
            source_filename
        )
        if yaml_content is None:
            my_output.error('skipping - not a yaml file')
            continue

        if not ssh_handler.scp_file(source_filename, destination_filename):
            my_output.error('file scp failed')
            return False

        command = 'oc apply -f %s' % (destination_filename)
        success, output, error = ssh_handler.run_cmd(command)
        if not success:
            my_output.error('Command failed: %s' % (command))
            my_output.default(str(output))
            my_output.default(str(error))
            return False
        
        my_output.default('~~~')
        my_output.default('# %s' % (command))
        my_output.default(str(output))
        my_output.default(str(error))
        my_output.default('~~~', after_newline=True)

    return True


def apply_cilium_bgp_cluster(user_settings, controller, k8s_handler, my_output):
    cluster_mo = {}
    cluster_mo['apiVersion'] = 'isovalent.com/v1'
    cluster_mo['kind'] = 'IsovalentBGPClusterConfig'
    cluster_mo['metadata'] = {}
    cluster_mo['metadata']['name'] = user_settings['cilium']['bgp']['name']
    cluster_mo['spec'] = {}
    cluster_mo['spec']['bgpInstances'] = []

    instance_mo = {}
    instance_mo['name'] = user_settings['cilium']['bgp']['name']
    instance_mo['localASN'] = controller['bgp']['asn']
    instance_mo['peers'] = []

    peer_mo = {}
    peer_mo['name'] = 'leaf_a'
    peer_mo['peerASN'] = user_settings['cilium']['bgp']['asn']
    peer_mo['peerAddress'] = controller['bgp']['leaf_A']['ip']
    peer_mo['peerConfigRef'] = {}
    peer_mo['peerConfigRef']['name'] = user_settings['cilium']['bgp']['name']
    instance_mo['peers'].append(
        peer_mo
    )

    peer_mo = {}
    peer_mo['name'] = 'leaf_b'
    peer_mo['peerASN'] = user_settings['cilium']['bgp']['asn']
    peer_mo['peerAddress'] = controller['bgp']['leaf_B']['ip']
    peer_mo['peerConfigRef'] = {}
    peer_mo['peerConfigRef']['name'] = user_settings['cilium']['bgp']['name']
    instance_mo['peers'].append(
        peer_mo
    )

    cluster_mo['spec']['bgpInstances'].append(
        instance_mo
    )

    my_output.default(yaml.dump(cluster_mo), before_newline=True)

    if k8s_handler.is_isovalent_bgp_cluster_config(user_settings['cilium']['bgp']['name'], cache_enabled=False):
        current_mo = k8s_handler.get_isovalent_bgp_cluster_config(user_settings['cilium']['bgp']['name'], return_mo=True, cache_enabled=False)
        cluster_mo['metadata']['resourceVersion'] = current_mo['metadata']['resourceVersion']
        success = k8s_handler.replace_resource(
            cluster_mo
        )
    else:
        success = k8s_handler.create_resource(
            cluster_mo
        )

    if not success:
        my_output.error('Kubernetes API failed')
        return False

    return True


def apply_cilium_bgp_peer(user_settings, k8s_handler, my_output):
    peer_mo = {}
    peer_mo['apiVersion'] = 'isovalent.com/v1'
    peer_mo['kind'] = 'IsovalentBGPPeerConfig'
    peer_mo['metadata'] = {}
    peer_mo['metadata']['name'] = user_settings['cilium']['bgp']['name']
    peer_mo['spec'] = {}
    peer_mo['spec']['timers'] = {}
    peer_mo['spec']['timers']['connectRetryTimeSeconds'] = user_settings['cilium']['bgp']['retry']
    peer_mo['spec']['timers']['holdTimeSeconds'] = user_settings['cilium']['bgp']['hold']
    peer_mo['spec']['timers']['keepAliveTimeSeconds'] = user_settings['cilium']['bgp']['keepalive']
    peer_mo['spec']['families'] = []

    family_mo = {}
    family_mo['afi'] = 'ipv4'
    family_mo['safi'] = 'unicast'
    family_mo['advertisements'] = {}
    family_mo['advertisements']['matchLabels'] = {}
    family_mo['advertisements']['matchLabels']['advertise'] = user_settings['cilium']['bgp']['name']

    peer_mo['spec']['families'].append(
        family_mo
    )

    my_output.default(yaml.dump(peer_mo), before_newline=True)

    if k8s_handler.is_isovalent_bgp_peer_config(user_settings['cilium']['bgp']['name'], cache_enabled=False):
        current_mo = k8s_handler.get_isovalent_bgp_peer_config(user_settings['cilium']['bgp']['name'], return_mo=True, cache_enabled=False)
        peer_mo['metadata']['resourceVersion'] = current_mo['metadata']['resourceVersion']
        success = k8s_handler.replace_isovalent_bgp_peer_config(
            peer_mo
        )
    else:
        success = k8s_handler.create_isovalent_bgp_peer_config(
            peer_mo
        )

    if not success:
        my_output.error('Kubernetes API failed')
        return False
    
    return True


def apply_cilium_bgp_advertisement(user_settings, k8s_handler, my_output):
    advertisement_mo = {}
    advertisement_mo['apiVersion'] = 'isovalent.com/v1'
    advertisement_mo['kind'] = 'IsovalentBGPAdvertisement'
    advertisement_mo['metadata'] = {}
    advertisement_mo['metadata']['name'] = user_settings['cilium']['bgp']['name']
    advertisement_mo['metadata']['labels'] = {}
    advertisement_mo['metadata']['labels']['advertise'] = user_settings['cilium']['bgp']['name']
    advertisement_mo['spec'] = {}
    advertisement_mo['spec']['advertisements'] = []

    if user_settings['cilium']['bgp']['pod']:
        adv_mo = {}
        adv_mo['advertisementType'] = 'PodCIDR'
        advertisement_mo['spec']['advertisements'].append(
            adv_mo
        )

    if user_settings['cilium']['bgp']['lb'] is not None:
        adv_mo = {}
        adv_mo['advertisementType'] = 'Service'
        adv_mo['service'] = {}
        adv_mo['service']['addresses'] = ['LoadBalancerIP']
        adv_mo['selector'] = {}
        adv_mo['selector']['matchExpressions'] = []
        
        expr_mo = {}
        expr_mo['key'] = user_settings['cilium']['bgp']['lb'].split(':')[0]
        expr_mo['operator'] = 'In'
        expr_mo['values'] = [user_settings['cilium']['bgp']['lb'].split(':')[1]]
        adv_mo['selector']['matchExpressions'].append(expr_mo)

        advertisement_mo['spec']['advertisements'].append(
            adv_mo
        )

    my_output.default(yaml.dump(advertisement_mo), before_newline=True)

    if k8s_handler.is_isovalent_bgp_advertisement(user_settings['cilium']['bgp']['name'], cache_enabled=False):
        current_mo = k8s_handler.get_isovalent_bgp_advertisement(user_settings['cilium']['bgp']['name'], return_mo=True, cache_enabled=False)
        advertisement_mo['metadata']['resourceVersion'] = current_mo['metadata']['resourceVersion']
        success = k8s_handler.replace_resource(
            advertisement_mo
        )
    else:
        success = k8s_handler.create_resource(
            advertisement_mo
        )

    if not success:
        my_output.error('Kubernetes API failed')
        return False

    return True


def apply_cilium_bgp(user_settings, k8s_handler, ssh_handler, my_output, log_id):
    my_output.default('Cilium BGP', before_newline=True, underline=True)
    my_output.default('- kube object base name: %s' % (user_settings['cilium']['bgp']['name']))
    my_output.default('- fabric asn: %s' % (user_settings['cilium']['bgp']['asn']))
    my_output.default('- pod cidr advertisement: %s' % (user_settings['cilium']['bgp']['pod']))
    if user_settings['cilium']['bgp']['lb'] is not None:
        my_output.default('- load balancer service advertisement: %s' % (user_settings['cilium']['bgp']['lb']))

    if 'fabric' not in user_settings or user_settings['fabric'] is None:
        return True
    
    if 'controller' not in user_settings['fabric'] or user_settings['fabric']['controller'] is None:
        return True
    
    for controller in user_settings['fabric']['controller']:
        if controller['type'] != 'aci':
            continue

        if 'bgp' not in controller:
            continue

        my_output.default('- cilium asn: %s' % (controller['bgp']['asn']))
        my_output.default('- fabric peer #1: %s' % (controller['bgp']['leaf_A']['ip']))
        my_output.default('- fabric peer #2: %s' % (controller['bgp']['leaf_B']['ip']))

        if not apply_cilium_bgp_cluster(user_settings, controller, k8s_handler, my_output):
            return False
        
        if not apply_cilium_bgp_peer(user_settings, k8s_handler, my_output):
            return False
        
        if not apply_cilium_bgp_advertisement(user_settings, k8s_handler, my_output):
            return False
    
    my_output.default('Wait for IsovalentBGPNodeConfig CRD', before_newline=True)
    nodes = k8s_handler.get_nodes_name()
    for node in nodes:
        my_output.default('- %s' % (node))
        if not k8s_handler.wait_isovalent_bgp_node_config(node):
            my_output.error('Timeout reached')
            return False

    my_output.default('Give a moment for sessions to be established...', before_newline=True, after_newline=True)
    time.sleep(5)

    my_output.default('Cilium State', underline=True, after_newline=True)

    success, output, error = ssh_handler.run_cmd('cilium state -n cilium')
    if not success:
        my_output.error('Cilium CLI not found')

        cli_workflow_params = {}
        cli_workflow_params['cluster'] = user_settings['connector']
        cli_workflow_success = cilium_cli_workflow.run(
            cli_workflow_params
        )
        if not cli_workflow_success:
            return False

    success, output, error = ssh_handler.run_cmd('cilium bgp peers -n cilium')
    if not success:
        my_output.error('Failed to get cilium bgp peers state')
        my_output.default(str(output))
        my_output.default(str(error))
        return False
    
    my_output.default('~~~\n%s\n~~~' % (str(output)))

    success, output, error = ssh_handler.run_cmd('cilium bgp routes advertised ipv4 unicast -n cilium')
    if not success:
        my_output.error('Failed to get cilium bgp advertised routes')
        my_output.default(str(output))
        my_output.default(str(error))
        return False
    
    my_output.default('~~~\n%s\n~~~' % (str(output)))

    bgp.print_state(
        user_settings['fabric'],
        my_output,
        log_id
    )

    return True


def apply_cilium(user_settings, k8s_handler, ssh_handler, my_output, log_id):
    if user_settings['network_type'] != 'Cilium':
        return True
    
    if user_settings['cilium']['bgp']['enabled']:
        if user_settings['cilium']['bgp']['asn'] is not None:
            success = apply_cilium_bgp(user_settings, k8s_handler, ssh_handler, my_output, log_id)
            if not success:
                return False
            
    return True


def run(user_settings, log_id):
    my_output = output_helper.OutputHelper(log_id=log_id)

    my_output.default('Cluster configuration...', before_newline=True, underline=True)
    k8s_handler = workflow_common.verify_cluster_name(
        user_settings['connector'],
        log_id=log_id
    )
    if k8s_handler is None:
        my_output.error('Failed to get kubernetes handler')
        return False

    my_output.default('- kubernetes handler ready')

    ssh_handler = workflow_common.get_management_node_ssh_handler(
        user_settings['connector'],
        log_id=log_id
    )
    if ssh_handler is None:
        my_output.error('Failed to get ssh handler to management node')
        return False    

    my_output.default('- management node ssh handler ready')

    success = apply_files(user_settings, ssh_handler, my_output)
    if not success:
        return False
    
    success = apply_cilium(user_settings, k8s_handler, ssh_handler, my_output, log_id)
    if not success:
        return False

    return True
