from lib.ucsm import manager


class UcsmChassis():
    def __init__(self):
        self.ucsm_chassis = None

    def load_pre_ucsm_chassis(self):
        self.ucsm_chassis = self.get_pre_cache('ucsm', 'chassis')
        if self.ucsm_chassis is None:
            return False
        return True

    def set_post_ucsm_chassis(self):
        return self.set_post_cache('ucsm-chassis', self.ucsm_chassis)

    def load_post_ucsm_chassis(self):
        self.ucsm_chassis = self.get_post_cache('ucsm-chassis')
        if self.ucsm_chassis is None:
            return False
        return True

    # ethSwitchFi - I/O Module Fabric Port
    #   "dn": "sys/chassis-1/slot-1/fabric/port-1"
    # ethServerFi - I/O Module Backplane Port
    #   "dn": "sys/chassis-1/slot-1/host/port-3"

    def get_ucsm_chassis_fabric_port_by_module(self, chassis_id, iom_id):
        ports = []
        for ucsm_name in self.ucsm_chassis:
            for chassis in self.ucsm_chassis[ucsm_name]:
                if chassis['id'] == chassis_id:
                    for port in chassis['ethSwitchFi']:
                        if port['iom_id'] == iom_id:
                            ports.append(port)
        return ports

    def get_ucsm_chassis_eth_object_by_dn(self, dn):
        keys = [
            'ethServerFi',
            'ethServerFiPc',
            'ethServerFiPcEp',
            'ethSwitchFi',
            'ethSwitchFiPc',
            'ethSwitchFiPcEp'
        ]
        for key in keys:
            for ucsm_name in self.ucsm_chassis:
                for chassis in self.ucsm_chassis[ucsm_name]:
                    for eth in chassis[key]:
                        if eth['dn'] == dn:
                            return eth
        return None

    def prepare_ucsm_chassis(self, cache_enabled=True):
        ucsm_instances = self.get_ucsm_handlers()
        if ucsm_instances is None or len(ucsm_instances) == 0:
            return False

        self.ucsm_chassis = {}

        for ucsm_instance in ucsm_instances:
            self.my_output.debug('UCSM chassis: %s' % (ucsm_instance['name']))

            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if ucsm_instance['name'] in self.ucsm_chassis:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('ucsm-%s-chassis' % (ucsm_instance['name']))
                if cache is not None:
                    self.my_output.debug('L3 Cache hit network')
                    self.ucsm_chassis[ucsm_instance['name']] = cache
                    continue

            self.my_output.debug('Cache miss')

            ucsm_handler = manager.UcsManager(
                ucsm_instance['ip'],
                ucsm_instance['username'],
                ucsm_instance['password'],
                log_id=self.log_id
            )

            self.ucsm_chassis[ucsm_instance['name']] = ucsm_handler.get_chassiz(net=True)
            if self.ucsm_chassis[ucsm_instance['name']] is None:
                return False

            self.set_cache(
                'ucsm-%s-chassis' % (ucsm_instance['name']),
                self.ucsm_chassis[ucsm_instance['name']]
            )

        return True

    def run_ucsm_chassis(self):
        if not self.set_post_ucsm_chassis():
            return False

        return True

    def run_ucsm_chassis_serial(self):
        for ucsm_name in self.ucsm_chassis:
            for chassis in self.ucsm_chassis[ucsm_name]:
                item = {}
                item['serial'] = chassis['serial']
                item['domain'] = self.domain_name
                item['scope'] = 'ucsm'
                item['type'] = 'Chassis'
                item['description'] = chassis['model']
                item['parent'] = None

                self.serial.append(
                    item
                )

        return True
