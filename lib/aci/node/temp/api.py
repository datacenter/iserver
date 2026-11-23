class NodeTempApi():
    def __init__(self):
        self.node_temp_mo = None

    def get_node_temp_mo(self, deduplicate=True):
        if self.node_temp_mo is not None:
            return self.node_temp_mo

        cache = self.get_object_cache(
            'eqptTemp'
        )
        if cache is not None:
            self.node_temp_mo = cache
            self.log.apic_mo(
                'eqptTemp',
                self.node_temp_mo
            )
            return self.node_temp_mo

        managed_objects = self.get_class(
            'eqptTemp'
        )
        if managed_objects is None:
            self.log.error(
                'get_node_temp_mo',
                'API failed'
            )
            return None

        self.node_temp_mo = []
        dns = []
        for managed_object in managed_objects['imdata']:
            if 'eqptTemp15min' in managed_object:
                if deduplicate and managed_object['eqptTemp15min']['attributes']['dn'] in dns:
                    continue

                dns.append(
                    managed_object['eqptTemp15min']['attributes']['dn']
                )
                self.node_temp_mo.append(
                    managed_object['eqptTemp15min']['attributes']
                )

        self.log.apic_mo(
            'eqptTemp',
            self.node_temp_mo
        )

        self.set_object_cache(
            'eqptTemp',
            self.node_temp_mo
        )

        return self.node_temp_mo
