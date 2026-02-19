from lib import filter_helper


class K8sNemoCustomizerInfo():
    def __init__(self):
        self.nemo_customizer = None

    def get_nemo_customizer_info(self, managed_object):
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
        return info

    def get_nemo_customizers_info(self, cache_enabled=True):
        if cache_enabled:
            if self.nemo_customizer is not None:
                return self.nemo_customizer

        managed_objects = self.get_nemo_customizer_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.nemo_customizer = []
        for managed_object in managed_objects:
            nemo_customizer_info = {}
            nemo_customizer_info['info'] = self.get_nemo_customizer_info(
                managed_object
            )
            nemo_customizer_info['mo'] = managed_object
            self.nemo_customizer.append(
                nemo_customizer_info
            )

        return self.nemo_customizer

    def match_nemo_customizer(self, nemo_customizer_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, nemo_customizer_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, nemo_customizer_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_nemo_customizer',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_nemo_customizers(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_nemo_customizers = self.get_nemo_customizers_info(cache_enabled=cache_enabled)
        if all_nemo_customizers is None:
            return None

        nemo_customizers = []

        for nemo_customizer_info in all_nemo_customizers:
            if not self.match_nemo_customizer(nemo_customizer_info['info'], object_filter):
                continue

            if return_mo:
                nemo_customizers.append(
                    nemo_customizer_info['mo']
                )
                continue

            nemo_customizers.append(
                nemo_customizer_info['info']
            )

        return nemo_customizers

    def is_nemo_customizer(self, namespace, name, cache_enabled=True):
        if self.get_nemo_customizer(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def is_any_nemo_customizer(self, cache_enabled=True):
        policies = self.get_nemo_customizers(cache_enabled=cache_enabled)
        if policies is None or len(policies) == 0:
            return False
        return True

    def get_nemo_customizer(self, namespace, name, deployment_info=False, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        nemo_customizers = self.get_nemo_customizers(
            object_filter=object_filter,
            deployment_info=deployment_info,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if nemo_customizers is None:
            return None

        if len(nemo_customizers) == 1:
            return nemo_customizers[0]

        return None
