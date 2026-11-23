class NodeSystemApi():
    def __init__(self):
        self.node_system_mo = None

    def get_node_system_mo(self):
        if self.node_system_mo is not None:
            return self.node_system_mo

        cache = self.get_object_cache(
            'topSystem'
        )
        if cache is not None:
            self.node_system_mo = cache
            self.log.apic_mo(
                'topSystem',
                self.node_system_mo
            )
            return self.node_system_mo

        managed_objects = self.get_class(
            'topSystem'
        )
        if managed_objects is None:
            self.log.error(
                'get_node_system_mo',
                'API failed'
            )
            return None

        self.node_system_mo = []
        for managed_object in managed_objects['imdata']:
            self.node_system_mo.append(
                managed_object['topSystem']['attributes']
            )

        self.log.apic_mo(
            'topSystem',
            self.node_system_mo
        )

        self.set_object_cache(
            'topSystem',
            self.node_system_mo
        )

        return self.node_system_mo
