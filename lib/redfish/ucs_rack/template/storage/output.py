class RedfishEndpointUcsRackTemplateStorageOutput(
    ):
    def __init__(self):
        pass

    def print_ucsc_storage_controller_properties(self, info, title=False):
        if title:
            self.my_output.default(
                'Storage Controller [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'Id',
            'Pid',
            'Model',
            'Vendor',
            'SerialNumber',
            'FirmwareVersion',
            'State',
            'Health',
            'PciSlot',
            'SupportedRAIDTypes',
            'PhysicalDiskCount',
            'VirtualDriveCount'
        ]

        headers = [
            'Controller',
            'Pid',
            'Model',
            'Vendor',
            'Serial',
            'Firmware',
            'State',
            'Health',
            'PCI Slot',
            'Raid Support',
            'PD',
            'VD'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['SupportedRAIDTypes']
            ),
            order=order,
            headers=headers,
            remove_empty_columns=False,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_ucsc_storage_drive_properties(self, info, title=False):
        if title:
            self.my_output.default(
                'Physical Disk [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'StateTick',
            'StorageControllerId',
            'DiskId',
            'VirtualDriveId',
            'SizeUnit',
            'Type',
            'Protocol',
            'BootableTick',
            'LinkSpeed',
            'Pid',
            'Model',
            'Vendor',
            'Revision',
            'SerialNumber'
        ]

        headers = [
            'State',
            'Controller',
            'Disk Id',
            'VD',
            'Size',
            'Type',
            'Protocol',
            'Bootable',
            'Link Speed',
            'Pid',
            'Model',
            'Vendor',
            'Fw',
            'Serial'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            remove_empty_columns=False,
            underline=True,
            table=True
        )

    def print_ucsc_storage_volume_properties(self, info, title=False):
        if title:
            self.my_output.default(
                'Virtual Drive [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'StateTick',
            'StorageControllerId',
            'VirtualDriveId',
            'SizeUnit',
            'PhysicalDiskCount',
            'Type',
            'Name',
            'BootableTick',
            'ActualWriteCachePolicy',
            'DriveState'
        ]

        headers = [
            'State',
            'Controller',
            'Drive Id',
            'Size',
            'Disks',
            'Type',
            'Name',
            'Bootable',
            'Write Cache',
            'Drive State'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            remove_empty_columns=False,
            underline=True,
            table=True
        )

    def print_ucsc_storage_properties(self, properties):
        self.print_ucsc_storage_controller_properties(
            properties['Controller'],
            title=True
        )

        self.print_ucsc_storage_drive_properties(
            properties['Drive'],
            title=True
        )

        self.print_ucsc_storage_volume_properties(
            properties['Volume'],
            title=True
        )
