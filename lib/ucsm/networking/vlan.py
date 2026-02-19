class Vlan():
    def __init__(self):
        self.vlan = None

    def get_vlan_mo(self, cache_enabled=True):
        if self.vlan is not None and cache_enabled:
            return self.vlan

        self.vlan = []

        keys = [
            'dn',
            'ep_dn',
            'id',
            'if_role',
            'if_type',
            'name',
            'oper_state',
            'peer_dn',
            'rn',
            'status',
            'switch_id',
            'transport',
            'type',
            'vlan_type'
        ]

        managed_objects = self.query_classid(
            'AdaptorVlan'
        )
        for managed_object in managed_objects:
            info = {}
            for key in keys:
                info[key] = getattr(managed_object, key, None)

            # "dn": "sys/chassis-1/blade-3/adaptor-1/host-eth-1/vlan-3",
            info['chassis_id'] = info['dn'].split('/')[1].split('-')[1]
            info['blade_id'] = info['dn'].split('/')[2].split('-')[1]

            self.vlan.append(
                info
            )

        return self.vlan

    def get_compute_vlans(self, chassis_id=None, blade_id=None):
        vlans = self.get_vlan_mo()

        compute_vlans = []
        for vlan in vlans:
            if chassis_id is not None:
                if vlan['chassis_id'] != chassis_id:
                    continue

            if blade_id is not None:
                if vlan['blade_id'] != blade_id:
                    continue

            compute_vlans.append(
                vlan

            )

        return compute_vlans