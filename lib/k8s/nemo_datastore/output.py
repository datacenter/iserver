class K8sNemoDatastoreOutput():
    def __init__(self):
        pass

    def print_nemo_datastores(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Nim Build', 'namespace_nameT']
            ]
        )