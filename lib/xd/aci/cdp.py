import copy
from lib import ip_helper
from lib.aci import apic
from lib.aci import helper as aci_helper


class AciCdp():
    def __init__(self):
        self.aci_cdp = None

    def load_pre_aci_cdp(self):
        self.aci_cdp = self.get_pre_cache('aci', 'cdp')
        if self.aci_cdp is None:
            return False
        return True

    def set_post_aci_cdp(self):
        return self.set_post_cache('aci-cdp', self.aci_cdp)

    def load_post_aci_cdp(self):
        self.aci_cdp = self.get_post_cache('aci-cdp')
        if self.aci_cdp is None:
            return False
        return True

    def get_aci_cdp(self):
        info = copy.deepcopy(self.aci_cdp)
        return info

    def prepare_aci_cdp(self, cache_enabled=True):
        aci_controllers = self.get_aci_handlers()
        if aci_controllers is None or len(aci_controllers) == 0:
            return False

        self.aci_cdp = {}

        for aci_controller in aci_controllers:
            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if aci_controller['name'] in self.aci_cdp:
                    continue

                # L3-cache
                cache = self.get_cache('aci-%s-cdp' % (aci_controller['name']))
                if cache is not None:
                    self.aci_cdp[aci_controller['name']] = cache
                    continue

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
                    'prepare_aci_cdp',
                    'Failed to get nodes: %s' % (aci_controller['name'])
                )
                continue

            self.aci_cdp[aci_controller['name']] = []
            for node in nodes:
                node_cdp_info = apic_handler.get_protocol_cdp(
                    node['podId'],
                    node['id'],
                    nei_info=True
                )
                for nei in node_cdp_info['neighbors']:
                    nei['apic'] = aci_controller['name']
                    nei['node_id'] = node['id']
                    self.aci_cdp[aci_controller['name']].append(
                        nei
                    )

            self.set_cache(
                'aci-%s-cdp' % (aci_controller['name']),
                self.aci_cdp[aci_controller['name']]
            )

        return True

    def run_aci_cdp(self):
        for key in self.aci_cdp:
            for item in self.aci_cdp[key]:
                item['xd'] = copy.deepcopy(self.xd)

        for key in self.aci_cdp:
            for item in self.aci_cdp[key]:
                item['hash'] = ip_helper.get_string_md5(
                    '%s %s' % (
                        item['apic'],
                        item['dn']
                    )
                )

                item['_index'] = aci_helper.get_aci_interface_id(
                    item['interfaceId']
                )

                item['node_name'] = self.get_aci_node_name_by_id(
                    item['node_id']
                )

                if 'sysName' not in item or item['sysName'] is None:
                    continue

                if 'ver' not in item or item['ver'] is None:
                    continue

                if item['ver'].startswith('Cisco Nexus Operating System'):
                    if self.get_nexus_device_by_hostname(item['sysName']) is not None:
                        item['xd']['DeviceType'] = 'Nexus'
                        item['xd']['DeviceSysName'] = item['sysName']
                        item['xd']['NexusDevice'] = self.get_nexus_device_by_hostname(
                            item['sysName']
                        )

                    if self.is_aci_node_name(item['sysName']):
                        node_info = self.get_aci_node_by_name(item['sysName'])
                        item['xd']['DeviceType'] = 'ACI'
                        item['xd']['DeviceSysName'] = item['sysName']
                        item['xd']['AciApicName'] = node_info['apic']
                        item['xd']['AciNodeName'] = item['sysName']
                        item['xd']['AciNodeId'] = self.get_aci_node_id_by_name(item['sysName'])
                        item['xd']['AciNodeRef'] = '%s-%s' % (node_info['apic'], item['sysName'])

                    if self.get_fi_by_name(item['sysName']) is not None:
                        item['xd']['DeviceType'] = 'FI'
                        item['xd']['FI'] = item['sysName']

                    continue

        if not self.set_post_aci_cdp():
            return False

        return True
