import time
import traceback


class OspUserApi():
    def __init__(self):
        self.user_mo = None

    def get_user_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.user_mo is not None:
                return self.user_mo

        api_handler = self.get_api_keystone(cache_enabled=cache_enabled)
        if api_handler is None:
            self.log.error(
                'get_user_mo',
                'No api handler'
            )
            return None

        try:
            start_time = int(time.time() * 1000)
            self.user_mo = api_handler.users.list()
            self.log.osp(
                'get',
                'users',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('osp.get_user_mo', traceback.format_exc())
            self.log.osp(
                'get',
                'users',
                True,
                int(time.time() * 1000) - start_time
            )
            return None

        return self.user_mo
