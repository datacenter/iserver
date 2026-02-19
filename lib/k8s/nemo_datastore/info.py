from lib import filter_helper


class K8sNemoDatastoreInfo():
    def __init__(self):
        self.nemo_datastore = None

    def get_nemo_datastore_info(self, managed_object):
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

    def get_nemo_datastores_info(self, cache_enabled=True):
        if cache_enabled:
            if self.nemo_datastore is not None:
                return self.nemo_datastore

        managed_objects = self.get_nemo_datastore_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.nemo_datastore = []
        for managed_object in managed_objects:
            nemo_datastore_info = {}
            nemo_datastore_info['info'] = self.get_nemo_datastore_info(
                managed_object
            )
            nemo_datastore_info['mo'] = managed_object
            self.nemo_datastore.append(
                nemo_datastore_info
            )

        return self.nemo_datastore

    def match_nemo_datastore(self, nemo_datastore_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, nemo_datastore_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, nemo_datastore_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_nemo_datastore',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_nemo_datastores(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_nemo_datastores = self.get_nemo_datastores_info(cache_enabled=cache_enabled)
        if all_nemo_datastores is None:
            return None

        nemo_datastores = []

        for nemo_datastore_info in all_nemo_datastores:
            if not self.match_nemo_datastore(nemo_datastore_info['info'], object_filter):
                continue

            if return_mo:
                nemo_datastores.append(
                    nemo_datastore_info['mo']
                )
                continue

            nemo_datastores.append(
                nemo_datastore_info['info']
            )

        return nemo_datastores

    def is_nemo_datastore(self, namespace, name, cache_enabled=True):
        if self.get_nemo_datastore(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def is_any_nemo_datastore(self, cache_enabled=True):
        policies = self.get_nemo_datastores(cache_enabled=cache_enabled)
        if policies is None or len(policies) == 0:
            return False
        return True

    def get_nemo_datastore(self, namespace, name, deployment_info=False, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        nemo_datastores = self.get_nemo_datastores(
            object_filter=object_filter,
            deployment_info=deployment_info,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if nemo_datastores is None:
            return None

        if len(nemo_datastores) == 1:
            return nemo_datastores[0]

        return None
