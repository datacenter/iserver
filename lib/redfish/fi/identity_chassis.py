import uuid

from lib import ip_helper


class RedfishEndpointFabricInterconnectTemplateIdentityChassis():
    def __init__(self):
        self.identity_main_url = '/'
        self.default_chassis_uri = '/redfish/v1/Chassis/1'

    def get_chassis_uri(self):
        uri = '/redfish/v1/Chassis'
        children = self.endpoint_handler.get_odata_ids(uri)
        if children is None:
            self.log.error(
                'get_chassis_uri',
                'Failed to discover Chassis: %s' % (uri)
            )
            return self.default_chassis_uri

        chassis_uri = None
        for child in children:
            if child == uri:
                continue

            leaf = child.split('/')[-1]

            if leaf == 'Chassis':
                continue

            if leaf == 'CMC':
                continue

            if leaf == 'PeerCMC':
                continue

            if leaf.startswith('FEM'):
                continue

            if leaf.startswith('Blade'):
                continue

            chassis_uri = 'Chassis/%s' % (leaf)
            break

        if chassis_uri is None:
            self.log.error(
                'get_chassis_uri',
                'Failed to find Chassis: %s' % (uri)
            )
            return self.default_chassis_uri

        return chassis_uri

    def get_identity_chassis_default_cache_name(self, properties):
        name = 'chassis-%s-%s' % (
            properties['Product'],
            properties['SerialNumber'].lower()
        )
        return name

    def get_template_identity_chassis_properties(self):
        main = self.get_properties(self.identity_main_url)
        if main is None:
            return None

        chassis = self.get_properties(self.get_chassis_uri())
        if chassis is None:
            return None

        properties = {}
        properties['Product'] = chassis['Model']
        properties['Model'] = chassis['Model']
        properties['Vendor'] = chassis['Manufacturer']
        properties['RedfishVersion'] = main['RedfishVersion']
        properties['SerialNumber'] = chassis['SerialNumber']
        properties['PowerState'] = 'Off'
        if self.is_chassis_power_on():
            properties['PowerState'] = 'On'
        properties['HostName'] = None
        properties['UUID'] = ip_helper.generate_uuid(
            properties['SerialNumber']
        )
        properties['Name'] = None

        properties['DefaultCacheName'] = self.get_identity_chassis_default_cache_name(properties)
        properties['CacheFileName'] = properties['UUID'].lower()

        return properties
