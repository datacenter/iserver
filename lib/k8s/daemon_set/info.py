import datetime
from lib import filter_helper


class K8sDaemonSetInfo():
    def __init__(self):
        self.daemon_set = None

    def get_daemon_set_info(self, daemon_set_mo):
        if daemon_set_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            daemon_set_mo
        )
        info.update(metadata_info)

        keys = [
            'currentNumberScheduled',
            'numberMisscheduled',
            'desiredNumberScheduled',
            'numberReady',
            'observedGeneration',
            'updatedNumberScheduled',
            'numberAvailable'
        ]
        for key in keys:
            info[key] = self.get(
                daemon_set_mo,
                'status:%s' % (key),
                on_error=0,
                on_none=0
            )

        info['scheduled_summary'] = '%s/%s' % (
            info['desiredNumberScheduled'],
            info['currentNumberScheduled']
        )
        if info['desiredNumberScheduled'] == info['currentNumberScheduled']:
            info['__Output']['scheduled_summary'] = 'Green'
        else:
            info['__Output']['scheduled_summary'] = 'Red'

        info['available_summary'] = '%s/%s' % (
            info['numberReady'],
            info['numberAvailable']
        )
        info['__Output']['available_summary'] = 'Red'
        if info['numberReady'] == info['numberAvailable']:
            if info['numberAvailable'] == info['desiredNumberScheduled']:
                info['__Output']['available_summary'] = 'Green'

        info['ready'] = False
        if info['desiredNumberScheduled'] > 0 and info['desiredNumberScheduled'] == info['numberAvailable']:
            info['ready'] = True

        info['node_selector'] = self.get(
            daemon_set_mo,
            'spec:template:spec:nodeSelector',
            on_error={},
            on_none={}
        )

        return info

    def get_daemon_sets_info(self, cache_enabled=True):
        if cache_enabled:
            if self.daemon_set is not None:
                return self.daemon_set

        managed_objects = self.get_daemon_set_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.daemon_set = []
        for managed_object in managed_objects:
            daemon_set_info = {}
            daemon_set_info['info'] = self.get_daemon_set_info(
                managed_object
            )
            daemon_set_info['mo'] = managed_object
            self.daemon_set.append(
                daemon_set_info
            )

        return self.daemon_set

    def match_daemon_set(self, daemon_set_info, daemon_set_filter):
        if daemon_set_filter is None or len(daemon_set_filter) == 0:
            return True

        for ap_rule in daemon_set_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, daemon_set_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_namespace_name(value, '%s/%s' % (daemon_set_info['namespace'], daemon_set_info['name'])):
                    return False

            if key == 'owner':
                key_found = True
                if not filter_helper.match_namespace_name(value, daemon_set_info['owner']):
                    return False

            if not key_found:
                self.log.error(
                    'match_daemon_set',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_daemon_sets(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_daemon_sets = self.get_daemon_sets_info(cache_enabled=cache_enabled)
        if all_daemon_sets is None:
            return None

        daemon_sets = []

        for daemon_set_info in all_daemon_sets:
            if not self.match_daemon_set(daemon_set_info['info'], object_filter):
                continue

            if return_mo:
                daemon_sets.append(
                    daemon_set_info['mo']
                )
                continue

            daemon_sets.append(
                daemon_set_info['info']
            )

        return daemon_sets

    def get_daemon_set(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        daemon_sets = self.get_daemon_sets(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if daemon_sets is None:
            return None

        if len(daemon_sets) == 1:
            return daemon_sets[0]

        return None

    def is_daemon_set(self, namespace, name, cache_enabled=True):
        if self.get_daemon_set(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True
    
    def is_daemon_set_ready(self, namespace, name, cache_enabled=True):
        ds_info = self.get_daemon_set(namespace, name, cache_enabled=cache_enabled)
        if ds_info is None:
            return False
        
        return ds_info['ready']

    def restart_daemon_set(self, namespace, name, my_output=None):
        if not self.is_daemon_set(namespace, name, cache_enabled=False):
            if my_output is not None:
                my_output.error('Daemon set [%s/%s] not found' % (namespace, name))
            return False

        now = datetime.datetime.utcnow()
        now = str(now.isoformat("T") + "Z")
        body = {
            'spec': {
                'template':{
                    'metadata': {
                        'annotations': {
                            'kubectl.kubernetes.io/restartedAt': now
                        }
                    }
                }
            }
        }

        if not self.patch_daemon_set_mo(namespace, name, body):
            if my_output is not None:
                my_output.error('Daemon set [%s/%s] patch failed' % (namespace, name))
            return False

        if my_output is not None:
            my_output.default('Daemon set [%s/%s] patch successful' % (namespace, name))

        return True

    def get_daemon_set_resources(self, namespace, name, cache_enabled=True):
        resources = {}
        resources['pod'] = []

        info = self.get_daemon_set(namespace, name, cache_enabled=cache_enabled)
        if info is None:
            return resources

        pods = self.get_pods_daemon_set(info['namespace'], info['name'], cache_enabled=cache_enabled)
        if pods is None:
            return resources

        for pod in pods:
            resources['pod'].append(
                dict(
                    namespace=pod['namespace'],
                    name=pod['name']
                )
            )

        return resources
