from lib import ip_helper
from lib.ucsm import manager


class UcsmBlade():
    def __init__(self):
        self.ucsm_blade = None

    def load_pre_ucsm_blade(self):
        self.ucsm_blade = self.get_pre_cache('ucsm', 'blade')
        if self.ucsm_blade is None:
            return False
        return True

    def set_post_ucsm_blade(self):
        return self.set_post_cache('ucsm-blade', self.ucsm_blade)

    def load_post_ucsm_blade(self):
        self.ucsm_blade = self.get_post_cache('ucsm-blade')
        if self.ucsm_blade is None:
            return False
        return True

    def get_blade_ucsm_name(self, serial):
        for ucsm_name in self.ucsm_blade:
            for blade in self.ucsm_blade[ucsm_name]:
                if blade['serial'].lower() == serial.lower():
                    return ucsm_name
        return None

    def get_ucsm_vic_by_dn(self, dn, incl_dce=False):
        for key in self.ucsm_blade:
            for blade in self.ucsm_blade[key]:
                for vic in blade['adaptor']:
                    if vic['dn'] == dn:
                        if incl_dce:
                            vic['dce'] = []
                            for dce in blade['extEthIf']:
                                if dce['adaptor_dn'] == vic['dn']:
                                    vic['dce'].append(
                                        dce
                                    )

                            vic['dce'] = sorted(
                                vic['dce'],
                                key=lambda i: i['id']
                            )

                        return vic
        return None

    def get_ucsm_ext_eth_if_by_dn(self, dn):
        for key in self.ucsm_blade:
            for blade in self.ucsm_blade[key]:
                for ext_eth_if in blade['extEthIf']:
                    if ext_eth_if['dn'] == dn:
                        return ext_eth_if
        return None

    def get_ucsm_blade_eth_if_by_mac(self, mac_address, incl_vifs=False):
        for key in self.ucsm_blade:
            for blade in self.ucsm_blade[key]:
                for host_eth_if in blade['hostEthIf']:
                    if ip_helper.is_mac_equal(mac_address, host_eth_if['mac']):
                        if incl_vifs:
                            host_eth_if['vif'] = []
                            for vif in blade['vif']:
                                if vif['chassis_id'] != host_eth_if['chassis_id']:
                                    continue

                                if vif['blade_id'] != host_eth_if['blade_id']:
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

    def prepare_ucsm_blade(self, cache_enabled=True):
        ucsm_instances = self.get_ucsm_handlers()
        if ucsm_instances is None or len(ucsm_instances) == 0:
            return False

        self.ucsm_blade = {}

        for ucsm_instance in ucsm_instances:
            self.my_output.debug('UCSM blades: %s' % (ucsm_instance['name']))

            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if ucsm_instance['name'] in self.ucsm_blade:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('ucsm-%s-blade' % (ucsm_instance['name']))
                if cache is not None:
                    self.my_output.debug('L3 Cache hit network')
                    self.ucsm_blade[ucsm_instance['name']] = cache
                    continue

            self.my_output.debug('Cache miss')

            ucsm_handler = manager.UcsManager(
                ucsm_instance['ip'],
                ucsm_instance['username'],
                ucsm_instance['password'],
                log_id=self.log_id
            )

            self.ucsm_blade[ucsm_instance['name']] = ucsm_handler.get_blades(net=True)
            if self.ucsm_blade[ucsm_instance['name']] is None:
                return False

            self.set_cache(
                'ucsm-%s-blade' % (ucsm_instance['name']),
                self.ucsm_blade[ucsm_instance['name']]
            )

        return True

    def run_ucsm_blade(self):
        if not self.set_post_ucsm_blade():
            return False

        return True
