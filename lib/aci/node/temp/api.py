class NodeTempApi():
    def __init__(self):
        self.nodes_temp_mo = None

    def get_nodes_temp_mo(self):
        if self.nodes_temp_mo is not None:
            return self.nodes_temp_mo

        managed_objects = self.get_class(
            'eqptTemp'
        )
        if managed_objects is None:
            self.log.error(
                'get_nodes_temp_mo',
                'API failed'
            )
            return None

        self.nodes_temp_mo = []
        for managed_object in managed_objects['imdata']:
            if 'eqptTemp15min' in managed_object:
                self.nodes_temp_mo.append(
                    managed_object['eqptTemp15min']['attributes']
                )

        self.log.apic_mo(
            'eqptTemp',
            self.nodes_temp_mo
        )

        return self.nodes_temp_mo
