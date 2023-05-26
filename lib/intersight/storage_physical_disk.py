from lib.intersight.intersight_common import IntersightCommon


class StoragePhysicalDisk(IntersightCommon):
    """Class for intersight storage physical disk objects
    {
        "AccountMoid": "5be4b2ce67626c6d661ca38d",
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
        "BackgroundOperations": "",
        "BlockSize": "512",
        "Bootable": "false",
        "ClassId": "storage.PhysicalDisk",
        "ConfigurationCheckpoint": "",
        "ConfigurationState": "not-applied",
        "CreateTime": "2022-09-02T07:26:18.436Z",
        "DeviceMoId": "61c35fa36f72612d3005590c",
        "DisabledForRemoval": false,
        "DiscoveredPath": "default",
        "DiskId": "3",
        "DiskState": "online",
        "DisplayNames": {
            "hierarchical": [
            "physicalDisk-3"
            ],
            "short": [
            "PhysicalDisk-3"
            ]
        },
        "Dn": "sys/rack-unit-3/board/storage-SAS-1/disk-3",
        "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
        "DriveFirmware": "",
        "DriveState": "",
        "EncryptionStatus": "",
        "FailurePredicted": false,
        "FdeCapable": "",
        "HotSpareType": "",
        "IndicatorLed": "",
        "InventoryDeviceInfo": null,
        "LinkSpeed": "12-gbps",
        "LinkState": "unknown",
        "LocatorLed": {
            "ClassId": "mo.MoRef",
            "Moid": "6311b01a76752d31398ef2fd",
            "ObjectType": "equipment.LocatorLed",
            "link": "https://www.intersight.com/api/v1/equipment/LocatorLeds/6311b01a76752d31398ef2fd"
        },
        "MaximumOperatingTemperature": 0,
        "MediaErrorCount": 0,
        "ModTime": "2022-09-02T07:41:09.148Z",
        "Model": "ST1200MM0088",
        "Moid": "6311b01a76752d31398ef2d6",
        "Name": "",
        "NonCoercedSizeBytes": 0,
        "NumBlocks": "2341795840",
        "ObjectType": "storage.PhysicalDisk",
        "OperPowerState": "active",
        "OperQualifierReason": "N/A",
        "Operability": "operable",
        "OperatingTemperature": 0,
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
        "PercentLifeLeft": 0,
        "PercentReservedCapacityConsumed": 0,
        "PerformancePercent": 0,
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
        "PhysicalBlockSize": "512",
        "PhysicalDiskExtensions": [],
        "Pid": "",
        "PowerCycleCount": 0,
        "PowerOnHours": 0,
        "PowerOnHoursPercentage": 0,
        "PredictedMediaLifeLeftPercent": 0,
        "PredictiveFailureCount": 0,
        "Presence": "equipped",
        "PreviousFru": null,
        "Protocol": "SAS",
        "RawSize": "1144641",
        "ReadErrorCountThreshold": 0,
        "ReadIoErrorCount": 0,
        "RegisteredDevice": {
            "ClassId": "mo.MoRef",
            "Moid": "61c35fa36f72612d3005590c",
            "ObjectType": "asset.DeviceRegistration",
            "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/61c35fa36f72612d3005590c"
        },
        "Revision": "0",
        "Rn": "",
        "RunningFirmware": [
            {
            "ClassId": "mo.MoRef",
            "Moid": "6311b01a76752d31398ef2d8",
            "ObjectType": "firmware.RunningFirmware",
            "link": "https://www.intersight.com/api/v1/firmware/RunningFirmwares/6311b01a76752d31398ef2d8"
            }
        ],
        "SasPorts": [],
        "Secured": "",
        "Serial": "S40222EH0000K701JJQ3",
        "SharedScope": "",
        "Size": "1143455",
        "StorageController": {
            "ClassId": "mo.MoRef",
            "Moid": "6311b01a76752d31398ef2c4",
            "ObjectType": "storage.Controller",
            "link": "https://www.intersight.com/api/v1/storage/Controllers/6311b01a76752d31398ef2c4"
        },
        "StorageEnclosure": null,
        "Tags": [],
        "Thermal": "unknown",
        "ThresholdOperatingTemperature": 0,
        "Type": "HDD",
        "VariantType": "default",
        "Vendor": "SEAGATE",
        "WearStatusInDays": 0,
        "WriteErrorCountThreshold": 0,
        "WriteIoErrorCount": 0
    }
    """
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'storage physicaldisk'
        self.cache_key = 'physical_disk'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id, cache_key=self.cache_key)

    def get_compute_disks(self, compute_id, cache=True, disk_type=None):
        if cache:
            self.prepare_cache()
        else:
            self.cache = self.get_all()

        if self.cache is None:
            return None

        disks = []

        for item in self.cache:
            if disk_type is not None and item['Type'] != disk_type:
                continue

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

    def get_compute_disks_count(self, compute_id, disk_type=None):
        disks = self.get_compute_disks(compute_id, disk_type=disk_type)
        if disks is None:
            return 0
        return len(disks)

    def get_compute_disks_size(self, compute_id, disk_type=None):
        disks = self.get_compute_disks(compute_id, disk_type=disk_type)
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

        # Default value in MB
        if factor == 1:
            factor = 1024 * 1024
            size_bytes = int(size.strip())

        return size_bytes * factor

    def is_physical_disk_ok(self, info):
        if info['Operability'] == 'operable' and info['Presence'] == 'equipped' and info['DiskState'].lower() in ['good', 'online', 'healthy']:
            return True

        if info['Operability'] == '' and info['Presence'] == 'equipped' and info['DiskState'].lower() in ['good', 'online', 'healthy']:
            return True

        if info['Operability'] == '' and info['Presence'] == '' and info['DiskState'].lower() in ['good', 'online', 'healthy']:
            return True

        return False

    def get_compute_disks_info(self, compute_id, disk_type=None, virtual_drives_info=None, storage_controllers_info=None):
        compute_disks = self.get_compute_disks(compute_id, disk_type=disk_type)
        if compute_disks is None:
            return None

        compute_disks_info = []

        keys = [
            'Moid',
            'Bootable',
            'DiskId',
            'DiskState',
            'Dn',
            'DriveFirmware',
            'DriveState',
            'LinkSpeed',
            'Model',
            'Pid',
            'OperPowerState',
            'Operability',
            'Presence',
            'Serial',
            'Size',
            'Type',
            'Vendor'
        ]

        for compute_disk in compute_disks:
            info = {}
            info['__Output'] = {}

            for key in keys:
                info[key] = compute_disk[key]

            try:
                info['_DiskId'] = int(info['DiskId'])
            except BaseException:
                info['_DiskId'] = 0

            info['SizeBytes'] = self.get_disk_size_bytes(
                info['Size']
            )

            info['SizeUnit'] = self.info_helper.convert_storage(
                info['SizeBytes']
            )

            info['VirtualDriveMoid'] = None
            info['VirtualDriveId'] = ''
            if virtual_drives_info is not None:
                for virtual_drive_info in virtual_drives_info:
                    if compute_disk['DiskId'] in virtual_drive_info['PhysicalDiskIds']:
                        info['VirtualDriveMoid'] = virtual_drive_info['Moid']
                        info['VirtualDriveId'] = virtual_drive_info['VirtualDriveId']

            info['StorageControllerId'] = ''
            info['StorageControllerName'] = ''
            if storage_controllers_info is not None:
                for storage_controller_info in storage_controllers_info:
                    if compute_disk['Moid'] in storage_controller_info['PhysicalDiskIds']:
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

            if info['DiskState'].lower() in ['good', 'online', 'healthy']:
                info['__Output']['DiskState'] = 'Green'
            else:
                info['__Output']['DiskState'] = 'Red'

            if info['Bootable'] == 'true':
                info['BootableTick'] = '\u2713'
                info['__Output']['BootableTick'] = 'Green'
            else:
                info['BootableTick'] = '\u2717'
                info['__Output']['BootableTick'] = 'Red'

            if self.is_physical_disk_ok(info):
                info['StateTick'] = '\u2713'
                info['__Output']['StateTick'] = 'Green'
            else:
                info['StateTick'] = '\u2717'
                info['__Output']['StateTick'] = 'Red'

            compute_disks_info.append(info)

        compute_disks_info = sorted(compute_disks_info, key=lambda i: i['_DiskId'])

        return compute_disks_info
