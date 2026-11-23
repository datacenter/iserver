class FabricEthLanPc():
    def __init__(self):
        self.fabric_eth_lan_pc = None

    def get_fabric_eth_lan_pc_mo(self, cache_enabled=True):
        if self.fabric_eth_lan_pc is not None and cache_enabled:
            return self.fabric_eth_lan_pc

        self.fabric_eth_lan_pc = []

        keys = [
            'admin_speed',
            'admin_state',
            'auto_negotiate',
            'bandwidth',
            'descr',
            'dn',
            'ep_dn',
            'flow_ctrl_policy',
            'if_role',
            'if_type',
            'is_uplink_peer_port_stp',
            'lacp_policy_name',
            'name',
            'oper_lacp_policy_name',
            'oper_speed',
            'oper_state',
            'overlapping_vlans',
            'peer_dn',
            'port_id',
            'rn',
            'state_qual',
            'status',
            'switch_id',
            'transport',
            'type',
            'vlan_status',
            'warnings'
        ]

        managed_objects = self.query_classid(
            'fabricEthLanPc'
        )
        for managed_object in managed_objects:
            info = {}
            for key in keys:
                info[key] = getattr(managed_object, key, None)

            self.fabric_eth_lan_pc.append(
                info
            )

        return self.fabric_eth_lan_pc

    def get_fabric_eth_lan_pc(self):
        return self.get_fabric_eth_lan_pc_mo()
