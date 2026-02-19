# Useful links
# https://cloudcult.dev/creating-openshift-clusters-with-the-assisted-service-api/
# https://cloudcult.dev/static-networking-with-assisted-installer/
# https://cloudcult.dev/calico-installation-openshift-assisted-installer/
# https://cloudcult.dev/cilium-installation-openshift-assisted-installer/
# https://api.openshift.com/?urls.primaryName=assisted-service%20service#/
# https://api.openshift.com/api/assisted-install/v2/openapi

import json
from lib import ip_helper
from lib import output_helper
from lib.workflow import ocp_common
from lib.workflow.ocp_bm_install import common as ocp_bm_common
from lib.workflow.ocp_bm_install import input as install_input
from lib.workflow.ocp_bm_install import install
from lib.workflow.ocp_bm_install import post as install_post
from lib.workflow.ocp_task import create as task
from menu import common


def run(location, log_id, install_mode, offline=False):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Bare Metal Installation', before_newline=True, after_newline=True, double_underline=True)

    user_settings, data, infra, manifests = install_input.run(
        location,
        install_mode,
        log_id=log_id,
        offline=offline
    )
    if user_settings is None:
        my_output.error('Some checks failed')
        return False

    if not offline:
        success = ocp_common.check_cluster_init_fqdn(user_settings, my_output, log_id)
        if not success:
            if not common.get_confirmation():
                return False

    my_output.default('Variables', underline=True, before_newline=True)
    for server in user_settings['server']:
        my_output.default('Server [%s]' % (server['hostname']))
        my_output.default(json.dumps(server['variables'], indent=4), wrap='~~~', before_newline=True)

    my_output.default('Cluster Data', underline=True, before_newline=True)
    my_output.default(json.dumps(data, indent=4))

    my_output.default('Infra Data', underline=True, before_newline=True)
    my_output.default(json.dumps(infra, indent=4))

    for network_config in infra['static_network_config']:
        hostname = None
        for server in user_settings['server']:
            for server_mac in server['interface_macs']:
                for interface_map in network_config['mac_interface_map']:
                    if ip_helper.is_mac_equal(server_mac, interface_map['mac_address']):
                        hostname = server['hostname']
                        break

                if hostname is not None:
                    break
        
        if hostname is None:
            my_output.error('Consistency check failed - cannot find server for network config interfaces')
            for interface_map in network_config['mac_interface_map']:
                my_output.default('- [%s] %s' % (interface_map['logical_nic_name'], interface_map['mac_address']))
            return False

        my_output.default('NMState [%s]' % (hostname), underline=True, before_newline=True)
        for interface_map in network_config['mac_interface_map']:
            my_output.default('- [%s] %s' % (interface_map['logical_nic_name'], interface_map['mac_address']))

        my_output.default(network_config['network_yaml'].replace('\r\n', '\n'), wrap='~~~', before_newline=True)

    if install_mode == 'check':
        my_output.default('All checks passed', before_newline=True, after_newline=True)
        return True
    
    cluster_id = install.run(
        user_settings,
        data,
        infra,
        manifests,
        log_id=log_id
    )
    if cluster_id is None:
        return False

    success = install_post.run(
        user_settings,
        cluster_id,
        log_id
    )
    if not success:
        return False

    success = ocp_bm_common.save_management_ip(
        user_settings['connector'],
        user_settings['management_ip'],
        log_id
    )
    if not success:
        my_output.error('Failed to save management ip information')
        return False

    success = task.run(
        user_settings['tasks'], 
        user_settings['name'], 
        confirmation=False, 
        cluster_settings=user_settings
    )
    if not success:
        return False

    return True
