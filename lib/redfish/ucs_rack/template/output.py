from lib.redfish.ucs_rack.template.account.output import RedfishEndpointUcsRackTemplateAccountOutput
from lib.redfish.ucs_rack.template.bios.output import RedfishEndpointUcsRackTemplateBiosOutput
from lib.redfish.ucs_rack.template.cpu.output import RedfishEndpointUcsRackTemplateCpuOutput
from lib.redfish.ucs_rack.template.fan.output import RedfishEndpointUcsRackTemplateFanOutput
from lib.redfish.ucs_rack.template.gpu.output import RedfishEndpointUcsRackTemplateGpuOutput
from lib.redfish.ucs_rack.template.identity.output import RedfishEndpointUcsRackTemplateIdentityOutput
from lib.redfish.ucs_rack.template.mem.output import RedfishEndpointUcsRackTemplateMemOutput
from lib.redfish.ucs_rack.template.net.output import RedfishEndpointUcsRackTemplateNetOutput
from lib.redfish.ucs_rack.template.pci.output import RedfishEndpointUcsRackTemplatePciOutput
from lib.redfish.ucs_rack.template.power.output import RedfishEndpointUcsRackTemplatePowerOutput
from lib.redfish.ucs_rack.template.psu.output import RedfishEndpointUcsRackTemplatePsuOutput
from lib.redfish.ucs_rack.template.role.output import RedfishEndpointUcsRackTemplateRoleOutput
from lib.redfish.ucs_rack.template.storage.output import RedfishEndpointUcsRackTemplateStorageOutput
from lib.redfish.ucs_rack.template.thermal.output import RedfishEndpointUcsRackTemplateThermalOutput


class RedfishEndpointUcsRackTemplateOutput(
        RedfishEndpointUcsRackTemplateAccountOutput,
        RedfishEndpointUcsRackTemplateBiosOutput,
        RedfishEndpointUcsRackTemplateCpuOutput,
        RedfishEndpointUcsRackTemplateFanOutput,
        RedfishEndpointUcsRackTemplateGpuOutput,
        RedfishEndpointUcsRackTemplateIdentityOutput,
        RedfishEndpointUcsRackTemplateMemOutput,
        RedfishEndpointUcsRackTemplateNetOutput,
        RedfishEndpointUcsRackTemplatePciOutput,
        RedfishEndpointUcsRackTemplatePowerOutput,
        RedfishEndpointUcsRackTemplatePsuOutput,
        RedfishEndpointUcsRackTemplateRoleOutput,
        RedfishEndpointUcsRackTemplateStorageOutput,
        RedfishEndpointUcsRackTemplateThermalOutput
        ):
    def __init__(self):
        RedfishEndpointUcsRackTemplateAccountOutput.__init__(self)
        RedfishEndpointUcsRackTemplateBiosOutput.__init__(self)
        RedfishEndpointUcsRackTemplateCpuOutput.__init__(self)
        RedfishEndpointUcsRackTemplateFanOutput.__init__(self)
        RedfishEndpointUcsRackTemplateGpuOutput.__init__(self)
        RedfishEndpointUcsRackTemplateIdentityOutput.__init__(self)
        RedfishEndpointUcsRackTemplateMemOutput.__init__(self)
        RedfishEndpointUcsRackTemplateNetOutput.__init__(self)
        RedfishEndpointUcsRackTemplatePciOutput.__init__(self)
        RedfishEndpointUcsRackTemplatePowerOutput.__init__(self)
        RedfishEndpointUcsRackTemplatePsuOutput.__init__(self)
        RedfishEndpointUcsRackTemplateRoleOutput.__init__(self)
        RedfishEndpointUcsRackTemplateStorageOutput.__init__(self)
        RedfishEndpointUcsRackTemplateThermalOutput.__init__(self)
