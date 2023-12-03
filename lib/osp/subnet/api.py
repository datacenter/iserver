import time
import traceback


class OspSubnetApi():
    def __init__(self):
        self.subnet_mo = None

    def get_subnet_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.subnet_mo is not None:
                return self.subnet_mo

        api_handler = self.get_api_neutron(cache_enabled=cache_enabled)
        if api_handler is None:
            self.log.error(
                'get_subnet_mo',
                'No api handler'
            )
            return None

        try:
            start_time = int(time.time() * 1000)
            self.subnet_mo = api_handler.list_subnets()['subnets']
            self.log.osp(
                'get',
                'subnets',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('osp.get_subnet_mo', traceback.format_exc())
            self.log.osp(
                'get',
                'subnets',
                True,
                int(time.time() * 1000) - start_time
            )
            return None

        return self.subnet_mo
