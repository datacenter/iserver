class K8sPvOutput():
    def __init__(self):
        pass

    def print_pvs(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Persistent Volume', 'name'],
                ['Status', 'phase'],
                ['Mode', 'volume_mode'],
                ['SC', 'storage_class'],
                ['Size', 'capacity.storage'],
                ['Access', 'access_modesT'],
                ['PVC', 'pvc_namespace_nameT'],
                ['Age', 'age']
            ]
        )

    def print_pvs_csi(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Persistent Volume', 'name'],
                ['Status', 'phase'],
                ['Size', 'capacity.storage'],
                ['SC', 'storage_class'],
                ['CSI Driver', 'csi_driverT'],
                ['CSI Handle', 'csi_handleT'],
                ['Device', 'deviceT'],
                ['Age', 'age']
            ]
        )
