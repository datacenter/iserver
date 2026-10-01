class K8sSplunkLicenseManagerOutput():
    def __init__(self):
        pass

    def print_splunk_license_managers_state(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Splunk License Manager', 'namespace_nameT']
            ]
        )