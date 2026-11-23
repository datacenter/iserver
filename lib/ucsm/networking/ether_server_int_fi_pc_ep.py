class EtherServerIntFiPcEp():
    def __init__(self):
        self.ether_server_int_fi_pc_ep = None

    def get_ether_server_int_fi_pc_ep_mo(self, cache_enabled=True):
        if self.ether_server_int_fi_pc_ep is not None and cache_enabled:
            return self.ether_server_int_fi_pc_ep

        self.ether_server_int_fi_pc_ep = []

        keys = [
            'admin_state',
            'aggr_port_id',
            'chassis_id',
            'dn',
            'ep_dn',
            'if_role',
            'if_type',
            'name',
            'peer_aggr_port_id',
            'peer_chassis_id',
            'peer_dn',
            'peer_port_id',
            'peer_slot_id',
            'port_id',
            'rn',
            'slot_id',
            'switch_id',
            'transport',
            'type'
        ]

        managed_objects = self.query_classid(
            'EtherServerIntFIoPcEp'
        )
        for managed_object in managed_objects:
            info = {}
            for key in keys:
                info[key] = getattr(managed_object, key, None)

            # "dn": "sys/chassis-2/slot-2/host/pc-1296/ep-slot-2-port-3"
            info['iom_id'] = info['dn'].split('/')[2].split('-')[1]

            self.ether_server_int_fi_pc_ep.append(
                info
            )

        return self.ether_server_int_fi_pc_ep

    def get_ether_server_int_fi_pc_eps(self, chassis_id=None):
        host_pcs = self.get_ether_server_int_fi_pc_ep_mo()

        chassis_pc = []
        for host_pc in host_pcs:
            if chassis_id is not None:
                if host_pc['chassis_id'] != chassis_id:
                    continue

            chassis_pc.append(
                host_pc
            )

        return chassis_pc