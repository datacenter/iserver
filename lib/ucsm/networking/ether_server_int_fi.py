class EtherServerIntFi():
    def __init__(self):
        self.ether_server_int_fi = None

    def get_ether_server_int_fi_mo(self, cache_enabled=True):
        if self.ether_server_int_fi is not None and cache_enabled:
            return self.ether_server_int_fi

        self.ether_server_int_fi = []

        keys = [
            'admin_speed',
            'admin_state',
            'aggr_port_id',
            'chassis_id',
            'connected_adaptor_type',
            'dn',
            'encap',
            'ep_dn',
            'if_role',
            'if_type',
            'mac',
            'mac_addr',
            'mode',
            'model',
            'name',
            'oper_border_aggr_port_id',
            'oper_border_port_id',
            'oper_border_slot_id',
            'oper_state',
            'peer_aggr_port_id',
            'peer_chassis_id',
            'peer_dn',
            'peer_encap',
            'peer_port_id',
            'peer_slot_id',
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
            'vendor',
            'xcvr_supported',
            'xcvr_type'
        ]

        managed_objects = self.query_classid(
            'EtherServerIntFIo'
        )
        for managed_object in managed_objects:
            info = {}
            for key in keys:
                info[key] = getattr(managed_object, key, None)

            # "dn": "sys/chassis-2/slot-1/fabric/port-1"
            info['iom_id'] = info['dn'].split('/')[2].split('-')[1]

            self.ether_server_int_fi.append(
                info
            )

        return self.ether_server_int_fi

    def get_ether_server_int_fis(self, chassis_id=None):
        ports = self.get_ether_server_int_fi_mo()

        chassis_ports = []
        for port in ports:
            if chassis_id is not None:
                if port['chassis_id'] != chassis_id:
                    continue

            chassis_ports.append(
                port
            )

        return chassis_ports