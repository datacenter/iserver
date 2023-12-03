import time
import traceback


class OspHypervisorApi():
    def __init__(self):
        self.hypervisor_mo = None

    def get_hypervisor_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.hypervisor_mo is not None:
                return self.hypervisor_mo

        api_handler = self.get_api_nova(cache_enabled=cache_enabled)
        if api_handler is None:
            self.log.error(
                'get_hypervisor_mo',
                'No api handler'
            )
            return None

        try:
            start_time = int(time.time() * 1000)
            self.hypervisor_mo = api_handler.hypervisors.list()
            self.log.osp(
                'get',
                'hypervisors',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('osp.get_hypervisor_mo', traceback.format_exc())
            self.log.osp(
                'get',
                'hypervisors',
                True,
                int(time.time() * 1000) - start_time
            )
            return None

        return self.hypervisor_mo
