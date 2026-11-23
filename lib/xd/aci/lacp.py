import copy
from lib import ip_helper
from lib.aci import apic


class AciLacp():
    def __init__(self):
        self.aci_lacp = None

    def load_pre_aci_lacp(self):
        self.aci_lacp = self.get_pre_cache('aci', 'lacp')
        if self.aci_lacp is None:
            return False
        return True

    def set_post_aci_lacp(self):
        return self.set_post_cache('aci-lacp', self.aci_lacp)

    def load_post_aci_lacp(self):
        self.aci_lacp = self.get_post_cache('aci-lacp')
        if self.aci_lacp is None:
            return False
        return True

    def get_aci_lacp(self):
        info = copy.deepcopy(self.aci_lacp)
        return info

    def prepare_aci_lacp(self, cache_enabled=True):
        aci_controllers = self.get_aci_handlers()
        if aci_controllers is None or len(aci_controllers) == 0:
            return False

        self.aci_lacp = {}

        for aci_controller in aci_controllers:
            self.my_output.debug('Aci lacp: %s' % (aci_controller['name']))
            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if aci_controller['name'] in self.aci_lacp:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('aci-%s-lacp' % (aci_controller['name']))
                if cache is not None:
                    self.aci_lacp[aci_controller['name']] = cache
                    self.my_output.debug('L3 Cache hit')
                    continue

            self.my_output.debug('Cache miss')

            apic_handler = apic.Apic(
                aci_controller['ip'],
                aci_controller['port'],
                aci_controller['username'],
                aci_controller['password'],
                apic_name=aci_controller['name'],
                log_id=self.log_id
            )

            nodes = apic_handler.get_nodes(
                node_filter=['role:!controller']
            )
            if nodes is None:
                self.log.error(
                    'prepare_aci_lacp',
                    'Failed to get nodes: %s' % (aci_controller['name'])
                )
                continue

            self.aci_lacp[aci_controller['name']] = []
            for node in nodes:
                node_lacp_info = apic_handler.get_protocol_lacp(
                    node['podId'],
                    node['id'],
                    instance_info=False,
                    interface_info=True,
                    event_info=False,
                    event_filter=False
                )
                if 'interfaces' not in node_lacp_info or node_lacp_info['interfaces'] is None:
                    self.log.error(
                        'prepare_aci_lacp',
                        'Failed to get node lacp: %s' % (node['id'])
                    )
                    continue

                for item in node_lacp_info['interfaces']:
                    item['apic'] = aci_controller['name']
                    item['node_id'] = node['id']
                    self.aci_lacp[aci_controller['name']].append(
                        item
                    )

            self.set_cache(
                'aci-%s-lacp' % (aci_controller['name']),
                self.aci_lacp[aci_controller['name']]
            )

        return True

    def run_aci_lacp(self):
        for key in self.aci_lacp:
            for item in self.aci_lacp[key]:
                for lacp in item['lacp']:
                    lacp['ServerMoid'] = None
                    lacp['ServerName'] = None
                    lacp['ServerInterface'] = None

                    if self.server_macs is None:
                        continue

                    # for server_mac in self.server_macs:
                    #     if ip_helper.is_mac_equal(lacp['adjacency']['sysId'], server_mac['MacAddress']):
                    #         lacp['ServerMoid'] = server_mac['ServerMoid']
                    #         lacp['ServerName'] = server_mac['ServerName']
                    #         lacp['ServerInterface'] = server_mac['InterfaceDn']

        if not self.set_post_aci_lacp():
            return False

        return True
