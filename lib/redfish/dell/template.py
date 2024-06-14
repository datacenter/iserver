import time

from lib.redfish.dell.identity import RedfishEndpointDellTemplateIdentity
from lib.redfish.dell.power import RedfishEndpointDellTemplatePower
from lib.redfish.dell.thermal import RedfishEndpointDellTemplateThermal


class RedfishEndpointDellTemplate(RedfishEndpointDellTemplateIdentity, RedfishEndpointDellTemplatePower, RedfishEndpointDellTemplateThermal):
    def __init__(self):
        RedfishEndpointDellTemplateIdentity.__init__(
            self
        )
        RedfishEndpointDellTemplatePower.__init__(
            self
        )
        RedfishEndpointDellTemplateThermal.__init__(
            self
        )

    def get_template_properties(self, template_name, cache_enabled=True, cache_key=None, cache_ttl=0):
        if cache_enabled and cache_key is not None:
            self.set_system_id(
                cache_key
            )
            properties = self.endpoint_handler.endpoint_settings_handler.get_endpoint_settings(
                cache_key,
                filename=template_name
            )
            if properties is not None:
                if cache_ttl == 0:
                    return properties['data']
                if int(time.time()) - properties['timestamp'] < cache_ttl:
                    return properties['data']

        properties = None

        if template_name == 'identity':
            properties = self.get_template_identity_properties()

        if template_name == 'power':
            properties = self.get_template_power_properties()

        if template_name == 'thermal':
            properties = self.get_template_thermal_properties()

        if properties is not None:
            if cache_enabled and cache_key is not None:
                cache_entry = {}
                cache_entry['timestamp'] = int(time.time())
                cache_entry['data'] = properties

                self.endpoint_handler.endpoint_settings_handler.set_endpoint_settings(
                    cache_key,
                    cache_entry,
                    filename=template_name
                )

        return properties
