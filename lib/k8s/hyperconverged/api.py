import time
import traceback


class K8sHyperConvergedApi():
    def __init__(self):
        self.hyperconverged_mo = None

    def get_hyperconverged_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.hyperconverged_mo is not None:
                return self.hyperconverged_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='hco.kubevirt.io/v1beta1',
                kind='HyperConverged'
            )
            self.hyperconverged_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'hyperconverged',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_hyperconverged_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'hyperconverged',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'hyperconverged',
            self.hyperconverged_mo
        )

        return self.hyperconverged_mo

    def create_hyperconverged_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='hco.kubevirt.io/v1beta1', kind='HyperConverged')
            success = True
            response = obj_list.create(
                body=body
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_hyperconverged', traceback.format_exc())

        self.log.ocp(
            'create',
            'hyperconverged',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def patch_hyperconverged_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            obj_list = api_handler.resources.get(api_version='hco.kubevirt.io/v1beta1', kind='HyperConverged')
            obj_list.patch(
                namespace=body['metadata']['namespace'],
                body=body,
                content_type='application/merge-patch+json'
            )

        except BaseException:
            self.log.error('k8s.patch_hyperconverged_mo', traceback.format_exc())
            print(traceback.format_exc())
            return False

        return True
    
    def delete_hyperconverged_mo(self, namespace, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='hco.kubevirt.io/v1beta1', kind='HyperConverged')
            success = True
            response = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_hyperconverged', traceback.format_exc())

        self.log.ocp(
            'delete',
            'hyperconverged',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
