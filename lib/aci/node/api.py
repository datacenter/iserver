class NodeApi():
    def __init__(self):
        self.node_mo = None

    def get_node_mo(self):
        if self.node_mo is not None:
            return self.node_mo

        cache = self.get_object_cache(
            'fabricNode'
        )
        if cache is not None:
            self.node_mo = cache
            self.log.apic_mo(
                'fabricNode',
                self.node_mo
            )
            return self.node_mo

        managed_objects = self.get_class(
            'fabricNode'
        )
        if managed_objects is None:
            self.log.error(
                'get_node_mo',
                'API failed'
            )
            return None

        self.node_mo = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['fabricNode']['attributes']
            self.node_mo.append(
                attributes
            )

        self.log.apic_mo(
            'fabricNode',
            self.node_mo
        )

        self.set_object_cache(
            'fabricNode',
            self.node_mo
        )

        return self.node_mo
