class K8sLeaseOutput():
    def __init__(self):
        pass

    def print_leases(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Lease', 'namespace_nameT']
            ]
        )