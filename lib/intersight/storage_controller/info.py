class StorageControllerInfo():
    def __init__(self):
        pass

    def get_board_info(self, storage_controllers_mo, physical_disks_mo=None):
        if storage_controllers_mo is None:
            return None

        controllers_info = []

        keys = [
            'Model',
            'Moid',
            'Vendor',
            'Serial',
            'Presence',
            'ControllerStatus',
            'PciAddr',
            'PciSlot',
            'ControllerId',
            'Dn',
            'RaidSupport'
        ]

        for controller in storage_controllers_mo:
            info = {}
            info['__Output'] = {}
            for key in keys:
                info[key] = controller[key]

            info['Name'] = info['Dn'].split('/')[-1]

            if physical_disks_mo is None:
                info['PhysicalDiskCount'] = len(controller['PhysicalDisks'])
                info['PhysicalDiskIds'] = []
                for physical_disk in controller['PhysicalDisks']:
                    info['PhysicalDiskIds'].append(physical_disk['Moid'])

            if physical_disks_mo is not None:
                candidate_moids = []
                for physical_disk in controller['PhysicalDisks']:
                    candidate_moids.append(physical_disk['Moid'])

                info['PhysicalDiskCount'] = 0
                info['PhysicalDiskIds'] = []
                for physical_disk_mo in physical_disks_mo:
                    if physical_disk_mo['Moid'] in candidate_moids:
                        if physical_disk_mo['DiskState'] != '':
                            info['PhysicalDiskCount'] = info['PhysicalDiskCount'] + 1
                            info['PhysicalDiskIds'].append(
                                physical_disk_mo['Moid']
                            )

            info['VirtualDriveCount'] = len(controller['VirtualDrives'])
            info['VirtualDriveIds'] = []
            for virtual_drive in controller['VirtualDrives']:
                info['VirtualDriveIds'].append(virtual_drive['Moid'])

            if info['Presence'] == 'equipped':
                info['__Output']['Presence'] = 'Green'
            else:
                info['__Output']['Presence'] = 'Red'

            controllers_info.append(info)

        return controllers_info

    def get_blade_info(self, controllers):
        if controllers is None:
            return None

        controllers_info = []

        keys = [
            'Model',
            'Moid',
            'Vendor',
            'Serial',
            'Presence',
            'ControllerStatus',
            'PciAddr',
            'PciSlot',
            'ControllerId',
            'Dn',
            'RaidSupport'
        ]

        for controller in controllers:
            info = {}
            info['__Output'] = {}

            for key in keys:
                info[key] = controller[key]

            info['Name'] = info['Dn'].split('/')[-1]
            info['PhysicalDiskCount'] = len(controller['PhysicalDisks'])
            info['PhysicalDiskIds'] = []
            for physical_disk in controller['PhysicalDisks']:
                info['PhysicalDiskIds'].append(physical_disk['Moid'])

            info['VirtualDriveCount'] = len(controller['VirtualDrives'])
            info['VirtualDriveIds'] = []
            for virtual_drive in controller['VirtualDrives']:
                info['VirtualDriveIds'].append(virtual_drive['Moid'])

            if info['Presence'] == 'equipped':
                info['__Output']['Presence'] = 'Green'
            else:
                info['__Output']['Presence'] = 'Red'

            controllers_info.append(info)

        return controllers_info
