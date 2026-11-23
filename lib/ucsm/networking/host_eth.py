class HostEth():
    def __init__(self):
        self.host_eth_ifs = None

    def get_host_eth_ifs_mo(self, cache_enabled=True):
        if self.host_eth_ifs is not None and cache_enabled:
            return self.host_eth_ifs

        self.host_eth_ifs = []

        keys = [
            'admin_state',
            'cdn_name',
            'chassis_id',
            'discovery',
            'dn',
            'ep_dn',
            'flt_aggr',
            'host_port',
            'id',
            'if_role',
            'if_type',
            'link_state',
            'mac',
            'model',
            'mtu',
            'name',
            'oper_qualifier_reason',
            'oper_state',
            'operability',
            'order',
            'pci_addr',
            'pci_func',
            'pci_slot',
            'peer_chassis_id',
            'peer_dn',
            'peer_port_id',
            'peer_slot_id',
            'perf',
            'pf_dn',
            'port_id',
            'power',
            'presence',
            'purpose',
            'q_in_q_enabled',
            'revision',
            'rn',
            'serial',
            'side',
            'slot_id',
            'sriov_hpn_preference',
            'status',
            'switch_id',
            'thermal',
            'transport',
            'type',
            'vendor',
            'virtualization_preference',
            'vnic_dn',
            'voltage'
        ]

        managed_objects = self.query_classid(
            'AdaptorHostEthIf'
        )
        for managed_object in managed_objects:
            info = {}
            for key in keys:
                info[key] = getattr(managed_object, key, None)

            if info['dn'].split('/')[1].split('-')[0] not in ['chassis', 'rack']:
                self.log.error(
                    'get_host_eth_ifs_mo',
                    'Unsupported object: %s' % (info['dn'])
                )

            if info['dn'].split('/')[1].split('-')[0] == 'chassis':
                # "dn": "sys/chassis-2/blade-1/adaptor-1/host-eth-2"
                info['chassis_id'] = info['dn'].split('/')[1].split('-')[1]
                info['blade_id'] = info['dn'].split('/')[2].split('-')[1]
                info['rack_id'] = None
                info['adaptor_id'] = info['dn'].split('/')[3].split('-')[1]
                info['interface_id'] = info['dn'].split('/')[4].split('-')[2]

            if info['dn'].split('/')[1].split('-')[0] == 'rack':
                # sys/rack-unit-1/adaptor-1/host-eth-1
                info['chassis_id'] = 'N/A'
                info['blade_id'] = None
                info['rack_id'] = info['dn'].split('/')[1].split('-')[2]
                info['adaptor_id'] = info['dn'].split('/')[2].split('-')[1]
                info['interface_id'] = info['dn'].split('/')[3].split('-')[2]

            self.host_eth_ifs.append(
                info
            )

        return self.host_eth_ifs

    def get_compute_host_eth_ifs(self, chassis_id=None, blade_id=None, rack_id=None):
        host_eth_ifs = self.get_host_eth_ifs_mo()

        compute_ifs = []

        serials = None
        if chassis_id is not None and blade_id is not None:
            serials = self.get_compute_adaptor_serials(chassis_id, blade_id)

        for host_eth_if in host_eth_ifs:
            if serials is not None:
                if host_eth_if['serial'] not in serials:
                    continue

            if rack_id is not None:
                if host_eth_if['rack_id'] is None:
                    continue

                if host_eth_if['rack_id'] != rack_id:
                    continue

            compute_ifs.append(
                host_eth_if
            )

        return compute_ifs
