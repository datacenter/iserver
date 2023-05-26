class FiThermal():
    def __init__(self, log_id=None):
        self.mo_equipment_psu_input_stats = None

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
