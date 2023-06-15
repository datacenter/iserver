class NodePsuApi():
    def __init__(self):
        self.node_psu_mo = None

    def get_node_psu_mo(self):
        if self.node_psu_mo is not None:
            return self.node_psu_mo

        cache = self.get_object_cache(
            'eqptPsu'
        )
        if cache is not None:
            self.node_psu_mo = cache
            self.log.apic_mo(
                'eqptPsu',
                self.node_psu_mo
            )
            return self.node_psu_mo

        managed_objects = self.get_class(
            'eqptPsu'
        )
        if managed_objects is None:
            self.log.error(
                'get_node_psu_mo',
                'API failed'
            )
            return None

        self.node_psu_mo = []
        for managed_object in managed_objects['imdata']:
            self.node_psu_mo.append(
                managed_object['eqptPsu']['attributes']
            )

        self.log.apic_mo(
            'eqptPsu',
            self.node_psu_mo
        )

        self.set_object_cache(
            'eqptPsu',
            self.node_psu_mo
        )

        return self.node_psu_mo
