import time
import traceback


class K8sPolicyBindingApi():
    def __init__(self):
        self.policy_binding_mo = None

    def get_policy_binding_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.policy_binding_mo is not None:
                return self.policy_binding_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='sts.min.io/v1beta1',
                kind='PolicyBinding'
            )
            self.policy_binding_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'policy_binding',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_policy_binding_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'policy_binding',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'policy_binding',
            self.policy_binding_mo
        )

        return self.policy_binding_mo

    def create_policy_binding_mo(self, policy_binding):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='sts.min.io/v1beta1', kind='PolicyBinding')
            success = True
            response = obj_list.create(
                body=policy_binding,
                namespace=policy_binding['metadata']['namespace']
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_policy_binding_mo', traceback.format_exc())

        self.log.ocp(
            'create',
            'policy_binding',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def delete_policy_binding_mo(self, namespace, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='sts.min.io/v1beta1', kind='PolicyBinding')
            success = True
            response = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_policy_binding_mo', traceback.format_exc())

        self.log.ocp(
            'delete',
            'delete_policy_binding',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
