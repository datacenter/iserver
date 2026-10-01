class K8sCatalogSourceOutput():
    def __init__(self):
        pass

    def print_catalog_sources_state(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Catalog Source', 'namespace_nameT'],
                ['Display Name', 'display_name'],
                ['Age', 'age']
            ]
        )