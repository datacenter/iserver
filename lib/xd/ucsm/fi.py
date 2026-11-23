from lib.ucsm import manager


class UcsmFi():
    def __init__(self):
        self.ucsm_fi = None

    def load_pre_ucsm_fi(self):
        self.ucsm_fi = self.get_pre_cache('ucsm', 'fi')
        if self.ucsm_fi is None:
            return False
        return True

    def set_post_ucsm_fi(self):
        return self.set_post_cache('ucsm-fi', self.ucsm_fi)

    def load_post_ucsm_fi(self):
        self.ucsm_fi = self.get_post_cache('ucsm-fi')
        if self.ucsm_fi is None:
            return False
        return True

    def get_ucsm_switch_eth_port_by_dn(self, dn):
        for ucsm_name in self.ucsm_fi:
            for fi in self.ucsm_fi[ucsm_name]:
                for eth in fi['ethPort']:
                    if eth['dn'] == dn:
                        return eth
        return None

    def prepare_ucsm_fi(self, cache_enabled=True):
        ucsm_instances = self.get_ucsm_handlers()
        if ucsm_instances is None or len(ucsm_instances) == 0:
            return False

        self.ucsm_fi = {}

        for ucsm_instance in ucsm_instances:
            self.my_output.debug('UCSM fi: %s' % (ucsm_instance['name']))

            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if ucsm_instance['name'] in self.ucsm_fi:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('ucsm-%s-fi' % (ucsm_instance['name']))
                if cache is not None:
                    self.my_output.debug('L3 Cache hit network')
                    self.ucsm_fi[ucsm_instance['name']] = cache
                    continue

            self.my_output.debug('Cache miss')

            ucsm_handler = manager.UcsManager(
                ucsm_instance['ip'],
                ucsm_instance['username'],
                ucsm_instance['password'],
                log_id=self.log_id
            )

            self.ucsm_fi[ucsm_instance['name']] = ucsm_handler.get_fis(net=True)
            if self.ucsm_fi[ucsm_instance['name']] is None:
                return False

            self.set_cache(
                'ucsm-%s-fi' % (ucsm_instance['name']),
                self.ucsm_fi[ucsm_instance['name']]
            )

        return True

    def run_ucsm_fi(self):
        if not self.set_post_ucsm_fi():
            return False

        return True
