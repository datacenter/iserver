class FabricNetGroup():
    def __init__(self):
        self.fabric_net_group = None

    def get_fabric_net_group_mo(self, cache_enabled=True):
        if self.fabric_net_group is not None and cache_enabled:
            return self.fabric_net_group

        self.fabric_net_group = []

        keys = [
            'descr',
            'dn',
            'id',
            'int_id',
            'name',
            'peer_dn',
            'rn',
            'size',
            'status',
            'switch_id',
            'type'
        ]

        managed_objects = self.query_classid(
            'fabricNetGroup'
        )
        for managed_object in managed_objects:
            info = {}
            for key in keys:
                info[key] = getattr(managed_object, key, None)

            self.fabric_net_group.append(
                info
            )

        return self.fabric_net_group

    def get_fabric_net_group(self):
        return self.get_fabric_net_group_mo()
