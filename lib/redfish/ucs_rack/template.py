from lib.redfish.ucs_rack.identity import RedfishEndpointUcsRackTemplateIdentity
from lib.redfish.ucs_rack.power import RedfishEndpointUcsRackTemplatePower
from lib.redfish.ucs_rack.thermal import RedfishEndpointUcsRackTemplateThermal


class RedfishEndpointUcsRackTemplate(RedfishEndpointUcsRackTemplateIdentity, RedfishEndpointUcsRackTemplatePower, RedfishEndpointUcsRackTemplateThermal):
    def __init__(self):
        RedfishEndpointUcsRackTemplateIdentity.__init__(
            self
        )
        RedfishEndpointUcsRackTemplatePower.__init__(
            self
        )
        RedfishEndpointUcsRackTemplateThermal.__init__(
            self
        )

    def get_template_properties(self, template_name):
        if template_name.lower() == 'power':
            return self.get_template_power_properties()

        if template_name.lower() == 'thermal':
            return self.get_template_thermal_properties()

        if template_name.lower() == 'identity':
            return self.get_template_identity_properties()

        self.my_output.error('Unsupported template: %s' % (template_name))
        self.my_output.default('Supported templates:')

        templates = ['identity', 'power', 'temp']
        for template in templates:
            self.my_output.default('- %s' % (template))

        return None

    def print_template_properties(self, template_name, properties):
        if template_name.lower() == 'identity':
            self.print_template_identity_properties(properties)

        if template_name.lower() == 'power':
            self.print_template_power_properties(properties)

        if template_name.lower() == 'thermal':
            self.print_template_thermal_properties(properties)
