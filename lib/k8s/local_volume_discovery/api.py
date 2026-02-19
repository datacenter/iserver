import time
import traceback


class K8sLocalVolumeDiscoveryApi():
    def __init__(self):
        self.local_volume_discovery_mo = None

    def get_local_volume_discovery_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.local_volume_discovery_mo is not None:
                return self.local_volume_discovery_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='local.storage.openshift.io/v1alpha1',
                kind='LocalVolumeDiscovery'
            )
            self.local_volume_discovery_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'local_volume_discovery',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_local_volume_discovery_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'local_volume_discovery',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'local_volume_discovery',
            self.local_volume_discovery_mo
        )

        return self.local_volume_discovery_mo

    def create_local_volume_discovery_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='local.storage.openshift.io/v1alpha1', kind='LocalVolumeDiscovery')
            success = True
            response = obj_list.create(
                body=body,
                namespace=body['metadata']['namespace'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_local_volume_discovery_mo', traceback.format_exc())

        self.log.ocp(
            'create',
            'local_volume_discovery',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def delete_local_volume_discovery_mo(self, namespace, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='local.storage.openshift.io/v1alpha1', kind='LocalVolumeDiscovery')
            success = True
            response = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_local_volume_discovery_mo', traceback.format_exc())

        self.log.ocp(
            'delete',
            'local_volume_discovery',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
