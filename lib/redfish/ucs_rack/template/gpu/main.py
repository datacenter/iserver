class RedfishEndpointUcsRackTemplateGpu():
    def __init__(self):
        self.defult_gpu_uri = '/redfish/v1/Systems/SYSTEM_ID/Processors'
        self.gpu = None

    def get_gpu_uri(self):
        return self.path_fixup(self.defult_gpu_uri)

    def get_gpus_uri(self):
        uri = self.get_gpu_uri()
        data = []
        odata_ids = self.endpoint_handler.get_odata_ids(uri)
        if odata_ids is not None:
            for odata_id in odata_ids:
                if odata_id != uri:
                    data.append(
                        odata_id
                    )

        return data

    def get_gpu_info(self, uri):
        info = {}
        info['__Output'] = {}

        data = self.get_properties(uri)

        info['Uri'] = uri

        keys = [
            'Id',
            'ProcessorType',
            'Description',
            'Name',
            'Model',
            'SerialNumber',
            'FirmwareVersion'
        ]
        for key in keys:
            info[key] = self.get_property_value(
                data,
                key
            )

        if info['ProcessorType'] not in ['GPU']:
            return None

        return info

    def get_gpus_info(self, cache_enabled=True):
        if cache_enabled and self.gpu is not None:
            return self.gpu

        self.gpu = []
        gpus_uri = self.get_gpus_uri()
        for gpu_uri in gpus_uri:
            gpu_info = self.get_gpu_info(
                gpu_uri
            )
            if gpu_info is not None:
                self.gpu.append(
                    gpu_info
                )

        self.gpu = sorted(
            self.gpu,
            key=lambda i: i['Id']
        )

        return self.gpu

    def get_template_gpu_properties(self, cache_enabled=True):
        all_properties = self.get_gpus_info(cache_enabled=cache_enabled)
        if all_properties is None:
            return None

        redfish_properties = []
        for redfish_property in all_properties:
            redfish_properties.append(
                redfish_property
            )

        return redfish_properties
