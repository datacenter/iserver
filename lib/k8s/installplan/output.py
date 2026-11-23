class K8sInstallplanOutput():
    def __init__(self):
        pass

    def print_installplans_state(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Install Plan', 'namespace_nameT'],
                ['Approved', 'approvedTick']
            ]
        )