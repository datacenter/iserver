from lib.redfish.ucs_rack.template.account.output import RedfishEndpointUcsRackTemplateAccountOutput
from lib.redfish.ucs_rack.template.identity.output import RedfishEndpointUcsRackTemplateIdentityOutput
from lib.redfish.ucs_rack.template.power.output import RedfishEndpointUcsRackTemplatePowerOutput
from lib.redfish.ucs_rack.template.role.output import RedfishEndpointUcsRackTemplateRoleOutput
from lib.redfish.ucs_rack.template.storage.output import RedfishEndpointUcsRackTemplateStorageOutput
from lib.redfish.ucs_rack.template.thermal.output import RedfishEndpointUcsRackTemplateThermalOutput


class RedfishEndpointUcsRackTemplateOutput(
        RedfishEndpointUcsRackTemplateAccountOutput,
        RedfishEndpointUcsRackTemplateIdentityOutput,
        RedfishEndpointUcsRackTemplatePowerOutput,
        RedfishEndpointUcsRackTemplateRoleOutput,
        RedfishEndpointUcsRackTemplateStorageOutput,
        RedfishEndpointUcsRackTemplateThermalOutput
        ):
    def __init__(self):
        RedfishEndpointUcsRackTemplateAccountOutput.__init__(self)
        RedfishEndpointUcsRackTemplateIdentityOutput.__init__(self)
        RedfishEndpointUcsRackTemplatePowerOutput.__init__(self)
        RedfishEndpointUcsRackTemplateRoleOutput.__init__(self)
        RedfishEndpointUcsRackTemplateStorageOutput.__init__(self)
        RedfishEndpointUcsRackTemplateThermalOutput.__init__(self)

    def print_ucsc_properties(self, template_name, properties, title=False):
        if template_name == 'account':
            self.print_ucsc_account_properties(
                properties,
                title=title
            )

        if template_name == 'identity':
            self.print_ucsc_identity_properties(properties)

        if template_name == 'power':
            self.print_ucsc_power_properties(properties)

        if template_name == 'role':
            self.print_ucsc_role_properties(
                properties,
                title=title
            )

        if template_name == 'storage':
            self.print_ucsc_storage_properties(properties)

        if template_name == 'thermal':
            self.print_ucsc_thermal_properties(properties)
