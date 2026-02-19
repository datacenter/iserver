from lib import filter_helper


class K8sNemoEntitystoreInfo():
    def __init__(self):
        self.nemo_entitystore = None

    def get_nemo_entitystore_info(self, managed_object):
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

    def get_nemo_entitystores_info(self, cache_enabled=True):
        if cache_enabled:
            if self.nemo_entitystore is not None:
                return self.nemo_entitystore

        managed_objects = self.get_nemo_entitystore_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.nemo_entitystore = []
        for managed_object in managed_objects:
            nemo_entitystore_info = {}
            nemo_entitystore_info['info'] = self.get_nemo_entitystore_info(
                managed_object
            )
            nemo_entitystore_info['mo'] = managed_object
            self.nemo_entitystore.append(
                nemo_entitystore_info
            )

        return self.nemo_entitystore

    def match_nemo_entitystore(self, nemo_entitystore_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, nemo_entitystore_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, nemo_entitystore_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_nemo_entitystore',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_nemo_entitystores(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_nemo_entitystores = self.get_nemo_entitystores_info(cache_enabled=cache_enabled)
        if all_nemo_entitystores is None:
            return None

        nemo_entitystores = []

        for nemo_entitystore_info in all_nemo_entitystores:
            if not self.match_nemo_entitystore(nemo_entitystore_info['info'], object_filter):
                continue

            if return_mo:
                nemo_entitystores.append(
                    nemo_entitystore_info['mo']
                )
                continue

            nemo_entitystores.append(
                nemo_entitystore_info['info']
            )

        return nemo_entitystores

    def is_nemo_entitystore(self, namespace, name, cache_enabled=True):
        if self.get_nemo_entitystore(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def is_any_nemo_entitystore(self, cache_enabled=True):
        policies = self.get_nemo_entitystores(cache_enabled=cache_enabled)
        if policies is None or len(policies) == 0:
            return False
        return True

    def get_nemo_entitystore(self, namespace, name, deployment_info=False, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        nemo_entitystores = self.get_nemo_entitystores(
            object_filter=object_filter,
            deployment_info=deployment_info,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if nemo_entitystores is None:
            return None

        if len(nemo_entitystores) == 1:
            return nemo_entitystores[0]

        return None
