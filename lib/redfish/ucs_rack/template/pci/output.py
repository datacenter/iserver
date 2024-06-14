class RedfishEndpointUcsRackTemplatePciOutput(
    ):
    def __init__(self):
        pass

    def print_ucsc_pci_properties(self, info, title=False):
        if title:
            self.my_output.default(
                'PCI [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'Id',
            'Name',
            'FirmwareVersion',
            'function.DeviceId',
            'function.VendorId',
            'function.SubsystemId',
            'function.SubsystemVendorId',
            'function.NetworkDeviceFunctions',
            'function.EthernetInterfaces',
            'function.StorageControllers',
            'function.Drives'
        ]

        headers = [
            'Id',
            'Name',
            'Fw',
            'DevId',
            'Vendor',
            'SubId',
            'SubVendor',
            'Net',
            'Eth',
            'Storage',
            'Drives'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['function']
            ),
            order=order,
            headers=headers,
            remove_empty_columns=False,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )
