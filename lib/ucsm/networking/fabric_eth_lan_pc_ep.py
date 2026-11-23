class FabricEthLanPcEp():
    def __init__(self):
        self.fabric_eth_lan_pc_ep = None

    def get_fabric_eth_lan_pc_ep_mo(self, cache_enabled=True):
        if self.fabric_eth_lan_pc_ep is not None and cache_enabled:
            return self.fabric_eth_lan_pc_ep

        self.fabric_eth_lan_pc_ep = []

        keys = [
            'admin_state',
            'aggr_port_id',
            'auto_negotiate',
            'chassis_id',
            'dn',
            'ep_dn',
            'eth_link_profile_name',
            'if_role',
            'if_type',
            'lic_gp',
            'lic_state',
            'membership',
            'name',
            'oper_eth_link_profile_name',
            'oper_state',
            'oper_state_reason',
            'peer_chassis_id',
            'peer_dn',
            'peer_port_id',
            'peer_slot_id',
            'port_id',
            'rn',
            'slot_id',
            'status',
            'switch_id',
            'transport',
            'type',
            'udld_oper_state',
            'usr_lbl',
            'warnings'
        ]

        managed_objects = self.query_classid(
            'fabricEthLanPcEp'
        )
        for managed_object in managed_objects:
            info = {}
            for key in keys:
                info[key] = getattr(managed_object, key, None)

            self.fabric_eth_lan_pc_ep.append(
                info
            )

        return self.fabric_eth_lan_pc_ep

    def get_fabric_eth_lan_pc_ep(self):
        return self.get_fabric_eth_lan_pc_ep_mo()
