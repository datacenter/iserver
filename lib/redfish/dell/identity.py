import uuid


class RedfishEndpointDellTemplateIdentity():
    def __init__(self):
        self.identity_main_url = '/'
        self.chassis_url = '/Chassis/System.Embedded.1'
        self.system_url = '/Systems/System.Embedded.1'
        self.idrac_url = '/Managers/iDRAC.Embedded.1'

    def get_identity_default_cache_name(self, properties):
        firmware = properties['Firmware']
        if len(firmware) > 0:
            firmware = firmware.replace('(', '.').replace(')', '')

        product = properties['Product'].replace(' ', '-')

        name = 'dell-%s-%s-%s-%s' % (
            product.lower(),
            properties['SerialNumber'].lower(),
            firmware.lower(),
            properties['PowerState'].lower()
        )
        return name

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

        properties['DefaultCacheName'] = self.get_identity_default_cache_name(properties)
        if properties['UUID'] == '':
            properties['CacheFileName'] = str(uuid.uuid4()).lower()
        else:
            properties['CacheFileName'] = properties['UUID'].lower()

        return properties
