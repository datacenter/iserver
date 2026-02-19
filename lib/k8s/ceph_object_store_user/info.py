from lib import filter_helper


class K8sCephObjectStoreUserInfo():
    def __init__(self):
        self.ceph_object_store_user = None

    def get_ceph_object_store_user_info(self, ceph_object_store_user_mo):
        if ceph_object_store_user_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            ceph_object_store_user_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(ceph_object_store_user_mo, 'spec')
        info['status'] = self.get(ceph_object_store_user_mo, 'status')

        info['phase'] = self.get(ceph_object_store_user_mo, 'status:phase')
        if info['phase'] is not None and info['phase'].lower() == 'ready':
            info['ready'] = True
            info['readyTick'] = '\u2713'
            info['__Output']['phase'] = 'Green'
            info['__Output']['readyTick'] = 'Green'
        else:
            info['ready'] = False
            info['readyTick'] = '\u2717'
            info['__Output']['phase'] = 'Red'
            info['__Output']['readyTick'] = 'Red'

        info['secret'] = self.get(ceph_object_store_user_mo, 'status:info:secretName')
        return info

    def get_ceph_object_store_users_info(self, cache_enabled=True):
        if cache_enabled:
            if self.ceph_object_store_user is not None:
                return self.ceph_object_store_user

        managed_objects = self.get_ceph_object_store_user_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.ceph_object_store_user = []
        for managed_object in managed_objects:
            info = {}
            info['info'] = self.get_ceph_object_store_user_info(
                managed_object
            )
            info['mo'] = managed_object
            self.ceph_object_store_user.append(
                info
            )

        return self.ceph_object_store_user

    def match_ceph_object_store_user(self, object_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, object_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_namespace_name(value, '%s/%s' % (object_info['namespace'], object_info['name'])):
                    return False

            if not key_found:
                self.log.error(
                    'match_ceph_object_store_user',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_ceph_object_store_users(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_objects_infos = self.get_ceph_object_store_users_info(cache_enabled=cache_enabled)
        if all_objects_infos is None:
            return None

        object_infos = []

        for object_info in all_objects_infos:
            if not self.match_ceph_object_store_user(object_info['info'], object_filter):
                continue

            if return_mo:
                object_infos.append(
                    object_info['mo']
                )
                continue

            object_infos.append(
                object_info['info']
            )

        return object_infos

    def is_ceph_object_store_user(self, namespace, name, cache_enabled=True):
        if self.get_ceph_object_store_user(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_ceph_object_store_user(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        objects_info = self.get_ceph_object_store_users(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if objects_info is None:
            return None

        if len(objects_info) == 1:
            return objects_info[0]

        return None
