import time
import traceback


class K8sPortworxStorageClusterApi():
    def __init__(self):
        self.portworx_storage_cluster_mo = None

    def get_portworx_storage_cluster_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.portworx_storage_cluster_mo is not None:
                return self.portworx_storage_cluster_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='core.libopenstorage.org/v1',
                kind='StorageCluster'
            )
            self.portworx_storage_cluster_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'portworx_storage_cluster',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_portworx_storage_cluster_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'portworx_storage_cluster',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'portworx_storage_cluster',
            self.portworx_storage_cluster_mo
        )

        return self.portworx_storage_cluster_mo

    def create_portworx_storage_cluster_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='core.libopenstorage.org/v1', kind='StorageCluster')
            success = True
            response = obj_list.create(
                body=body,
                namespace=body['metadata']['namespace'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_portworx_storage_cluster', traceback.format_exc())

        self.log.ocp(
            'create',
            'portworx_storage_cluster',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def delete_portworx_storage_cluster_mo(self, namespace, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='core.libopenstorage.org/v1', kind='StorageCluster')
            success = True
            response = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_portworx_storage_cluster', traceback.format_exc())

        self.log.ocp(
            'delete',
            'portworx_storage_cluster',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
