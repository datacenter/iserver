from lib import filter_helper


class K8sCiliumConfigInfo():
    def __init__(self):
        self.cilium_config = None

    def get_cilium_config_info(self, cilium_config_mo):
        if cilium_config_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            cilium_config_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(cilium_config_mo, 'spec')
        info['status'] = self.get(cilium_config_mo, 'status')
        
        info['values_error'] = True
        info['values_error_reason'] = None
        info['values_error_message'] = None
        info['processing_error'] = True
        info['processing_error_reason'] = None
        info['processing_error_message'] = None

        conditions_mo = self.get(cilium_config_mo, 'status:conditions')
        if conditions_mo is not None:
            for condition_mo in conditions_mo:
                condition_type = self.get(condition_mo, 'type')
                if condition_type is not None:
                    if condition_type == 'ValuesError':
                        if self.get(condition_mo, 'status') == 'False':
                            info['values_error'] = False
                        if self.get(condition_mo, 'status') == 'True':
                            info['values_error_reason'] = self.get(condition_mo, 'reason')
                            info['values_error_message'] = self.get(condition_mo, 'message')

                    if condition_type == 'ProcessingError':
                        if self.get(condition_mo, 'status') == 'False':
                            info['processing_error'] = False
                        if self.get(condition_mo, 'status') == 'True':
                            info['processing_error_reason'] = self.get(condition_mo, 'reason')
                            info['processing_error_message'] = self.get(condition_mo, 'message')

        info['valid'] = not info['values_error'] and not info['processing_error']
        return info

    def get_cilium_configs_info(self, cache_enabled=True):
        if cache_enabled:
            if self.cilium_config is not None:
                return self.cilium_config

        managed_objects = self.get_cilium_config_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.cilium_config = []
        for managed_object in managed_objects:
            cilium_config_info = {}
            cilium_config_info['info'] = self.get_cilium_config_info(
                managed_object
            )
            cilium_config_info['mo'] = managed_object
            self.cilium_config.append(
                cilium_config_info
            )

        return self.cilium_config

    def match_cilium_config(self, cilium_config_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, cilium_config_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_cilium_config',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_cilium_configs(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_cilium_configs = self.get_cilium_configs_info(cache_enabled=cache_enabled)
        if all_cilium_configs is None:
            return None

        cilium_configs = []

        for cilium_config_info in all_cilium_configs:
            if not self.match_cilium_config(cilium_config_info['info'], object_filter):
                continue

            if return_mo:
                cilium_configs.append(
                    cilium_config_info['mo']
                )
                continue

            cilium_configs.append(
                cilium_config_info['info']
            )

        return cilium_configs

    def is_cilium_config(self, name=None, cache_enabled=True):
        if self.get_cilium_config(name=name, cache_enabled=cache_enabled) is None:
            return False
        
        return True

    def get_cilium_config(self, name=None, return_mo=False, cache_enabled=True):
        object_filter = []
        if name is not None:
            object_filter.append(
                'name:%s' % (name)
            )
        cilium_configs = self.get_cilium_configs(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if cilium_configs is None:
            return None

        if len(cilium_configs) == 1:
            return cilium_configs[0]

        return None
