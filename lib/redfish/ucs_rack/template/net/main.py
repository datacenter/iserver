class RedfishEndpointUcsRackTemplateNet():
    def __init__(self):
        self.defult_net_uri = '/redfish/v1/Systems/SYSTEM_ID/EthernetInterfaces'
        self.net = None

    def get_net_uri(self):
        return self.path_fixup(self.defult_net_uri)

    def get_nets_uri(self):
        uri = self.get_net_uri()
        data = []
        odata_ids = self.endpoint_handler.get_odata_ids(uri)
        if odata_ids is not None:
            for odata_id in odata_ids:
                if odata_id != uri:
                    data.append(
                        odata_id
                    )

        return data

    def get_net_info(self, uri):
        info = {}
        info['__Output'] = {}

        data = self.get_properties(uri)

        info['Uri'] = uri

        keys = [
            'Id',
            'MACAddress',
            'Name',
            'PermanentMACAddress'
        ]
        for key in keys:
            info[key] = self.get_property_value(
                data,
                key
            )

        return info

    def get_nets_info(self, cache_enabled=True):
        if cache_enabled and self.net is not None:
            return self.net

        self.net = []
        nets_uri = self.get_nets_uri()
        for net_uri in nets_uri:
            net_info = self.get_net_info(
                net_uri
            )
            if net_info is not None:
                self.net.append(
                    net_info
                )

        self.net = sorted(
            self.net,
            key=lambda i: i['Id']
        )

        return self.net

    def get_template_net_properties(self, cache_enabled=True):
        all_properties = self.get_nets_info(cache_enabled=cache_enabled)
        if all_properties is None:
            return None

        redfish_properties = []
        for redfish_property in all_properties:
            redfish_properties.append(
                redfish_property
            )

        return redfish_properties
