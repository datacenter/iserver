from lib import filter_helper


class K8sCephBucketTopicInfo():
    def __init__(self):
        self.ceph_bucket_topic = None

    def get_ceph_bucket_topic_info(self, managed_object):
        return self.get_base_info(managed_object)
    
    def get_ceph_bucket_topics(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'ceph_bucket_topic', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_ceph_bucket_topic(self, namespace, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'ceph_bucket_topic', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_ceph_bucket_topic(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_ceph_bucket_topic(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def is_any_ceph_bucket_topic(self, cache_enabled=True):
        infos = self.get_ceph_bucket_topics(cache_enabled=cache_enabled)
        if infos is None or len(infos) == 0:
            return False
        return True