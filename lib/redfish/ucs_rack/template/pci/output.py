class RedfishEndpointUcsRackTemplatePciOutput(
    ):
    def __init__(self):
        pass

    def print_ucsc_pci_properties(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['PCI Id', 'Id'],
                ['Name', 'Name'],
                ['Fw', 'FirmwareVersion'],
                ['DevId', 'function.DeviceId'],
                ['Vendor', 'function.VendorId'],
                ['SubId', 'function.SubsystemId'],
                ['SubVendor', 'function.SubsystemVendorId'],
                ['Net', 'function.NetworkDeviceFunctions'],
                ['Eth', 'function.EthernetInterfaces'],
                ['Storage', 'function.StorageControllers'],
                ['Drives', 'function.Drives']
            ]
        )
