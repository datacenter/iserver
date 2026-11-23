class RedfishEndpointUcsRackTemplateGpuOutput(
    ):
    def __init__(self):
        pass

    def print_ucsc_gpu_properties(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['GPU Id', 'Id'],
                ['Name', 'Name'],
                ['Model', 'Model'],
                ['Serial', 'SerialNumber'],
                ['Firmware', 'FirmwareVersion']
            ]
        )
