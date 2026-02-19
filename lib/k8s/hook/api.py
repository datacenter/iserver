import time
import traceback


class K8sHookApi():
    def __init__(self):
        self.hook_mo = None

    def get_hook_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.hook_mo is not None:
                return self.hook_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='forklift.konveyor.io/v1beta1',
                kind='Hook'
            )
            self.hook_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'hook',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_hook_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'hook',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'hook',
            self.hook_mo
        )

        return self.hook_mo

    def create_hook_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='forklift.konveyor.io/v1beta1', kind='Hook')
            success = True
            response = obj_list.create(
                body=body,
                namespace=body['metadata']['namespace'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_hook', traceback.format_exc())

        self.log.ocp(
            'create',
            'hook',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def replace_hook_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='forklift.konveyor.io/v1beta1', kind='Hook')
            success = True
            response = obj_list.replace(
                body=body,
                namespace=body['metadata']['namespace'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.replace_hook_mo', traceback.format_exc())

        self.log.ocp(
            'replace',
            'hook',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
    
    def delete_hook_mo(self, namespace, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='forklift.konveyor.io/v1beta1', kind='Hook')
            success = True
            response = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_hook_mo', traceback.format_exc())

        self.log.ocp(
            'delete',
            'hook',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
    