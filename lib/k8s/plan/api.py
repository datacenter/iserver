import time
import traceback


class K8sPlanApi():
    def __init__(self):
        self.plan_mo = None

    def get_plan_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.plan_mo is not None:
                return self.plan_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='forklift.konveyor.io/v1beta1',
                kind='Plan'
            )
            self.plan_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'plan',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_plan_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'plan',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'plan',
            self.plan_mo
        )

        return self.plan_mo

    def create_plan_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='forklift.konveyor.io/v1beta1', kind='Plan')
            success = True
            response = obj_list.create(
                body=body,
                namespace=body['metadata']['namespace'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_plan', traceback.format_exc())

        self.log.ocp(
            'create',
            'plan',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def patch_plan_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            obj_list = api_handler.resources.get(api_version='forklift.konveyor.io/v1beta1', kind='Plan')
            obj_list.patch(
                namespace=body['metadata']['namespace'],
                body=body,
                content_type='application/merge-patch+json'
            )

        except BaseException:
            self.log.error('k8s.patch_plan_mo', traceback.format_exc())
            print(traceback.format_exc())
            return False

        return True
    
    def replace_plan_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='forklift.konveyor.io/v1beta1', kind='Plan')
            success = True
            response = obj_list.replace(
                body=body,
                namespace=body['metadata']['namespace'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.replace_plan_mo', traceback.format_exc())

        self.log.ocp(
            'replace',
            'plan',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
    
    def delete_plan_mo(self, namespace, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='forklift.konveyor.io/v1beta1', kind='Plan')
            success = True
            response = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_plan_mo', traceback.format_exc())

        self.log.ocp(
            'delete',
            'plan',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
    