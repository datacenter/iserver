import time
import traceback


class K8sCephClientApi():
    def __init__(self):
        self.ceph_client_mo = None

    def get_ceph_client_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.ceph_client_mo is not None:
                return self.ceph_client_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='ceph.rook.io/v1',
                kind='CephClient'
            )
            self.ceph_client_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'ceph_client',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_ceph_client_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'ceph_client',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'ceph_client',
            self.ceph_client_mo
        )

        return self.ceph_client_mo

    def create_ceph_client_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='ceph.rook.io/v1', kind='CephClient')
            success = True
            response = obj_list.create(
                body=body,
                namespace=body['metadata']['namespace'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_ceph_client_mo', traceback.format_exc())

        self.log.ocp(
            'create',
            'ceph_client',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def replace_ceph_client_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='ceph.rook.io/v1', kind='CephClient')
            success = True
            response = obj_list.replace(
                body=body,
                namespace=body['metadata']['namespace'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.replace_ceph_client_mo', traceback.format_exc())

        self.log.ocp(
            'replace',
            'ceph_client',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def delete_ceph_client_mo(self, namespace, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='ceph.rook.io/v1', kind='CephClient')
            success = True
            response = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_ceph_client_mo', traceback.format_exc())

        self.log.ocp(
            'delete',
            'ceph_client',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
