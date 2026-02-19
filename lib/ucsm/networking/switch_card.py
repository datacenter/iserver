class SwitchCard():
    def __init__(self):
        self.switch_card = None

    def get_switch_card_mo(self, cache_enabled=True):
        if self.switch_card is not None and cache_enabled:
            return self.switch_card

        self.switch_card = []

        keys = [
            'descr',
            'dn',
            'hotswap_thermal',
            'id',
            'inlet2_thermal',
            'model',
            'num_ports',
            'oper_qualifier_reason',
            'oper_state',
            'operability',
            'outlet_thermal',
            'perf',
            'power',
            'presence',
            'revision',
            'rn',
            'serial',
            'state',
            'status',
            'thermal',
            'vendor',
            'voltage'
        ]

        managed_objects = self.query_classid(
            'equipmentSwitchCard'
        )
        for managed_object in managed_objects:
            info = {}
            for key in keys:
                info[key] = getattr(managed_object, key, None)

            # sys/switch-A/slot-1
            info['switch_id'] = info['dn'].split('/')[1].split('-')[1]

            self.switch_card.append(
                info
            )

        return self.switch_card

    def get_switch_cards(self, fi_id=None):
        switch_cards = self.get_switch_card_mo()

        fi_switch_cards = []
        for switch_card in switch_cards:
            if fi_id is not None:
                if switch_card['switch_id'] != fi_id:
                    continue

            fi_switch_cards.append(
                switch_card

            )

        return fi_switch_cards