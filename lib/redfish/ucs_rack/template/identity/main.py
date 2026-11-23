import uuid


class RedfishEndpointUcsRackTemplateIdentity():
    def __init__(self):
        self.identity_main_url = '/'
        self.identity_system_url = '/Systems/%s' % (self.get_system_id())
        self.identity_firmware_url = '/UpdateService/FirmwareInventory/CIMC'

    def get_template_identity_properties(self):
        main = self.get_properties(self.identity_main_url)
        system = self.get_properties(self.identity_system_url)
        firmware = self.get_properties(self.identity_firmware_url)

        if main is None:
            return None

        properties = {}
        properties['Product'] = main['Product']
        properties['Vendor'] = main['Vendor']
        properties['RedfishVersion'] = main['RedfishVersion']

        if system is not None:
            keys = [
                'SerialNumber',
                'PowerState',
                'HostName',
                'UUID',
                'Name',
                'BiosVersion',
                'Model'

            ]
            for key in keys:
                properties[key] = ''
                if key in system:
                    properties[key] = system[key]

        properties['Firmware'] = ''
        if firmware is not None:
            if 'Version' in firmware:
                properties['Firmware'] = firmware['Version']

        return properties
