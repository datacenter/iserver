import time
import traceback


class K8sCustomResourceDefinitionApi():
    def __init__(self):
        self.custom_resource_definition_mo = None

    def get_custom_resource_definition_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.custom_resource_definition_mo is not None:
                return self.custom_resource_definition_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='apiextensions.k8s.io/v1',
                kind='CustomResourceDefinition'
            )
            self.custom_resource_definition_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'custom_resource_definition',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_custom_resource_definition_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'custom_resource_definition',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'custom_resource_definition',
            self.custom_resource_definition_mo
        )

        return self.custom_resource_definition_mo
