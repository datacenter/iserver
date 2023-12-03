import time
import traceback


class OspNetworkApi():
    def __init__(self):
        self.network_mo = None

    def get_network_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.network_mo is not None:
                return self.network_mo

        api_handler = self.get_api_neutron(cache_enabled=cache_enabled)
        if api_handler is None:
            self.log.error(
                'get_network_mo',
                'No api handler'
            )
            return None

        try:
            start_time = int(time.time() * 1000)
            self.network_mo = api_handler.list_networks()['networks']
            self.log.osp(
                'get',
                'networks',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('osp.get_network_mo', traceback.format_exc())
            self.log.osp(
                'get',
                'networks',
                True,
                int(time.time() * 1000) - start_time
            )
            return None

        return self.network_mo
