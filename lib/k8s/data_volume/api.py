import time
import json
import traceback


class K8sDataVolumeApi():
    def __init__(self):
        self.data_volume_mo = None

    def get_data_volume_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.data_volume_mo is not None:
                return self.data_volume_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='cdi.kubevirt.io/v1beta1',
                kind='DataVolume'
            )
            self.data_volume_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'data_volume',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_data_volume_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'data_volume',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'data_volume',
            self.data_volume_mo
        )

        return self.data_volume_mo

    def create_data_volume(self, data_volume):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='cdi.kubevirt.io/v1beta1', kind='DataVolume')
            success = True
            response = obj_list.create(
                body=data_volume,
                namespace=data_volume['metadata']['namespace'],
            )
        except BaseException:
            success = False
            self.log.error(
                'k8s.create_data_volume',
                'PVC create failed: %s' % (json.dumps(data_volume, indent=4))
            )
            self.log.error(
                'k8s.create_data_volume',
                traceback.format_exc()
            )

        self.log.ocp(
            'create',
            'dv',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def delete_data_volume(self, namespace, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            success = True
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='cdi.kubevirt.io/v1beta1', kind='DataVolume')
            success = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('k8s.create_data_volume', traceback.format_exc())

        self.log.ocp(
            'delete',
            'dv',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
