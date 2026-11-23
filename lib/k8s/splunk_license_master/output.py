class K8sSplunkLicenseMasterOutput():
    def __init__(self):
        pass

    def print_splunk_license_masters_state(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Splunk License Master', 'namespace_nameT']
            ]
        )