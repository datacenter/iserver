from lib import ip_helper
from lib.ucsm import manager


class UcsmRack():
    def __init__(self):
        self.ucsm_rack = None

    def load_pre_ucsm_rack(self):
        self.ucsm_rack = self.get_pre_cache('ucsm', 'rack')
        if self.ucsm_rack is None:
            return False
        return True

    def set_post_ucsm_rack(self):
        return self.set_post_cache('ucsm-rack', self.ucsm_rack)

    def load_post_ucsm_rack(self):
        self.ucsm_rack = self.get_post_cache('ucsm-rack')
        if self.ucsm_rack is None:
            return False
        return True

    def get_rack_ucsm_name(self, serial):
        for ucsm_name in self.ucsm_rack:
            for rack in self.ucsm_rack[ucsm_name]:
                if rack['serial'].lower() == serial.lower():
                    return ucsm_name
        return None

    def get_ucsm_rack_eth_if_by_mac(self, mac_address, incl_vifs=False):
        for key in self.ucsm_rack:
            for rack in self.ucsm_rack[key]:
                for host_eth_if in rack['hostEthIf']:
                    if ip_helper.is_mac_equal(mac_address, host_eth_if['mac']):
                        if incl_vifs:
                            host_eth_if['vif'] = []
                            for vif in rack['vif']:
                                if vif['rack_id'] is None:
                                    continue

                                if vif['rack_id'] != host_eth_if['rack_id']:
                                    continue

                                if vif['adaptor_id'] != host_eth_if['adaptor_id']:
                                    continue

                                if vif['interface_id'] != host_eth_if['id']:
                                    continue

                                host_eth_if['vif'].append(
                                    vif
                                )

                        return host_eth_if

        return None

    def prepare_ucsm_rack(self, cache_enabled=True):
        ucsm_instances = self.get_ucsm_handlers()
        if ucsm_instances is None or len(ucsm_instances) == 0:
            return False

        self.ucsm_rack = {}

        for ucsm_instance in ucsm_instances:
            self.my_output.debug('UCSM racks: %s' % (ucsm_instance['name']))

            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if ucsm_instance['name'] in self.ucsm_rack:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('ucsm-%s-rack' % (ucsm_instance['name']))
                if cache is not None:
                    self.my_output.debug('L3 Cache hit network')
                    self.ucsm_rack[ucsm_instance['name']] = cache
                    continue

            self.my_output.debug('Cache miss')

            ucsm_handler = manager.UcsManager(
                ucsm_instance['ip'],
                ucsm_instance['username'],
                ucsm_instance['password'],
                log_id=self.log_id
            )

            self.ucsm_rack[ucsm_instance['name']] = ucsm_handler.get_racks(net=True)
            if self.ucsm_rack[ucsm_instance['name']] is None:
                return False

            self.set_cache(
                'ucsm-%s-rack' % (ucsm_instance['name']),
                self.ucsm_rack[ucsm_instance['name']]
            )

        return True

    def run_ucsm_rack(self):
        if not self.set_post_ucsm_rack():
            return False

        return True
