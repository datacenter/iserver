import time
import traceback


class OspRoleApi():
    def __init__(self):
        self.role_mo = None

    def get_role_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.role_mo is not None:
                return self.role_mo

        api_handler = self.get_api_keystone(cache_enabled=cache_enabled)
        if api_handler is None:
            self.log.error(
                'get_role_mo',
                'No api handler'
            )
            return None

        try:
            start_time = int(time.time() * 1000)
            self.role_mo = api_handler.roles.list()
            self.log.osp(
                'get',
                'roles',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('osp.get_role_mo', traceback.format_exc())
            self.log.osp(
                'get',
                'roles',
                True,
                int(time.time() * 1000) - start_time
            )
            return None

        return self.role_mo
