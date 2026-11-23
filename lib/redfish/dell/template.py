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

    def get_template_properties(self, template_name):
        properties = None

        if template_name == 'identity':
            properties = self.get_template_identity_properties()

        if template_name == 'power':
            properties = self.get_template_power_properties()

        if template_name == 'thermal':
            properties = self.get_template_thermal_properties()

        return properties
