import time
import traceback


class OspPortApi():
    def __init__(self):
        self.port_mo = None

    def get_port_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.port_mo is not None:
                return self.port_mo

        api_handler = self.get_api_neutron(cache_enabled=cache_enabled)
        if api_handler is None:
            self.log.error(
                'get_port_mo',
                'No api handler'
            )
            return None

        try:
            start_time = int(time.time() * 1000)
            self.port_mo = api_handler.list_ports()['ports']
            self.log.osp(
                'get',
                'ports',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('osp.get_port_mo', traceback.format_exc())
            self.log.osp(
                'get',
                'ports',
                True,
                int(time.time() * 1000) - start_time
            )
            return None

        return self.port_mo
