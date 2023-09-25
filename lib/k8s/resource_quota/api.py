import time
import traceback


class K8sResourceQuotaApi():
    def __init__(self):
        self.resource_quota_mo = None

    def get_resource_quota_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.resource_quota_mo is not None:
                return self.resource_quota_mo

        api_handler = self.get_api()
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.list_resource_quota_for_all_namespaces(
                timeout_seconds=self.api_timeout_seconds
            )
            self.log.k8s(
                'get',
                'resource_quota',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_resource_quota_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'resource_quota',
                True,
                int(time.time() * 1000) - start_time
            )
            return False

        self.resource_quota_mo = []
        for item in response.items:
            resource_quota_mo = self.convert_object(item.to_dict())
            self.resource_quota_mo.append(
                resource_quota_mo
            )

        self.log.k8s_mo(
            'resource_quota',
            self.resource_quota_mo
        )

        return self.resource_quota_mo
