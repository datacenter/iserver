from lib.k8s.ceph_bucket_topic.api import K8sCephBucketTopicApi
from lib.k8s.ceph_bucket_topic.info import K8sCephBucketTopicInfo


class K8sCephBucketTopic(
        K8sCephBucketTopicApi,
        K8sCephBucketTopicInfo
        ):
    def __init__(self):
        K8sCephBucketTopicApi.__init__(self)
        K8sCephBucketTopicInfo.__init__(self)
