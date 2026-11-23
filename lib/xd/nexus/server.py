import copy
from lib import ip_helper


class NexusServer():
    def __init__(self):
        self.nexus_server = None

    def set_post_nexus_server(self):
        return self.set_post_cache('nexus-server', self.nexus_server)

    def load_post_nexus_server(self):
        self.nexus_server = self.get_post_cache('nexus-server')
        if self.nexus_server is None:
            return False
        return True

    def get_nexus_server(self):
        info = copy.deepcopy(
            self.nexus_server
        )
        return info

    def run_nexus_server(self):
        self.nexus_server = {}
        for nexus_name in self.nexus_lldp:
            self.nexus_server[nexus_name] = {}

            for server in self.servers:
                for fabric in server['Fabric']:
                    for intf in fabric['nexus']['intf']:
                        (nexus_id, intf_id) = intf.split(':')
                        if nexus_id != nexus_name:
                            continue

                        if intf_id in self.nexus_server[nexus_id]:
                            if self.nexus_server[nexus_id][intf_id]['ServerMoid'] != server['Moid']:
                                # print('wtf')
                                success = False
                        else:
                            item = {}
                            item['Nexus'] = nexus_name
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
                            item['MacAddress'] = fabric['MacAddress']
                            item['Lldp'] = []
                            item['Mac'] = []

                            for lldp in fabric['nexus']['lldp']:
                                if lldp['device_name'] == nexus_name and lldp['l_port_id'] == intf_id:
                                    item['Lldp'].append(
                                        lldp
                                    )

                            for mac in fabric['nexus']['mac']:
                                if mac['device_name'] == nexus_name and mac['port'] == intf_id:
                                    item['Mac'].append(
                                        mac
                                    )

                            item['_index'] = 0
                            if len(intf_id.split('/')) == 2:
                                item['_index'] = int(intf_id.split('/')[1])

                            if len(intf_id.split('/')) == 3:
                                item['_index'] = int(intf_id.split('/')[1]) * 1000 + int(intf_id.split('/')[2])


                            self.nexus_server[nexus_id][intf_id] = item

        if not self.set_post_nexus_server():
            return False

        return True
