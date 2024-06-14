import json


class ImcCliBoot():
    def __init__(self):
        self.boot_mo = None
        self.boot_device_mo = None

    def get_boot_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.boot_mo is not None:
                return self.boot_mo

            self.boot_mo = self.get_icm_cli_cache_entry(
                'boot'
            )
            if self.boot_mo is not None:
                return self.boot_mo

        # Boot Order 1:
        #     Boot Device: (Bus 18 Dev 00)PCI RAID Adapter
        #     Device Type: HDD
        #     Boot Policy: NonPolicyTarget
        #     Slot Num:
        #     Lun Id:

        self.boot_mo = self.show_list(
            'show actual-boot-order detail',
            'Boot Order',
            'Boot Order',
            method='last word',
            scope='bios'
        )

        if self.boot_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'boot',
            self.boot_mo
        )

        self.log.debug(
            'get_boot_mo',
            json.dumps(self.boot_mo, indent=4)
        )

        return self.boot_mo

    def get_boot_device_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.boot_device_mo is not None:
                return self.boot_device_mo

            self.boot_device_mo = self.get_icm_cli_cache_entry(
                'boot_device'
            )
            if self.boot_device_mo is not None:
                return self.boot_device_mo

        # Boot Device localhdd:
        #     Device Type: LOCALHDD
        #     Device State: Disabled
        #     Device Order: 1
        #     Slot Id:
        #     Boot Loader Name:
        #     Boot Loader Path:
        #     Boot Loader Description:

        self.boot_device_mo = self.show_list(
            'show boot-device detail',
            'Boot Device',
            'Boot Device',
            method='last word',
            scope='bios'
        )

        if self.boot_device_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'boot_device',
            self.boot_device_mo
        )

        self.log.debug(
            'get_boot_mo',
            json.dumps(self.boot_device_mo, indent=4)
        )

        return self.boot_device_mo

    def get_boot_info(self, boot_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip

        for key in boot_mo:
            info[key] = boot_mo[key]

        info['__Key'] = 'Boot Order'
        info['__Value'] = info[info['__Key']]
        self.log.debug(
            'get_boot_info',
            json.dumps(info, indent=4)
        )

        return info

    def get_boot_device_info(self, boot_device_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip

        for key in boot_device_mo:
            info[key] = boot_device_mo[key]

        self.log.debug(
            'get_boot_device_info',
            json.dumps(info, indent=4)
        )

        return info

    def get_boot(self, order_info=True, device_info=True, cache_enabled=True):
        boot_info = {}

        if order_info:
            boot_mo = self.get_boot_mo(cache_enabled=cache_enabled)
            if boot_mo is None:
                return None

            boot_info['order'] = []
            for item in boot_mo:
                boot_info['order'].append(
                    self.get_boot_info(
                        item
                    )
                )

        if device_info:
            boot_device_mo = self.get_boot_device_mo(cache_enabled=cache_enabled)
            if boot_device_mo is None:
                return None

            boot_info['device'] = []
            for item in boot_device_mo:
                boot_info['device'].append(
                    self.get_boot_device_info(
                        item
                    )
                )

        return boot_info

    def validate_boot_order(self, boot_order):
        if boot_order is None:
            self.log.error(
                'validate_boot_order',
                'None value invalid'
            )
            return False

        if not isinstance(boot_order, list):
            self.log.error(
                'validate_boot_order',
                'list expected'
            )
            return False

        allowed = ['hdd', 'pxe', 'fdd', 'efi', 'cdrom']
        for item in boot_order:
            if item not in allowed:
                self.log.error(
                    'validate_boot_order',
                    'invalid item: %s' % (item)
                )
                return False

        return True

    def set_boot_order(self, boot_order):
        commands = []
        commands.append('top')
        commands.append('scope bios')
        commands.append('set boot-order %s' % (','.join(boot_order)))

        success, output = self.run_commands(
            commands
        )

        if not success:
            self.log.error(
                'set_boot_order',
                'Failed to set boot order'
            )
            return False

        self.log.debug(
            'set_boot_order',
            output
        )

        return True

    def is_top_boot_order_from_device_type(self, device_type, cache_enabled=True):
        boot_order = self.get_boot(
            order_info=True,
            cache_enabled=cache_enabled
        )
        if boot_order is None:
            self.log.error(
                'is_boot_from_device_type',
                'Failed to get current boot order'
            )
            return False

        for item in boot_order['order']:
            if item['Boot Order'] == '1':
                if item['Device Type'] == device_type:
                    return True
                return False

        self.log.error(
            'is_boot_from_device_type',
            'Failed to get current 1st boot order'
        )
        return False

    def validate_boot_device_type(self, device_type):
        allowed = [
            'PXE',
            'ISCSI',
            'LOCALHDD',
            'SAN',
            'USB',
            'VMEDIA',
            'PCHSTORAGE',
            'UEFISHELL',
            'NVME',
            'LOCALCDD',
            'HTTP',
            'EMBEDDEDSTORAGE'
        ]
        if device_type not in allowed:
            self.log.error(
                'validate_boot_device_type',
                'invalid device type: %s' % (device_type)
            )
            return False

        return True

    def is_boot_device_type(self, device_type, cache_enabled=False):
        boot_devices = self.get_boot(
            device_info=True,
            cache_enabled=cache_enabled
        )
        if boot_devices is None:
            self.log.error(
                'is_boot_device_type',
                'Failed to get current boot devices'
            )
            return False

        for item in boot_devices['device']:
            if item['Device Type'] == device_type:
                return True

        return False

    def is_boot_device_name(self, device_name, cache_enabled=False):
        boot_devices = self.get_boot(
            device_info=True,
            cache_enabled=cache_enabled
        )
        if boot_devices is None:
            self.log.error(
                'is_boot_device',
                'Failed to get current boot devices'
            )
            return False

        for item in boot_devices['device']:
            if item['Boot Device'] == device_name:
                return True

        return False

    def create_boot_device(self, device_name, device_type, device_order=None):
        if not self.validate_boot_device_type(device_type):
            return False

        commands = []
        commands.append('top')
        commands.append('scope bios')
        commands.append('create-boot-device %s %s' % (device_name, device_type))
        commands.append('enable-all-boot-device')
        if device_order is not None:
            commands.append('rearrange-boot-device %s:%s' % (device_name, device_order))

        success, output = self.run_commands(
            commands
        )

        if not success:
            self.log.error(
                'create_boot_device',
                'Failed to set boot order'
            )
            return False

        self.log.debug(
            'create_boot_device',
            output
        )

        return True

    def delete_boot_device(self, device_name):
        commands = []
        commands.append('top')
        commands.append('scope bios')
        commands.append('remove-boot-device %s' % (device_name))

        success, output = self.run_commands(
            commands
        )

        if not success:
            self.log.error(
                'delete_boot_device',
                'Failed to delete boot order'
            )
            return False

        self.log.debug(
            'delete_boot_device',
            output
        )

        return True
