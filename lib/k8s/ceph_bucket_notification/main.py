from lib.k8s.ceph_bucket_notification.api import K8sCephBucketNotificationApi
from lib.k8s.ceph_bucket_notification.info import K8sCephBucketNotificationInfo


class K8sCephBucketNotification(
        K8sCephBucketNotificationApi,
        K8sCephBucketNotificationInfo
        ):
    def __init__(self):
        K8sCephBucketNotificationApi.__init__(self)
        K8sCephBucketNotificationInfo.__init__(self)
