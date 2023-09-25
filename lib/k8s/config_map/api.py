import time
import traceback


class K8sConfigMapApi():
    def __init__(self):
        self.config_map_mo = None

    def get_config_map_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.config_map_mo is not None:
                return self.config_map_mo

        api_handler = self.get_api()
        if api_handler is None:
            return None

        # https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/CoreV1Api.md#list_config_map_for_all_namespaces
        try:
            start_time = int(time.time() * 1000)
            response = api_handler.list_config_map_for_all_namespaces(
                timeout_seconds=self.api_timeout_seconds
            )
            self.log.k8s(
                'get',
                'config_map',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_config_map_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'config_map',
                True,
                int(time.time() * 1000) - start_time
            )
            return False

        self.config_map_mo = []
        for item in response.items:
            config_map_mo = self.convert_object(item.to_dict())
            self.config_map_mo.append(
                config_map_mo
            )

        self.log.k8s_mo(
            'config_map',
            self.config_map_mo
        )

        return self.config_map_mo
