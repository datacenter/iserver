class EthPort():
    def __init__(self):
        self.eth_port = None

    def get_eth_port_mo(self, cache_enabled=True):
        if self.eth_port is not None and cache_enabled:
            return self.eth_port

        self.eth_port = []

        keys = [
            'admin_state',
            'admin_transport',
            'aggr_port_id',
            'chassis_id',
            'dn',
            'encap',
            'ep_dn',
            'if_role',
            'if_type',
            'is_breakout_xcvr',
            'is_port_channel_member',
            'is_uplink_peer_port_stp',
            'lic_gp',
            'lic_state',
            'mac',
            'mode',
            'model',
            'name',
            'non_c_r4',
            'oper_speed',
            'oper_state',
            'peer_aggr_port_id',
            'peer_chassis_id',
            'peer_dn',
            'peer_port_id',
            'peer_slot_id',
            'port_capability',
            'port_id',
            'revision',
            'rn',
            'serial',
            'slot_id',
            'state_qual',
            'status',
            'switch_id',
            'transport',
            'type',
            'unified_port',
            'usr_lbl',
            'vendor',
            'xcvr_type'
        ]

        managed_objects = self.query_classid(
            'EtherPIo'
        )
        for managed_object in managed_objects:
            info = {}
            for key in keys:
                info[key] = getattr(managed_object, key, None)

            self.eth_port.append(
                info
            )

        return self.eth_port

    def get_eth_ports(self, fi_id=None):
        ports = self.get_eth_port_mo()

        fi_ports = []
        for port in ports:
            if port['switch_id'] != fi_id:
                continue

            fi_ports.append(
                port
            )

        return fi_ports