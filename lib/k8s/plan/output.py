class K8sPlanOutput():
    def __init__(self):
        pass

    def print_plans(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Migration Plan', 'namespace_nameT'],
                ['State', 'stateT'],
                ['Type', 'migration_type'],
                ['Src', 'provider_source'],
                ['Dest', 'provider_destination'],
                ['Network', 'network_mapT'],
                ['Storage', 'storage_mapT'],
                ['Source VM', 'vm_migration_state.vm'],
                ['Phase', 'vm_migration_state.state']
            ]
        )