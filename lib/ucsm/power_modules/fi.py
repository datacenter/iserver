class FiPower():
    def __init__(self, log_id=None):
        self.mo_equipment_psu_input_stats = None

    def get_equipment_psu_input_stats_info(self, managed_object):
        info = {}

        keys = [
            'dn',
            'input_status',
            'time_collected'
        ]
        for key in keys:
            info[key] = getattr(managed_object, key)

        info['switch_name'] = info['dn'].split('/')[1]
        info['psu_name'] = info['dn'].split('/')[2]

        for suffix in ['', '_avg', '_min', '_max']:
            info['current%s' % (suffix)] = getattr(managed_object, 'current%s' % (suffix))
            info['power%s' % (suffix)] = getattr(managed_object, 'power%s' % (suffix))
            info['voltage%s' % (suffix)] = getattr(managed_object, 'voltage%s' % (suffix))

        return info

    def get_equipment_psu_input_stats(self):
        if self.mo_equipment_psu_input_stats is None:
            managed_objects = self.query_classid(
                'EquipmentPsuInputStats'
            )
            if managed_objects is None:
                return None

            self.mo_equipment_psu_input_stats = managed_objects

        psu_stats = []

        for managed_object in self.mo_equipment_psu_input_stats:
            psu_stats.append(
                self.get_equipment_psu_input_stats_info(
                    managed_object
                )
            )

        return psu_stats
