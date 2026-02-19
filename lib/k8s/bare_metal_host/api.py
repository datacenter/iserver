import time
import traceback


class K8sBareMetalHostApi():
    def __init__(self):
        self.bare_metal_host_mo = None

    def get_bare_metal_host_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.bare_metal_host_mo is not None:
                return self.bare_metal_host_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='metal3.io/v1alpha1',
                kind='BareMetalHost'
            )
            self.bare_metal_host_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'bare_metal_host',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_bare_metal_host_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'bare_metal_host',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'bare_metal_host',
            self.bare_metal_host_mo
        )

        return self.bare_metal_host_mo

    def set_bare_metal_host_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='metal3.io/v1alpha1', kind='BareMetalHost')
            response = obj_list.replace(
                body=body
            )
            self.log.k8s(
                'set',
                'bare_metal_host',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_bare_metal_host_mo', traceback.format_exc())
            self.log.k8s(
                'set',
                'bare_metal_host',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return False

        return True
