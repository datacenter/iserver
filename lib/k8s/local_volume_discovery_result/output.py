class K8sLocalVolumeDiscoveryResultOutput():
    def __init__(self):
        pass

    def print_local_volume_discovery_results(self, info, title=False, available=True, unavailable=True):
        if available:
            if title:
                self.my_output.default(
                    'Local Volume Discovery Result - Available Devices',
                    underline=True,
                    before_newline=True
                )

            if len(info) == 0:
                self.my_output.default('None')
                return

            order = [
                'node',
                'deviceSummary',
                'available_devices.path',
                'available_devices.wwn',
                'available_devices.sizeT',
                'available_devices.property',
                'available_devices.type',
                'available_devices.fstype'
            ]

            headers = [
                'Local Volume Discovery Result',
                'Summary',
                'Path',
                'WWN',
                'Size',
                'Property',
                'Type',
                'FSType'
            ]

            self.my_output.my_table(
                self.my_output.expand_lists(
                    info,
                    order,
                    ['available_devices']
                ),
                order=order,
                headers=headers,
                row_separator=True,
                allow_order_subkeys=True,
                underline=True,
                table=True
            )

        if unavailable:
            if title:
                self.my_output.default(
                    'Local Volume Discovery Result - Unavailable Devices',
                    underline=True,
                    before_newline=True
                )

            if len(info) == 0:
                self.my_output.default('None')
                return

            order = [
                'node',
                'unavailable_devices.path',
                'unavailable_devices.wwn',
                'unavailable_devices.sizeT',
                'unavailable_devices.property',
                'unavailable_devices.type',
                'aunvailable_devices.fstype'
            ]

            headers = [
                'Node',
                'Path',
                'WWN',
                'Size',
                'Property',
                'Type',
                'FSType'
            ]

            self.my_output.my_table(
                self.my_output.expand_lists(
                    info,
                    order,
                    ['unavailable_devices']
                ),
                order=order,
                headers=headers,
                row_separator=True,
                allow_order_subkeys=True,
                underline=True,
                table=True
            )
