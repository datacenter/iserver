class RedfishEndpointUcsRackTemplateFan():
    def __init__(self):
        self.fan_uri = '/redfish/v1/Chassis/1/Thermal'
        self.fan = None

    def get_fans_uri(self):
        uri = self.fan_uri
        data = []
        odata_ids = self.endpoint_handler.get_odata_ids(uri)
        if odata_ids is not None:
            for odata_id in odata_ids:
                if odata_id != uri:
                    data.append(
                        odata_id
                    )

        return data

    def get_fan_info(self, fan_mo):
        info = {}
        info['__Output'] = {}

        keys = [
            'MemberId',
            'Name',
            'ReadingUnits',
            'Reading'
        ]
        for key in keys:
            info[key] = self.get_property_value(
                fan_mo,
                key
            )

        try:
            info['_index'] = int(info['MemberId'])
        except BaseException:
            info['_index'] = -1

        info['Health'] = self.get_property_value(
            fan_mo,
            'Status:Health'
        )
        info['__Output']['Health'] = 'Red'
        if info['Health'] == 'OK':
            info['__Output']['Health'] = 'Green'

        info['State'] = self.get_property_value(
            fan_mo,
            'Status:State'
        )
        info['__Output']['State'] = 'Red'
        if info['State'] == 'Enabled':
            info['__Output']['State'] = 'Green'

        return info

    def get_fans_info(self, cache_enabled=True):
        if cache_enabled and self.fan is not None:
            return self.fan

        self.fan = []
        fans_mo = self.get_properties(self.fan_uri)
        if fans_mo is not None and 'Fans' in fans_mo:
            for fan_mo in fans_mo['Fans']:
                fan_info = self.get_fan_info(
                    fan_mo
                )
                self.fan.append(
                    fan_info
                )

        self.fan = sorted(
            self.fan,
            key=lambda i: i['_index']
        )

        return self.fan

    def get_template_fan_properties(self, cache_enabled=True):
        all_properties = self.get_fans_info(cache_enabled=cache_enabled)
        if all_properties is None:
            return None

        redfish_properties = []
        for redfish_property in all_properties:
            redfish_properties.append(
                redfish_property
            )

        return redfish_properties
