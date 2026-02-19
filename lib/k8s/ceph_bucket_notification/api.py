import time
import traceback


class K8sCephBucketNotificationApi():
    def __init__(self):
        self.ceph_bucket_notification_mo = None

    def get_ceph_bucket_notification_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.ceph_bucket_notification_mo is not None:
                return self.ceph_bucket_notification_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='ceph.rook.io/v1',
                kind='CephBucketNotification'
            )
            self.ceph_bucket_notification_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'ceph_bucket_notification',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_ceph_bucket_notification_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'ceph_bucket_notification',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'ceph_bucket_notification',
            self.ceph_bucket_notification_mo
        )

        return self.ceph_bucket_notification_mo

    def create_ceph_bucket_notification_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='ceph.rook.io/v1', kind='CephBucketNotification')
            success = True
            response = obj_list.create(
                body=body,
                namespace=body['metadata']['namespace'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_ceph_bucket_notification_mo', traceback.format_exc())

        self.log.ocp(
            'create',
            'ceph_bucket_notification',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def replace_ceph_bucket_notification_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='ceph.rook.io/v1', kind='CephBucketNotification')
            success = True
            response = obj_list.replace(
                body=body,
                namespace=body['metadata']['namespace'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.replace_ceph_bucket_notification_mo', traceback.format_exc())

        self.log.ocp(
            'replace',
            'ceph_bucket_notification',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def delete_ceph_bucket_notification_mo(self, namespace, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='ceph.rook.io/v1', kind='CephBucketNotification')
            success = True
            response = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_ceph_bucket_notification_mo', traceback.format_exc())

        self.log.ocp(
            'delete',
            'ceph_bucket_notification',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
