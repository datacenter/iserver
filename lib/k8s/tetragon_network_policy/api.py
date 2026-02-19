import time
import traceback


class K8sTetragonNetworkPolicyApi():
    def __init__(self):
        self.tetragon_network_policy_mo = None

    def get_tetragon_network_policy_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.tetragon_network_policy_mo is not None:
                return self.tetragon_network_policy_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='cilium.io/v1alpha1',
                kind='TetragonNetworkPolicy'
            )
            self.tetragon_network_policy_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'tetragon_network_policy',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_tetragon_network_policy_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'tetragon_network_policy',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'tetragon_network_policy',
            self.tetragon_network_policy_mo
        )

        return self.tetragon_network_policy_mo

    def create_tetragon_network_policy(self, tetragon_network_policy):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='cilium.io/v1alpha1', kind='TetragonNetworkPolicy')
            success = True
            response = obj_list.create(
                body=tetragon_network_policy,
                name=tetragon_network_policy['metadata']['name'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_tetragon_network_policy', traceback.format_exc())

        self.log.ocp(
            'create',
            'tetragon_network_policy',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def replace_tetragon_network_policy(self, tetragon_network_policy):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='cilium.io/v1alpha1', kind='TetragonNetworkPolicy')
            success = True
            response = obj_list.replace(
                body=tetragon_network_policy,
                name=tetragon_network_policy['metadata']['name'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.replace_tetragon_network_policy', traceback.format_exc())

        self.log.ocp(
            'replace',
            'tetragon_network_policy',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def create_tetragon_network_policy(self, tetragon_network_policy_name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='cilium.io/v1alpha1', kind='TetragonNetworkPolicy')
            success = True
            response = obj_list.delete(
                tetragon_network_policy_name
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_tetragon_network_policy', traceback.format_exc())

        self.log.ocp(
            'create',
            'tetragon_network_policy',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

