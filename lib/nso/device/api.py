import time
import traceback


class NsoDeviceApi():
    def __init__(self):
        self.device_base_mo = None
        self.device_sync_mo = {}
        self.device_config_mo = {}

    def get_device_base_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.device_base_mo is not None:
                return self.device_base_mo

        try:
            start_time = int(time.time() * 1000)
            success, content = self.rest_handler.get_rest(
                'json',
                None,
                'Accept',
                'application/yang-data',
                'data/tailf-ncs:devices/device',
                'fields=name;address;port;authgroup;device-type;state/admin-state'
            )
            self.log.nso(
                'get',
                'device_base',
                success,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            success = False
            self.log.nso(
                'get',
                'device_base',
                success,
                int(time.time() * 1000) - start_time
            )

        if not success or content is None:
            self.log.error(
                'nso.get_device_base_mo',
                'Failed to get device list'
            )
            return None

        self.device_base_mo = content['tailf-ncs:device']

        self.log.nso_mo(
            'device_base',
            self.device_base_mo
        )

        return self.device_base_mo

    def get_device_sync_mo(self, device_name, cache_enabled=True):
        if cache_enabled:
            if device_name in self.device_sync_mo:
                return self.device_sync_mo[device_name]

        try:
            start_time = int(time.time() * 1000)
            success, content = self.rest_handler.post_rest(
                'xml',
                None,
                'Content-Type',
                'application/yang-data',
                None,
                path='data/tailf-ncs:devices/device=%s/check-sync' % (device_name)
            )
            self.log.nso(
                'get',
                'device_sync',
                success,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            success = False
            self.log.nso(
                'get',
                'device_sync',
                success,
                int(time.time() * 1000) - start_time
            )
            self.log.error(
                'get_device_sync_mo',
                traceback.format_exc()
            )

        if not success:
            self.log.error(
                'nso.get_device_sync',
                'Failed to get device sync state: %s' % (device_name)
            )
            return None

        self.device_sync_mo[device_name] = content

        self.log.nso_mo(
            'device_sync_mo.%s' % (device_name),
            self.device_sync_mo[device_name]
        )

        return self.device_sync_mo[device_name]

    def get_device_config_mo(self, device_name, cache_enabled=True):
        if cache_enabled:
            if device_name in self.device_config_mo:
                return self.device_config_mo[device_name]

        try:
            start_time = int(time.time() * 1000)
            success, content = self.rest_handler.get_rest(
                'json',
                None,
                'Accept',
                'application/yang-data',
                'data/tailf-ncs:devices/device=%s/config' % (device_name)
            )

            self.log.nso(
                'get',
                'device_config',
                success,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            success = False
            self.log.nso(
                'get',
                'device_config',
                success,
                int(time.time() * 1000) - start_time
            )

        if not success:
            self.log.error(
                'nso.get device_config',
                'Failed to get device config: %s' % (device_name)
            )
            return None

        self.device_config_mo[device_name] = content['tailf-ncs:config']

        self.log.nso_mo(
            'device_config.%s' % (device_name),
            self.device_config_mo[device_name]
        )

        return self.device_config_mo[device_name]
