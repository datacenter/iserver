import copy
from lib import ip_helper
from lib.aci import apic


class AciEp():
    def __init__(self):
        self.aci_ep = None

    def load_pre_aci_ep(self):
        self.aci_ep = self.get_pre_cache('aci', 'ep')
        if self.aci_ep is None:
            return False
        return True

    def set_post_aci_ep(self):
        return self.set_post_cache('aci-ep', self.aci_ep)

    def load_post_aci_ep(self):
        self.aci_ep = self.get_post_cache('aci-ep')
        if self.aci_ep is None:
            return False
        return True

    def get_aci_ep(self):
        info = copy.deepcopy(self.aci_ep)
        return info

    def prepare_aci_ep(self, cache_enabled=True):
        aci_controllers = self.get_aci_handlers()
        if aci_controllers is None or len(aci_controllers) == 0:
            return False

        self.aci_ep = {}

        for aci_controller in aci_controllers:
            self.my_output.debug('Aci ep: %s' % (aci_controller['name']))
            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if aci_controller['name'] in self.aci_ep:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('aci-%s-ep' % (aci_controller['name']))
                if cache is not None:
                    self.aci_ep[aci_controller['name']] = cache
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

            apic_endpoints = apic_handler.get_endpoints(
                fabric_info=True
            )
            if apic_endpoints is None:
                continue

            self.aci_ep[aci_controller['name']] = []
            for item in apic_endpoints:
                item['apic'] = aci_controller['name']
                self.aci_ep[aci_controller['name']].append(
                    item
                )

            self.set_cache(
                'aci-%s-ep' % (aci_controller['name']),
                self.aci_ep[aci_controller['name']]
            )

        return True

    def run_aci_ep(self):
        for key in self.aci_ep:
            for item in self.aci_ep[key]:
                item['hash'] = ip_helper.get_string_md5(
                    '%s %s' % (
                        item['apic'],
                        item['dn']
                    )
                )

                item['epg_hash'] = None
                if len(item['epgNameApTenant']) > 0:
                    item['epg_hash'] = ip_helper.get_string_md5(
                        '%s %s' % (
                            item['apic'],
                            item['epgNameApTenant']
                        )
                    )

                item['bd_hash'] = None
                if len(item['bdNameTenant']) > 0:
                    item['bd_hash'] = ip_helper.get_string_md5(
                        '%s %s' % (
                            item['apic'],
                            item['bdNameTenant']
                        )
                    )

                item['vrf_hash'] = None
                if len(item['vrfNameTenant']) > 0:
                    item['vrf_hash'] = ip_helper.get_string_md5(
                        '%s %s' % (
                            item['apic'],
                            item['vrfNameTenant']
                        )
                    )

                item['ServerMoid'] = None
                item['ServerName'] = None
                item['ServerInterface'] = None
                if self.server_macs is None:
                    continue

                for server_mac in self.server_macs:
                    if ip_helper.is_mac_equal(item['mac'], server_mac['MacAddress']):
                        item['ServerMoid'] = server_mac['ServerMoid']
                        item['ServerName'] = server_mac['ServerName']
                        item['ServerInterface'] = server_mac['InterfaceDn']

        if not self.set_post_aci_ep():
            return False

        return True
