class NodeSystemApi():
    def __init__(self):
        self.nodes_system_mo = None

    def get_nodes_system_mo(self):
        if self.nodes_system_mo is not None:
            return self.nodes_system_mo

        managed_objects = self.get_class(
            'topSystem'
        )
        if managed_objects is None:
            self.log.error(
                'get_nodes_system_mo',
                'API failed'
            )
            return None

        self.nodes_system_mo = []
        for managed_object in managed_objects['imdata']:
            self.nodes_system_mo.append(
                managed_object['topSystem']['attributes']
            )

        self.log.apic_mo(
            'topSystem',
            self.nodes_system_mo
        )

        return self.nodes_system_mo
