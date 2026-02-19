import re


class LinuxLvm():
    def __init__(self):
        self.lvm = None

    def get_lvms_info(self, output):
        lvms = []

        lvm_section = False
        for line in output.split('\n'):
            if '--- Logical volume ---' in line:
                lvm_info = {}
                lvm_info['name'] = None
                lvm_section = True
                continue

            if lvm_section:
                line = re.sub(' +', ' ', line)
                if 'LV Path' in line:
                    lvm_info['path'] = line.split('LV Path')[1].strip()
                    continue

                if 'LV Name' in line:
                    lvm_info['name'] = line.split('LV Name')[1].strip()
                    continue

                if 'VG Name' in line:
                    lvm_info['vg'] = line.split('VG Name')[1].strip()
                    continue

                if 'LV UUID' in line:
                    lvm_info['uuid'] = line.split('LV UUID')[1].strip()
                    continue

                if 'LV Write Access' in line:
                    lvm_info['access'] = line.split('LV Write Access')[1].strip()
                    continue

                if 'LV Pool name' in line:
                    lvm_info['pool'] = line.split('LV Pool name')[1].strip()
                    continue

                if 'LV Status' in line:
                    lvm_info['status'] = line.split('LV Status')[1].strip()
                    continue

                if 'LV Size' in line:
                    lvm_info['size'] = line.split('LV Size')[1].strip()
                    continue

                if 'Mapped size' in line:
                    lvm_info['mapped'] = line.split('Mapped size')[1].strip()
                    continue

                if 'Block device' in line:
                    lvm_info['block_device'] = line.split('Block device')[1].strip()
                    lvms.append(lvm_info)
                    lvm_section = False
                    continue

        return lvms

    def get_lvms(self, progress_bar=False, cache=False):
        if cache and self.lvm is not None:
            return self.lvm

        commands = ['sudo lvm lvdisplay']
        outputs = self.run_commands(commands, progress_bar=progress_bar)
        if outputs is None:
            self.log.error(
                'get_lvms',
                'Commands output collection failed'
            )
            return None

        self.lvm = self.get_lvms_info(
            outputs['sudo lvm lvdisplay']
        )

        return self.lvm
