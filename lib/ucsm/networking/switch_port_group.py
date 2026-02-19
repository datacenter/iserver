class SwitchPortGroup():
    def __init__(self):
        self.switch_port_group = None

    def get_switch_port_group_mo(self, cache_enabled=True):
        if self.switch_port_group is not None and cache_enabled:
            return self.switch_port_group

        self.switch_port_group = []

        keys = [
            'dn',
            'name',
            'rn',
            'status',
            'transport',
            'type'
        ]

        managed_objects = self.query_classid(
            'portGroup'
        )
        for managed_object in managed_objects:
            info = {}
            for key in keys:
                info[key] = getattr(managed_object, key, None)

            # sys/switch-A/slot-1
            info['switch_id'] = info['dn'].split('/')[1].split('-')[1]

            self.switch_port_group.append(
                info
            )

        return self.switch_port_group

    def get_switch_port_groups(self, fi_id=None):
        switch_port_groups = self.get_switch_port_group_mo()

        fi_switch_port_groups = []
        for switch_port_group in switch_port_groups:
            if fi_id is not None:
                if switch_port_group['switch_id'] != fi_id:
                    continue

            fi_switch_port_groups.append(
                switch_port_group

            )

        return fi_switch_port_groups
