from lib import filter_helper


class K8sStatefulSetInfo():
    def __init__(self):
        self.stateful_set = None

    def get_stateful_set_info(self, stateful_set_mo):
        if stateful_set_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            stateful_set_mo
        )
        info.update(metadata_info)

        return info

    def get_stateful_sets_info(self, cache_enabled=True):
        if cache_enabled:
            if self.stateful_set is not None:
                return self.stateful_set

        managed_objects = self.get_stateful_set_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.stateful_set = []
        for managed_object in managed_objects:
            stateful_set_info = {}
            stateful_set_info['info'] = self.get_stateful_set_info(
                managed_object
            )
            stateful_set_info['mo'] = managed_object
            self.stateful_set.append(
                stateful_set_info
            )

        return self.stateful_set

    def match_stateful_set(self, stateful_set_info, stateful_set_filter):
        if stateful_set_filter is None or len(stateful_set_filter) == 0:
            return True

        for ap_rule in stateful_set_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, stateful_set_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_namespace_name(value, '%s/%s' % (stateful_set_info['namespace'], stateful_set_info['name'])):
                    return False

            if key == 'owner':
                key_found = True
                if not filter_helper.match_namespace_name(value, stateful_set_info['owner']):
                    return False

            if not key_found:
                self.log.error(
                    'match_stateful_set',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_stateful_sets(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_stateful_sets = self.get_stateful_sets_info(cache_enabled=cache_enabled)
        if all_stateful_sets is None:
            return None

        stateful_sets = []

        for stateful_set_info in all_stateful_sets:
            if not self.match_stateful_set(stateful_set_info['info'], object_filter):
                continue

            if return_mo:
                stateful_sets.append(
                    stateful_set_info['mo']
                )
                continue

            stateful_sets.append(
                stateful_set_info['info']
            )

        return stateful_sets
