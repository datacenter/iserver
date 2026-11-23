class K8sObjectStoreOutput():
    def __init__(self):
        pass

    def print_object_stores_state(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Object Store', 'namespace_nameT']
            ]
        )