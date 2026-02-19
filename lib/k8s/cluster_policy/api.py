import time
import traceback


class K8sClusterPolicyApi():
    def __init__(self):
        self.cluster_policy_mo = None

    def get_cluster_policy_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.cluster_policy_mo is not None:
                return self.cluster_policy_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='nvidia.com/v1',
                kind='ClusterPolicy'
            )
            self.cluster_policy_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'cluster_policy',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_cluster_policy_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'cluster_policy',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'cluster_policy',
            self.cluster_policy_mo
        )

        return self.cluster_policy_mo

    def create_cluster_policy_mo(self, policy):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='nvidia.com/v1', kind='ClusterPolicy')
            success = True
            response = obj_list.create(
                body=policy
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_cluster_policy', traceback.format_exc())

        self.log.ocp(
            'create',
            'cluster_policy',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def delete_cluster_policy_mo(self, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='nvidia.com/v1', kind='ClusterPolicy')
            success = True
            response = obj_list.delete(
                name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_cluster_policy', traceback.format_exc())

        self.log.ocp(
            'delete',
            'cluster_policy',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
