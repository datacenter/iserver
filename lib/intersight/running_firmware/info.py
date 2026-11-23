class RunningFirmwareInfo():
    def __init__(self):
        pass

    def get_firmware_name(self, info):
        if info['Type'] == 'adaptor':
            return 'Adapter'

        if info['Type'] == 'blade-bios':
            return 'BIOS'

        if info['Type'] == 'local-disk':
            return 'Disk'

        if info['Type'] == 'storage-controller':
            return 'Storage Controller'

        if info['Component'] == 'boot-loader' and info['Type'] == 'blade-controller':
            return 'Board Controller'

        if info['Component'] == 'system' and info['Type'] == 'blade-controller':
            return 'CIMC Controller'

        return ''

    def get_info(self, managed_object):
        keys = [
            'Component',
            'Dn',
            'Type',
            'PackageVersion',
            'Version'
        ]
        info = {}
        for key in keys:
            info[key] = managed_object[key].replace('\n', '')

        info['Name'] = self.get_firmware_name(info)

        return info

    def get_version(self, managed_objects):
        for managed_object in managed_objects:
            if managed_object['Component'] == 'system' and managed_object['Type'] == 'blade-controller':
                return managed_object['Version']
        return None
