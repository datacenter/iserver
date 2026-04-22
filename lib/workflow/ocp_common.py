import os
import json
import time
import yaml
import copy
from menu import common
from lib import file_helper
from lib import filter_helper
from lib import ip_helper
from lib import log_helper
from lib import ssh
from lib.linux import main as linux
from lib.k8s import main as k8s
from lib.ocp import settings as ocp_settings
from lib.workflow.ocp_cluster import ready as cluster_ready
from lib.workflow.ocp_access import check as ocp_check
from lib.workflow.ocp_cilium_cni import common as cilium_common


def check_cluster_init_fqdn(user_settings, my_output, log_id):
    if user_settings['randomize']:
        return True

    my_output.default('\nChecking cluster fqdn resolution')

    success = True
    apps = [
        'oauth-openshift',
        'console-openshift-console',
        'grafana-openshift-monitoring',
        'thanos-querier-openshift-monitoring',
        'prometheus-k8s-openshift-monitoring',
        'alertmanager-main-openshift-monitoring',
        'hyperconverged-cluster-cli-download-openshift-cnv'
    ]
    for app in apps:
        fqdn = '%s.apps.%s.%s' % (
            app,
            user_settings['name'],
            user_settings['base_dns_domain']
        )
        resolved = ip_helper.get_ip(fqdn)
        if resolved != user_settings['ingress']:
            success = False
            my_output.error(
                'Cluster FQDNs resolved incorrectly: %s expected %s resolved %s' % (
                    fqdn,
                    user_settings['ingress'],
                    resolved
                )
            )

    fqdn = 'api.%s.%s' % (
        user_settings['name'],
        user_settings['base_dns_domain']
    )
    resolved = ip_helper.get_ip(fqdn)
    if resolved != user_settings['api']:
        success = False
        my_output.error(
            'Cluster FQDNs resolved incorrectly: %s expected %s resolved %s' % (
                fqdn,
                user_settings['api'],
                resolved
            )
        )

    if success:
        my_output.default('Cluster FQDNs resolved correctly')

    return success


def get_ocp_cluster_filename(cluster_name, log_id=None):
    ocp_settings_handler = ocp_settings.OcpSettings(log_id=log_id)
    return ocp_settings_handler.get_ocp_cluster_filename(cluster_name, 'ssh.pub')


def verify_cluster_name(cluster_name, log_id=None, management_access=False):
    ocp_settings_handler = ocp_settings.OcpSettings(log_id=log_id)
    if not ocp_settings_handler.is_ocp_cluster(cluster_name):
        return None

    ocp_cluster_settings = ocp_settings_handler.get_ocp_cluster(cluster_name)
    k8s_handler = k8s.K8s(kubeconfig_filename=ocp_cluster_settings['kubeconfig'], cluster_type='ocp', log_id=log_id)

    if k8s_handler.get_nodes() is None:
        print('Kubernetes API failed')
        return None
    
    if management_access:
        if not ocp_settings_handler.is_management_ip(cluster_name):
            ip_address = input('Cluster management IP address required: ')
            if not ip_helper.is_valid_ipv4_address(ip_address):
                print('Invalid IPv4 address')
                return None

            if not ocp_settings_handler.set_management_ip(cluster_name, ip_address):
                print('Failed to configure management ip')
                return None

        if not ocp_settings_handler.is_management_ssh_pub(cluster_name):
            filename = input('Cluster management ssh public key filename required: ')
            if not os.path.isfile(filename):
                print('File not found')
                return None

            if not ocp_settings_handler.set_management_ssh_pub(cluster_name, filename):
                print('Failed to configure management ssh public kye')
                return None

    return k8s_handler


def get_cluster_nodes_ip(k8s_handler=None, cluster_name=None, log_id=None):
    if k8s_handler is None and cluster_name is None:
        return None

    if k8s_handler is None:
        k8s_handler = verify_cluster_name(cluster_name, log_id=log_id)
        if k8s_handler is None:
            return None

    return k8s_handler.get_nodes_ip()


def add_operator(params, my_output=None):
    params['subscription_info'] = params['k8s_handler'].get_subscription_by_package(
        params['name'],
        cache_enabled=False
    )
    if params['subscription_info'] is not None:
        my_output.default('Subscription already found: %s' % (params['name']))
        params['success'] = True
        return params

    if my_output is not None:
        my_output.default('Subscription to be added: %s' % (params['name']))

    catalog = None
    if 'catalog' in params:
        catalog = params['catalog']

    params['package_info'] = params['k8s_handler'].get_package(
        params['name'],
        catalog=catalog
    )
    if params['package_info'] is None:
        params['success'] = False
        params['error'] = 'Package not found in marketplace: %s' % (params['name'])
        return params

    if my_output is not None:
        my_output.default('Package found in marketplace: %s' % (params['name']))

    params['channel_info'] = None
    target_channel = params['channel']
    if target_channel == '__default__':
        target_channel = filter_helper.get(params, 'package_info:status:defaultChannel')
        if target_channel is None:
            params['success'] = False
            params['error'] = 'Default channel not found'
            return params

    try:
        for channel in params['package_info']['status']['channels']:
            if channel['name'] == target_channel:
                params['channel_info'] = channel
    except BaseException:
        params['channel_info'] = None

    if params['channel_info'] is None:
        params['success'] = False
        params['error'] = 'Channel not found: %s' % (target_channel)
        return params

    if my_output is not None:
        my_output.default('Channel', before_newline=True, underline=True)
        my_output.default('- Name [%s]' % (target_channel))
        my_output.default('- Description [%s]' % (params['channel_info']['currentCSVDesc']['description']))
        my_output.default('- Name [%s]' % (params['channel_info']['currentCSVDesc']['displayName']))
        my_output.default('- Version [%s]' % (params['channel_info']['currentCSVDesc']['version']))
        my_output.default('- Provider [%s]' % (params['channel_info']['currentCSVDesc']['provider']['name']))
        if 'maturity' in params['channel_info']['currentCSVDesc']:
            my_output.default('- Maturity [%s]' % (params['channel_info']['currentCSVDesc']['maturity']))

    try:
        target_namespace = params['channel_info']['currentCSVDesc']['annotations']['operatorframework.io/suggested-namespace']
        if my_output is not None:
            my_output.default('- Installation namespace [%s]' % (target_namespace))
    except BaseException:
        target_namespace = params['namespace']
        if my_output is not None:
            my_output.default('- Installation namespace [%s]' % (target_namespace))

    subscription_yaml = 'kind: Subscription\n'
    subscription_yaml += 'apiVersion: operators.coreos.com/v1alpha1\n'
    subscription_yaml += 'metadata:\n'
    subscription_yaml += '  name: %s\n' % (params['name'])
    subscription_yaml += '  namespace: %s\n' % (target_namespace)
    subscription_yaml += 'spec:\n'
    subscription_yaml += '  channel: %s\n' % (target_channel)
    subscription_yaml += '  installPlanApproval: Automatic\n'
    subscription_yaml += '  name: %s\n' % (params['name'])
    subscription_yaml += '  source: %s\n' % (params['package_info']['status']['catalogSource'])
    subscription_yaml += '  sourceNamespace: %s\n' % (params['package_info']['status']['catalogSourceNamespace'])
    subscription_yaml += '  startingCSV: %s\n' % (params['channel_info']['currentCSV'])

    if my_output is not None:
        my_output.default('\n%s' % (subscription_yaml))
    params['subscription_yaml'] = subscription_yaml

    if params['confirmation']:
        if not common.get_confirmation(title='Install operator'):
            params['success'] = False
            params['error'] = 'User abort'
            return params

    if not params['k8s_handler'].is_namespace(target_namespace, cache_enabled=False):
        if not params['k8s_handler'].create_namespace_mo(target_namespace):
            params['success'] = False
            params['error'] = 'Namespace create failed: %s' % (target_namespace)
            return params

        if my_output is not None:
            my_output.default('Namespace created: %s' % (target_namespace))

    object_filter = ['namespace:%s' % (target_namespace)]
    operator_groups = params['k8s_handler'].get_operator_groups(object_filter=object_filter)
    if operator_groups is None:
        params['success'] = False
        params['error'] = 'Failed to get operator groups'
        return params

    if len(operator_groups) == 0:
        success = params['k8s_handler'].create_operator_group(
            target_namespace, 
            confirmation=False, 
            my_output=my_output, 
            wait=True
        )
        if not success:
            params['success'] = False
            params['error'] = 'Failed to create operator group for namespace %s' % (target_namespace)
            return params
        
        if my_output is not None:
            my_output.default('Operator group created for namespace: %s' % (target_namespace))

    try:
        subscription_json = yaml.safe_load(subscription_yaml)
    except BaseException:
        params['success'] = False
        params['error'] = 'Subsciption yaml to json failed'
        return params

    params['subscription_json'] = subscription_json

    success = params['k8s_handler'].create_resource(subscription=subscription_json)
    if not success:
        params['success'] = False
        params['error'] = 'Subsciption create api failed'
        return params

    if my_output is not None:
        my_output.default('Subsciption create api successful')

    if my_output is not None:
        my_output.default('Wait for install plan...')

    params['install_plan_name'] = params['k8s_handler'].wait_subscription_install_plan(target_namespace, params['name'])
    if params['install_plan_name'] is None:
        params['success'] = False
        params['error'] = 'Installation has not started: %s/%s' % (target_namespace, params['name'])
        return params

    if my_output is not None:
        my_output.default('Wait for install plan %s finished...' % (params['install_plan_name']))

    if not params['k8s_handler'].wait_installplan_ready(target_namespace, params['install_plan_name']):
        params['success'] = False
        params['error'] = 'Installation has not finished'
        return params

    if my_output is not None:
        my_output.default('Install plan succeeded')

    params['success'] = True
    params['error'] = None

    return params


def get_management_node_ssh_handler(connector, log_id=None, optional=False):
    log_handler = log_helper.Log(log_id)
    ocp_settings_handler = ocp_settings.OcpSettings(log_id=log_id)
    if not ocp_settings_handler.is_ocp_cluster(connector):
        log_handler.error(
            'get_management_node_ssh_handler',
            'Connector not found: %s' % (connector)
        )
        return None

    management_ip = ocp_settings_handler.get_ocp_cluster_file(
        connector,
        'management_ip'
    )
    if management_ip is None:
        if not optional:
            log_handler.error(
                'get_management_node_ssh_handler',
                'management_ip cluster file not found: %s' % (connector)
            )
        return None

    filename = ocp_settings_handler.get_ocp_cluster_filename(
        connector,
        'ssh.pub'
    )
    if filename is None:
        if not optional:
            log_handler.error(
                'get_management_node_ssh_handler',
                'ssh.pub cluster file not found: %s' % (connector)
            )
        return None

    ssh_handler = ssh.Ssh(
        management_ip,
        'core',
        key_filename=filename,
        log_id=log_id
    )

    return ssh_handler


def get_management_node_linux_handler(connector, log_id=None):
    ocp_settings_handler = ocp_settings.OcpSettings(log_id=log_id)
    if not ocp_settings_handler.is_ocp_cluster(connector):
        return None

    management_ip = ocp_settings_handler.get_ocp_cluster_file(
        connector,
        'management_ip'
    )
    if management_ip is None:
        return None

    filename = ocp_settings_handler.get_ocp_cluster_filename(
        connector,
        'ssh.pub'
    )
    if filename is None:
        return None

    ssh_handler = linux.Linux(
        management_ip,
        'core',
        key_filename=filename
    )

    return ssh_handler


def get_nodes_linux_handler(cluster_name, k8s_handler, log_id=None):
    ocp_settings_handler = ocp_settings.OcpSettings(log_id=log_id)
    if not ocp_settings_handler.is_ocp_cluster(cluster_name):
        return None

    filename = ocp_settings_handler.get_ocp_cluster_filename(
        cluster_name,
        'ssh.pub'
    )
    if filename is None:
        return None

    nodes = k8s_handler.get_nodes_info()
    if nodes is None:
        return None

    handlers = {}

    for node in nodes:
        node_name = node['info']['name']
        handlers[node_name] = linux.Linux(
            node['info']['ssh_ip'],
            'core',
            password=None,
            key_filename=filename,
            server_name=None,
            ocp_cluster_name=cluster_name,
            ocp_node_name=node_name,
            no_cache=True,
            log_id=log_id
        )

    return handlers


def get_nodes_ssh_handler(cluster_name, k8s_handler, log_id=None):
    ocp_settings_handler = ocp_settings.OcpSettings(log_id=log_id)
    if not ocp_settings_handler.is_ocp_cluster(cluster_name):
        return None

    filename = ocp_settings_handler.get_ocp_cluster_filename(
        cluster_name,
        'ssh.pub'
    )
    if filename is None:
        return None

    nodes = k8s_handler.get_nodes_info()
    if nodes is None:
        return None

    handlers = {}

    for node in nodes:
        node_name = node['info']['name']
        handlers[node_name] = ssh.Ssh(
            node['info']['ssh_ip'],
            'core',
            key_filename=filename,
            log_id=log_id
        )

    return handlers


def get_node_ssh_handler(cluster_name, node_name, k8s_handler, log_id=None):
    ocp_settings_handler = ocp_settings.OcpSettings(log_id=log_id)
    if not ocp_settings_handler.is_ocp_cluster(cluster_name):
        return None

    filename = ocp_settings_handler.get_ocp_cluster_filename(
        cluster_name,
        'ssh.pub'
    )
    if filename is None:
        return None

    node = k8s_handler.get_node(node_name)
    if node is None:
        return None

    handler = ssh.Ssh(
        node['ssh_ip'],
        'core',
        key_filename=filename,
        log_id=log_id
    )

    return handler


def is_helm_ready(cluster_name, log_id=None, my_output=None):
    ssh_handler = get_management_node_ssh_handler(
        cluster_name,
        log_id=log_id
    )
    if ssh_handler is None:
        if my_output is not None:
            my_output.error('Failed to get ssh handler to management node')
        return False

    success, output, error = ssh_handler.run_cmd('helm ls -A')
    if not success:
        if my_output is not None:
            my_output.error('Failed to check helm chart')
            my_output.default(str(output))
            my_output.default(str(error))
        return False

    return True


def is_helm(cluster_name, helm_namespace, helm_name, log_id=None, my_output=None):
    ssh_handler = get_management_node_ssh_handler(
        cluster_name,
        log_id=log_id
    )
    if ssh_handler is None:
        if my_output is not None:
            my_output.error('Failed to get ssh handler to management node')
        return False

    success, output, error = ssh_handler.run_cmd('helm ls -n %s' % (helm_namespace))
    if not success:
        if my_output is not None:
            my_output.error('Failed to check nfs helm chart')
        return False

    if helm_name not in output:
        return False

    return True


def get_linux_lsblk(cluster_name, k8s_handler, my_output=None, log_id=None, device_names=None, include_disk_paths=False):
    if my_output is not None:
        my_output.default(
            'Collect linux level lsblk per node...',
            before_newline=True
        )

    linux_handlers = get_nodes_linux_handler(
        cluster_name,
        k8s_handler,
        log_id=log_id
    )
    
    node_names = k8s_handler.get_worker_nodes_name()
    lsblk = {}

    for node_name in node_names:
        lsblk[node_name] = linux_handlers[node_name].get_lsblks(
            device_names=device_names, 
            include_disk_paths=include_disk_paths,
            cache_enabled=False
        )

    return lsblk


def dictionary(my_output, title, item, info, underline=True, start='\n\n', verbose=True):
    headers = []
    order = []
    for key in info:
        headers.append(key[0])
        order.append(key[1])

    if verbose:
        stream = 'default'
    else:
        stream = 'debug'

    my_output.dictionary(
        item,
        title=title,
        prefix='- ',
        keys=order,
        justify=True,
        values=order,
        title_keys=headers,
        underline=underline,
        start=start,
        stream=stream
    )


def prepare_namespace(k8s_handler, name, my_output):
    my_output.default('Create namespace', before_newline=True, underline=True)
    my_output.default('- namespace: %s' % (name))

    if k8s_handler.is_namespace(name, cache_enabled=False):
        my_output.error('Namespace already exists')
        return False
    
    my_output.default('- namespace does not exist')

    success = k8s_handler.create_namespace_mo(name)
    if not success:
        my_output.error('Namespace create failed')
        return False
    
    my_output.default('- namespace created')
    return True


def cleanup_namespace(k8s_handler, name, my_output):
    my_output.default('Delete namespace', before_newline=True, underline=True)
    if not k8s_handler.is_namespace(name, cache_enabled=False):
        my_output.default('- namespace does not exist: %s' % (name))
        return True
    
    success = k8s_handler.delete_namespace_mo(name)
    if not success:
        my_output.error('Namespace delete failed: %s' % (name))
        return False
    
    my_output.default('- namespace deleted: %s' % (name))
    return True


def wait_node_ssh(k8s_handler, cluster_name, node_name, max_time=600):
    start_time = int(time.time())
    while True:
        try:
            handler = get_node_ssh_handler(
                cluster_name, 
                node_name, 
                k8s_handler
            )
            success, output, error = handler.run_cmd('ls')
            if success:
                return True            
        except BaseException:
            pass

        duration = int(time.time()) - start_time
        if duration > max_time:
            return False

        time.sleep(30)


def wait_node(k8s_handler, cluster_name, node_name, my_output=None, max_time=600):
    if my_output is not None:
        my_output.default('Wait for node [%s] up' % (node_name))

    if my_output is not None:
        my_output.default('- ssh')

    if not wait_node_ssh(k8s_handler, cluster_name, node_name, max_time=max_time):
        if my_output is not None:
            my_output.error('Timed out')
        return False
    
    if my_output is not None:
        my_output.default('- k8s api')

    if not k8s_handler.wait_api(max_time=max_time):
        if my_output is not None:
            my_output.error('Timed out')
        return False
    
    if my_output is not None:
        my_output.default('- node ready')

    if not k8s_handler.wait_node_ready(node_name, max_time=max_time):
        if my_output is not None:
            my_output.error('Timed out')
        return False
    
    return True


def run_node_cli(k8s_handler, cluster_name, node_name, command, my_output=None, log_id=None):
    handler = get_node_ssh_handler(
        cluster_name, 
        node_name, 
        k8s_handler, 
        log_id=log_id
    )
    if my_output is not None:
        my_output.default('Node [%s] cli [%s]' % (node_name, command))

    success, output, error = handler.run_cmd(command)
    if not success:
        if my_output is not None:
            my_output.error('Cli failed')
            my_output.default('%s\n%s' % (str(output), str(error)))
        return False

    if my_output is not None:
        my_output.default('%s\n%s' % (str(output), str(error)))

    return True


def print_subscription(subscription, my_output, brief=False):
    if my_output is None:
        return
    
    if brief:
        my_output.default('Subscription %s %s' % (subscription['package'], my_output.add_color('found', 'Green')))
        return
    
    try:
        subscription['__Output']['installplan.approvedTick'] = subscription['installplan']['__Output']['approvedTick']
    except BaseException:
        pass
    
    dictionary(
        my_output, 
        'Operator',
        subscription,
        [
            ['subscription', 'namespace_name'],
            ['package', 'packageT'],
            ['channel', 'channel'],
            ['install plan', 'install_planT'],
            ['install plan approved', 'installplan.approvedTick'],
            ['installed csv', 'csvT'],
            ['latest_csv', 'csvTick']
        ],
        underline=False,
        start='\n'
    )


def get_subscription(k8s_handler, package, my_output=None, output_on_error_only=False, brief=False, cache_enabled=False):
    subscription = k8s_handler.get_subscription_by_package(
        package,
        csv_info=True,
        plan_info=True,
        return_mo=False,
        cache_enabled=cache_enabled
    )
    if subscription is None:
        if my_output is not None:
            my_output.default('Subscription %s: %s' % (my_output.add_color('not found', 'Red'), package))
        return None

    if not output_on_error_only:
        print_subscription(subscription, my_output, brief=brief)
    return subscription


def is_cluster_ready(cluster, mcp=True, node=True, co=True, verbose=True):
    params = {}
    params['cluster'] = cluster
    params['mcp'] = mcp
    params['node'] = node
    params['co'] = co
    params['verbose'] = verbose
    return cluster_ready.run(params)


def check_parameters(params, rules, extras=None, nested={}):
    allowed_keys = []
    if extras is not None:
        for key in extras:
            allowed_keys.append(key)

    if '__variables__' not in params:
        params['__variables__'] = {}
    
    for rule in rules:
        (name, none_allowed, cast_if_none, expected_type, range_min, range_max, allowed_values, variables) = rule
        if variables is None:
            variables = {}

        for global_var in params['__variables__']:
            if global_var not in variables:
                variables[global_var] = params['__variables__'][global_var]
                
        allowed_keys.append(name)
        success, params[name] = check_paramater(
            params,
            name,
            none_allowed=none_allowed,
            cast_if_none=cast_if_none,
            expected_type=expected_type,
            range_min=range_min,
            range_max=range_max,
            allowed_values=allowed_values,
            variables=variables
        )
        if not success:
            return False, params[name], None
    
        if expected_type == 'list-of-dict' and name in nested:
            new_value = []
            for item in params[name]:
                new_item = {}
                for nested_rule in nested[name]:
                    (nested_name, nested_none_allowed, nested_cast_if_none, nested_expected_type, nested_range_min, nested_range_max, nested_allowed_values, nested_variables) = nested_rule
                    success, new_item[nested_name] = check_paramater(
                        item,
                        nested_name,
                        none_allowed=nested_none_allowed,
                        cast_if_none=nested_cast_if_none,
                        expected_type=nested_expected_type,
                        range_min=nested_range_min,
                        range_max=nested_range_max,
                        allowed_values=nested_allowed_values,
                        variables=nested_variables
                    )
                    if not success:
                        return False, 'parameter %s member error: %s' % (name, new_item[nested_name]), None

                new_value.append(
                    new_item
                )

            params[name] = new_value

    if 'initialize' not in params:
        params['initialize'] = True

    if 'silent' not in params:
        params['silent'] = False

    if 'wait' not in params:
        params['wait'] = True

    if 'verbose' not in params:
        params['verbose'] = False

    if not isinstance(params['verbose'], bool):
        return None, 'verbose param must be true or false'
    
    if 'check-verbose' not in params:
        params['check-verbose'] = params['verbose']

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'

    if 'confirmation' not in params:
        params['confirmation'] = True

    allowed_keys.append('initialize')
    allowed_keys.append('silent')
    allowed_keys.append('wait')
    allowed_keys.append('verbose')
    allowed_keys.append('check-verbose')
    allowed_keys.append('confirmation')

    return True, params, allowed_keys


def check_paramater(
        params, 
        name, 
        none_allowed=False, 
        cast_if_none=None,
        expected_type=None, 
        range_min=None, 
        range_max=None, 
        allowed_values=None, 
        variables=None
    ):
    if name not in params:
        params[name] = cast_if_none

    if params[name] is None:
        if none_allowed:
            return True, None
                
        return False, 'Parameter %s required' % (name)
    
    value = params[name]
    if variables is None:
        variables = {}

    if '__id__' in params and params['__id__'] is not None:
        if '__id__' not in variables:
            variables['__id__'] = params['__id__']

    if not none_allowed and value is None:
        return False, 'Parameter %s non-null value required' % (name)

    if expected_type is not None:
        if expected_type == 'str':
            if not isinstance(value, str):
                return False, 'Parameter %s of type str required' % (name)
            
            if allowed_values is not None:
                if value not in allowed_values:
                    return False, 'Parameter %s value %s must be one of: %s' % (name, value, ', '.join(allowed_values))

            value = filter_helper.replace_attributes(value, variables)

        if expected_type == 'ip':
            if not ip_helper.is_valid_ipv4_address(value) and not ip_helper.is_valid_ipv6_address(value):
                return False, 'parameter %s ip address value required' % (name)

        if expected_type == 'mac':
            value = ip_helper.reformat_mac(value)
            if value is None:
                return False, 'parameter %s mac address value required' % (name)
                            
        if expected_type == 'k8s':
            if not isinstance(value, str):
                return False, 'Parameter %s of type str required' % (name)
            
            value = filter_helper.replace_attributes(value, variables)

            if len(value.split('/')) > 2:
                return False, 'Parameter %s in namespace/name or name syntax required' % (name)

        if expected_type == 'file-text':
            if not isinstance(value, str):
                return False, 'Parameter %s string required' % (name)
            
            if file_helper.get_file_text(value) is None:
                return False, 'Parameter %s valid text filename required' % (name)

        if expected_type == 'file-k8s':
            if not isinstance(value, str):
                return False, 'Parameter %s string required' % (name)
            
            content = file_helper.get_file_yaml(value) 
            if content is None:
                return False, 'Parameter %s valid yaml filename required' % (name)
            
            if 'kind' not in content:
                return False, 'Parameter %s valid kube yaml filename required' % (name)

        if expected_type == 'int':
            if not isinstance(value, int):
                return False, 'Parameter %s of type int required' % (name)
            
            if range_min is not None:
                if value < range_min:
                    return False, 'Parameter %s must be ge %s' % (name, range_min)

            if range_max is not None:
                if value > range_max:
                    return False, 'Parameter %s must be le %s' % (name, range_max)
                
        if expected_type == 'bool':
            if not isinstance(value, bool):
                return False, 'Parameter %s of type bool required' % (name)

        if expected_type == 'dict':
            if not isinstance(value, dict):
                return False, 'Parameter %s of type dict required' % (name)
            
            new_item = {}
            for key in value:
                if isinstance(value[key], str):
                    new_item[key] = filter_helper.replace_attributes(value[key], variables)
                else:
                    new_item[key] = value[key]

            value = copy.deepcopy(new_item)

        if expected_type == 'list-of-dict':
            if not isinstance(value, list):
                return False, 'Parameter %s of type list required' % (name)
            
            new_list = []
            for item in value:
                if not isinstance(item, dict):
                    return False, 'Parameter %s list of dict required' % (name)
            
                new_item = {}
                for key in item:
                    if isinstance(item[key], str):
                        new_item[key] = filter_helper.replace_attributes(item[key], variables)
                    else:
                        new_item[key] = item[key]

                new_list.append(new_item)

            value = copy.deepcopy(new_list)

            if range_min is not None:
                if len(value) < range_min:
                    return False, 'Parameter %s must have at least %s entry' % (name, range_min)
                
        if expected_type in ['list-of-str', 'list-of-cidr']:
            if not isinstance(value, list):
                return False, 'Parameter %s of type list required' % (name)
            
            if range_min is not None:
                if len(value) < range_min:
                    return False, 'Parameter %s list with at least %s items required' % (name, range_min)
            
            for item in value:
                if not isinstance(item, str):
                    return False, 'Parameter %s list of str required' % (name)

            new_list = []
            for item in value:
                new_list.append(filter_helper.replace_attributes(item, variables))

            value = copy.deepcopy(new_list)

        if expected_type == 'list-of-cidr':
            for item in value:
                if not ip_helper.is_valid_ipv4_cidr(item) and not ip_helper.is_valid_ipv6_cidr(item):
                    return False, 'cidr list with v4/v6 subnets required'

        if expected_type == 'list-of-ip':
            for item in value:
                if not ip_helper.is_valid_ipv4_address(item) and not ip_helper.is_valid_ipv6_address(item):
                    return False, 'list with v4/v6 addresses required'

        if expected_type == 'list-of-ip-range':
            for item in value:
                if ip_helper.is_valid_ipv4_cidr(item) or ip_helper.is_valid_ipv6_cidr(item):
                    continue

                if len(item.split('-')) != 2:
                    return False, 'list with v4/v6 addresses range required'
                
                if ip_helper.is_valid_ipv4_address(item.split('-')[0]) and ip_helper.is_valid_ipv4_address(item.split('-')[1]):
                    continue
                
                if ip_helper.is_valid_ipv6_address(item.split('-')[0]) and ip_helper.is_valid_ipv6_address(item.split('-')[1]):
                    continue

                return False, 'list with v4/v6 addresses range required'

    return True, value


def sanitize_params(params, allowed_keys, defaults=None):
    new_params = {}
    for key in params:
        if key in allowed_keys:
            new_params[key] = params[key]

    new_params['__default__'] = {}
    if defaults is not None:
        for key in defaults:
            new_params['__default__'][key] = defaults[key]

    if 'k8s_handler' in params:
        new_params['k8s_handler'] = params['k8s_handler']

    if 'ssh_handler' in params:
        new_params['ssh_handler'] = params['ssh_handler']

    return new_params


def workflow_init(params, my_output, log_id, ssh_required=False, cilium_required=False, hide={}):
    if params['verbose']:
        my_output.default('Workflow Parameters', underline=True)
        display_params = copy.deepcopy(params)
        for key in hide:
            if key in display_params and display_params[key] is not None:
                display_params[key] = '*** user defined ***'
        my_output.default(json.dumps(display_params, indent=4), after_newline=True)
    else:
        my_output.debug('Workflow Parameters', underline=True)
        display_params = copy.deepcopy(params)
        my_output.debug(json.dumps(display_params, indent=4), after_newline=True)

    ocp_check_params = {}
    ocp_check_params['cluster'] = params['cluster']
    ocp_check_params['verbose'] = params['check-verbose']
    ocp_params, errors = ocp_check.run(
        ocp_check_params,
        log_id=log_id
    )
    if errors is not None:
        my_output.error(errors)
        return None

    params['k8s_handler'] = ocp_params['data']['ocp_handler'].k8s_handler
    if ssh_required:
        params['ssh_handler'] = get_management_node_ssh_handler(params['cluster'], log_id=log_id)
        if params['ssh_handler'] is None:
            return None

    if cilium_required:
        if not cilium_common.is_cilium(params, my_output):
            return None

    return params
