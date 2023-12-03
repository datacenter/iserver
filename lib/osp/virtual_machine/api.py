import time
import traceback


class OspVirtualMachineApi():
    def __init__(self):
        self.virtual_machine_mo = None

    def get_virtual_machine_id_mo(self, virtual_machine_id, cache_enabled=True):
        if cache_enabled:
            if self.virtual_machine_mo is not None:
                for item in self.virtual_machine_mo:
                    if item.id == virtual_machine_id:
                        return item

        api_handler = self.get_api_nova(cache_enabled=cache_enabled)
        if api_handler is None:
            self.log.error(
                'get_virtual_machine_mo',
                'No api handler'
            )
            return None

        try:
            start_time = int(time.time() * 1000)
            virtual_machine_mo = api_handler.servers.get(virtual_machine_id)
            self.log.osp(
                'get',
                'virtual_machine',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('osp.get_virtual_machine_id_mo', traceback.format_exc())
            self.log.osp(
                'get',
                'virtual_machines',
                True,
                int(time.time() * 1000) - start_time
            )
            return None

        return virtual_machine_mo

    def get_virtual_machine_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.virtual_machine_mo is not None:
                return self.virtual_machine_mo

        api_handler = self.get_api_nova(cache_enabled=cache_enabled)
        if api_handler is None:
            self.log.error(
                'get_virtual_machine_mo',
                'No api handler'
            )
            return None

        try:
            start_time = int(time.time() * 1000)
            self.virtual_machine_mo = api_handler.servers.list(search_opts={'all_tenants': 1})
            self.log.osp(
                'get',
                'virtual_machines',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('osp.get_virtual_machine_mo', traceback.format_exc())
            self.log.osp(
                'get',
                'virtual_machines',
                True,
                int(time.time() * 1000) - start_time
            )
            return None

        return self.virtual_machine_mo
