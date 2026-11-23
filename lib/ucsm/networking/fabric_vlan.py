class FabricVlan():
    def __init__(self):
        self.fabric_vlan = None

    def get_fabric_vlan_mo(self, cache_enabled=True):
        if self.fabric_vlan is not None and cache_enabled:
            return self.fabric_vlan

        self.fabric_vlan = []

        keys = [
            'assoc_primary_vlan_state',
            'assoc_primary_vlan_switch_id',
            'compression_type',
            'config_overlap',
            'default_net',
            'dn',
            'ep_dn',
            'id',
            'if_role',
            'if_type',
            'name',
            'oper_state',
            'overlap_state_for_a',
            'overlap_state_for_b',
            'peer_dn',
            'rn',
            'status',
            'switch_id',
            'transport',
            'type'
        ]

        managed_objects = self.query_classid(
            'fabricVlan'
        )
        for managed_object in managed_objects:
            info = {}
            for key in keys:
                info[key] = getattr(managed_object, key, None)

            self.fabric_vlan.append(
                info
            )

        return self.fabric_vlan

    def get_fabric_vlan(self):
        return self.get_fabric_vlan_mo()
