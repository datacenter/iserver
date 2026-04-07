from lib import output_helper
from lib.k8s import output as k8s_output
from lib.linux import main as linux
from lib.workflow import ocp_common as workflow_common


def get_interfaces(params, my_output, log_id, node_name_filter=None):
    my_output.default('Get interface details', before_newline=True, underline=True)

    node_ip = params['k8s_handler'].get_nodes_ip()

    interfaces = {}
    for node_name in node_ip:
        if node_name_filter is not None and node_name != node_name_filter:
            continue

        my_output.default('- node [%s]' % (node_name))
        interfaces[node_name], error = get_node_ethernet_details(
            params['k8s_handler'],
            params['cluster'],
            node_name,
            node_ip[node_name],
            my_output,
            log_id
        )

        if interfaces[node_name] is None:
            return None, error

    return interfaces, None


def get_node_ethernet_details(k8s_handler, cluster_name, node_name, node_ip, my_output, log_id):
    key_filename = workflow_common.get_ocp_cluster_filename(cluster_name, log_id=log_id)
    if key_filename is None:
        return None, 'Node ssh public key not found'

    nns = k8s_handler.wait_node_network_state(node_name)
    if nns is None:
        return None, 'Node network state collection failed'

    linux_handler = linux.Linux(
        node_ip,
        'core',
        key_filename=key_filename,
        log_id=log_id
    )

    ethernet_ifs = []

    for interface in nns['interface']:
        my_output.default('\tinterface: %s' % (interface['name']))
        if interface['type'] != 'ethernet':
            continue

        if interface['state'] == 'ignore':
            continue

        ethernet_if = {}
        ethernet_if['linux_handler'] = linux_handler
        ethernet_if['name'] = interface['name']
        ethernet_if['lldp_configurable'] = False
        ethernet_if['lldp_enabled'] = False
        if 'lldp_enabled' in interface:
            ethernet_if['lldp_configurable'] = True
            ethernet_if['lldp_enabled'] = interface['lldp_enabled']

        my_output.default('\t\tethtool')
        ethernet_if['params'] = linux_handler.get_inteface_ethtool(interface['name'])
        if ethernet_if['params'] is None:
            return None, 'Ethtool failed on %s' % (interface['name'])

        my_output.default('\t\tlspci')
        ethernet_if['lspci'] = linux_handler.get_inteface_lspci(ethernet_if['params']['bus-info'])
        if ethernet_if['lspci'] is None:
            return None, 'lspci failed on %s' % (interface['name'])

        my_output.default('\t\tpriv flags')
        ethernet_if['flags'] = None
        if 'Intel' in ethernet_if['lspci']:
            ethernet_if['flags'] = linux_handler.get_inteface_ethtool_priv_flags(interface['name'])

        my_output.default('\t\tstate')
        ethernet_if['state'] = linux_handler.get_interface_by_name(
            interface['name']
        )

        ethernet_ifs.append(
            ethernet_if
        )

    return ethernet_ifs, None


def configure_node(node_name, interfaces, log_id):
    # https://edc.intel.com/content/www/us/en/design/products/ethernet/adapters-and-devices-user-guide/firmware-link-layer-discovery-protocol-fw-lldp/
    my_output = output_helper.OutputHelper(log_id=log_id)

    my_output.default('Disable lldp on ethernet interface fw level [%s]' % (node_name))

    for interface in interfaces:
        my_output.debug('Interface state %s' % (interface['name']))
        my_output.debug('- driver: %s' % (interface['params']['driver']))
        my_output.debug('- version: %s' % (interface['params']['version']))
        my_output.debug('- pci: %s' % (interface['params']['bus-info']))
        my_output.debug('- vendor: %s' % (interface['lspci'].split('Ethernet controller: '))[1])

        is_action = False
        if interface['flags'] is not None:
            if 'fw-lldp-agent' in interface['flags']:
                my_output.debug('- fw-lldp-agent: %s' % (interface['flags']['fw-lldp-agent']))
                if interface['flags']['fw-lldp-agent'] == 'on':
                    is_action = True
                    my_output.default('Action: set fw-lldp-agent to off')
                    interface['linux_handler'].set_inteface_ethtool_priv_flags(
                        interface['name'],
                        'fw-lldp-agent',
                        'off'
                    )

            if 'disable-fw-lldp' in interface['flags']:
                my_output.debug('- disable-fw-lldp: %s' % (interface['flags']['disable-fw-lldp']))
                if interface['flags']['disable-fw-lldp'] == 'off':
                    is_action = True
                    my_output.default('Action: set disable-fw-lldp to on')
                    interface['linux_handler'].set_inteface_ethtool_priv_flags(
                        interface['name'],
                        'disable-fw-lldp',
                        'on'
                    )

        if is_action:
            my_output.default('Interface %s [%s] - fw lldp disabled' % (interface['name'], interface['params']['bus-info']))
        else:
            my_output.default('Interface %s [%s] - no change' % (interface['name'], interface['params']['bus-info']))


def configure_nic(params, log_id=None):
    node_ip = params['k8s_handler'].get_nodes_ip()
    for node_name in node_ip:
        configure_node(
            node_name,
            params['interfaces'][node_name],
            log_id
        )


def enable_nns(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)

    params['success'] = True
    params['error'] = None
    policy_names = []
    for node_name in params['interfaces']:
        my_output.default('Enable lldp on nmstate level [%s]' % (node_name))

        for interface in params['interfaces'][node_name]:
            if not params['settings']['include-down'] and not interface['state']['up']:
                my_output.default('Interface %s - skip on interface oper down' % (interface['name']))
                continue

            if not interface['lldp_configurable']:
                my_output.default('Interface %s - lldp not configurable' % (interface['name']))
                continue

            if interface['lldp_enabled']:
                my_output.default('Interface %s - already enabled' % (interface['name']))
                continue

            success, policy_name = params['k8s_handler'].set_nncp_interface_lldp_enabled(
                interface['name'],
                node_name=node_name,
                wait=False
            )
            if not success:
                params['success'] = False
                params['error'] = 'Failed to create nncp for %s:%s' % (node_name, interface['name'])
                return params

            my_output.default('Interface %s - enabling with nncp (%s)' % (interface['name'], policy_name))
            policy_names.append(
                policy_name
            )

    if len(policy_names) == 0:
        return params

    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    object_filter = ['names:%s' % (','.join(policy_names))]
    policies = params['k8s_handler'].get_node_network_configuration_policies(object_filter=object_filter, cache_enabled=False)
    if policies is not None:
        k8s_output_handler.print_node_network_configuration_policys_state(policies)

    success = params['k8s_handler'].wait_node_network_configuration_policies_status(
        policy_names=policy_names,
        my_output=my_output
    )
    if not success:
        my_output.error('Not all nncp finished in time')

    policies = params['k8s_handler'].get_node_network_configuration_policies(object_filter=object_filter, cache_enabled=False)
    if policies is not None:
        k8s_output_handler.print_node_network_configuration_policys_state(policies)

    if not params['settings']['delete-nncp']:
        my_output.default('Node network policies not deleted (based on user flag)')

    if params['settings']['delete-nncp']:
        my_output.default('All policies are deleted (except for progressing if any)...')
        for policy in policy_names:
            policy_info = params['k8s_handler'].get_node_network_configuration_policy(policy)
            if policy_info is None or policy_info['status'] == 'Progressing':
                my_output.default('- %s [Skipping]' % policy)
            else:
                success = params['k8s_handler'].delete_node_network_configuration_policy_mo(policy)
                if success:
                    my_output.default('- %s [Deleted]' % policy)
                else:
                    my_output.default('- %s [ERROR]' % policy)

    return params
