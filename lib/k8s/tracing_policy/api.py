import time
import traceback


class K8sTracingPolicyApi():
    def __init__(self):
        self.tracing_policy_mo = None

    def get_tracing_policy_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.tracing_policy_mo is not None:
                return self.tracing_policy_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='cilium.io/v1alpha1',
                kind='TracingPolicy'
            )
            self.tracing_policy_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'tracing_policy',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_tracing_policy_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'tracing_policy',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'tracing_policy',
            self.tracing_policy_mo
        )

        return self.tracing_policy_mo

    def create_tracing_policy_mo(self, tracing_policy):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='cilium.io/v1alpha1', kind='TracingPolicy')
            success = True
            response = obj_list.create(
                body=tracing_policy,
                name=tracing_policy['metadata']['name'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_tracing_policy', traceback.format_exc())

        self.log.ocp(
            'create',
            'tracing_policy',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def replace_tracing_policy_mo(self, tracing_policy):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='cilium.io/v1alpha1', kind='TracingPolicy')
            success = True
            response = obj_list.replace(
                body=tracing_policy,
                name=tracing_policy['metadata']['name'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.replace_tracing_policy', traceback.format_exc())

        self.log.ocp(
            'replace',
            'tracing_policy',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def delete_tracing_policy_mo(self, tracing_policy_name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='cilium.io/v1alpha1', kind='TracingPolicy')
            success = True
            response = obj_list.delete(
                tracing_policy_name
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_tracing_policy', traceback.format_exc())

        self.log.ocp(
            'create',
            'tracing_policy',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
