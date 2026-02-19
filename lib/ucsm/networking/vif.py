class Vif():
    def __init__(self):
        self.vif = None

    def get_vif_mo(self, cache_enabled=True):
        if self.vif is not None and cache_enabled:
            return self.vif

        self.vif = []

        keys = [
            'admin_state',
            'dn',
            'ep_dn',
            'id',
            'if_role',
            'if_type',
            'inst_type',
            'link_state',
            'name',
            'oper_state',
            'prot_peer_id',
            'prot_role',
            'prot_state',
            'rn',
            'state',
            'status',
            'switch_id',
            'type'
        ]

        managed_objects = self.query_classid(
            'DcxVIf'
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
                # sys/chassis-1/blade-3/adaptor-1/host-eth-1/vif-792
                info['chassis_id'] = info['dn'].split('/')[1].split('-')[1]
                info['blade_id'] = info['dn'].split('/')[2].split('-')[1]
                info['rack_id'] = None
                info['adaptor_id'] = info['dn'].split('/')[3].split('-')[1]
                info['interface_id'] = info['dn'].split('/')[4].split('-')[2]

            if info['dn'].split('/')[1].split('-')[0] == 'rack':
                # sys/rack-unit-1/adaptor-1/host-eth-1/vif-792
                info['chassis_id'] = 'N/A'
                info['blade_id'] = None
                info['rack_id'] = info['dn'].split('/')[1].split('-')[2]
                info['adaptor_id'] = info['dn'].split('/')[2].split('-')[1]
                info['interface_id'] = info['dn'].split('/')[3].split('-')[2]

            self.vif.append(
                info
            )

        return self.vif

    def get_compute_vifs(self, chassis_id=None, blade_id=None, rack_id=None):
        vifs = self.get_vif_mo()

        compute_vifs = []
        for vif in vifs:
            if chassis_id is not None:
                if vif['chassis_id'] != chassis_id:
                    continue

            if blade_id is not None:
                if vif['blade_id'] is None:
                    continue

                if vif['blade_id'] != blade_id:
                    continue

            if rack_id is not None:
                if vif['rack_id'] is None:
                    continue

                if vif['rack_id'] != rack_id:
                    continue

            compute_vifs.append(
                vif

            )

        return compute_vifs
