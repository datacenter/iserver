import time
import traceback


class K8sSandboxPolicyApi():
    def __init__(self):
        self.sandbox_policy_mo = None

    def get_sandbox_policy_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.sandbox_policy_mo is not None:
                return self.sandbox_policy_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='cilium.io/v1alpha1',
                kind='SandboxPolicy'
            )
            self.sandbox_policy_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'sandbox_policy',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_sandbox_policy_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'sandbox_policy',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'sandbox_policy',
            self.sandbox_policy_mo
        )

        return self.sandbox_policy_mo

    def create_sandbox_policy_mo(self, sandbox_policy):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='cilium.io/v1alpha1', kind='SandboxPolicy')
            success = True
            response = obj_list.create(
                body=sandbox_policy,
                name=sandbox_policy['metadata']['name'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_sandbox_policy', traceback.format_exc())

        self.log.ocp(
            'create',
            'sandbox_policy',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def replace_sandbox_policy_mo(self, sandbox_policy):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='cilium.io/v1alpha1', kind='SandboxPolicy')
            success = True
            response = obj_list.replace(
                body=sandbox_policy,
                name=sandbox_policy['metadata']['name'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.replace_sandbox_policy', traceback.format_exc())

        self.log.ocp(
            'replace',
            'sandbox_policy',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def delete_sandbox_policy(self, sandbox_policy_name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='cilium.io/v1alpha1', kind='SandboxPolicy')
            success = True
            response = obj_list.delete(
                sandbox_policy_name
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_sandbox_policy', traceback.format_exc())

        self.log.ocp(
            'create',
            'sandbox_policy',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
