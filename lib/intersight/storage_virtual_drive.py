from lib.intersight import storage_physical_disk_usage
from lib.intersight.intersight_common import IntersightCommon


class StorageVirtualDrive(IntersightCommon):
    """Class for intersight storage virtual drive objects
    {
        "AccessPolicy": "read-write",
        "AccountMoid": "5be4b2ce67626c6d661ca38d",
        "ActualWriteCachePolicy": "write-through",
        "Ancestors": [
            {
            "ClassId": "mo.MoRef",
            "Moid": "6311b01a76752d31398ef2c4",
            "ObjectType": "storage.Controller",
            "link": "https://www.intersight.com/api/v1/storage/Controllers/6311b01a76752d31398ef2c4"
            },
            {
            "ClassId": "mo.MoRef",
            "Moid": "6311ac4676752d31398e5331",
            "ObjectType": "compute.Board",
            "link": "https://www.intersight.com/api/v1/compute/Boards/6311ac4676752d31398e5331"
            },
            {
            "ClassId": "mo.MoRef",
            "Moid": "6311aae876752d31398e1a50",
            "ObjectType": "compute.RackUnit",
            "link": "https://www.intersight.com/api/v1/compute/RackUnits/6311aae876752d31398e1a50"
            }
        ],
        "AvailableSize": "0",
        "BlockSize": "512",
        "Bootable": "true",
        "ClassId": "storage.VirtualDrive",
        "ConfigState": "orphaned",
        "ConfiguredWriteCachePolicy": "write-through",
        "ConnectionProtocol": "unspecified",
        "CreateTime": "2022-09-02T07:26:18.446Z",
        "DeviceMoId": "61c35fa36f72612d3005590c",
        "DiskGroup": null,
        "DisplayNames": {
            "hierarchical": [
            "virtualDrive-RAID10_3456"
            ],
            "short": [
            "VirtualDrive-RAID10_3456"
            ]
        },
        "Dn": "sys/rack-unit-3/board/storage-SAS-1/vd-0",
        "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
        "DriveCache": "no-change",
        "DriveSecurity": "no",
        "DriveState": "optimal",
        "InventoryDeviceInfo": null,
        "IoPolicy": "direct",
        "ModTime": "2022-09-02T07:41:09.149Z",
        "Model": "",
        "Moid": "6311b01a76752d31398ef2f6",
        "Name": "RAID10_3456",
        "NumBlocks": "388624384",
        "ObjectType": "storage.VirtualDrive",
        "OperState": "undefined",
        "Operability": "operable",
        "Owners": [
            "5be4b2ce67626c6d661ca38d",
            "61c35fa36f72612d3005590c"
        ],
        "Parent": {
            "ClassId": "mo.MoRef",
            "Moid": "6311b01a76752d31398ef2c4",
            "ObjectType": "storage.Controller",
            "link": "https://www.intersight.com/api/v1/storage/Controllers/6311b01a76752d31398ef2c4"
        },
        "PermissionResources": [
            {
            "ClassId": "mo.MoRef",
            "Moid": "5dee1d736972652d321d26b5",
            "ObjectType": "organization.Organization",
            "link": "https://www.intersight.com/api/v1/organization/Organizations/5dee1d736972652d321d26b5"
            },
            {
            "ClassId": "mo.MoRef",
            "Moid": "625706a06972652d3202a8f9",
            "ObjectType": "organization.Organization",
            "link": "https://www.intersight.com/api/v1/organization/Organizations/625706a06972652d3202a8f9"
            },
            {
            "ClassId": "mo.MoRef",
            "Moid": "6242d1016972652d32eda017",
            "ObjectType": "organization.Organization",
            "link": "https://www.intersight.com/api/v1/organization/Organizations/6242d1016972652d32eda017"
            }
        ],
        "PhysicalBlockSize": "unknown",
        "PhysicalDiskUsages": [],
        "Presence": "equipped",
        "PreviousFru": null,
        "ReadPolicy": "normal",
        "RegisteredDevice": {
            "ClassId": "mo.MoRef",
            "Moid": "61c35fa36f72612d3005590c",
            "ObjectType": "asset.DeviceRegistration",
            "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/61c35fa36f72612d3005590c"
        },
        "Revision": "0",
        "Rn": "",
        "SecurityFlags": "",
        "Serial": "",
        "SharedScope": "",
        "Size": "2286910",
        "StorageController": {
            "ClassId": "mo.MoRef",
            "Moid": "6311b01a76752d31398ef2c4",
            "ObjectType": "storage.Controller",
            "link": "https://www.intersight.com/api/v1/storage/Controllers/6311b01a76752d31398ef2c4"
        },
        "StorageVirtualDriveContainer": null,
        "StripSize": "64",
        "Tags": [],
        "Type": "mirror-stripe",
        "Uuid": "41b43588-6ba3-4849-8dca-2a0420468108",
        "VdMemberEps": [
            {
            "ClassId": "mo.MoRef",
            "Moid": "6311b01a76752d31398ef305",
            "ObjectType": "storage.VdMemberEp",
            "link": "https://www.intersight.com/api/v1/storage/VdMemberEps/6311b01a76752d31398ef305"
            },
            {
            "ClassId": "mo.MoRef",
            "Moid": "6311b01a76752d31398ef309",
            "ObjectType": "storage.VdMemberEp",
            "link": "https://www.intersight.com/api/v1/storage/VdMemberEps/6311b01a76752d31398ef309"
            },
            {
            "ClassId": "mo.MoRef",
            "Moid": "6311b01a76752d31398ef30b",
            "ObjectType": "storage.VdMemberEp",
            "link": "https://www.intersight.com/api/v1/storage/VdMemberEps/6311b01a76752d31398ef30b"
            },
            {
            "ClassId": "mo.MoRef",
            "Moid": "6311b01a76752d31398ef30d",
            "ObjectType": "storage.VdMemberEp",
            "link": "https://www.intersight.com/api/v1/storage/VdMemberEps/6311b01a76752d31398ef30d"
            }
        ],
        "Vendor": "",
        "VendorUuid": "678da6e7-15d5-7460-23fe-a8c7196781e6",
        "VirtualDriveExtension": null,
        "VirtualDriveId": "0"
    }
    """
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'storage virtualdrive'
        self.cache_key = 'virtual_drive'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id, cache_key=self.cache_key)

    def get_virtual_drives(self, compute_id, cache=True):
        if cache:
            self.prepare_cache()
        else:
            self.cache = self.get_all()

        if self.cache is None:
            return None

        disks = []

        for item in self.cache:
            match = False
            for ancestor in item['Ancestors']:
                if ancestor['ObjectType'] == 'compute.Board' and ancestor['Moid'] == compute_id:
                    match = True
                    break

                if ancestor['ObjectType'] == 'compute.Blade' and ancestor['Moid'] == compute_id:
                    match = True
                    break

            if match:
                disks.append(item)

        return disks

    def get_virtual_drives_count(self, compute_id):
        disks = self.get_virtual_drives(compute_id)
        if disks is None:
            return 0
        return len(disks)

    def get_virtual_drives_size(self, compute_id):
        disks = self.get_virtual_drives(compute_id)
        if disks is None:
            return 0

        size = 0
        for disk in disks:
            if disk['Size'].endswith(' MB'):
                size = size + int(disk['Size'].split(' ')[0])
                continue

            size = size + int(disk['Size'])

        size = size * 1024 * 1024
        return size

    def get_disk_size_bytes(self, size):
        if isinstance(size, int):
            return size

        factor = 1
        size_bytes = 0

        if size.endswith('MB'):
            factor = 1024 * 1024
            size_bytes = int(size.split('MB')[0].strip())

        if size.endswith('GB'):
            factor = 1024 * 1024 * 1024
            size_bytes = int(size.split('GB')[0].strip())

        if size.endswith('TB'):
            factor = 1024 * 1024 * 1024 * 1024
            size_bytes = int(size.split('TB')[0].strip())

        if factor == 1:
            factor = 1024 * 1024
            size_bytes = int(size.strip())

        return size_bytes * factor

    def is_virtual_drive_ok(self, info):
        if info['Operability'] == 'operable' and info['Presence'] == 'equipped' and info['DriveState'].lower() == 'optimal':
            return True

        if info['Operability'] == '' and info['Presence'] == '' and info['DriveState'].lower() == 'optimal':
            return True

        return False

    def get_virtual_drives_info(self, compute_id, storage_controllers_info=None):
        virtual_drives = self.get_virtual_drives(compute_id)
        if virtual_drives is None:
            return None

        virtual_drives_info = []

        keys = [
            'Moid',
            'Name',
            'Dn',
            'Size',
            'Type',
            'VirtualDriveId',
            'Bootable',
            'DriveState',
            'Operability',
            'Presence',
            'ActualWriteCachePolicy',
            'ConfiguredWriteCachePolicy',
            'IoPolicy'
        ]

        for virtual_drive in virtual_drives:
            info = {}
            info['__Output'] = {}

            for key in keys:
                info[key] = virtual_drive[key]

            try:
                info['_VirtualDriveId'] = int(info['VirtualDriveId'])
            except BaseException:
                info['_VirtualDriveId'] = 0

            info['SizeBytes'] = self.get_disk_size_bytes(
                info['Size']
            )

            info['SizeUnit'] = self.info_helper.convert_storage(
                info['SizeBytes']
            )

            info['PhysicalDiskCount'] = max(
                len(virtual_drive['PhysicalDiskUsages']),
                len(virtual_drive['VdMemberEps'])
            )

            info['StorageControllerId'] = None
            info['StorageControllerName'] = None
            if storage_controllers_info is not None:
                for storage_controller_info in storage_controllers_info:
                    if info['Moid'] in storage_controller_info['VirtualDriveIds']:
                        info['StorageControllerId'] = storage_controller_info['ControllerId']
                        info['StorageControllerName'] = storage_controller_info['Name']

            if info['Presence'] == 'equipped':
                info['__Output']['Presence'] = 'Green'
            else:
                info['__Output']['Presence'] = 'Red'

            if info['Operability'] == 'operable':
                info['__Output']['Operability'] = 'Green'
            else:
                info['__Output']['Operability'] = 'Red'

            if info['DriveState'].lower() == 'optimal':
                info['__Output']['DriveState'] = 'Green'
            else:
                info['__Output']['DriveState'] = 'Red'

            if info['Bootable'] == 'true':
                info['BootableTick'] = '\u2713'
                info['__Output']['BootableTick'] = 'Green'
            else:
                info['BootableTick'] = '\u2717'
                info['__Output']['BootableTick'] = 'Red'

            if self.is_virtual_drive_ok(info):
                info['StateTick'] = '\u2713'
                info['__Output']['StateTick'] = 'Green'
            else:
                info['StateTick'] = '\u2717'
                info['__Output']['StateTick'] = 'Red'

            virtual_drives_info.append(info)

        virtual_drives_info = sorted(virtual_drives_info, key=lambda i: i['_VirtualDriveId'])

        for info in virtual_drives_info:
            info['PhysicalDiskIds'] = []
            if info['PhysicalDiskCount'] > 0:
                storage_physical_disk_usage_handler = storage_physical_disk_usage.StoragePhysicalDiskUsage(self.iaccount)
                storage_physical_disk_usage_handler.set_get_filter("StorageVirtualDrive/Moid eq '%s'" % (info['Moid']))
                disk_usages = storage_physical_disk_usage_handler.get_all()
                if disk_usages is not None:
                    for disk_usage in disk_usages:
                        info['PhysicalDiskIds'].append(disk_usage['PhysicalDrive'])

        return virtual_drives_info
