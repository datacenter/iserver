from lib.redfish.fi.identity_chassis import RedfishEndpointFabricInterconnectTemplateIdentityChassis
from lib.redfish.fi.identity_server import RedfishEndpointFabricInterconnectTemplateIdentityServer
from lib.redfish.fi.power_chassis import RedfishEndpointFabricInterconnectTemplatePowerChassis
from lib.redfish.fi.power_server import RedfishEndpointFabricInterconnectTemplatePowerServer
from lib.redfish.fi.thermal_chassis import RedfishEndpointFabricInterconnectTemplateThermalChassis
from lib.redfish.fi.thermal_server import RedfishEndpointFabricInterconnectTemplateThermalServer


class RedfishEndpointFabricInterconnectTemplates(
    RedfishEndpointFabricInterconnectTemplateIdentityChassis,
    RedfishEndpointFabricInterconnectTemplateIdentityServer,
    RedfishEndpointFabricInterconnectTemplatePowerChassis,
    RedfishEndpointFabricInterconnectTemplatePowerServer,
    RedfishEndpointFabricInterconnectTemplateThermalChassis,
    RedfishEndpointFabricInterconnectTemplateThermalServer
    ):
    def __init__(self):
        RedfishEndpointFabricInterconnectTemplateIdentityChassis.__init__(
            self
        )
        RedfishEndpointFabricInterconnectTemplateIdentityServer.__init__(
            self
        )
        RedfishEndpointFabricInterconnectTemplatePowerChassis.__init__(
            self
        )
        RedfishEndpointFabricInterconnectTemplatePowerServer.__init__(
            self
        )
        RedfishEndpointFabricInterconnectTemplateThermalChassis.__init__(
            self
        )
        RedfishEndpointFabricInterconnectTemplateThermalServer.__init__(
            self
        )

    def get_template_identity_properties(self):
        if self.inventory_type == 'Chassis':
            return self.get_template_identity_chassis_properties()

        if self.inventory_type == 'Server':
            return self.get_template_identity_server_properties()

        return None

    def get_template_properties(self, template_name):
        if template_name == 'identity':
            if self.inventory_type == 'Chassis':
                return self.get_template_identity_chassis_properties()

            if self.inventory_type == 'Server':
                return self.get_template_identity_server_properties()

        if template_name == 'power':
            if self.inventory_type == 'Chassis':
                return self.get_template_power_chassis_properties()

            if self.inventory_type == 'Server':
                return self.get_template_power_server_properties()

        if template_name == 'thermal':
            if self.inventory_type == 'Chassis':
                return self.get_template_thermal_chassis_properties()

            if self.inventory_type == 'Server':
                return self.get_template_thermal_server_properties()

        self.log.error(
            'get_template_properties',
            'Unsupported template: %s for inventory type %s' % (template_name, self.inventory_type)
        )

        return None

    def print_template_properties(self, template_name, properties):
        if template_name.lower() == 'identity':
            if self.inventory_type == 'Chassis':
                self.print_template_identity_chassis_properties(properties)

            if self.inventory_type == 'Server':
                self.print_template_identity_server_properties(properties)

        if template_name.lower() == 'power':
            if self.inventory_type == 'Chassis':
                self.print_template_power_chassis_properties(properties)

            if self.inventory_type == 'Server':
                self.print_template_power_server_properties(properties)

        if template_name.lower() == 'thermal':
            if self.inventory_type == 'Chassis':
                self.print_template_thermal_chassis_properties(properties)

            if self.inventory_type == 'Server':
                self.print_template_thermal_server_properties(properties)
