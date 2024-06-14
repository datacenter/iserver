from lib.redfish.ucs_rack.template.output import RedfishEndpointUcsRackTemplateOutput


class RedfishEndpointUcsRackOutput(
        RedfishEndpointUcsRackTemplateOutput
        ):
    def __init__(self):
        RedfishEndpointUcsRackTemplateOutput.__init__(self)

    def print_ucsc_properties(self, template_name, properties, title=False):
        if template_name == 'account':
            self.print_ucsc_account_properties(properties, title=title)

        if template_name == 'bios':
            self.print_ucsc_bios_properties(properties, title=title)

        if template_name == 'bios-diff':
            self.print_ucsc_bios_diff_properties(properties, title=title)

        if template_name == 'cpu':
            self.print_ucsc_cpu_properties(properties, title=title)

        if template_name == 'fan':
            self.print_ucsc_fan_properties(properties, title=title)

        if template_name == 'gpu':
            self.print_ucsc_gpu_properties(properties, title=title)

        if template_name == 'identity':
            self.print_ucsc_identity_properties(properties)

        if template_name == 'mem':
            self.print_ucsc_mem_properties(properties, title=title)

        if template_name == 'net':
            self.print_ucsc_net_properties(properties, title=title)

        if template_name == 'pci':
            self.print_ucsc_pci_properties(properties, title=title)

        if template_name == 'power':
            self.print_ucsc_power_properties(properties)

        if template_name == 'psu':
            self.print_ucsc_psu_properties(properties, title=title)

        if template_name == 'role':
            self.print_ucsc_role_properties(properties, title=title)

        if template_name == 'storage':
            self.print_ucsc_storage_properties(properties)

        if template_name == 'thermal':
            self.print_ucsc_thermal_properties(properties)
