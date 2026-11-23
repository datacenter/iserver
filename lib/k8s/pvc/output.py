class K8sPvcOutput():
    def __init__(self):
        pass

    def print_pvcs_base(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['PVC', 'namespace_nameT'],
                ['Status', 'phase'],
                ['PV', 'volume_name'],
                ['Mode', 'volume_mode'],
                ['Size', 'size'],
                ['Access', 'access_modesT'],
                ['Storage Class', 'storage_class_name'],
                ['Age', 'age']
            ]
        )

    def print_pvcs(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['PVC', 'namespace_nameT'],
                ['Status', 'phase'],
                ['Mode', 'volume_mode'],
                ['Size', 'size'],
                ['Access', 'access_modesT'],
                ['Storage Class', 'storage_class_name'],
                ['Usage', 'usage'],
                ['PV', 'volume_name'],
                ['Age', 'age']
            ]
        )

    def print_pvcs_metadata(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['PVC', 'namespace_nameT'],
                ['Owner', 'ownerT'],
                ['Label', 'labelT'],
                ['Annotation', 'annotationT']
            ]
        )
