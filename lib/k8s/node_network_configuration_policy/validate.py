import json
import copy
from lib import ip_helper


class K8sNodeNetworkConfigurationPolicyValidate():
    def __init__(self):
        pass

    def check_route(self, item, check, node, my_output):
        data = {}

        if 'destination' not in item:
            my_output.error('destination attribute expected')
            my_output.default(json.dumps(item))
            return None

        if not ip_helper.is_valid_ipv4_cidr(item['destination']):
            my_output.error('destination cidrv4 expected')
            my_output.default(json.dumps(item))
            return None

        data['destination'] = item['destination']

        data['gateway'] = None
        if 'gateway' in item:
            if not ip_helper.is_valid_ipv4_address(item['gateway']):
                my_output.error('gateway ipv4 expected')
                my_output.default(json.dumps(item))
                return None

            data['gateway'] = item['gateway']

        data['metric'] = None
        if 'metric' in item:
            try:
                data['metric'] = int(item['metric'])
            except BaseException:
                my_output.error('metric integer value expected')
                my_output.default(json.dumps(item))
                return None

        data['table'] = None
        if 'table' in item:
            try:
                data['table'] = int(item['table'])
            except BaseException:
                my_output.error('table integer value expected')
                my_output.default(json.dumps(item))
                return None

        data['interface'] = None
        if 'interface' in item:
            data['interface'] = item['interface']

        if check and data['interface'] is not None:
            nns = self.get_nncp_input_nns(
                node,
                my_output
            )
            if nns is None:
                return None
            
            my_output.default('Check nns data', underline=True, before_newline=True)
            for item in nns:
                interface_found = False
                for interface_mo in item['interface']:
                    if interface_mo['type'] not in ['ethernet', 'vlan', 'bond']:
                        continue

                    if interface_mo['name'] == data['interface']:
                        interface_found = True
                        break

                if not interface_found:
                    my_output.default(
                        '- [WARNING] %s next-hop interface not found: %s' % (
                            item['name'],
                            data['interface']
                        )
                    )
                
                if interface_found:
                    my_output.default(
                        '- %s next-hop interface found: %s' % (
                            item['name'],
                            data['name']
                        )
                    )

        return data

    def get_nncp_input_nns(self, node, my_output):
        my_output.default('Get nns data', underline=True, before_newline=True)
        node_names = []
        if node == '_all_':
            node_names = self.get_nodes_name()

        if node == '_workers_':
            node_names = self.get_worker_nodes_name()

        if node not in ['_all_', '_workers_']:
            node_names = [node]

        nns = []
        for node_name in node_names:
            node_nns = self.get_node_network_state(node_name)
            if node_nns is None:
                my_output.error('Failed to get nns for node [%s]' % (node_name))
                return None
            
            my_output.default('- %s' % (node_name))
            nns.append(node_nns)

        return nns
    
    def check_nncp_input_eth(self, item, check, node, my_output):
        data = {}
        data['type'] = 'eth'

        if 'name' not in item:
            my_output.error('name attribute expected')
            my_output.default(json.dumps(item))
            return None
        
        data['name'] = item['name']

        if 'state' not in item:
            my_output.error('state attribute expected')
            my_output.default(json.dumps(item))
            return None
        
        if item['state'] not in ['up', 'down']:
            my_output.error('state attribute value up or down expected')
            my_output.default(json.dumps(item))
            return None
        
        data['state'] = item['state']

        data['ipv4'] = None
        if 'ipv4' in item:
            if item['ipv4'] in ['none', 'dhcp']:        
                data['ipv4'] = item['ipv4']
            else:
                if not ip_helper.is_valid_ipv4_cidr(item['ipv4']):
                    my_output.error('ipv4 attribute value none, dhcp or cidrv4 expected')
                    my_output.default(json.dumps(item))
                    return None

                data['ipv4'] = item['ipv4']
      
        if check:
            nns = self.get_nncp_input_nns(
                node,
                my_output
            )
            if nns is None:
                return None
            
            my_output.default('Check nns data', underline=True, before_newline=True)
            for item in nns:
                interface_found = False
                for interface_mo in item['interface']:
                    if interface_mo['type'] not in ['ethernet']:
                        continue

                    if interface_mo['name'] == data['name']:
                        interface_found = True
                        break

                if not interface_found:
                    my_output.default(
                        '- [ERROR] %s ethernet interface not found: %s' % (
                            item['name'],
                            data['name']
                        )
                    )
                    return None

                my_output.default(
                    '- %s ethernet interface found: %s' % (
                        item['name'],
                        data['name']
                    )
                )

        return data

    def check_nncp_input_vlan(self, item, check, node, my_output):
        data = {}
        data['type'] = 'vlan'

        if 'base' not in item:
            my_output.error('base attribute expected')
            my_output.default(json.dumps(item))
            return None
        
        data['base'] = item['base']

        if 'vlan' not in item:
            my_output.error('vlan attribute expected')
            my_output.default(json.dumps(item))
            return None
        
        try:
            vlan_id = int(item['vlan'])
        except BaseException:
            my_output.error('vlan attribute must be integer')
            my_output.default(json.dumps(item))
            return None
        
        data['vlan_id'] = vlan_id

        if 'state' not in item:
            my_output.error('state attribute expected')
            my_output.default(json.dumps(item))
            return None
        
        if item['state'] not in ['up', 'absent']:
            my_output.error('state attribute value up or absent expected')
            my_output.default(json.dumps(item))
            return None
        
        data['state'] = item['state']

        if data['state'] == 'up':
            data['ipv4'] = None
            if 'ipv4' in item:
                if item['ipv4'] in ['none', 'dhcp']:        
                    data['ipv4'] = item['ipv4']
                else:
                    if not ip_helper.is_valid_ipv4_cidr(item['ipv4']):
                        my_output.error('ipv4 attribute value none, dhcp or cidrv4 expected')
                        my_output.default(json.dumps(item))
                        return None

                    data['ipv4'] = item['ipv4']
        
        if check:
            nns = self.get_nncp_input_nns(
                node,
                my_output
            )
            if nns is None:
                return None
            
            my_output.default('Check nns data', underline=True, before_newline=True)
            for item in nns:
                interface_found = False
                for interface_mo in item['interface']:
                    if interface_mo['type'] not in ['ethernet', 'bond']:
                        continue

                    if interface_mo['name'] == data['base']:
                        interface_found = True
                        break

                if not interface_found:
                    my_output.default(
                        '- [WARNING] %s base interface not found: %s' % (
                            item['name'],
                            data['base']
                        )
                    )

                if interface_found:
                    my_output.default(
                        '- %s base interface found: %s' % (
                            item['name'],
                            data['base']
                        )
                    )

                vlan_found = False
                for interface_mo in item['interface']:
                    if interface_mo['type'] != 'vlan':
                        continue

                    if interface_mo['vlan_base'] == data['base'] and interface_mo['vlan_id'] == data['vlan_id']:
                        vlan_found = True
                        break

                if vlan_found:
                    my_output.default(
                        '- %s vlan interface found: %s.%s' % (
                            item['name'],
                            data['base'],
                            data['vlan_id']
                        )
                    )
                else:
                    my_output.default(
                        '- %s vlan interface not found: %s.%s' % (
                            item['name'],
                            data['base'],
                            data['vlan_id']
                        )
                    )

        return data
        
    def check_nncp_input_bond(self, item, check, node, my_output):
        data = {}
        data['type'] = 'bond'

        if 'name' not in item:
            my_output.error('name attribute expected')
            my_output.default(json.dumps(item))
            return None
        
        data['name'] = item['name']

        if 'state' not in item:
            my_output.error('state attribute expected')
            my_output.default(json.dumps(item))
            return None
        
        if item['state'] not in ['up', 'absent']:
            my_output.error('state attribute value up or absent expected')
            my_output.default(json.dumps(item))
            return None
        
        data['state'] = item['state']

        if data['state'] == 'up':
            if 'port' not in item:
                my_output.error('port attribute expected')
                my_output.default(json.dumps(item))
                return None
            
            if len(item['port'].split(',')) == 1:
                my_output.error('port must define at least two comman-separated interfaces')
                my_output.default(json.dumps(item))
                return None
            
            data['port'] = item['port']

            data['ipv4'] = None
            if 'ipv4' in item:
                if item['ipv4'] in ['none', 'dhcp']:        
                    data['ipv4'] = item['ipv4']
                else:
                    if not ip_helper.is_valid_ipv4_cidr(item['ipv4']):
                        my_output.error('ipv4 attribute value none, dhcp or cidrv4 expected')
                        my_output.default(json.dumps(item))
                        return None

                    data['ipv4'] = item['ipv4']
        
            if 'mode' not in item:
                my_output.error('mode attribute expected')
                my_output.default(json.dumps(item))
                return None
            
            if item['mode'] not in ['active-backup', 'balance-xor', '802.3ad']:
                my_output.error('mode attribute value active-backup, balance-xor or 802.3ad expected')
                my_output.default(json.dumps(item))
                return None

            data['mode'] = item['mode']

            if 'mtu' in item:
                if not isinstance(item['mtu'], int):
                    my_output.error('mtu attribute integer value expected')
                    my_output.default(json.dumps(item))
                    return None

                data['mtu'] = item['mtu']

            data['miimon'] = None
            if 'miimon' in item:
                data['miimon'] = item['miimon']

        if check:
            nns = self.get_nncp_input_nns(
                node,
                my_output
            )
            if nns is None:
                return None
            
            my_output.default('Check nns data', underline=True, before_newline=True)
            for item in nns:
                interface_found = False
                for interface_mo in item['interface']:
                    if interface_mo['type'] not in ['bond']:
                        continue

                    if interface_mo['name'] == data['name']:
                        interface_found = True
                        break

                if not interface_found:
                    my_output.default(
                        '- %s bond interface not found: %s' % (
                            item['name'],
                            data['name']
                        )
                    )

                if interface_found:
                    my_output.default(
                        '- %s bond interface found: %s' % (
                            item['name'],
                            data['name']
                        )
                    )

                if data['state'] == 'up':
                    for interface_name in data['port'].split(','):
                        interface_found = False
                        for interface_mo in item['interface']:
                            if interface_mo['type'] not in ['ethernet']:
                                continue

                            if interface_mo['name'] == interface_name:
                                interface_found = True
                                break

                        if not interface_found:
                            my_output.default(
                                '- [ERROR] %s ethernet interface not found: %s' % (
                                    item['name'],
                                    interface_name
                                )
                            )
                            return None

                        my_output.default(
                            '- %s ethernet interface found: %s' % (
                                item['name'],
                                interface_name
                            )
                        )

        return data

    def check_nncp_input_lb(self, item, check, node, my_output):
        data = {}
        data['type'] = 'lb'

        if 'name' not in item:
            my_output.error('name attribute expected')
            my_output.default(json.dumps(item))
            return None
        
        data['name'] = item['name']

        if 'state' not in item:
            my_output.error('state attribute expected')
            my_output.default(json.dumps(item))
            return None
        
        if item['state'] not in ['up', 'absent']:
            my_output.error('state attribute value up or absent expected')
            my_output.default(json.dumps(item))
            return None
        
        data['state'] = item['state']

        if data['state'] == 'up':
            if 'port' not in item:
                my_output.error('port attribute expected')
                my_output.default(json.dumps(item))
                return None
            
            if len(item['port'].split(',')) > 1:
                my_output.error('single upstream interface expected')
                my_output.default(json.dumps(item))
                return None
            
            data['port'] = item['port']

            data['ipv4'] = None
            if 'ipv4' in item:
                if item['ipv4'] in ['none', 'dhcp']:        
                    data['ipv4'] = item['ipv4']
                else:
                    if not ip_helper.is_valid_ipv4_cidr(item['ipv4']):
                        my_output.error('ipv4 attribute value none, dhcp or cidrv4 expected')
                        my_output.default(json.dumps(item))
                        return None

                    data['ipv4'] = item['ipv4']
        
            if 'stp' not in item:
                my_output.error('stp attribute expected')
                my_output.default(json.dumps(item))
                return None
            
            if not isinstance(item['stp'], bool):
                my_output.error('stp boolean expected')
                my_output.default(json.dumps(item))
                return None

            data['stp'] = item['stp']

        if check:
            nns = self.get_nncp_input_nns(
                node,
                my_output
            )
            if nns is None:
                return None
            
            my_output.default('Check nns data', underline=True, before_newline=True)
            for item in nns:
                interface_found = False
                for interface_mo in item['interface']:
                    if interface_mo['type'] not in ['libux-bridge']:
                        continue

                    if interface_mo['name'] == data['name']:
                        interface_found = True
                        break

                if not interface_found:
                    my_output.default(
                        '- %s linux bridge interface not found: %s' % (
                            item['name'],
                            data['name']
                        )
                    )

                if interface_found:
                    my_output.default(
                        '- %s linux bridge interface found: %s' % (
                            item['name'],
                            data['name']
                        )
                    )

                if data['state'] == 'up':
                    interface_found = False
                    for interface_mo in item['interface']:
                        if interface_mo['type'] not in ['ethernet', 'bond', 'vlan']:
                            continue

                        if interface_mo['name'] == data['port']:
                            interface_found = True
                            break

                    if not interface_found:
                        my_output.default(
                            '- [WARNING] %s upstream interface not found: %s' % (
                                item['name'],
                                data['port']
                            )
                        )

                    if interface_found:
                        my_output.default(
                            '- %s upstream interface found: %s' % (
                                item['name'],
                                data['port']
                            )
                        )

        return data

    def check_nncp_input_data(self, params, my_output):
        if not isinstance(params, list):
            my_output.error('JSON list expected')
            return None
        
        data = []
        for param in params:
            if 'node' not in param:
                param['node'] = '_all_'

            if param['node'] not in ['_all_', '_workers_']:
                if not self.is_node(param['node']):
                    my_output.error('node not found: %s' % (param['node']))
                    return None

            if 'delete' not in param:
                param['delete'] = False

            if not isinstance(param['delete'], bool):
                my_output.error('delete attribute bool value expected')
                my_output.default(json.dumps(param))
                return None

            if 'check' not in param:
                param['check'] = True

            if not isinstance(param['check'], bool):
                my_output.error('check attribute bool value expected')
                my_output.default(json.dumps(param))
                return None

            if 'routes' in param:
                new_routes = []
                for route in param['routes']:
                    new_route = self.check_route(route, param['check'], param['node'], my_output)
                    if new_route is None:
                        return None

                    new_routes.append(
                        new_route
                    )

                param['routes'] = copy.deepcopy(new_routes)

            if 'interfaces' in param:
                new_interfaces = []
                for interface in param['interfaces']:
                    if 'type' not in interface:
                        my_output.error('interface.type attribute expected')
                        return None

                    supported_types = ['bond', 'eth', 'lb', 'vlan']
                    if interface['type'] not in supported_types:
                        my_output.error('unsupported interface.type value')
                        return None

                    new_interface = None
                    if interface['type'] == 'vlan':
                        new_interface = self.check_nncp_input_vlan(interface, param['check'], param['node'], my_output)

                    if interface['type'] == 'eth':
                        new_interface = self.check_nncp_input_eth(interface, param['check'], param['node'], my_output)

                    if interface['type'] == 'bond':
                        new_interface = self.check_nncp_input_bond(interface, param['check'], param['node'], my_output)

                    if interface['type'] == 'lb':
                        new_interface = self.check_nncp_input_lb(interface, param['check'], param['node'], my_output)

                    if new_interface is None:
                        return None

                    new_interfaces.append(
                        new_interface
                    )

                param['interfaces'] = copy.deepcopy(new_interfaces)

            data.append(
                param
            )

        return data
    