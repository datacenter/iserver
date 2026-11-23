import time
import traceback


class OspRouterApi():
    def __init__(self):
        self.router_mo = None

    def get_router_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.router_mo is not None:
                return self.router_mo

        api_handler = self.get_api_neutron(cache_enabled=cache_enabled)
        if api_handler is None:
            self.log.error(
                'get_router_mo',
                'No api handler'
            )
            return None

        try:
            start_time = int(time.time() * 1000)
            self.router_mo = api_handler.list_routers()['routers']
            self.log.osp(
                'get',
                'routers',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('osp.get_router_mo', traceback.format_exc())
            self.log.osp(
                'get',
                'routers',
                True,
                int(time.time() * 1000) - start_time
            )
            return None

        return self.router_mo
