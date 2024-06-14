class StoragePhysicalDiskInfo():
    def __init__(self):
        pass

    def get_compute_disks_size(self, disks_info):
        if disks_info is None:
            return 0

        size = 0
        for disk_info in disks_info:
            size = size + disk_info['SizeBytes']

        return size

    def get_disk_size_bytes(self, size):
        if isinstance(size, int):
            return size

        if len(size.strip()) == 0:
            return 0

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
        if info['Operability'] == 'operable' and info['Presence'] == 'equipped' and info['DiskState'].lower() in ['good', 'online', 'healthy', 'ok', '']:
            return True

        if info['Operability'] == '' and info['Presence'] == 'equipped' and info['DiskState'].lower() in ['good', 'online', 'healthy', 'ok', '']:
            return True

        if info['Operability'] == '' and info['Presence'] == '' and info['DiskState'].lower() in ['good', 'online', 'healthy', 'ok', '']:
            return True

        return False

    def get_info(self, physical_disks_mo, disk_type=None, virtual_drives_info=None, storage_controllers_info=None):
        if physical_disks_mo is None:
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
            'PartNumber',
            'Pid',
            'OperPowerState',
            'Operability',
            'Presence',
            'Protocol',
            'Serial',
            'Size',
            'Type',
            'Vendor'
        ]

        for compute_disk in physical_disks_mo:
            if compute_disk['DriveState'] == 'Absent':
                continue

            info = {}
            info['__Output'] = {}

            for key in keys:
                if key  not in compute_disk:
                    info[key] = None
                else:
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

                    if compute_disk['Moid'] in virtual_drive_info['PhysicalDiskMoids']:
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

            if len(info['DiskState']) > 0:
                if info['DiskState'].lower() in ['good', 'online', 'healthy', 'ok']:
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
