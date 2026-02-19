import json


class LinuxLsblkInfo():
    def __init__(self):
        self.lsblk = None

    def get_lsblk_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        for key in managed_object:
            info[key] = managed_object[key]

        info['fstypeT'] = info['fstype']
        if info['fstype'] is None:
            info['fstypeT'] = '---'
        
        if info['fstype'] == 'LVM2_member':
            info['fstypeT'] = 'LVM2'

        if info['fstype'] == 'ceph_bluestore':
            info['fstypeT'] = 'Ceph'

        info['boot'] = False
        info['bootT'] = ''
        if 'children' in info:
            for child in info['children']:
                if child['mountpoint'] == '/boot':
                    info['boot'] = True
        
        if info['boot']:
            info['bootT'] = '\u2713'

        return info

    def get_lsblks_info(self, cache_enabled=True, exclude_boot=False):
        if cache_enabled and self.lsblk is not None:
            return self.lsblk

        try:
            lsblks_mo = json.loads(
                self.get_lsblk_cmd(cache_enabled=cache_enabled)
            )['blockdevices']
        except BaseException:
            self.log.error(
                'get_lsblks_info',
                'Commands output parsing failed'
            )
            return None
        
        self.lsblk = []
        for lsblk_mo in lsblks_mo:
            lsblk_info = self.get_lsblk_info(
                lsblk_mo
            )

            if exclude_boot:
                if lsblk_info['boot']:
                    continue

            self.lsblk.append(
                lsblk_info
            )

        self.log.linux_mo(
            '%s.lsblk' % (self.server_display_name),
            self.lsblk
        )

        return self.lsblk

    def get_lsblks(self, device_names=None, include_disk_paths=False, cache_enabled=True, exclude_boot=False):
        all_items = self.get_lsblks_info(
            cache_enabled=cache_enabled,
            exclude_boot=exclude_boot
        )
        if all_items is None:
            return None

        items = []
        for item in all_items:
            if device_names is None or len(device_names) == 0:
                items.append(item)
                continue

            if item['path'] in device_names:
                items.append(item)
                continue

        if include_disk_paths:
            for item in items:
                item['disk-path'] = None
                item['disk-wwn'] = None

            success, output, error = self.ssh_handler.run_cmd(
                'ls -l /dev/disk/by-path'
            )
            if success:            
                disk_path = {}
                for line in output.split('\n'):
                    if len(line.split(' -> ')) == 2:
                        disk_path[line.split(' -> ')[1].split('/')[-1]] = '/dev/disk/by-path/%s' % (line.split(' -> ')[0].split(' ')[-1])

                for item in items:
                    if item['name'] in disk_path:
                        item['disk-path'] = disk_path[item['name']]

            success, output, error = self.ssh_handler.run_cmd(
                'ls -l /dev/disk/by-id'
            )
            if success:            
                disk_path = {}
                for line in output.split('\n'):
                    if len(line.split(' -> ')) == 2:
                        if line.split(' -> ')[0].split(' ')[-1].startswith('wwn-'):
                            disk_path[line.split(' -> ')[1].split('/')[-1]] = '/dev/disk/by-id/%s' % (line.split(' -> ')[0].split(' ')[-1])

                for item in items:
                    if item['name'] in disk_path:
                        item['disk-wwn'] = disk_path[item['name']]

        self.log.linux_info(
            '%s.lsblk' % (self.server_display_name),
            items
        )

        return items                
