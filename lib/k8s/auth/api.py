import time
import traceback


class K8sAuthApi():
    def __init__(self):
        self.auth_mo = None

    def get_auth_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.auth_mo is not None:
                return self.auth_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='services.platform.opendatahub.io/v1alpha1',
                kind='Auth'
            )
            self.auth_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'auth',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_auth_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'auth',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'auth',
            self.auth_mo
        )

        return self.auth_mo

    def delete_auth_mo(self, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='services.platform.opendatahub.io/v1alpha1', kind='Auth')
            success = True
            response = obj_list.delete(
                name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_auth_mo', traceback.format_exc())

        self.log.ocp(
            'delete',
            'auth',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
