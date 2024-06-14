class RedfishEndpointUcsRackTemplateMem():
    def __init__(self):
        self.defult_mem_uri = '/redfish/v1/Systems/SYSTEM_ID/Memory'
        self.mem = None

    def get_mem_uri(self):
        return self.path_fixup(self.defult_mem_uri)

    def get_mems_uri(self):
        uri = self.get_mem_uri()
        data = []
        odata_ids = self.endpoint_handler.get_odata_ids(uri)
        if odata_ids is not None:
            for odata_id in odata_ids:
                if odata_id != uri:
                    data.append(
                        odata_id
                    )

        return data

    def get_mem_info(self, uri):
        info = {}
        info['__Output'] = {}

        data = self.get_properties(uri)

        info['Uri'] = uri

        keys = [
            'Id',
            'CapacityMiB',
            'Description',
            'DeviceLocator',
            'Manufacturer',
            'MemoryDeviceType',
            'MemoryType',
            'Name',
            'OperatingSpeedMhz',
            'OperatingMemoryModes',
            'SecurityCapabilities',
            'PartNumber',
            'SerialNumber'
        ]
        for key in keys:
            info[key] = self.get_property_value(
                data,
                key
            )

        try:
            info['_index'] = int(info['Id'])
        except BaseException:
            info['_index'] = -1

        info['Health'] = self.get_property_value(
            data,
            'Status:Health'
        )
        info['__Output']['Health'] = 'Red'
        if info['Health'] == 'OK':
            info['__Output']['Health'] = 'Green'

        info['State'] = self.get_property_value(
            data,
            'Status:State'
        )
        info['__Output']['State'] = 'Red'
        if info['State'] == 'Enabled':
            info['__Output']['State'] = 'Green'

        info['Channel'] = self.get_property_value(
            data,
            'MemoryLocation:Channel'
        )

        info['Slot'] = self.get_property_value(
            data,
            'MemoryLocation:Slot'
        )

        info['Socket'] = self.get_property_value(
            data,
            'MemoryLocation:Socket'
        )

        return info

    def get_mems_info(self, cache_enabled=True):
        if cache_enabled and self.mem is not None:
            return self.mem

        self.mem = []
        mems_uri = self.get_mems_uri()
        for mem_uri in mems_uri:
            mem_info = self.get_mem_info(
                mem_uri
            )
            if mem_info is not None:
                self.mem.append(
                    mem_info
                )

        self.mem = sorted(
            self.mem,
            key=lambda i: i['_index']
        )

        return self.mem

    def get_template_mem_properties(self, cache_enabled=True):
        all_properties = self.get_mems_info(cache_enabled=cache_enabled)
        if all_properties is None:
            return None

        redfish_properties = []
        for redfish_property in all_properties:
            redfish_properties.append(
                redfish_property
            )

        return redfish_properties
