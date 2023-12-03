import time
import traceback


class OspFloatingIpApi():
    def __init__(self):
        self.floating_ip_mo = None

    def get_floating_ip_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.floating_ip_mo is not None:
                return self.floating_ip_mo

        api_handler = self.get_api_neutron(cache_enabled=cache_enabled)
        if api_handler is None:
            self.log.error(
                'get_floating_ip_mo',
                'No api handler'
            )
            return None

        try:
            start_time = int(time.time() * 1000)
            self.floating_ip_mo = api_handler.list_floatingips()['floatingips']
            self.log.osp(
                'get',
                'floating_ips',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('osp.get_floating_ip_mo', traceback.format_exc())
            self.log.osp(
                'get',
                'floating_ips',
                True,
                int(time.time() * 1000) - start_time
            )
            return None

        return self.floating_ip_mo
