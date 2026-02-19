import time
import traceback


class K8sForkliftControllerApi():
    def __init__(self):
        self.forklift_controller_mo = None

    def get_forklift_controller_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.forklift_controller_mo is not None:
                return self.forklift_controller_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='forklift.konveyor.io/v1beta1',
                kind='ForkliftController'
            )
            self.forklift_controller_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'forklift_controller',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_forklift_controller_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'forklift_controller',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'forklift_controller',
            self.forklift_controller_mo
        )

        return self.forklift_controller_mo

    def create_forklift_controller_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='forklift.konveyor.io/v1beta1', kind='ForkliftController')
            success = True
            response = obj_list.create(
                body=body,
                namespace=body['metadata']['namespace'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_forklift_controller', traceback.format_exc())

        self.log.ocp(
            'create',
            'forklift_controller',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def replace_forklift_controller_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='forklift.konveyor.io/v1beta1', kind='ForkliftController')
            success = True
            response = obj_list.replace(
                body=body,
                namespace=body['metadata']['namespace'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.replace_forklift_controller_mo', traceback.format_exc())

        self.log.ocp(
            'replace',
            'forklift_controller',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
    
    def delete_forklift_controller_mo(self, namespace, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='forklift.konveyor.io/v1beta1', kind='ForkliftController')
            success = True
            response = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_forklift_controller_mo', traceback.format_exc())

        self.log.ocp(
            'delete',
            'forklift_controller',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
    