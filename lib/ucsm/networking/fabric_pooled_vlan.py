class FabricPooledVlan():
    def __init__(self):
        self.fabric_pooled_vlan = None

    def get_fabric_pooled_vlan_mo(self, cache_enabled=True):
        if self.fabric_pooled_vlan is not None and cache_enabled:
            return self.fabric_pooled_vlan

        self.fabric_pooled_vlan = []

        keys = [
            'dn',
            'name',
            'poolable_dn',
            'rn',
            'status'
        ]

        managed_objects = self.query_classid(
            'fabricPooledVlan'
        )
        for managed_object in managed_objects:
            info = {}
            for key in keys:
                info[key] = getattr(managed_object, key, None)

            info['net_group_rn'] = info['dn'].split('/')[2]

            self.fabric_pooled_vlan.append(
                info
            )

        return self.fabric_pooled_vlan

    def get_fabric_pooled_vlan(self):
        return self.get_fabric_pooled_vlan_mo()
