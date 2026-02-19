import uuid


class RedfishEndpointHpeTemplateIdentity():
    def __init__(self):
        self.identity_main_url = '/'
        self.chassis_url = '/Chassis/1'
        self.system_url = '/Systems/1'

    def get_template_identity_properties(self):
        main = self.get_properties(self.identity_main_url)
        chassis = self.get_properties(self.chassis_url)
        system = self.get_properties(self.system_url)

        if main is None or chassis is None or system is None:
            return None

        properties = {}
        properties['Product'] = main['Product']
        properties['Model'] = system['Model']
        properties['Vendor'] = main['Vendor']
        properties['UUID'] = main['UUID']
        properties['Firmware'] = main['Oem']['Hpe']['Manager'][0]['ManagerFirmwareVersion']
        properties['HostName'] = main['Oem']['Hpe']['Manager'][0]['HostName']
        properties['Name'] = system['Name']
        properties['SerialNumber'] = chassis['SerialNumber']
        properties['PowerState'] = chassis['PowerState']
        properties['BiosVersion'] = system['BiosVersion']
        properties['RedfishVersion'] = main['RedfishVersion']

        return properties
