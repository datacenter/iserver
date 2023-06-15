class NodePowerApi():
    def __init__(self):
        self.node_power_mo = None

    def get_node_power_mo(self, deduplicate=True):
        if self.node_power_mo is not None:
            return self.node_power_mo

        cache = self.get_object_cache(
            'eqptPsPower'
        )
        if cache is not None:
            self.node_power_mo = cache
            self.log.apic_mo(
                'eqptPsPower',
                self.node_power_mo
            )
            return self.node_power_mo

        managed_objects = self.get_class(
            'eqptPsPower'
        )
        if managed_objects is None:
            self.log.error(
                'get_node_power_mo',
                'API failed'
            )
            return None

        self.node_power_mo = []
        dns = []
        for managed_object in managed_objects['imdata']:
            if 'eqptPsPower15min' in managed_object:
                if deduplicate and managed_object['eqptPsPower15min']['attributes']['dn'] in dns:
                    continue

                dns.append(
                    managed_object['eqptPsPower15min']['attributes']['dn']
                )
                self.node_power_mo.append(
                    managed_object['eqptPsPower15min']['attributes']
                )

        self.log.apic_mo(
            'eqptPsPower',
            self.node_power_mo
        )

        self.set_object_cache(
            'eqptPsPower',
            self.node_power_mo
        )

        return self.node_power_mo
