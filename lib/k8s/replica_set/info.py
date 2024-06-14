from lib import filter_helper


class K8sReplicaSetInfo():
    def __init__(self):
        self.replica_set = None

    def get_replica_set_info(self, replica_set_mo):
        if replica_set_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            replica_set_mo
        )
        info.update(metadata_info)

        keys = [
            'fullyLabeledReplicas',
            'replicas',
            'readyReplicas',
            'availableReplicas',
            'observedGeneration'
        ]
        for key in keys:
            info[key] = self.get(replica_set_mo, 'status:%s' % (key))

        if info['replicas'] is not None and info['replicas'] == 0:
            if info['availableReplicas'] is None:
                info['availableReplicas'] = 0
            if info['readyReplicas'] is None:
                info['readyReplicas'] = 0

        return info

    def get_replica_sets_info(self, cache_enabled=True):
        if cache_enabled:
            if self.replica_set is not None:
                return self.replica_set

        managed_objects = self.get_replica_set_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.replica_set = []
        for managed_object in managed_objects:
            replica_set_info = {}
            replica_set_info['info'] = self.get_replica_set_info(
                managed_object
            )
            replica_set_info['mo'] = managed_object
            self.replica_set.append(
                replica_set_info
            )

        return self.replica_set

    def match_replica_set(self, replica_set_info, replica_set_filter):
        if replica_set_filter is None or len(replica_set_filter) == 0:
            return True

        for ap_rule in replica_set_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, replica_set_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_namespace_name(value, '%s/%s' % (replica_set_info['namespace'], replica_set_info['name'])):
                    return False

            if key == 'owner':
                key_found = True
                if not filter_helper.match_namespace_name(value, replica_set_info['owner']):
                    return False

            if not key_found:
                self.log.error(
                    'match_replica_set',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_replica_sets(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_replica_sets = self.get_replica_sets_info(cache_enabled=cache_enabled)
        if all_replica_sets is None:
            return None

        replica_sets = []

        for replica_set_info in all_replica_sets:
            if not self.match_replica_set(replica_set_info['info'], object_filter):
                continue

            if return_mo:
                replica_sets.append(
                    replica_set_info['mo']
                )
                continue

            replica_sets.append(
                replica_set_info['info']
            )

        return replica_sets
