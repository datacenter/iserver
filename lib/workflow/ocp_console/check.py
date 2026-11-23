import os
import json
from lib import output_helper
from lib.ocp import settings
from lib.ocp import main as ocp
from lib import ssh
from lib.linux import main as linux
from lib import ip_helper


def validate(params, log_id):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'verbose' not in params:
        params['verbose'] = False

    if 'break-on-error' not in params:
        params['break-on-error'] = True

    if 'fqdn-check' not in params:
        params['fqdn-check'] = False

    if 'kc-check' not in params:
        params['kc-check'] = True

    if 'kc-required' not in params:
        params['kc-required'] = params['kc-check']

    if 'kube-api-check' not in params:
        params['kube-api-check'] = True

    if 'kube-api-required' not in params:
        params['kube-api-required'] = params['kube-api-check']

    if params['kube-api-check']:
        params['kc-check'] = True
        params['kc-required'] = True
        params['break-on-error'] = True

    if 'fqdn-check' not in params:
        params['fqdn-check'] = True

    if 'fqdn-required' not in params:
        params['fqdn-required'] = params['fqdn-check']

    if 'ssh-fixup' in params and params['ssh-fixup']:
        params['ssh-check'] = True
        params['ssh-required'] = True
        params['ssh-fixup'] = True

    if 'ssh-required' in params and params['ssh-required']:
        params['ssh-check'] = True
        params['ssh-required'] = True

    if 'ssh-check' not in params:
        params['ssh-check'] = False

    if 'ssh-required' not in params:
        params['ssh-required'] = params['ssh-check']

    if 'ssh-fixup' not in params:
        params['ssh-fixup'] = False

    if 'mgmt-fixup' in params and params['mgmt-fixup']:
        params['ssh-check'] = True
        params['ssh-required'] = True
        params['ssh-fixup'] = True
        params['mgmt-check'] = True
        params['mgmt-required'] = True
        params['mgmt-fixup'] = True

    if 'mgmt-required' in params and params['mgmt-required']:
        params['ssh-check'] = True
        params['ssh-required'] = True
        params['mgmt-check'] = True
        params['mgmt-required'] = True

    if 'mgmt-check' not in params:
        params['mgmt-check'] = False

    if 'mgmt-required' not in params:
        params['mgmt-required'] = params['mgmt-check']

    if 'mgmt-fixup' not in params:
        params['mgmt-fixup'] = False

    if 'cli-check' not in params:
        params['cli-check'] = False

    if 'cli-cilium-required' in params and params['cli-cilium-required']:
        params['cli-cilium-check'] = True
        params['cli-cilium-required'] = True

    if 'cli-cilium-check' not in params:
        params['cli-cilium-check'] = params['cli-check']

    if 'cli-cilium-required' not in params:
        params['cli-cilium-required'] = False

    if 'cli-cilium-fixup' not in params:
        params['cli-cilium-fixup'] = False

    if params['cli-cilium-check']:
        params['mgmt-check'] = True
        params['break-on-error'] = True

    if 'cli-helm-required' in params and params['cli-helm-required']:
        params['cli-helm-check'] = True
        params['cli-helm-required'] = True

    if 'cli-helm-check' not in params:
        params['cli-helm-check'] = params['cli-check']

    if 'cli-helm-required' not in params:
        params['cli-helm-required'] = False

    if 'cli-helm-fixup' not in params:
        params['cli-helm-fixup'] = False

    if params['cli-helm-check']:
        params['mgmt-check'] = True
        params['break-on-error'] = True

    if 'cli-virtctl-required' in params and params['cli-virtctl-required']:
        params['cli-virtctl-check'] = True
        params['cli-virtctl-required'] = True

    if 'cli-virtctl-check' not in params:
        params['cli-virtctl-check'] = params['cli-check']

    if 'cli-virtctl-required' not in params:
        params['cli-virtctl-required'] = False

    if 'cli-virtctl-fixup' not in params:
        params['cli-virtctl-fixup'] = False

    if params['cli-virtctl-check']:
        params['mgmt-check'] = True
        params['break-on-error'] = True

    if 'cli-hubble-required' in params and params['cli-hubble-required']:
        params['cli-hubble-check'] = True
        params['cli-hubble-required'] = True

    if 'cli-hubble-check' not in params:
        params['cli-hubble-check'] = params['cli-check']

    if 'cli-hubble-required' not in params:
        params['cli-hubble-required'] = False

    if 'cli-hubble-fixup' not in params:
        params['cli-hubble-fixup'] = False

    if params['cli-hubble-check']:
        params['mgmt-check'] = True
        params['break-on-error'] = True

    params['data'] = {}
    params['data']['log_id'] = log_id
    return params, None


def check_kubeconfig(params, settings_handler):
    if not params['kc-check']:
        return params, None
    
    params['data']['kubeconfig_filename'] = settings_handler.get_ocp_cluster_kubeconfig_filename(params['cluster'])
    if not os.path.isfile(params['data']['kubeconfig_filename']):
        return params, 'Kubeconfig file not found: %s' % (params['data']['kubeconfig_filename'])
    
    return params, None


def check_kube_api(params, my_output):
    if not params['kube-api-check']:
        return params, None
    
    params['data']['ocp_handler'] = ocp.Ocp(
        params['cluster'],
        verbose=False,
        debug=False,
        log_id=params['data']['log_id']
    )
    params['data']['node_ip'] = params['data']['ocp_handler'].k8s_handler.get_any_worker_node_ip()
    if params['data']['node_ip'] is None:
        return params, 'K8s api fails'
    
    node_names = params['data']['ocp_handler'].k8s_handler.get_nodes_name()
    params['data']['nodes'] = {}
    for node_name in node_names:
        params['data']['nodes'][node_name] = params['data']['ocp_handler'].k8s_handler.get_node_ip(node_name)

    if params['verbose']:
        my_output.default(
            '- api [%s]: %s' % (
                params['data']['kubeconfig_filename'],
                my_output.add_color('ok', 'Green'),
            )
        )

    return params, None


def check_fqdn(params, settings_handler, my_output):
    if not params['kube-api-check']:
        return params, None

    if not settings_handler.is_etc_hosts(params['cluster']):
        config_info = params['data']['ocp_handler'].k8s_handler.get_ingress_config()
        if config_info is None:
            return params, 'Failed to get cluster ingress configuration'
        
        if config_info['info']['domain'] is None:
            return params, 'Failed to get cluster ingress domain'

        infra_info = params['data']['ocp_handler'].k8s_handler.get_infrastructure_cluster_config()
        if infra_info is None:
            return params, 'Failed to get cluster infrastructure configuration'

        if infra_info['api_ip'] is None:
            return params, 'Failed to get cluster api vip'

        if infra_info['ingress_ip'] is None:
            return params, 'Failed to get cluster api vip'

        if infra_info['api_hostname'] is None:
            return params, 'Failed to get cluster api hostname'

        entries = '%s\t%s' % (
            infra_info['api_ip'],
            infra_info['api_hostname']
        )

        keys = [
            'oauth-openshift',
            'console-openshift-console',
            'grafana-openshift-monitoring',
            'thanos-querier-openshift-monitoring',
            'prometheus-k8s-openshift-monitoring',
            'alertmanager-main-openshift-monitoring',
            'hyperconverged-cluster-cli-download-openshift-cnv'
        ]
        for key in keys:
            entries = '%s\n%s\t%s.%s' % (
                entries,
                infra_info['ingress_ip'],
                key,
                config_info['info']['domain']
            )

        if not settings_handler.set_etc_hosts(params['cluster'], entries):
            return params, 'Failed to set etc_hosts entries'

    success, etc_hosts = settings_handler.check_etc_hosts(params['cluster'])
    if not success:
        failed = []
        if etc_hosts is not None:
            for item in etc_hosts:
                if not item['resolved']:
                    failed.append('FQDN [%s] <=> IP [%s]' % (item['address'], item['fqdn']))

        return params, 'DNS resolution failed: %s' % (','.join(failed))

    if params['verbose']:
        my_output.default('- dns resolution: %s' % (my_output.add_color('ok', 'Green')))

    return params, None


def check_ssh(params, settings_handler, my_output):
    if not params['ssh-check']:
        return params, None
    
    params['data']['ssh_public_key_filename'] = settings_handler.get_management_ssh_pub_filename(params['cluster'])
    params['data']['ssh_public_key'] = settings_handler.get_management_ssh_pub(params['cluster'])

    if params['data']['ssh_public_key'] is None:
        if not params['ssh-required']:
            my_output.default('- ssh public key: %s' % (my_output.add_color('undefined', 'Yellow')))
            return params, None
        
        if not params['ssh-fixup']:
            return params, 'SSH public key undefined'
        
        my_output.error('SSH public key undefined')
        filename = input('Define filename: ')
        if not os.path.isfile(filename):
            return params, 'SSH public key undefined'

        if not settings_handler.set_management_ssh_pub(params['cluster'], filename):
            return params, 'Failed to configure management ssh public key'

    if 'node_ip' not in params['data'] or params['data']['node_ip'] is None:
        return params, 'Cluster node ip undefined - ssh cannot be verified'

    ssh_handler = ssh.Ssh(
        params['data']['node_ip'], 
        'core', 
        key_filename=params['data']['ssh_public_key_filename']
    )
    success, exception_name, error = ssh_handler.is_ssh()
    if not success:
        return params, 'SSH access to cluster node [%s] failed [%s]' % (params['data']['node_ip'], exception_name)
    
    if params['verbose']:
        my_output.default('- cluster node [%s] [key:%s]: %s' % (params['data']['node_ip'], params['data']['ssh_public_key_filename'], my_output.add_color('ok', 'Green')))

    return params, None


def check_management(params, settings_handler, my_output):
    if not params['mgmt-check']:
        return params, None
    
    params['data']['management_ip'] = settings_handler.get_management_ip(params['cluster'])
    if params['data']['management_ip'] is None:
        if not params['mgmt-required']:
            my_output.default('- management node: %s' % (my_output.add_color('undefined', 'Yellow')))
            return params, None
        
        if not params['mgmt-fixup']:
            return params, 'Management host ip undefined'

        my_output.error('Management host ip undefined')
        management_ip = input('Define ip: ')
        if not ip_helper.is_valid_ipv4_address(management_ip):
            my_output.error('Invalid IPv4 address')
            return params, 'Management host ip undefined'

        if not settings_handler.set_management_ip(params['cluster'], management_ip):
            return params, 'Failed to configure management ip address'
        
        params['data']['management_ip'] = management_ip

    params['data']['ssh_public_key'] = settings_handler.get_management_ssh_pub(params['cluster'])
    params['data']['ssh_public_key_filename'] = settings_handler.get_management_ssh_pub_filename(params['cluster'])

    if params['data']['ssh_public_key'] is None:
        return params, 'SSH public key undefined'
    
    params['data']['management_handler'] = ssh.Ssh(
        params['data']['management_ip'], 
        'core', 
        key_filename=params['data']['ssh_public_key_filename']
    )
    if not params['data']['management_handler'].is_ssh():
        return params, 'SSH access to management [%s] failed' % (params['data']['management_ip'])
    
    if params['verbose']:
        my_output.default('- management node [%s] [key:%s]: %s' % (params['data']['management_ip'], params['data']['ssh_public_key_filename'], my_output.add_color('ok', 'Green')))

    params['data']['management_linux_handler'] = linux.Linux(
        params['data']['management_ip'], 
        'core', 
        key_filename=params['data']['ssh_public_key_filename']
    )
    if not params['data']['management_linux_handler'].ssh_handler.is_ssh():
        return params, 'SSH (linux) access to management [%s] failed' % (params['data']['management_ip'])

    return params, None


def check_cli_helm(params, my_output):
    if not params['cli-helm-check']:
        return params, None
    
    if 'management_handler' not in params['data']:
        if not params['mgmt-required']:
            return params, None
        
        return params, 'Helm cannot be checked - no management node access'
    
    success, output, error = params['data']['management_handler'].run_cmd('helm help')
    if not success:
        if not params['cli-helm-required']:
            my_output.default('- cli helm: %s' % my_output.add_color('not found', 'Yellow'))
            return params, None

        return params, 'Helm not found'
    
    if params['verbose']:
        my_output.default('- cli helm: %s' % my_output.add_color('ok', 'Green'))

    return params, None


def check_cli_virtctl(params, my_output):
    if not params['cli-virtctl-check']:
        return params, None

    if 'management_handler' not in params['data']:
        if not params['mgmt-required']:
            return params, None
        
        return params, 'Virtctl cannot be checked - no management node access'
    
    success, output, error = params['data']['management_handler'].run_cmd('virtctl help')
    if not success:
        if not params['cli-virtctl-required']:
            my_output.default('- cli virtctl: %s' % my_output.add_color('not found', 'Yellow'))
            return params, None

        return params, 'Virtctl not found'
    
    if params['verbose']:
        my_output.default('- cli virtctl: %s' % my_output.add_color('ok', 'Green'))

    return params, None


def check_cli_cilium(params, my_output):
    if not params['cli-cilium-check']:
        return params, None
    
    if 'management_handler' not in params['data']:
        if not params['mgmt-required']:
            return params, None
        
        return params, 'Cilium cannot be checked - no management node access'
    
    success, output, error = params['data']['management_handler'].run_cmd('cilium help')
    if not success:
        if not params['cli-cilium-required']:
            my_output.default('- cli cilium: %s' % my_output.add_color('not found', 'Yellow'))
            return params, None

        return params, 'Cilium not found'
    
    if params['verbose']:
        my_output.default('- cli cilium: %s' % my_output.add_color('ok', 'Green'))

    return params, None


def check_cli_hubble(params, my_output):
    if not params['cli-hubble-check']:
        return params, None
    
    if 'management_handler' not in params['data']:
        if not params['mgmt-required']:
            return params, None
        
        return params, 'Hubble cannot be checked - no management node access'
    
    success, output, error = params['data']['management_handler'].run_cmd('hubble help')
    if not success:
        if not params['cli-hubble-required']:
            my_output.default('- cli hubble: %s' % my_output.add_color('not found', 'Yellow'))
            return params, None

        return params, 'Hubble not found'
    
    if params['verbose']:
        my_output.default('- cli hubble: %s' % my_output.add_color('ok', 'Green'))

    return params, None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)

    params, error = validate(params, log_id)
    if params is None:
        return None, [error]

    settings_handler = settings.OcpSettings(log_id=log_id)

    cluster_settings = settings_handler.get_ocp_cluster(params['cluster'], strict_match=False)
    if cluster_settings is None:
        return None, ['Cluster not found: %s' % (params['cluster'])]
    
    if params['verbose']:
        my_output.default('OpenShift Cluster', before_newline=True, underline=True)
        if cluster_settings['domain'] is not None:
            my_output.default('- cluster: %s [domain:%s]' % (my_output.add_color(params['cluster'], 'Blue'), cluster_settings['domain']))
        else:
            my_output.default('- cluster: %s' % (my_output.add_color(params['cluster'], 'Blue')))

    errors = []

    params, error = check_kubeconfig(params, settings_handler)
    if error is not None:
        errors.append(error)
        if params['kc-required'] or params['break-on-error']:
            return None, errors

    params, error = check_kube_api(params, my_output)
    if error is not None:
        errors.append(error)
        if params['kube-api-required'] or params['break-on-error']:
            return None, errors

    params, error = check_fqdn(params, settings_handler, my_output)
    if error is not None:
        errors.append(error)
        if params['fqdn-required'] or params['break-on-error']:
            return None, errors

    params, error = check_ssh(params, settings_handler, my_output)
    if error is not None:
        errors.append(error)
        if params['ssh-required'] or params['break-on-error']:
            return None, errors

    params, error = check_management(params, settings_handler, my_output)
    if error is not None:
        errors.append(error)
        if params['mgmt-required'] or params['break-on-error']:
            return None, errors

    params, error = check_cli_helm(params, my_output)
    if error is not None:
        if not params['helm-cli-required']:
            if params['verbose']:
                my_output.default('- helm: not found')

        if params['helm-cli-required']:
            errors.append(error)
            if params['break-on-error']:
                return None, errors
            
    params, error = check_cli_virtctl(params, my_output)
    if error is not None:
        if not params['virtctl-cli-required']:
            if params['verbose']:
                my_output.default('- virtctl: not found')

        if params['virtctl-cli-required']:
            errors.append(error)
            if params['break-on-error']:
                return None, errors
            
    params, error = check_cli_cilium(params, my_output)
    if error is not None:
        if not params['cilium-cli-required']:
            if params['verbose']:
                my_output.default('- cilium: not found')

        if params['cilium-cli-required']:
            errors.append(error)
            if params['break-on-error']:
                return None, errors

    params, error = check_cli_hubble(params, my_output)
    if error is not None:
        if not params['hubble-cli-required']:
            if params['verbose']:
                my_output.default('- hubble: not found')

        if params['hubble-cli-required']:
            errors.append(error)
            if params['break-on-error']:
                return None, errors
    
    my_output.default('')
    return params, None
