import time
import traceback


class K8sUserApi():
    def __init__(self):
        self.user_mo = None

    def get_user_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.user_mo is not None:
                return self.user_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='user.openshift.io/v1',
                kind='User'
            )
            self.user_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'user',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_user_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'user',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'user',
            self.user_mo
        )

        return self.user_mo

    def delete_user_mo(self, user_mo, include_identity=False):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='user.openshift.io/v1', kind='User')
            success = True
            response = obj_list.delete(
                name=user_mo['metadata']['name'],
            )
        except BaseException:
            success = False
            self.log.error('k8s.update_user_mo', traceback.format_exc())

        self.log.k8s(
            'update',
            'user',
            success,
            int(time.time() * 1000) - start_time
        )

        if include_identity:
            if 'identities' in user_mo:
                for identity in user_mo['identities']:
                    if not self.delete_identity_mo(identity):
                        success = False

        return success
