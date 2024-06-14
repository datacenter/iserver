class RedfishEndpointUcsRackTemplatePci():
    def __init__(self):
        self.pci_uri = '/redfish/v1/Chassis/1/PCIeDevices'
        self.pci = None

    def get_pcis_uri(self):
        uri = self.pci_uri
        data = []
        odata_ids = self.endpoint_handler.get_odata_ids(uri)
        if odata_ids is not None:
            for odata_id in odata_ids:
                if odata_id != uri:
                    data.append(
                        odata_id
                    )

        return data

    def get_pci_info(self, uri):
        info = {}
        info['__Output'] = {}

        data = self.get_properties(uri)

        furi = self.get_property_value(
            data,
            'PCIeFunctions:@odata.id'
        )
        functions = []
        if furi is not None:
            fdata = self.get_properties(furi)
            if fdata is not None:
                members = self.get_property_value(
                    fdata,
                    'Members'
                )
                if members is not None:
                    for member in members:
                        function_data = self.get_properties(
                            member['@odata.id']
                        )
                        if function_data is not None:
                            functions.append(
                                function_data
                            )

        info['Uri'] = uri
        info['UriFunctions'] = furi

        keys = [
            'Id',
            'FirmwareVersion',
            'Name'
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

        info['function'] = []
        for function_mo in functions:
            function_info = {}
            keys = [
                'Id',
                'DeviceId',
                'Name',
                'SubsystemId',
                'SubsystemVendorId',
                'VendorId'
            ]
            for key in keys:
                function_info[key] = self.get_property_value(
                    function_mo,
                    key
                )

            keys = [
                'Drives',
                'EthernetInterfaces',
                'NetworkDeviceFunctions',
                'StorageControllers'
            ]
            for key in keys:
                function_info[key] = self.get_property_value(
                    function_mo,
                    'Links:%s@odata.count' % (key)
                )

            info['function'].append(
                function_info
            )

        return info

    def get_pcis_info(self, cache_enabled=True):
        if cache_enabled and self.pci is not None:
            return self.pci

        self.pci = []
        pcis_uri = self.get_pcis_uri()
        for pci_uri in pcis_uri:
            pci_info = self.get_pci_info(
                pci_uri
            )
            if pci_info is not None:
                self.pci.append(
                    pci_info
                )

        self.pci = sorted(
            self.pci,
            key=lambda i: i['_index']
        )

        return self.pci

    def get_template_pci_properties(self, cache_enabled=True):
        all_properties = self.get_pcis_info(cache_enabled=cache_enabled)
        if all_properties is None:
            return None

        redfish_properties = []
        for redfish_property in all_properties:
            redfish_properties.append(
                redfish_property
            )

        return redfish_properties
