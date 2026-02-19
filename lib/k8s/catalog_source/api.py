import time
import traceback


class K8sCatalogSourceApi():
    def __init__(self):
        self.catalog_source_mo = None

    def get_catalog_source_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.catalog_source_mo is not None:
                return self.catalog_source_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='operators.coreos.com/v1alpha1',
                kind='CatalogSource'
            )
            self.catalog_source_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'catalog_source',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_catalog_source_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'catalog_source',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'catalog_source',
            self.catalog_source_mo
        )

        return self.catalog_source_mo

    def create_catalog_source_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='operators.coreos.com/v1alpha1', kind='CatalogSource')
            success = True
            response = obj_list.create(
                body=body,
                namespace=body['metadata']['namespace'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_catalog_source', traceback.format_exc())

        self.log.ocp(
            'create',
            'catalog_source',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def delete_catalog_source_mo(self, namespace, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='operators.coreos.com/v1alpha1', kind='CatalogSource')
            success = True
            response = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_catalog_source_mo', traceback.format_exc())

        self.log.ocp(
            'delete',
            'catalog_source',
            success,
            int(time.time() * 1000) - start_time
        )

        return success