import time
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

        keys = [
            'observedGeneration',
            'replicas',
            'updatedReplicas',
            'readyReplicas',
            'availableReplicas',
            'conditions'
        ]
        for key in keys:
            info[key] = self.get(stateful_set_mo, 'status:%s' % (key))

        info['ready'] = False
        if info['replicas'] is not None and info['readyReplicas'] is not None:
            if info['replicas'] > 0 and info['replicas'] == info['readyReplicas']:
                info['ready'] = True

        info['readyT'] = '%s/%s' % (
            info['replicas'],
            info['readyReplicas']
        )

        if info['ready']:
            info['__Output']['readyT'] = 'Green'
        else:
            info['__Output']['readyT'] = 'Red'

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

    def get_stateful_set(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        stateful_sets = self.get_stateful_sets(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if stateful_sets is None:
            return None

        if len(stateful_sets) == 1:
            return stateful_sets[0]

        return None

    def wait_stateful_set_ready_state(self, namespace, name, max_time=600, optional=False):
        start_time = int(time.time())
        while True:
            stateful_set = self.get_stateful_set(
                namespace,
                name,
                cache_enabled=False
            )
            if stateful_set is not None:
                if stateful_set['ready']:
                    return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                if optional and stateful_set is True:
                    self.log.error(
                        'k8s.wait_stateful_set_ready_state',
                        'Max time reached but stateful_set optional: %s/%s' % (namespace, name)
                    )
                    return True

                self.log.error(
                    'k8s.wait_stateful_set_ready_state',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

    def wait_stateful_sets_ready_state(self, stateful_sets, max_time=600, my_output=None, optional=False):
        if my_output is not None:
            my_output.default('Wait for stateful sets ready...')

        for stateful_set in stateful_sets:
            if my_output is not None:
                my_output.default('- %s/%s' % (stateful_set['namespace'], stateful_set['name']))

            if not self.wait_stateful_set_ready_state(stateful_set['namespace'], stateful_set['name'], max_time=max_time, optional=optional):
                if my_output is not None:
                    my_output.error('Stateful set did not reach ready state')
                return False

        return True

    def wait_no_stateful_set(self, namespace, name, max_time=600, optional=False):
        start_time = int(time.time())
        while True:
            stateful_set = self.get_stateful_set(
                namespace,
                name,
                cache_enabled=False
            )
            if stateful_set is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                if optional:
                    self.log.error(
                        'k8s.wait_no_stateful_set',
                        'Max time reached but stateful set optional: %s/%s' % (namespace, name)
                    )
                    return True

                self.log.error(
                    'k8s.wait_no_stateful_set',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

    def wait_no_stateful_sets(self, stateful_sets, max_time=600, my_output=None, optional=False):
        if my_output is not None:
            my_output.default('Wait for stateful sets deleted (optional: %s)...' % (optional))

        for stateful_set in stateful_sets:
            if my_output is not None:
                my_output.default('- %s/%s' % (stateful_set['namespace'], stateful_set['name']))

            if not self.wait_no_stateful_set(stateful_set['namespace'], stateful_set['name'], max_time=max_time, optional=optional):
                if my_output is not None:
                    my_output.error('Stateful set still there...')
                return False

        return True