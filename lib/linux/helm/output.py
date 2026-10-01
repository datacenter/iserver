class LinuxHelmOutput():
    def __init__(self):
        pass

    def print_helm_repos_state(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Repository Name', 'name'],
                ['URL', 'url']
            ]
        )

    def print_helm_charts_state(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Namespace', 'namespace'],
                ['Name', 'name'],
                ['Revision', 'revision'],
                ['Updated', 'updated'],
                ['Status', 'status'],
                ['Chart', 'chart'],
                ['App Version', 'app_version']
            ]
        )
