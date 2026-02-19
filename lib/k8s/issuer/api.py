import time
import traceback


class K8sIssuerApi():
    def __init__(self):
        self.issuer_mo = None

    def get_issuer_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.issuer_mo is not None:
                return self.issuer_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='cert-manager.io/v1',
                kind='Issuer'
            )
            self.issuer_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'issuer',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_issuer_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'issuer',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'issuer',
            self.issuer_mo
        )

        return self.issuer_mo

    def create_issuer_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='cert-manager.io/v1', kind='Issuer')
            success = True
            response = obj_list.create(
                body=body,
                namespace=body['metadata']['namespace'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_issuer_mo', traceback.format_exc())

        self.log.ocp(
            'create',
            'create_issuer',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def replace_issuer_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='cert-manager.io/v1', kind='Issuer')
            success = True
            response = obj_list.replace(
                body=body,
                namespace=body['metadata']['namespace'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_issuer', traceback.format_exc())

        self.log.ocp(
            'create',
            'create_issuer',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def delete_issuer_mo(self, namespace, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='cert-manager.io/v1', kind='Issuer')
            success = True
            response = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_issuer', traceback.format_exc())

        self.log.ocp(
            'delete',
            'issuer',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
