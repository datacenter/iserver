from lib import filter_helper
from lib.workflow.ocp_interface_state_up import get as ocp_workflow


class K8sNodeNetworkStateInfo():
    def __init__(self):
        self.node_network_state = None
        self.node_network_state_interface_up = None

    def get_node_network_state_ethernet_summary(self, info):
        summary = {}
        summary['interfaceT'] = []

        eth_up = 0
        eth = []
        for ethernet in info['ethernet']:
            if ethernet['state'] == 'up':
                eth_up += 1
                if ethernet['lldp_enabled']:
                    eth.append('\u2713 %s lldp:%s' % (ethernet['name'], len(ethernet['lldp_neighbors'])))
                else:
                    eth.append('\u2713 %s' % (ethernet['name']))    
            else:
                eth.append('\u2717 %s' % (ethernet['name']))
                    
        vlan_up = 0
        vlan_intf = []
        for vlan in info['vlan']:
            if vlan['state'] == 'up':
                vlan_up += 1
                if vlan['lldp_enabled']:
                    vlan_intf.append('\u2713 %s lldp:%s' % (vlan['name'], len(vlan['lldp_neighbors'])))
                else:
                    vlan_intf.append('\u2713 %s' % (vlan['name']))
            else:
                vlan_intf.append('\u2717 %s' % (vlan['name']))

        bond_up = 0
        bond_intf = []
        for bond in info['bond']:
            if bond['state'] == 'up':
                bond_up += 1
                if bond['lldp_enabled']:
                    bond_intf.append('\u2713 %s [%s] lldp:%s' % (bond['name'], ','.join(bond['lacp_port']), len(bond['lldp_neighbors'])))
                else:
                    bond_intf.append('\u2713 %s [%s]' % (bond['name'], ','.join(bond['lacp_port'])))
            else:
                bond_intf.append('\u2717 %s [%s]' % (bond['name'], ','.join(bond['lacp_port'])))

        summary['interfaceT'].append('Eth %s/%s' % (eth_up, len(info['ethernet'])))
        summary['interfaceT'] = summary['interfaceT'] + eth   

        if len(vlan_intf) > 0:
            summary['interfaceT'].append('---')
            summary['interfaceT'].append('Vlan %s/%s' % (vlan_up, len(info['vlan'])))
            summary['interfaceT'] = summary['interfaceT'] + vlan_intf

        if len(bond_intf) > 0:
            summary['interfaceT'].append('---')
            summary['interfaceT'].append('Bond %s/%s' % (bond_up, len(info['bond'])))
            summary['interfaceT'] = summary['interfaceT'] + bond_intf

        return summary
    
    def get_node_network_state_bridge_summary(self, info):
        summary = {}

        summary['ovsT'] = []
        count = 0
        for ovs in info['ovs']:
            if count > 0:
                summary['ovsT'].append('---')

            if ovs['state'] == 'up':
                summary['ovsT'].append(
                    '\u2713 %s' % (
                        ovs['name']
                    )
                )
            else:
                summary['ovsT'].append(
                    '\u2717 %s' % (
                        ovs['name']
                    )
                )

            for item in ovs['bridge_port']:
                if item['name'] == ovs['name']:
                    continue

                summary['ovsT'].append(
                    item['name']
                )
                
            count += 1

        if len(info['ovn']) > 1:
            if count > 0:
                summary['ovsT'].append('---')
            
            summary['ovsT'].append('Bridge mapping')
            for item in info['ovn']:
                summary['ovsT'].append('- %s:%s' % (item['bridge'], item['localnet']))

        summary['bridgeT'] = summary['ovsT']

        return summary
    
    def get_node_network_state_dns_summary(self, info):
        summary = {}
        summary['dnsT'] = self.get(info, 'dns:search', on_error=[], on_none=[])
        summary['dnsT'].append('---')
        summary['dnsT'] = summary['dnsT'] + self.get(info, 'dns:server', on_error=[], on_none=[])
        return summary
    
    def get_node_network_state_route_summary(self, info):
        summary = {}

        summary['routeT'] = []
        summary['routeT'].append('Entries: %s' % (len(info['route'])))

        table = {}
        for route in info['route']:
            table_id = self.get(route, 'table-id')
            if table_id is None:
                continue

            if table_id not in table:
                table[table_id] = 0

            table[table_id] += 1

        vrf = {}
        vrf_table = {}
        vrf_table_id = {}
        for route in info['route']:
            vrf_name = self.get(route, 'vrf-name')
            table_id = self.get(route, 'table-id')
            if vrf_name is None:
                continue

            vrf_table[vrf_name] = table_id
            vrf_table_id[table_id] = vrf_name
            if vrf_name not in vrf:
                vrf[vrf_name] = 0

            vrf[vrf_name] += 1

        nh = {}
        nh_table = {}
        for route in info['route']:
            nhi = self.get(route, 'next-hop-interface')
            table_id = self.get(route, 'table-id')
            if nhi is None:
                continue

            if nhi not in nh_table:
                nh_table[nhi] = []

            if nhi not in nh:
                nh[nhi] = 0

            nh[nhi] += 1
            if table_id is not None and table_id not in nh_table[nhi]:
                nh_table[nhi].append(table_id)

        if len(table) > 0:
            summary['routeT'].append('---')
            for table_id in table:
                if table_id == 254:
                    summary['routeT'].append('table %s [main]: %s' % (table_id, table[table_id]))
                    continue

                if table_id in vrf_table_id:
                    summary['routeT'].append('table %s [vrf:%s]: %s' % (table_id, vrf_table_id[table_id], table[table_id]))
                    continue

                summary['routeT'].append('table %s: %s' % (table_id, table[table_id]))

        if len(vrf) > 0:
            summary['routeT'].append('---')
            for vrf_name in vrf:
                summary['routeT'].append('vrf %s [%s]: %s' % (vrf_name, vrf_table[vrf_name], vrf[vrf_name]))
            
        if len(nh) > 0:
            summary['routeT'].append('---')
            for nhi in nh:
                summary['routeT'].append('nh %s [%s]: %s' % (nhi, ','.join(str(x) for x in nh_table[nhi]), nh[nhi]))

        return summary

    def get_node_network_state_summary(self, info):
        summary = {}
        summary.update(self.get_node_network_state_ethernet_summary(info))
        summary.update(self.get_node_network_state_bridge_summary(info))
        summary.update(self.get_node_network_state_dns_summary(info))
        summary.update(self.get_node_network_state_route_summary(info))
        return summary
    
    def get_node_network_state_info(self, managed_object):
        if managed_object is None:
            return None

        info = self.get_base_info(managed_object)
        info.update(self.get_node_network_state_interfaces_info(managed_object))
        info['dns'] = self.get_node_network_state_dns_info(managed_object)
        info['route'] = self.get_node_network_state_route_info(managed_object)
        info.update(self.get_node_network_state_summary(info))
        return info

    def get_node_network_states_info(self, cache_enabled=True):
        if cache_enabled:
            if self.node_network_state is not None:
                return self.node_network_state

        managed_objects = self.get_node_network_state_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.node_network_state = []
        for managed_object in managed_objects:
            node_network_state_info = {}
            node_network_state_info['info'] = self.get_node_network_state_info(
                managed_object
            )
            node_network_state_info['mo'] = managed_object
            self.node_network_state.append(
                node_network_state_info
            )

        return self.node_network_state

    def match_node_network_state(self, node_network_state_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, node_network_state_info['name']):
                    return False

            if key.startswith('interface-'):
                key_found = True

            if not key_found:
                self.log.error(
                    'match_node_network_state',
                    'Unsupported key: %s' % (key)
                )

        return True

    def match_node_network_state_interface(self, node_network_state_interface_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True

            if key == 'interface-type':
                key_found = True
                if not filter_helper.match_string(value, node_network_state_interface_info['interface']):
                    return False

            if not key_found:
                self.log.error(
                    'match_node_network_state_interface',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_node_network_states(self, object_filter=None, return_mo=False, cluster_name=None, fixup=False, cache_enabled=True):
        if fixup and cluster_name is not None:
            if cache_enabled and self.node_network_state_interface_up is None or not cache_enabled:
                params = {}
                params['cluster'] = self.cluster_name
                self.node_network_state_interface_up = ocp_workflow.run(params, log_id=self.log_id)

        all_node_network_states = self.get_node_network_states_info(cache_enabled=cache_enabled)
        if all_node_network_states is None:
            return None

        node_network_states = []

        for node_network_state_info in all_node_network_states:
            if not self.match_node_network_state(node_network_state_info['info'], object_filter):
                continue

            if return_mo:
                node_network_states.append(
                    node_network_state_info['mo']
                )
                continue

            interfaces_info = []
            for node_network_state_interface_info in node_network_state_info['info']['interface']:
                if not self.match_node_network_state_interface(node_network_state_interface_info, object_filter):
                    continue

                interfaces_info.append(
                    node_network_state_interface_info
                )

            node_network_state_info['info']['interface'] = interfaces_info

            node_network_states.append(
                node_network_state_info['info']
            )

        return node_network_states

    def is_node_network_state(self, name, cache_enabled=True):
        if self.get_node_network_state(name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_node_network_state(self, node_name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'name:%s' % (node_name)
        )
        node_network_states = self.get_node_network_states(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if node_network_states is None:
            return None

        if len(node_network_states) == 1:
            return node_network_states[0]

        return None
