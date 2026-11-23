class K8sDataSourceOutput():
    def __init__(self):
        pass

    def print_data_sources(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Data Source', 'name'],
                ['Import Schedule', 'schedule'],
                ['Ready', 'readyTick'],
                ['DV / PVC', 'pvc_name'],
                ['DV Phase', 'dv_phase'],
                ['PVC Phase', 'pvc_phase']
            ]
        )