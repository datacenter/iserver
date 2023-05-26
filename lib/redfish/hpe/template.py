from lib.redfish.hpe.identity import RedfishEndpointHpeTemplateIdentity
from lib.redfish.hpe.power import RedfishEndpointHpeTemplatePower
from lib.redfish.hpe.thermal import RedfishEndpointHpeTemplateThermal


class RedfishEndpointHpeTemplate(RedfishEndpointHpeTemplateIdentity, RedfishEndpointHpeTemplatePower, RedfishEndpointHpeTemplateThermal):
    def __init__(self):
        RedfishEndpointHpeTemplateIdentity.__init__(
            self
        )
        RedfishEndpointHpeTemplatePower.__init__(
            self
        )
        RedfishEndpointHpeTemplateThermal.__init__(
            self
        )

    def get_template_properties(self, template_name):
        if template_name.lower() == 'identity':
            return self.get_template_identity_properties()

        if template_name.lower() == 'power':
            return self.get_template_power_properties()

        if template_name.lower() == 'thermal':
            return self.get_template_thermal_properties()

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
