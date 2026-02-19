import time
import traceback


class K8sIdentityApi():
    def __init__(self):
        self.identity_mo = None

    def get_identity_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.identity_mo is not None:
                return self.identity_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='user.openshift.io/v1',
                kind='Identity'
            )
            self.identity_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'identity',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_identity_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'identity',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'identity',
            self.identity_mo
        )

        return self.identity_mo

    def delete_identity_mo(self, identity_name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='user.openshift.io/v1', kind='Identity')
            success = True
            response = obj_list.delete(
                name=identity_name,
            )
        except BaseException:
            success = False
            self.log.error('k8s.update_identity_mo', traceback.format_exc())

        self.log.k8s(
            'update',
            'identity',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
