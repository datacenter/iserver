class StorageVirtualDriveInfo():
    def __init__(self):
        pass

    def get_virtual_drives_size(self, virtual_drives_info):
        size = 0
        for virtual_drive_info in virtual_drives_info:
            size = size + virtual_drive_info['SizeBytes']
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
        if info['Operability'] not in ['operable', 'ok', '']:
            return False

        if info['Presence'] not in ['equipped', '']:
            return False

        if info['DriveState'].lower() not in ['optimal']:
            return False

        return True

    def get_info(self, virtual_drives_mo, storage_controllers_info=None):
        if virtual_drives_mo is None:
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

        for virtual_drive in virtual_drives_mo:
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

        return virtual_drives_info
