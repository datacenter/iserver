class K8sLocalVolumeDiscoveryResultOutput():
    def __init__(self):
        pass

    def print_local_volume_discovery_results(self, info, available=True, unavailable=True):
        if available:
            self.my_output.my_table_ng(
                info,
                [
                    ['LV Discovery Result', 'node'],
                    ['Available', 'deviceSummary'],
                    ['Path', 'available_devices.path'],
                    ['WWN', 'available_devices.wwn'],
                    ['Size', 'available_devices.sizeT'],
                    ['Property', 'available_devices.property'],
                    ['Type', 'available_devices.type'],
                    ['FSType', 'available_devices.fstype']
                ]
            )

        if unavailable:
            self.my_output.my_table_ng(
                info,
                [
                    ['LV Discovery Result', 'node'],
                    ['Unavailable', 'deviceSummary'],
                    ['Path', 'unavailable_devices.path'],
                    ['WWN', 'unavailable_devices.wwn'],
                    ['Size', 'unavailable_devices.sizeT'],
                    ['Property', 'unavailable_devices.property'],
                    ['Type', 'unavailable_devices.type'],
                    ['FSType', 'unavailable_devices.fstype']
                ]
            )
