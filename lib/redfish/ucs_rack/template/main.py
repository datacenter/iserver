import time

from lib.redfish.ucs_rack.template.account.main import RedfishEndpointUcsRackTemplateAccount
from lib.redfish.ucs_rack.template.identity.main import RedfishEndpointUcsRackTemplateIdentity
from lib.redfish.ucs_rack.template.power.main import RedfishEndpointUcsRackTemplatePower
from lib.redfish.ucs_rack.template.role.main import RedfishEndpointUcsRackTemplateRole
from lib.redfish.ucs_rack.template.storage.main import RedfishEndpointUcsRackTemplateStorage
from lib.redfish.ucs_rack.template.thermal.main import RedfishEndpointUcsRackTemplateThermal


class RedfishEndpointUcsRackTemplate(
        RedfishEndpointUcsRackTemplateAccount,
        RedfishEndpointUcsRackTemplateIdentity,
        RedfishEndpointUcsRackTemplatePower,
        RedfishEndpointUcsRackTemplateRole,
        RedfishEndpointUcsRackTemplateStorage,
        RedfishEndpointUcsRackTemplateThermal
        ):
    def __init__(self, endpoint_handler):
        self.endpoint_handler = endpoint_handler

        RedfishEndpointUcsRackTemplateAccount.__init__(
            self
        )
        RedfishEndpointUcsRackTemplateIdentity.__init__(
            self
        )
        RedfishEndpointUcsRackTemplatePower.__init__(
            self
        )
        RedfishEndpointUcsRackTemplateRole.__init__(
            self
        )
        RedfishEndpointUcsRackTemplateStorage.__init__(
            self
        )
        RedfishEndpointUcsRackTemplateThermal.__init__(
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
        if template_name == 'account':
            properties = self.get_template_account_properties(role_info=True, cache_enabled=cache_enabled)

        if template_name == 'identity':
            properties = self.get_template_identity_properties()

        if template_name == 'power':
            properties = self.get_template_power_properties()

        if template_name == 'role':
            properties = self.get_template_role_properties(account_info=True, cache_enabled=cache_enabled)

        if template_name == 'storage':
            properties = self.get_template_storage_properties()

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
