class NodePsuApi():
    def __init__(self):
        self.nodes_psu_mo = None

    def get_nodes_psu_mo(self):
        if self.nodes_psu_mo is not None:
            return self.nodes_psu_mo

        managed_objects = self.get_class(
            'eqptPsu'
        )
        if managed_objects is None:
            self.log.error(
                'get_nodes_psu_mo',
                'API failed'
            )
            return None

        self.nodes_psu_mo = []
        for managed_object in managed_objects['imdata']:
            self.nodes_psu_mo.append(
                managed_object['eqptPsu']['attributes']
            )

        self.log.apic_mo(
            'eqptPsu',
            self.nodes_psu_mo
        )

        return self.nodes_psu_mo
