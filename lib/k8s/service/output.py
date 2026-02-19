class K8sServiceOutput():
    def __init__(self):
        pass

    def print_services(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Service', 'namespace_nameT'],
                ['Type', 'type'],
                ['IP', 'ipT'],
                ['Port', 'portT'],
                ['Selector', 'selectorT'],
                ['POD', 'podT'],
                ['Age', 'age']
            ]
        )

    def print_services_metadata(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Service', 'namespace_nameT'],
                ['Owner', 'ownerT'],
                ['Label', 'labelT'],
                ['Selector', 'selectorT']
            ]
        )
