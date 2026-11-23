class RedfishEndpointUcsRackTemplateStorageOutput(
    ):
    def __init__(self):
        pass

    def print_ucsc_storage_properties(self, info):
        self.my_output.my_table_ng(
            info['Controller'],
            [
                ['Controller', 'Id'],
                ['Pid', 'Pid'],
                ['Model', 'Model'],
                ['Vendor', 'Vendor'],
                ['Serial', 'SerialNumber'],
                ['Firmware', 'FirmwareVersion'],
                ['State', 'State'],
                ['Health', 'Health'],
                ['PCI Slot', 'PciSlot'],
                ['Raid Support', 'SupportedRAIDTypes'],
                ['PD', 'PhysicalDiskCount'],
                ['VD', 'VirtualDriveCount']
            ]
        )

        self.my_output.my_table_ng(
            info['Drive'],
            [
                ['PhyDisk Id', 'DiskId'],
                ['State', 'StateTick'],
                ['Controller', 'StorageControllerId'],
                ['VD', 'VirtualDriveId'],
                ['Size', 'SizeUnit'],
                ['Type', 'Type'],
                ['Protocol', 'Protocol'],
                ['Bootable', 'BootableTick'],
                ['Link Speed', 'LinkSpeed'],
                ['Pid', 'Pid'],
                ['Model', 'Model'],
                ['Vendor', 'Vendor'],
                ['Fw', 'Revision'],
                ['Serial', 'SerialNumber']
            ]
        )

        self.my_output.my_table_ng(
            info['Volume'],
            [
                ['Virtual Drive Id', 'VirtualDriveId'],
                ['State', 'StateTick'],
                ['Controller', 'StorageControllerId'],
                ['Size', 'SizeUnit'],
                ['Disks', 'PhysicalDiskCount'],
                ['Type', 'Type'],
                ['Name', 'Name'],
                ['Bootable', 'BootableTick'],
                ['Write Cache', 'ActualWriteCachePolicy'],
                ['Raid SupportDrive State', 'DriveState']
            ]
        )

