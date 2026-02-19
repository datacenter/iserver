class ExtEth():
    def __init__(self):
        self.ext_eth_ifs = None

    def get_ext_eth_ifs_mo(self, cache_enabled=True):
        if self.ext_eth_ifs is not None and cache_enabled:
            return self.ext_eth_ifs

        self.ext_eth_ifs = []

        keys = [
            'adapter_id',
            'admin_state',
            'aggr_port_id',
            'chassis_id',
            'dn',
            'ep_dn',
            'id',
            'if_type',
            'if_role',
            'link_state',
            'lldp_mac',
            'mac',
            'mac_addr_type',
            'name',
            'oper_state',
            'oper_state_desc',
            'peer_aggr_port_id',
            'peer_chassis_id',
            'peer_dn',
            'peer_port_id',
            'peer_slot_id',
            'phys_ep_dn',
            'port_id',
            'rn',
            'side',
            'slot_id',
            'status',
            'switch_id',
            'transport',
            'type'
        ]

        managed_objects = self.query_classid(
            'AdaptorExtEthIf'
        )
        for managed_object in managed_objects:
            info = {}
            for key in keys:
                info[key] = getattr(managed_object, key, None)

            # "dn": "sys/chassis-2/blade-2/adaptor-2/ext-eth-3"
            # "dn": "sys/rack-unit-3/adaptor-1/ext-eth-1"
            info['rack_id'] = None
            info['blade_id'] = None

            if len(info['dn'].split('/')[1].split('-')) == 2:
                info['blade_id'] = info['dn'].split('/')[2].split('-')[1]
                info['adaptor_dn'] = 'sys/chassis-%s/blade-%s/adaptor-%s' % (
                    info['chassis_id'],
                    info['blade_id'],
                    info['adapter_id']
                )

            if len(info['dn'].split('/')[1].split('-')) == 3:
                info['rack_id'] = info['dn'].split('/')[1].split('-')[2]
                info['adaptor_dn'] = 'sys/rack-unit-%s/adaptor-%s' % (
                    info['rack_id'],
                    info['adapter_id']
                )

            self.ext_eth_ifs.append(
                info
            )

        return self.ext_eth_ifs

    def get_compute_ext_eth_ifs(self, chassis_id=None, blade_id=None, rack_id=None):
        ext_eth_ifs = self.get_ext_eth_ifs_mo()

        compute_ifs = []

        for ext_eth_if in ext_eth_ifs:
            if chassis_id is not None:
                if ext_eth_if['chassis_id'] != chassis_id:
                    continue

            if blade_id is not None:
                if ext_eth_if['blade_id'] is None:
                    continue

                if ext_eth_if['blade_id'] != blade_id:
                    continue

            if rack_id is not None:
                if ext_eth_if['rack_id'] is None:
                    continue

                if ext_eth_if['rack_id'] != rack_id:
                    continue

            compute_ifs.append(
                ext_eth_if
            )

        return compute_ifs
