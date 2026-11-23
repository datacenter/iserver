import json


class K8sGrafanaOutput():
    def __init__(self):
        pass

    def print_grafanas(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Grafana Instance', 'namespace_nameT'],
                ['Ready', 'readyTick'],
                ['Label', 'labelT'],
                ['Access', 'access'],
                ['Datasource', 'datasource.dsT'],
                ['Dashboard', 'dashboardCount']
            ]
        )
