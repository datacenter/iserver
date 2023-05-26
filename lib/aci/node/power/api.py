class NodePowerApi():
    def __init__(self):
        self.nodes_power_mo = None

    def get_nodes_power_mo(self):
        if self.nodes_power_mo is not None:
            return self.nodes_power_mo

        managed_objects = self.get_class(
            'eqptPsPower'
        )
        if managed_objects is None:
            self.log.error(
                'get_nodes_power_mo',
                'API failed'
            )
            return None

        self.nodes_power_mo = []
        for managed_object in managed_objects['imdata']:
            if 'eqptPsPower15min' in managed_object:
                self.nodes_power_mo.append(
                    managed_object['eqptPsPower15min']['attributes']
                )

        self.log.apic_mo(
            'eqptPsPower',
            self.nodes_power_mo
        )

        return self.nodes_power_mo
