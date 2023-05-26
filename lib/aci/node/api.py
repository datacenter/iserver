class NodeApi():
    def __init__(self):
        self.nodes_mo = None

    def get_nodes_mo(self):
        if self.nodes_mo is not None:
            return self.nodes_mo

        managed_objects = self.get_class(
            'fabricNode'
        )
        if managed_objects is None:
            self.log.error(
                'get_nodes_mo',
                'API failed'
            )
            return None

        self.nodes_mo = []
        for managed_object in managed_objects['imdata']:
            self.nodes_mo.append(
                managed_object['fabricNode']['attributes']
            )

        self.log.apic_mo(
            'fabricNode',
            self.nodes_mo
        )

        return self.nodes_mo
