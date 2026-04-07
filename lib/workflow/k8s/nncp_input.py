from lib import ip_helper


def get_nncp_input_data_lb(params, my_output):
    params['name'] = my_output.get_input('\nLinux bridge name: ')
    if len(params['name']) == 0:
        return None
    
    params['state'] = my_output.select_from_list(
        'State',
        ['up', 'absent'],
        default='up'
    )
    if params['state'] is None:
        return None
    
    if params['state'] == 'up':
        stp = my_output.select_from_list(
            'Spanning Tree Protocol',
            ['true', 'false'],
            default='true'
        )
        if stp == 'true':
            params['stp'] = True
        else:
            params['stp'] = False

        params['port'] = my_output.get_input('\nUpstream interface: ')
        if len(params['port']) == 0:
            return None
                
        params['ipv4'] = my_output.get_input('\nIPv4 (none, dhcp, cidrv4): ')
        if len(params['ipv4']) == 0:
            return None

        if params['ipv4'] not in ['none', 'dhcp']:
            if not ip_helper.is_valid_ipv4_cidr(params['ipv4']):
                my_output.error('Invalid IPv4 CIDR')
                return None

    return params


def get_nncp_input_data_eth(params, my_output):
    params['name'] = my_output.get_input('\nInterface name: ')
    if len(params['name']) == 0:
        return None
    
    params['state'] = my_output.select_from_list(
        'State',
        ['up', 'down'],
        default='up'
    )
    if params['state'] is None:
        return None
    
    params['ipv4'] = my_output.get_input('\nIPv4 (none, dhcp, cidrv4): ')
    if len(params['ipv4']) == 0:
        return None

    if params['ipv4'] not in ['none', 'dhcp']:
        if not ip_helper.is_valid_ipv4_cidr(params['ipv4']):
            my_output.error('Invalid IPv4 CIDR')
            return None
        
    return params


def get_nncp_input_data_bond(params, my_output):
    params['name'] = my_output.get_input('\nInterface name: ')
    if len(params['name']) == 0:
        return None
    
    params['state'] = my_output.select_from_list(
        'State',
        ['up', 'absent'],
        default='up'
    )
    if params['state'] is None:
        return None
    
    if params['state'] == 'up':
        params['mode'] = my_output.select_from_list(
            'Mode',
            ['active-backup', 'balance-xor', '802.3ad']
        )
        if params['mode'] is None:
            return None

        params['port'] = my_output.get_input('\nBond members (comma separated): ')
        if len(params['port']) == 0:
            return None
                
        params['ipv4'] = my_output.get_input('\nIPv4 (none, dhcp, cidrv4): ')
        if len(params['ipv4']) == 0:
            return None

        if params['ipv4'] not in ['none', 'dhcp']:
            if not ip_helper.is_valid_ipv4_cidr(params['ipv4']):
                my_output.error('Invalid IPv4 CIDR')
                return None
            
        mtu = my_output.get_input('\nMTU: ')
        if len(mtu) > 0:
            try:
                params['mtu'] = int(mtu)
            except BaseException:
                my_output.error('Integer expected')
                return None

        params['miimon'] = my_output.get_input('\nMiimon option: ')
        if len(params['miimon']) == 0:
            params['miimon'] = None

    return params


def get_nncp_input_data_vlan(params, my_output):
    params['base'] = my_output.get_input('\nInterface name: ')
    if len(params['base']) == 0:
        return None
    
    params['vlan'] = my_output.get_input('\nVLAN ID: ')
    if len(params['vlan']) == 0:
        return None

    params['state'] = my_output.select_from_list(
        'State',
        ['up', 'absent'],
        default='up'
    )
    if params['state'] is None:
        return None
    
    return params


def get_nncp_input_data_node(k8s_handler, params, my_output):
    supported_nodes = k8s_handler.get_nodes_name()
    supported_nodes.append('__workers__')
    supported_nodes.append('__all__')

    node_selection = my_output.select_from_list(
        'Select target node',
        supported_nodes,
        default='__all__'
    )
    if node_selection is None:
        return None
    
    params['node'] = node_selection
    return params


def run(k8s_handler, my_output):
    params = {}

    params['policy'] = my_output.get_input('\nPolicy name (def: policy): ')
    if len(params['policy']) == 0:
        params['policy'] = 'policy'

    supported_types = ['bond', 'eth', 'lb', 'vlan']
    params['type'] = my_output.select_from_list(
        'Select interface type',
        supported_types
    )
    if params['type'] is None:
        return None

    if params['type'] == 'lb':
        params = get_nncp_input_data_lb(
            params, 
            my_output
        )

    if params['type'] == 'eth':
        params = get_nncp_input_data_eth(
            params, 
            my_output
        )

    if params['type'] == 'vlan':
        params = get_nncp_input_data_vlan(
            params, 
            my_output
        )

    if params['type'] == 'bond':
        params = get_nncp_input_data_bond(
            params, 
            my_output
        )

    params = get_nncp_input_data_node(
        k8s_handler,
        params, 
        my_output
    )
    if params is None:
        return None

    params['delete'] = my_output.select_from_list(
        'Delete policy once applied',
        ['true', 'false'],
        default='false'
    )
    if params['delete'] is None:
        return None

    if params['delete'] == 'true':
        params['delete'] = True
    else:
        params['delete'] = False
    
    data = {}
    data['policy'] = params['policy']
    data['node'] = params['node']
    data['delete'] = params['delete']
    data['check'] = True
    data['interfaces'] = []

    interface_mo = {}
    interface_mo['type'] = params['type']
    for attr in ['name', 'base', 'vlan', 'state', 'ipv4', 'port', 'mode', 'miimon', 'stp', 'mtu']:
        if attr in params:
            interface_mo[attr] = params[attr]

    data['interfaces'].append(
        interface_mo
    )

    return data