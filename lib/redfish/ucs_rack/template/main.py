import time

from lib.redfish.ucs_rack.template.account.main import RedfishEndpointUcsRackTemplateAccount
from lib.redfish.ucs_rack.template.bios.main import RedfishEndpointUcsRackTemplateBios
from lib.redfish.ucs_rack.template.cpu.main import RedfishEndpointUcsRackTemplateCpu
from lib.redfish.ucs_rack.template.fan.main import RedfishEndpointUcsRackTemplateFan
from lib.redfish.ucs_rack.template.gpu.main import RedfishEndpointUcsRackTemplateGpu
from lib.redfish.ucs_rack.template.identity.main import RedfishEndpointUcsRackTemplateIdentity
from lib.redfish.ucs_rack.template.mem.main import RedfishEndpointUcsRackTemplateMem
from lib.redfish.ucs_rack.template.net.main import RedfishEndpointUcsRackTemplateNet
from lib.redfish.ucs_rack.template.pci.main import RedfishEndpointUcsRackTemplatePci
from lib.redfish.ucs_rack.template.power.main import RedfishEndpointUcsRackTemplatePower
from lib.redfish.ucs_rack.template.psu.main import RedfishEndpointUcsRackTemplatePsu
from lib.redfish.ucs_rack.template.role.main import RedfishEndpointUcsRackTemplateRole
from lib.redfish.ucs_rack.template.storage.main import RedfishEndpointUcsRackTemplateStorage
from lib.redfish.ucs_rack.template.thermal.main import RedfishEndpointUcsRackTemplateThermal


class RedfishEndpointUcsRackTemplate(
        RedfishEndpointUcsRackTemplateAccount,
        RedfishEndpointUcsRackTemplateBios,
        RedfishEndpointUcsRackTemplateCpu,
        RedfishEndpointUcsRackTemplateFan,
        RedfishEndpointUcsRackTemplateGpu,
        RedfishEndpointUcsRackTemplateIdentity,
        RedfishEndpointUcsRackTemplateMem,
        RedfishEndpointUcsRackTemplateNet,
        RedfishEndpointUcsRackTemplatePci,
        RedfishEndpointUcsRackTemplatePower,
        RedfishEndpointUcsRackTemplatePsu,
        RedfishEndpointUcsRackTemplateRole,
        RedfishEndpointUcsRackTemplateStorage,
        RedfishEndpointUcsRackTemplateThermal
        ):
    def __init__(self, endpoint_handler):
        self.endpoint_handler = endpoint_handler

        RedfishEndpointUcsRackTemplateAccount.__init__(self)
        RedfishEndpointUcsRackTemplateBios.__init__(self)
        RedfishEndpointUcsRackTemplateCpu.__init__(self)
        RedfishEndpointUcsRackTemplateFan.__init__(self)
        RedfishEndpointUcsRackTemplateGpu.__init__(self)
        RedfishEndpointUcsRackTemplateIdentity.__init__(self)
        RedfishEndpointUcsRackTemplateMem.__init__(self)
        RedfishEndpointUcsRackTemplateNet.__init__(self)
        RedfishEndpointUcsRackTemplatePci.__init__(self)
        RedfishEndpointUcsRackTemplatePower.__init__(self)
        RedfishEndpointUcsRackTemplatePsu.__init__(self)
        RedfishEndpointUcsRackTemplateRole.__init__(self)
        RedfishEndpointUcsRackTemplateStorage.__init__(self)
        RedfishEndpointUcsRackTemplateThermal.__init__(self)

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

        if template_name == 'bios':
            properties = self.get_template_bios_properties(cache_enabled=cache_enabled)

        if template_name == 'cpu':
            properties = self.get_template_cpu_properties(cache_enabled=cache_enabled)

        if template_name == 'fan':
            properties = self.get_template_fan_properties(cache_enabled=cache_enabled)

        if template_name == 'gpu':
            properties = self.get_template_gpu_properties(cache_enabled=cache_enabled)

        if template_name == 'identity':
            properties = self.get_template_identity_properties()

        if template_name == 'mem':
            properties = self.get_template_mem_properties(cache_enabled=cache_enabled)

        if template_name == 'net':
            properties = self.get_template_net_properties(cache_enabled=cache_enabled)

        if template_name == 'pci':
            properties = self.get_template_pci_properties(cache_enabled=cache_enabled)

        if template_name == 'power':
            properties = self.get_template_power_properties()

        if template_name == 'psu':
            properties = self.get_template_psu_properties(cache_enabled=cache_enabled)

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
