import uuid


class RedfishEndpointFabricInterconnectTemplateIdentityServer():
    def __init__(self):
        self.identity_main_url = '/'
        self.identity_system_url = '/Systems/SYSTEM_ID'
        self.identity_firmware_url = '/UpdateService/FirmwareInventory/CIMC'

    def get_template_identity_server_properties(self):
        main = self.get_properties(self.identity_main_url)
        if main is None:
            return None

        system = self.get_properties(self.identity_system_url)
        if system is None:
            return None

        firmware = self.get_properties(self.identity_firmware_url)
        if firmware is None:
            return None

        properties = {}
        properties['UUID'] = main['UUID']
        properties['RedfishVersion'] = main['RedfishVersion']
        properties['Product'] = system['Model']
        properties['Vendor'] = system['Manufacturer']

        if system is not None:
            keys = [
                'SerialNumber',
                'PowerState',
                'Name',
                'BiosVersion',
                'Model'
            ]
            for key in keys:
                properties[key] = ''
                if key in system:
                    properties[key] = system[key]

        properties['HostName'] = properties['Name']
        properties['Firmware'] = ''
        if firmware is not None:
            if 'Version' in firmware:
                properties['Firmware'] = firmware['Version']

        return properties
