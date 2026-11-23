class NodeApi():
    def __init__(self):
        self.node_mo = None

    def get_node_mo(self):
        if self.node_mo is not None:
            return self.node_mo

        cache = self.get_object_cache(
            'physicalNode'
        )
        if cache is not None:
            self.node_mo = cache
            self.log.apic_mo(
                'physicalNode',
                self.node_mo
            )
            return self.node_mo

        response = self.get_resource(
            '/crosswork/inventory/restconf/data/v2/resource-physical:node'
        )
        if response is None:
            self.log.error(
                'get_node_mo',
                'API failed'
            )
            return None

        try:
            self.node_mo = response['com.response-message']['com.data']['nd.node']
        except BaseException:
            self.log.error(
                'get_node_mo',
                'Unexpected response structure'
            )
            return None

        self.log.cnc_mo(
            'physicalNode',
            self.node_mo
        )

        self.set_object_cache(
            'physicalNode',
            self.node_mo
        )

        return self.node_mo
