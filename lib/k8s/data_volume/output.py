class K8sDataVolumeOutput():
    def __init__(self):
        pass

    def print_data_volumes(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Data Volume', 'namespace_nameT'],
                ['Bound', 'boundTick'],
                ['Ready', 'readyTick'],
                ['Phase', 'phase'],
                ['Progress', 'progress'],
                ['Size', 'size'],
                ['Usage', 'usage'],
                ['Age', 'age']
            ]
        )
