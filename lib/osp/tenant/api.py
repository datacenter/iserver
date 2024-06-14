import time
import traceback


class OspTenantApi():
    def __init__(self):
        self.tenant_mo = None

    def get_tenant_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.tenant_mo is not None:
                return self.tenant_mo

        api_handler = self.get_api_keystone(cache_enabled=cache_enabled)
        if api_handler is None:
            self.log.error(
                'get_tenant_mo',
                'No api handler'
            )
            return None

        try:
            start_time = int(time.time() * 1000)
            if self.api_version == 2:
                self.tenant_mo = api_handler.tenants.list()
            if self.api_version == 3:
                self.tenant_mo = api_handler.projects.list()

            self.log.osp(
                'get',
                'tenants',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('osp.get_tenant_mo', traceback.format_exc())
            self.log.osp(
                'get',
                'tenants',
                True,
                int(time.time() * 1000) - start_time
            )
            return None

        return self.tenant_mo
