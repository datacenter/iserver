import copy
from lib import ip_helper


class AciServer():
    def __init__(self):
        self.aci_node_servers = None
        self.aci_node_intfs = None

    def set_post_aci_node_servers(self):
        return self.set_post_cache('aci-node-server', self.aci_node_servers)

    def load_post_aci_node_servers(self):
        self.aci_node_servers = self.get_post_cache('aci-node-server')
        if self.aci_node_servers is None:
            return False
        return True

    def set_post_aci_node_intfs(self):
        return self.set_post_cache('aci-node-intf', self.aci_node_intfs)

    def load_post_aci_node_intfs(self):
        self.aci_node_intfs = self.get_post_cache('aci-node-intf')
        if self.aci_node_intfs is None:
            return False
        return True

    def get_aci_node_servers(self):
        info = copy.deepcopy(self.aci_node_servers)
        return info

    def run_aci_server(self):
        self.aci_node_servers = {}
        self.aci_node_intfs = {}

        aci_node_names = self.get_aci_node_names()
        for controller_name in aci_node_names:
            self.aci_node_servers[controller_name] = {}
            self.aci_node_intfs[controller_name] = {}
            for node_name in aci_node_names[controller_name]:
                self.aci_node_servers[controller_name][node_name] = []
                self.aci_node_intfs[controller_name][node_name] = []

        for controller_name in aci_node_names:
            for server in self.servers:
                for fabric in server['Fabric']:
                    for intf in fabric['aci']['intf']:
                        (apic_name, node_id, intf_id) = intf.split(':')
                        node_name = self.get_aci_node_name_by_id(node_id)
                        if intf_id in self.aci_node_intfs[apic_name][node_name]:
                            continue

                        item = {}
                        item['ServerMoid'] = server['Moid']
                        item['ServerName'] = server['Name']
                        item['ServerTags'] = server['Tags']
                        item['ServerSerial'] = server['Serial']
                        item['ServerInterface'] = None
                        for mac_info in server['MacAddressInfo']:
                            if ip_helper.is_mac_equal(fabric['MacAddress'], mac_info['MacAddress']):
                                item['ServerInterface'] = mac_info['InterfaceName']
                                break

                        item['InterfaceId'] = intf_id
                        item['Fabric'] = fabric
                        item['_index'] = 0
                        if len(intf_id.split('/')) == 2:
                            item['_index'] = int(intf_id.split('/')[1])

                        if len(intf_id.split('/')) == 3:
                            item['_index'] = int(intf_id.split('/')[1]) * 1000 + int(intf_id.split('/')[2])

                        self.aci_node_servers[apic_name][node_name].append(
                            item
                        )
                        self.aci_node_intfs[apic_name][node_name].append(
                            intf_id
                        )

        if not self.set_post_aci_node_servers():
            return False

        if not self.set_post_aci_node_intfs():
            return False

        return True
