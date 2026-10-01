import json
from lib import filter_helper


class LinuxLsblkInfo():
    def __init__(self):
        self.lsblk = None

    def get_lsblk_info(self, managed_object, trim_managed_object):
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
        
        info['lvm_children'] = False
        info['lvm_childrenT'] = '\u2717'
        if 'children' in info:
            for child in info['children']:
                if child['type'] == 'lvm':
                    info['lvm_children'] = True
                    info['lvm_childrenT'] = '\u2713'

        info['warningT'] = None
        if info['fstypeT'] != 'LVM2' and info['lvm_children']:
            info['warningT'] = []
            info['warningT'].append('LVM children')
            
        if info['boot']:
            info['bootT'] = '\u2713'

        info['hwT'] = []
        if info['model'] is not None:
            info['hwT'].append(
                info['model']
            )
        if info['serial'] is not None:
            info['hwT'].append(
                info['serial']
            )

        info['pathT'] = '%s (%s)' % (info['path'], info['kname'])

        info['trim'] = False
        info['trimT'] = '\u2717'
        if trim_managed_object is not None:
            if filter_helper.get(trim_managed_object, 'disc-gran', on_error="0B", on_none="0B") != "0B":
                if filter_helper.get(trim_managed_object, 'disc-max', on_error="0B", on_none="0B") != "0B":
                    info['trim'] = True
                    info['trimT'] = '\u2713'
                    
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
        
        try:
            lsblks_trim_mo = json.loads(
                self.get_lsblk_trim_cmd(cache_enabled=cache_enabled)
            )['blockdevices']
        except BaseException:
            lsblks_trim_mo = None
            
        self.lsblk = []
        for lsblk_mo in lsblks_mo:
            trim_mo = None
            if lsblks_trim_mo is not None:
                for lsblk_trim_mo in lsblks_trim_mo:
                    if lsblk_mo['name'] == lsblk_trim_mo['name']:
                        trim_mo = lsblk_trim_mo
                        break

            lsblk_info = self.get_lsblk_info(
                lsblk_mo,
                trim_mo
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

    def add_lsblk_disk_path(self, items, include_disk_paths):
        for item in items:
            item['disk-id'] = None

        if not include_disk_paths:
            return items
        
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

                    if line.split(' -> ')[0].split(' ')[-1].startswith('nvme-') and not line.split(' -> ')[0].split(' ')[-1].startswith('nvme-eui.'):
                        if not line.split(' -> ')[0].split(' ')[-1].endswith('_1'):
                            disk_path[line.split(' -> ')[1].split('/')[-1]] = '/dev/disk/by-id/%s' % (line.split(' -> ')[0].split(' ')[-1])

        for item in items:
            item['disk-id'] = []
            if item['disk-path'] is not None:
                item['disk-id'].append(
                    item['disk-path']
                )

            if item['disk-wwn'] is not None:
                item['disk-id'].append(
                    item['disk-wwn']
                )
            else:
                if item['name'] in disk_path:
                    item['disk-id'].append(
                        disk_path[item['name']]
                    )
                
        return items
    
    def get_lsblks(self, device_names=None, fstypes=None, include_disk_paths=False, cache_enabled=True, exclude_boot=False):
        all_items = self.get_lsblks_info(
            cache_enabled=cache_enabled,
            exclude_boot=exclude_boot
        )
        if all_items is None:
            return None

        items = []
        for item in all_items:
            if device_names is not None and len(device_names) > 0:
                if item['path'] in device_names:
                    items.append(item)

                continue

            if fstypes is not None and len(fstypes) > 0:
                if item['fstypeT'] in fstypes:
                    items.append(item)

                continue
            
            items.append(item)

        items = sorted(
            self.add_lsblk_disk_path(items, include_disk_paths),
            key=lambda i: i['kname'].lower()
        )

        self.log.linux_info(
            '%s.lsblk' % (self.server_display_name),
            items
        )

        return items