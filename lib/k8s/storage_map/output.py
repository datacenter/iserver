class K8sStorageMapOutput():
    def __init__(self):
        pass

    def print_storage_maps(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Storage Map', 'namespace_nameT'],
                ['Owner', 'ownerT'],
                ['Source', 'source_provider'],
                ['Storage', 'map.source'],
                ['Destination', 'destination_provider'],
                ['Storage', 'map.destination'],
                ['Status', 'status'],
                ['Plan', 'plan']
            ]
        )