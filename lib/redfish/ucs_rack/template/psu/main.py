class RedfishEndpointUcsRackTemplatePsu():
    def __init__(self):
        self.psu_uri = '/redfish/v1/Chassis/1/Power'
        self.psu = None

    def get_psus_uri(self):
        uri = self.psu_uri
        data = []
        odata_ids = self.endpoint_handler.get_odata_ids(uri)
        if odata_ids is not None:
            for odata_id in odata_ids:
                if odata_id != uri:
                    data.append(
                        odata_id
                    )

        return data

    def get_psu_info(self, psu_mo):
        info = {}
        info['__Output'] = {}

        keys = [
            'MemberId',
            'FirmwareVersion',
            'Manufacturer',
            'Model',
            'Name',
            'PartNumber',
            'SerialNumber',
            'SparePartNumber'
        ]
        for key in keys:
            info[key] = self.get_property_value(
                psu_mo,
                key
            )

        try:
            info['_index'] = int(info['MemberId'])
        except BaseException:
            info['_index'] = -1

        info['State'] = self.get_property_value(
            psu_mo,
            'Status:State'
        )
        info['__Output']['State'] = 'Red'
        if info['State'] == 'Enabled':
            info['__Output']['State'] = 'Green'

        return info

    def get_psus_info(self, cache_enabled=True):
        if cache_enabled and self.psu is not None:
            return self.psu

        self.psu = []
        psus_mo = self.get_properties(self.psu_uri)
        if psus_mo is not None and 'PowerSupplies' in psus_mo:
            for psu_mo in psus_mo['PowerSupplies']:
                psu_info = self.get_psu_info(
                    psu_mo
                )
                self.psu.append(
                    psu_info
                )

        self.psu = sorted(
            self.psu,
            key=lambda i: i['_index']
        )

        return self.psu

    def get_template_psu_properties(self, cache_enabled=True):
        all_properties = self.get_psus_info(cache_enabled=cache_enabled)
        if all_properties is None:
            return None

        redfish_properties = []
        for redfish_property in all_properties:
            redfish_properties.append(
                redfish_property
            )

        return redfish_properties
