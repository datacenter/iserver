class EtherSwitchIntFiPc():
    def __init__(self):
        self.ether_switch_int_fi_pc = None

    def get_ether_switch_int_fi_pc_mo(self, cache_enabled=True):
        if self.ether_switch_int_fi_pc is not None and cache_enabled:
            return self.ether_switch_int_fi_pc

        self.ether_switch_int_fi_pc = []

        keys = [
            'admin_state',
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
            'transport',
            'type'
        ]

        managed_objects = self.query_classid(
            'EtherSwitchIntFIoPc'
        )
        for managed_object in managed_objects:
            info = {}
            for key in keys:
                info[key] = getattr(managed_object, key, None)

            # "dn": "sys/chassis-2/slot-2/fabric-pc/pc-1154",
            info['iom_id'] = info['dn'].split('/')[2].split('-')[1]

            self.ether_switch_int_fi_pc.append(
                info
            )

        return self.ether_switch_int_fi_pc

    def get_ether_switch_int_fi_pcs(self, chassis_id=None):
        host_pcs = self.get_ether_switch_int_fi_pc_mo()

        fi_pc = []
        for host_pc in host_pcs:
            if chassis_id is not None:
                if host_pc['chassis_id'] != chassis_id:
                    continue

            fi_pc.append(
                host_pc
            )

        return fi_pc