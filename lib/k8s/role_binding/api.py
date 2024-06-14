import time
import traceback


class K8sRoleBindingApi():
    def __init__(self):
        self.role_binding_mo = None

    def get_role_binding_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.role_binding_mo is not None:
                return self.role_binding_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='rbac.authorization.k8s.io/v1',
                kind='RoleBinding'
            )
            self.role_binding_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'role_binding',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_role_binding_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'role_binding',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'role_binding',
            self.role_binding_mo
        )

        return self.role_binding_mo
