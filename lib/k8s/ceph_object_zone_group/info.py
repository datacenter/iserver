from lib import filter_helper


class K8sCephObjectZoneGroupInfo():
    def __init__(self):
        self.ceph_object_zone_group = None

    def get_ceph_object_zone_group_info(self, ceph_object_zone_group_mo):
        if ceph_object_zone_group_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            ceph_object_zone_group_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(ceph_object_zone_group_mo, 'spec')
        info['status'] = self.get(ceph_object_zone_group_mo, 'status')
        return info

    def get_ceph_object_zone_groups_info(self, cache_enabled=True):
        if cache_enabled:
            if self.ceph_object_zone_group is not None:
                return self.ceph_object_zone_group

        managed_objects = self.get_ceph_object_zone_group_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.ceph_object_zone_group = []
        for managed_object in managed_objects:
            info = {}
            info['info'] = self.get_ceph_object_zone_group_info(
                managed_object
            )
            info['mo'] = managed_object
            self.ceph_object_zone_group.append(
                info
            )

        return self.ceph_object_zone_group

    def match_ceph_object_zone_group(self, object_info, object_filter):
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
                    'match_ceph_object_zone_group',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_ceph_object_zone_groups(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_objects_infos = self.get_ceph_object_zone_groups_info(cache_enabled=cache_enabled)
        if all_objects_infos is None:
            return None

        object_infos = []

        for object_info in all_objects_infos:
            if not self.match_ceph_object_zone_group(object_info['info'], object_filter):
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

    def is_ceph_object_zone_group(self, namespace, name, cache_enabled=True):
        if self.get_ceph_object_zone_group(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_ceph_object_zone_group(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        objects_info = self.get_ceph_object_zone_groups(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if objects_info is None:
            return None

        if len(objects_info) == 1:
            return objects_info[0]

        return None
