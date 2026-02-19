class K8sGrafanaDashboardOutput():
    def __init__(self):
        pass

    def print_grafana_dashboards(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Grafana Dashboard', 'namespace_nameT'],
                ['Ready', 'readyTick'],
                ['UID', 'uid'],
                ['Folder', 'folder'],
                ['Title', 'title'],
                ['Instance', 'instance'],
                ['Resync', 'resync']
            ]
        )
        