import uuid


class RedfishEndpointDellTemplateIdentity():
    def __init__(self):
        self.identity_main_url = '/'
        self.chassis_url = '/Chassis/System.Embedded.1'
        self.system_url = '/Systems/System.Embedded.1'
        self.idrac_url = '/Managers/iDRAC.Embedded.1'

    def get_template_identity_properties(self):
        main = self.get_properties(self.identity_main_url)
        chassis = self.get_properties(self.chassis_url)
        system = self.get_properties(self.system_url)
        idrac = self.get_properties(self.idrac_url)

        if main is None or chassis is None or system is None or idrac is None:
            return None

        properties = {}
        properties['Product'] = chassis['Model']
        properties['Model'] = chassis['Model']
        properties['Vendor'] = main['Vendor']
        properties['RedfishVersion'] = main['RedfishVersion']
        properties['UUID'] = chassis['UUID']
        properties['Firmware'] = idrac['FirmwareVersion']
        properties['HostName'] = system['HostName']
        properties['Name'] = system['Name']
        properties['SerialNumber'] = system['SerialNumber']
        properties['PowerState'] = system['PowerState']
        properties['BiosVersion'] = system['BiosVersion']

        return properties
