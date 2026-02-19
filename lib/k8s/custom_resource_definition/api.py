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

    def create_custom_resource_definition_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='apiextensions.k8s.io/v1', kind='CustomResourceDefinition')
            success = True
            response = obj_list.create(
                body=body,
                name=body['metadata']['name'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_custom_resource_definition', traceback.format_exc())

        self.log.ocp(
            'create',
            'custom_resource_definition',
            success,
            int(time.time() * 1000) - start_time
        )

        return success


    def delete_custom_resource_definition(self, crd_name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='apiextensions.k8s.io/v1', kind='CustomResourceDefinition')
            success = True
            response = obj_list.delete(
                crd_name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_custom_resource_definition', traceback.format_exc())

        self.log.ocp(
            'delete',
            'custom_resource_definition',
            success,
            int(time.time() * 1000) - start_time
        )

        return success