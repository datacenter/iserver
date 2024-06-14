import time
import traceback


class OspQuotaApi():
    def __init__(self):
        self.quota_mo = {}

    def get_quota_mo(self, tenant_ids, cache_enabled=True):
        if cache_enabled:
            cache_ready = True
            for tenant_id in tenant_ids:
                if tenant_id not in self.quota_mo or self.quota_mo[tenant_id] is None:
                    cache_ready = False
                    break

            if cache_ready:
                return self.quota_mo

        api_handler = self.get_api_nova(cache_enabled=cache_enabled)
        if api_handler is None:
            self.log.error(
                'get_quota_mo',
                'No api handler'
            )
            return None

        try:
            start_time = int(time.time() * 1000)
            for tenant_id in tenant_ids:
                perform_api = True
                if cache_enabled and tenant_id in self.quota_mo and self.quota_mo[tenant_id] is not None:
                    perform_api = False

                if perform_api:
                    self.quota_mo[tenant_id] = api_handler.quotas.get(tenant_id)

            self.log.osp(
                'get',
                'quotas',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('osp.get_quota_mo', traceback.format_exc())
            self.log.osp(
                'get',
                'quotas',
                True,
                int(time.time() * 1000) - start_time
            )
            return None

        return self.quota_mo
