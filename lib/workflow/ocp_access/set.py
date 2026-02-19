import os
from lib import output_helper
from lib.ocp import settings
from lib import ip_helper


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if params['cluster'] is None:
        return None, 'Cluster name required'
    
    if 'domain' not in params:
        params['domain'] = None

    if 'kubeconfig_filename' not in params:
        params['kubeconfig_filename'] = None

    if 'ssh_public_key_filename' not in params:
        params['ssh_public_key_filename'] = None

    if 'management_ip' not in params:
        params['management_ip'] = None

    return params, None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)

    params, error = validate(params)
    if params is None:
        my_output.error(error)
        return False

    settings_handler = settings.OcpSettings(log_id=log_id)

    my_output.default('OpenShift Cluster', before_newline=True, underline=True)

    cluster_settings = settings_handler.get_ocp_cluster(params['cluster'], strict_match=False)
    if cluster_settings is None:
        my_output.default('- new cluster: %s' % (params['cluster']))
        if params['kubeconfig_filename'] is None:
            my_output.error('Define OCP kubeconfig filename for new cluster')
            return False

        if not os.path.isfile(params['kubeconfig_filename']):
            my_output.error('Kubeconfig file not found')
            return False

        success = settings_handler.create_ocp_cluster(
            params['cluster'],
            params['kubeconfig_filename']
        )
        if not success:
            my_output.error('Failed to create ocp cluster kubeconfig')
            return False

        my_output.default('- kubeconfig set')

    if cluster_settings is not None:
        my_output.default('- existing cluster: %s' % (params['cluster']))
        if params['kubeconfig_filename'] is None:
            if settings_handler.is_kubeconfig(params['cluster']):
                my_output.default('- kubeconfig not modified')
            else:
                my_output.default(my_output.add_color('- kubeconfig not modified and currently unset', 'Red'))

    if cluster_settings is not None and params['kubeconfig_filename'] is not None:
        success = settings_handler.set_ocp_cluster_kubeconfig(
            params['cluster'],
            params['kubeconfig_filename']
        )
        if not success:
            my_output.error('Failed to update ocp cluster kubeconfig')
            return False

        my_output.default('- kubeconfig set')

    if params['ssh_public_key_filename'] is None:
        if settings_handler.is_management_ssh_pub(params['cluster']):
            my_output.default('- ssh public key not modified')
        else:
            my_output.default('- ssh public key not modified and currently unset')

    if params['ssh_public_key_filename'] is not None:
        if not os.path.isfile(params['ssh_public_key_filename']):
            my_output.error('SSH public key file not found')
            return False

        if not settings_handler.set_management_ssh_pub(params['cluster'], params['ssh_public_key_filename']):
            my_output.error('Failed to set ssh public key')
            return False

        my_output.default('- ssh public key set')

    if params['management_ip'] is None:
        if settings_handler.is_management_ip(params['cluster']):
            my_output.default('- management ip not modified')
        else:
            my_output.default('- management ip not modified and currently unset')
            
    if params['management_ip'] is not None:
        if not ip_helper.is_valid_ipv4_address(params['management_ip']):
            my_output.error('Invalid IPv4 address: %s' % (params['management_ip']))
            return False
        
        if not settings_handler.set_management_ip(params['cluster'], params['management_ip']):
            my_output.error('Failed to set management address')
            return False

        my_output.default('- management host ip address set')

    if params['domain'] is None:
        if settings_handler.is_domain(params['cluster']):
            my_output.default('- domain not modified')
        else:
            my_output.default('- domain not modified and currently unset')
            
    if params['domain'] is not None:
        if not settings_handler.set_domain(params['cluster'], params['domain']):
            my_output.error('Failed to set cluster domain')
            return False

        my_output.default('- domain set')

    return True
