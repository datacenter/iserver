class K8sAdminJobOutput():
    def __init__(self):
        pass

    def print_admin_jobs(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Admin Job', 'namespace_nameT']
            ]
        )