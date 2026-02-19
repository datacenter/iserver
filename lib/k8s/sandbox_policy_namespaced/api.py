import time
import traceback


class K8sSandboxPolicyNamespacedApi():
    def __init__(self):
        self.sandbox_policy_namespaced_mo = None

    def get_sandbox_policy_namespaced_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.sandbox_policy_namespaced_mo is not None:
                return self.sandbox_policy_namespaced_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='cilium.io/v1alpha1',
                kind='SandboxPolicyNamespaced'
            )
            self.sandbox_policy_namespaced_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'sandbox_policy_namespaced',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_sandbox_policy_namespaced_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'sandbox_policy_namespaced',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'sandbox_policy_namespaced',
            self.sandbox_policy_namespaced_mo
        )

        return self.sandbox_policy_namespaced_mo

    def create_sandbox_policy_namespaced_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='cilium.io/v1alpha1', kind='SandboxPolicyNamespaced')
            success = True
            response = obj_list.create(
                body=body,
                namespace=body['metadata']['namespace'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_sandbox_policy_namespaced', traceback.format_exc())

        self.log.ocp(
            'create',
            'sandbox_policy_namespaced',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def replace_sandbox_policy_namespaced_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='cilium.io/v1alpha1', kind='SandboxPolicyNamespaced')
            success = True
            response = obj_list.replace(
                body=body,
                namespace=body['metadata']['namespace'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.replace_sandbox_policy_namespaced', traceback.format_exc())

        self.log.ocp(
            'replace',
            'sandbox_policy_namespaced',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def delete_sandbox_policy_namespaced(self, namespace, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='cilium.io/v1alpha1', kind='SandboxPolicyNamespaced')
            success = True
            response = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_sandbox_policy_namespaced', traceback.format_exc())

        self.log.ocp(
            'create',
            'sandbox_policy_namespaced',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
