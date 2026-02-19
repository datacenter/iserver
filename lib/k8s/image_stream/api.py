import time
import traceback


class K8sImageStreamApi():
    def __init__(self):
        self.image_stream_mo = None

    def get_image_stream_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.image_stream_mo is not None:
                return self.image_stream_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='image.openshift.io/v1',
                kind='ImageStream'
            )
            self.image_stream_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'image_stream',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_image_stream_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'image_stream',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'image_stream',
            self.image_stream_mo
        )

        return self.image_stream_mo
    
    def delete_image_stream_mo(self, namespace, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='image.openshift.io/v1', kind='ImageStream')
            success = True
            response = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_image_stream_mo', traceback.format_exc())

        self.log.ocp(
            'delete',
            'delete_image_stream',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
