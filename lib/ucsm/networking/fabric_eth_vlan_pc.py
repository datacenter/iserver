class FabricEthVlanPc():
    def __init__(self):
        self.fabric_eth_vlan_pc = None

    def get_fabric_eth_vlan_pc_mo(self, cache_enabled=True):
        if self.fabric_eth_vlan_pc is not None and cache_enabled:
            return self.fabric_eth_vlan_pc

        self.fabric_eth_vlan_pc = []

        keys = [
            'admin_speed',
            'admin_state',
            'descr',
            'dn',
            'ep_dn',
            'if_role',
            'if_type',
            'is_native',
            'name',
            'oper_speed',
            'oper_state',
            'peer_dn',
            'port_id',
            'rn',
            'state_qual',
            'status',
            'switch_id',
            'transport',
            'type',
            'warnings'
        ]

        managed_objects = self.query_classid(
            'fabricEthVlanPc'
        )
        for managed_object in managed_objects:
            info = {}
            for key in keys:
                info[key] = getattr(managed_object, key, None)

            self.fabric_eth_vlan_pc.append(
                info
            )

        return self.fabric_eth_vlan_pc

    def get_fabric_eth_vlan_pc(self):
        return self.get_fabric_eth_vlan_pc_mo()
