class K8sSplunkMonitoringConsoleOutput():
    def __init__(self):
        pass

    def print_splunk_monitoring_consoles_state(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Splunk Monitoring Console', 'namespace_nameT'],
                ['Age', 'age']
            ]
        )
