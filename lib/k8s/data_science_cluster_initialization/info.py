from lib import filter_helper


class K8sDataScienceClusterInitializationInfo():
    def __init__(self):
        self.data_science_cluster_initialization = None

    def get_data_science_cluster_initialization_info(self, managed_object):
        if managed_object is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            managed_object
        )
        info.update(metadata_info)

        info['spec'] = self.get(managed_object, 'spec')
        info['status'] = self.get(managed_object, 'status')

        info['phase'] = self.get(managed_object, 'status:phase')
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

        info['conditions'] = self.get_conditions(
            self.get(managed_object, 'status:conditions')
        )

        info['release_name'] = self.get(managed_object, 'status:release:name')
        info['release_version'] = self.get(managed_object, 'status:release:version')
        info['release'] = None
        if info['release_name'] is not None and info['release_version'] is not None:
            info['release'] = '%s v%s' % (
                info['release_name'],
                info['release_version']
            )
            
        return info

    def get_data_science_cluster_initializations_info(self, cache_enabled=True):
        if cache_enabled:
            if self.data_science_cluster_initialization is not None:
                return self.data_science_cluster_initialization

        managed_objects = self.get_data_science_cluster_initialization_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.data_science_cluster_initialization = []
        for managed_object in managed_objects:
            data_science_cluster_initialization_info = {}
            data_science_cluster_initialization_info['info'] = self.get_data_science_cluster_initialization_info(
                managed_object
            )
            data_science_cluster_initialization_info['mo'] = managed_object
            self.data_science_cluster_initialization.append(
                data_science_cluster_initialization_info
            )

        return self.data_science_cluster_initialization

    def match_data_science_cluster_initialization(self, data_science_cluster_initialization_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, data_science_cluster_initialization_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_data_science_cluster_initialization',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_data_science_cluster_initializations(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_data_science_cluster_initializations = self.get_data_science_cluster_initializations_info(cache_enabled=cache_enabled)
        if all_data_science_cluster_initializations is None:
            return None

        data_science_cluster_initializations = []

        for data_science_cluster_initialization_info in all_data_science_cluster_initializations:
            if not self.match_data_science_cluster_initialization(data_science_cluster_initialization_info['info'], object_filter):
                continue

            if return_mo:
                data_science_cluster_initializations.append(
                    data_science_cluster_initialization_info['mo']
                )
                continue

            data_science_cluster_initializations.append(
                data_science_cluster_initialization_info['info']
            )

        return data_science_cluster_initializations

    def is_data_science_cluster_initialization(self, name, cache_enabled=True):
        if self.get_data_science_cluster_initialization(name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def is_any_data_science_cluster_initialization(self, cache_enabled=True):
        policies = self.get_data_science_cluster_initializations(cache_enabled=cache_enabled)
        if policies is None or len(policies) == 0:
            return False
        return True

    def get_data_science_cluster_initialization(self, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'name:%s' % (name)
        )
        data_science_cluster_initializations = self.get_data_science_cluster_initializations(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if data_science_cluster_initializations is None:
            return None

        if len(data_science_cluster_initializations) == 1:
            return data_science_cluster_initializations[0]

        return None
