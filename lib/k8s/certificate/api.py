import time
import traceback


class K8sCertificateApi():
    def __init__(self):
        self.certificate_mo = None

    def get_certificate_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.certificate_mo is not None:
                return self.certificate_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='cert-manager.io/v1',
                kind='Certificate'
            )
            self.certificate_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'certificate',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_certificate_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'certificate',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'certificate',
            self.certificate_mo
        )

        return self.certificate_mo

    def create_certificate_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='cert-manager.io/v1', kind='Certificate')
            success = True
            response = obj_list.create(
                body=body,
                namespace=body['metadata']['namespace'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_certificate_mo', traceback.format_exc())

        self.log.ocp(
            'create',
            'create_certificate',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def replace_certificate_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='cert-manager.io/v1', kind='Certificate')
            success = True
            response = obj_list.replace(
                body=body,
                namespace=body['metadata']['namespace'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_certificate', traceback.format_exc())

        self.log.ocp(
            'create',
            'create_certificate',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def delete_certificate_mo(self, namespace, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='cert-manager.io/v1', kind='Certificate')
            success = True
            response = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_certificate', traceback.format_exc())

        self.log.ocp(
            'delete',
            'certificate',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
