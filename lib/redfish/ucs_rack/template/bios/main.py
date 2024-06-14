class RedfishEndpointUcsRackTemplateBios():
    def __init__(self):
        self.default_bios_uri = '/redfish/v1/Systems/SYSTEM_ID/Bios'
        self.bios = None

    def get_bios_uri(self):
        return self.path_fixup(self.default_bios_uri)

    def get_bios_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.bios is not None:
                return self.bios

        bios_mo = self.get_properties(
            self.get_bios_uri()
        )
        if bios_mo is None:
            return None

        self.bios = self.get_property_value(
            bios_mo,
            'Attributes'
        )

        return self.bios

    def get_bios_info(self, bios_mo):
        info = {}
        for key in bios_mo:
            info[key] = bios_mo[key]
        return info

    def get_template_bios_properties(self, cache_enabled=True):
        bios_mo = self.get_bios_mo(cache_enabled=cache_enabled)
        if bios_mo is None:
            return None

        bios_info = self.get_bios_info(
            bios_mo
        )

        return bios_info
