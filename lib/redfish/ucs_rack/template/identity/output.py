class RedfishEndpointUcsRackTemplateIdentityOutput(
    ):
    def __init__(self):
        pass

    def print_ucsc_identity_properties(self, properties):
        keys = [
            'Product',
            'Vendor',
            'Model',
            'Name',
            'HostName',
            'SerialNumber',
            'UUID',
            'BiosVersion',
            'Firmware',
            'PowerState',
            'RedfishVersion'
        ]

        headers = [
            'Product',
            'Vendor',
            'Model',
            'Name',
            'Hostname',
            'Serial Number',
            'UUID',
            'Bios Version',
            'Firmware',
            'Power State',
            'Redfish Version'
        ]

        self.my_output.dictionary(
            properties,
            title='UCS Rack Redfish Endpoint',
            underline=True,
            prefix="- ",
            justify=True,
            keys=keys,
            title_keys=headers
        )
