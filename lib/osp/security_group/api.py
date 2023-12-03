import time
import traceback


class OspSecurityGroupApi():
    def __init__(self):
        self.security_group_mo = None

    def get_security_group_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.security_group_mo is not None:
                return self.security_group_mo

        api_handler = self.get_api_neutron(cache_enabled=cache_enabled)
        if api_handler is None:
            self.log.error(
                'get_security_group_mo',
                'No api handler'
            )
            return None

        try:
            start_time = int(time.time() * 1000)
            self.security_group_mo = api_handler.list_security_groups()['security_groups']
            self.log.osp(
                'get',
                'security_groups',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('osp.get_security_group_mo', traceback.format_exc())
            self.log.osp(
                'get',
                'security_groups',
                True,
                int(time.time() * 1000) - start_time
            )
            return None

        return self.security_group_mo
