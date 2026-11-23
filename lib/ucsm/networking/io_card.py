class IoCard():
    def __init__(self):
        self.io_card = None

    def get_io_card_mo(self, cache_enabled=True):
        if self.io_card is not None and cache_enabled:
            return self.io_card

        self.io_card = []

        keys = [
            'admin_peer_power_state',
            'admin_power_state',
            'admin_state',
            'asset_tag',
            'base_addr',
            'chassis_id',
            'config_state',
            'dn',
            'id',
            'inlet1_sensor',
            'inlet2_sensor',
            'inlet2_thermal',
            'mfg_time',
            'model',
            'num_of_active_fabric_ports',
            'oper_evac_state',
            'oper_qualifier',
            'oper_qualifier_reason',
            'oper_state',
            'operability',
            'outlet_sensor',
            'outlet_thermal',
            'part_number',
            'peer_comm_status',
            'peer_dn',
            'perf',
            'power',
            'presence',
            'processor_thermal_state',
            'reset_required',
            'revision',
            'rn',
            'serial',
            'side',
            'slow_drain_admin_state',
            'slow_drain_correction',
            'status',
            'switch_id',
            'thermal',
            'upgrade_status',
            'usr_lbl',
            'vendor',
            'vid',
            'voltage'
        ]

        managed_objects = self.query_classid(
            'equipmentIOCard'
        )
        for managed_object in managed_objects:
            info = {}
            for key in keys:
                info[key] = getattr(managed_object, key, None)

            self.io_card.append(
                info
            )

        return self.io_card

    def get_io_cards(self, chassis_id=None):
        io_cards = self.get_io_card_mo()

        chassis_io_cards = []
        for io_card in io_cards:
            if chassis_id is not None:
                if io_card['chassis_id'] != chassis_id:
                    continue

            chassis_io_cards.append(
                io_card

            )

        return chassis_io_cards