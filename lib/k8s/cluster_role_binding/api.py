import time
import traceback


class K8sClusterRoleBindingApi():
    def __init__(self):
        self.cluster_role_binding_mo = None

    def get_cluster_role_binding_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.cluster_role_binding_mo is not None:
                return self.cluster_role_binding_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='rbac.authorization.k8s.io/v1',
                kind='ClusterRoleBinding'
            )
            self.cluster_role_binding_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'cluster_role_binding',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_cluster_role_binding_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'cluster_role_binding',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'cluster_role_binding',
            self.cluster_role_binding_mo
        )

        return self.cluster_role_binding_mo

    def create_cluster_role_binding_mo(self, crb):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='rbac.authorization.k8s.io/v1', kind='ClusterRoleBinding')
            success = True
            response = obj_list.create(
                body=crb,
                name=crb['metadata']['name'],
            )
        except BaseException:
            success = False
            self.log.error('k8s.create_cluster_role_binding_mo', traceback.format_exc())

        self.log.k8s(
            'create',
            'cluster_role_binding',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def update_cluster_role_binding_mo(self, crb):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='rbac.authorization.k8s.io/v1', kind='ClusterRoleBinding')
            success = True
            response = obj_list.replace(
                body=crb,
                name=crb['metadata']['name'],
            )
        except BaseException:
            success = False
            self.log.error('k8s.update_cluster_role_binding_mo', traceback.format_exc())

        self.log.k8s(
            'update',
            'cluster_role_binding',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def delete_cluster_role_binding_mo(self, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='rbac.authorization.k8s.io/v1', kind='ClusterRoleBinding')
            success = True
            response = obj_list.delete(
                name
            )
        except BaseException:
            success = False
            self.log.error('k8s.update_cluster_role_binding_mo', traceback.format_exc())

        self.log.k8s(
            'delete',
            'cluster_role_binding',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
