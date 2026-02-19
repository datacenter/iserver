import time
from lib import filter_helper


class K8sOcsInitializationInfo():
    def __init__(self):
        self.ocs_initialization = None

    def get_ocs_initialization_info(self, ocs_initialization_mo):
        if ocs_initialization_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            ocs_initialization_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(ocs_initialization_mo, 'spec')
        info['status'] = self.get(ocs_initialization_mo, 'status')

        info['available'] = False
        info['upgradeable'] = False

        info['phase'] = self.get(ocs_initialization_mo, 'status:phase')
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

        conditions_mo = self.get(ocs_initialization_mo, 'status:conditions')
        if conditions_mo is not None:
            for condition_mo in conditions_mo:
                type_mo = self.get(condition_mo, 'type')
                status_mo = self.get(condition_mo, 'status')
                if type_mo == 'Available':
                    if status_mo == 'True':
                        info['available'] = True
                        info['availableTick'] = '\u2713'
                        info['__Output']['availableTick'] = 'Green'
                    else:
                        info['available'] = False
                        info['availableTick'] = '\u2717'
                        info['__Output']['availableTick'] = 'Red'

                if type_mo == 'Upgradeable':
                    if status_mo == 'True':
                        info['upgradeable'] = True
                        info['upgradeableTick'] = '\u2713'
                        info['__Output']['upgradeableTick'] = 'Green'
                    else:
                        info['upgradeable'] = False
                        info['upgradeableTick'] = '\u2717'
                        info['__Output']['upgradeableTick'] = 'Red'

        return info

    def get_ocs_initializations_info(self, cache_enabled=True):
        if cache_enabled:
            if self.ocs_initialization is not None:
                return self.ocs_initialization

        managed_objects = self.get_ocs_initialization_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.ocs_initialization = []
        for managed_object in managed_objects:
            ocs_initialization_info = {}
            ocs_initialization_info['info'] = self.get_ocs_initialization_info(
                managed_object
            )
            ocs_initialization_info['mo'] = managed_object
            self.ocs_initialization.append(
                ocs_initialization_info
            )

        return self.ocs_initialization

    def match_ocs_initialization(self, ocs_initialization_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, ocs_initialization_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, ocs_initialization_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_ocs_initialization',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_ocs_initializations(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_ocs_initializations = self.get_ocs_initializations_info(cache_enabled=cache_enabled)
        if all_ocs_initializations is None:
            return None

        ocs_initializations = []

        for ocs_initialization_info in all_ocs_initializations:
            if not self.match_ocs_initialization(ocs_initialization_info['info'], object_filter):
                continue

            if return_mo:
                ocs_initializations.append(
                    ocs_initialization_info['mo']
                )
                continue

            ocs_initializations.append(
                ocs_initialization_info['info']
            )

        return ocs_initializations

    def is_ocs_initialization(self, cache_enabled=True):
        if self.get_ocs_initialization(cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_ocs_initialization(self, return_mo=False, cache_enabled=True):
        ocs_initializations = self.get_ocs_initializations(
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if ocs_initializations is None:
            return None

        if len(ocs_initializations) == 1:
            return ocs_initializations[0]

        return None

    def delete_namespaced_ocs_initialization(self, namespace, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete odf ocs initialization', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))

        items = self.get_ocs_initializations(
            object_filter=['namespace:%s' % (namespace)]
        )
        if items is None:
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        for item in items:
            my_output.default('- %s' % (item['name']))
            success = self.delete_ocs_initialization_mo(item['namespace'], item['name'])
            if not success:
                if my_output is not None:
                    my_output.error('REST API failed')

                if wait:
                    if my_output is not None:
                        my_output.default('- wait for no ocs initialization...')

                    if not self.wait_no_ocs_initialization():
                        if my_output is not None:
                            my_output.error('Timed out')
                        return False
                    
        return True

    def wait_no_ocs_initialization(self, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.get_ocs_initialization(
                cache_enabled=False
            )
            if info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_ocs_initialization',
                    'Max time reached'
                )
                return False

            time.sleep(5)
