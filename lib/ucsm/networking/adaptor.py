class Adaptor():
    def __init__(self):
        self.adaptor = None

    def get_adaptor_mo(self, cache_enabled=True):
        if self.adaptor is not None and cache_enabled:
            return self.adaptor

        self.adaptor = []

        keys = [
            'base_mac',
            'blade_id',
            'chassis_id',
            'conn_path',
            'conn_status',
            'dn',
            'id',
            'model',
            'oper_state',
            'operability',
            'part_number',
            'pci_addr',
            'pci_slot',
            'power',
            'presence',
            'reachability',
            'serial',
            'status',
            'thermal',
            'vendor',
            'vid',
            'visibility',
            'voltage'
        ]

        managed_objects = self.query_classid(
            'AdaptorUnit'
        )
        for managed_object in managed_objects:
            info = {}
            for key in keys:
                info[key] = getattr(managed_object, key, None)

            info['rack_id'] = None
            if info['chassis_id'] is None or info['chassis_id'] == 'N/A':
                # "dn": "sys/rack-unit-3/adaptor-1"
                if len(info['dn'].split('/')[1].split('rack-unit-')) == 2:
                    info['rack_id'] = info['dn'].split('/')[1].split('rack-unit-')[1]

            self.adaptor.append(
                info
            )

        return self.adaptor

    def get_compute_adaptor_serials(self, chassis_id, blade_id):
        serials = []

        adaptors = self.get_compute_adaptors(chassis_id=chassis_id, blade_id=blade_id)
        if adaptors is None:
            return serials

        for adaptor in adaptors:
            serials.append(
                adaptor['serial']
            )

        return serials

    def get_compute_adaptors(self, chassis_id=None, blade_id=None, rack_id=None):
        adaptors = self.get_adaptor_mo()

        compute_adaptors = []
        for adaptor in adaptors:
            if chassis_id is not None:
                if adaptor['chassis_id'] != chassis_id:
                    continue

            if blade_id is not None:
                if adaptor['blade_id'] != blade_id:
                    continue

            if rack_id is not None:
                if adaptor['rack_id'] is None:
                    continue

                if adaptor['rack_id'] != rack_id:
                    continue

            compute_adaptors.append(
                adaptor

            )

        return compute_adaptors
