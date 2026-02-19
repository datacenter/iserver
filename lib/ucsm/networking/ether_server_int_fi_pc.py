class EtherServerIntFiPc():
    def __init__(self):
        self.ether_server_int_fi_pc = None

    def get_ether_server_int_fi_pc_mo(self, cache_enabled=True):
        if self.ether_server_int_fi_pc is not None and cache_enabled:
            return self.ether_server_int_fi_pc

        self.ether_server_int_fi_pc = []

        keys = [
            'chassis_id',
            'dn',
            'ep_dn',
            'if_role',
            'if_type',
            'name',
            'oper_speed',
            'oper_state',
            'peer_dn',
            'port_id',
            'rn',
            'state_qual',
            'status',
            'switch_id',
            'type'
        ]

        managed_objects = self.query_classid(
            'EtherServerIntFIoPc'
        )
        for managed_object in managed_objects:
            info = {}
            for key in keys:
                info[key] = getattr(managed_object, key, None)

            # "dn": "sys/chassis-2/slot-1/host/pc-1280"
            info['iom_id'] = info['dn'].split('/')[2].split('-')[1]

            self.ether_server_int_fi_pc.append(
                info
            )

        return self.ether_server_int_fi_pc

    def get_ether_server_int_fi_pcs(self, chassis_id=None):
        host_pcs = self.get_ether_server_int_fi_pc_mo()

        chassis_pc = []
        for host_pc in host_pcs:
            if chassis_id is not None:
                if host_pc['chassis_id'] != chassis_id:
                    continue

            chassis_pc.append(
                host_pc
            )

        return chassis_pc