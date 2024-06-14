class RedfishEndpointUcsRackTemplateCpu():
    def __init__(self):
        self.defult_cpu_uri = '/redfish/v1/Systems/SYSTEM_ID/Processors'
        self.cpu = None

    def get_cpu_uri(self):
        return self.path_fixup(self.defult_cpu_uri)

    def get_processors_uri(self):
        uri = self.get_cpu_uri()
        data = []
        odata_ids = self.endpoint_handler.get_odata_ids(uri)
        if odata_ids is not None:
            for odata_id in odata_ids:
                if odata_id != uri:
                    data.append(
                        odata_id
                    )

        return data

    def get_processor_info(self, uri):
        info = {}
        info['__Output'] = {}

        data = self.get_properties(uri)

        info['Uri'] = uri

        keys = [
            'Id',
            'InstructionSet',
            'Manufacturer',
            'MaxSpeedMHz',
            'Model',
            'Name',
            'ProcessorArchitecture',
            'ProcessorType',
            'Socket',
            'TotalCores',
            'TotalEnabledCores',
            'TotalThreads'
        ]
        for key in keys:
            info[key] = self.get_property_value(
                data,
                key
            )

        if info['ProcessorType'] not in ['CPU']:
            return None

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

        info['EffectiveFamily'] = self.get_property_value(
            data,
            'ProcessorId:EffectiveFamily'
        )

        info['EffectiveModel'] = self.get_property_value(
            data,
            'ProcessorId:EffectiveModel'
        )

        info['Step'] = self.get_property_value(
            data,
            'ProcessorId:Step'
        )

        info['VendorId'] = self.get_property_value(
            data,
            'ProcessorId:VendorId'
        )

        return info

    def get_processors_info(self, cache_enabled=True):
        if cache_enabled and self.cpu is not None:
            return self.cpu

        self.cpu = []
        processors_uri = self.get_processors_uri()
        for processor_uri in processors_uri:
            processor_info = self.get_processor_info(
                processor_uri
            )
            if processor_info is not None:
                self.cpu.append(
                    processor_info
                )

        self.cpu = sorted(
            self.cpu,
            key=lambda i: i['Id']
        )

        return self.cpu

    def get_template_cpu_properties(self, cache_enabled=True):
        all_properties = self.get_processors_info(cache_enabled=cache_enabled)
        if all_properties is None:
            return None

        redfish_properties = []
        for redfish_property in all_properties:
            redfish_properties.append(
                redfish_property
            )

        return redfish_properties
