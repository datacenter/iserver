from lib.ucsm import manager


class UcsmFabric():
    def __init__(self):
        self.ucsm_fabric = None

    def load_pre_ucsm_fabric(self):
        self.ucsm_fabric = self.get_pre_cache('ucsm', 'fabric')
        if self.ucsm_fabric is None:
            return False
        return True

    def set_post_ucsm_fabric(self):
        return self.set_post_cache('ucsm-fabric', self.ucsm_fabric)

    def load_post_ucsm_fabric(self):
        self.ucsm_fabric = self.get_post_cache('ucsm-fabric')
        if self.ucsm_fabric is None:
            return False
        return True

    def get_ucsm_fabric_vlan_by_id(self, vlan_id):
        for ucsm_name in self.ucsm_fabric:
            for vlan in self.ucsm_fabric[ucsm_name]['vlan']:
                if vlan['id'] == vlan_id:
                    return vlan
        return None

    def get_ucsm_fabric_pooled_vlan_by_name(self, name):
        for ucsm_name in self.ucsm_fabric:
            for vlan in self.ucsm_fabric[ucsm_name]['pooledVlan']:
                if vlan['name'] == name:
                    return vlan
        return None

    def get_ucsm_fabric_net_group_by_rn(self, name):
        for ucsm_name in self.ucsm_fabric:
            for net_group in self.ucsm_fabric[ucsm_name]['netGroup']:
                if net_group['rn'] == name:
                    return net_group
        return None

    def get_ucsm_fabric_vlan_pc_by_net_group_rn(self, switch_id, net_group_rn):
        for ucsm_name in self.ucsm_fabric:
            for vlan_pc in self.ucsm_fabric[ucsm_name]['ethVlanPc']:
                if vlan_pc['switch_id'] == switch_id:
                    if vlan_pc['dn'].split('/')[2] == net_group_rn:
                        return vlan_pc
        return None

    def get_ucsm_fabric_lan_pc_by_name(self, switch_id, name):
        for ucsm_name in self.ucsm_fabric:
            for lan_pc in self.ucsm_fabric[ucsm_name]['ethLanPc']:
                if lan_pc['switch_id'] == switch_id:
                    if lan_pc['name'] == name:
                        return lan_pc
        return None

    def get_ucsm_fabric_lan_pc_ep_by_pc_dn(self, switch_id, dn):
        ep = []
        for ucsm_name in self.ucsm_fabric:
            for lan_pc_ep in self.ucsm_fabric[ucsm_name]['ethLanPcEp']:
                if lan_pc_ep['switch_id'] == switch_id:
                    if '/'.join(lan_pc_ep['dn'].split('/')[:-1]) == dn:
                        ep.append(
                            lan_pc_ep
                        )

        return ep

    def prepare_ucsm_fabric(self, cache_enabled=True):
        ucsm_instances = self.get_ucsm_handlers()
        if ucsm_instances is None or len(ucsm_instances) == 0:
            return False

        self.ucsm_fabric = {}

        for ucsm_instance in ucsm_instances:
            self.my_output.debug('UCSM fabric: %s' % (ucsm_instance['name']))

            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if ucsm_instance['name'] in self.ucsm_fabric:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('ucsm-%s-fabric' % (ucsm_instance['name']))
                if cache is not None:
                    self.my_output.debug('L3 Cache hit network')
                    self.ucsm_fabric[ucsm_instance['name']] = cache
                    continue

            self.my_output.debug('Cache miss')

            ucsm_handler = manager.UcsManager(
                ucsm_instance['ip'],
                ucsm_instance['username'],
                ucsm_instance['password'],
                log_id=self.log_id
            )

            self.ucsm_fabric[ucsm_instance['name']] = ucsm_handler.get_fabric()
            if self.ucsm_fabric[ucsm_instance['name']] is None:
                return False

            self.set_cache(
                'ucsm-%s-fabric' % (ucsm_instance['name']),
                self.ucsm_fabric[ucsm_instance['name']]
            )

        return True

    def run_ucsm_fabric(self):
        if not self.set_post_ucsm_fabric():
            return False

        return True
