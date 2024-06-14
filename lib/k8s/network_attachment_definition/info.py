import json

from lib import filter_helper


class K8sNetworkAttachmentDefinitionInfo():
    def __init__(self):
        self.nad = None

    def get_nad_info(self, nad_mo):
        if nad_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            nad_mo
        )
        info.update(metadata_info)

        info['resource_name'] = self.get(nad_mo, 'metadata:annotations:k8s.v1.cni.cncf.io/resourceName')
        info['config'] = json.loads(
            self.get(nad_mo, 'spec:config')
        )

        return info

    def get_nads_info(self, cache_enabled=True):
        if cache_enabled:
            if self.nad is not None:
                return self.nad

        managed_objects = self.get_nad_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.nad = []
        for managed_object in managed_objects:
            nad_info = {}
            nad_info['info'] = self.get_nad_info(
                managed_object
            )
            nad_info['mo'] = managed_object
            self.nad.append(
                nad_info
            )

        return self.nad

    def match_nad(self, nad_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, nad_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_namespace_name(value, '%s/%s' % (nad_info['namespace'], nad_info['name'])):
                    return False

            if key == 'resource':
                key_found = True
                if not filter_helper.match_string(value, nad_info['resource_name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_nad',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_nads(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_nads = self.get_nads_info(cache_enabled=cache_enabled)
        if all_nads is None:
            return None

        nads = []

        for nad_info in all_nads:
            if not self.match_nad(nad_info['info'], object_filter):
                continue

            if return_mo:
                nads.append(
                    nad_info['mo']
                )
                continue

            nads.append(
                nad_info['info']
            )

        return nads

    def is_nad(self, namespace, name, cache_enabled=True):
        if self.get_nad(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_nad(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        nads = self.get_nads(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if nads is None:
            return None

        if len(nads) == 1:
            return nads[0]

        return None

    def get_nad_with_resource_name(self, resource_name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'resource:%s' % (resource_name)
        )
        nads = self.get_nads(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if nads is None:
            return None

        if len(nads) == 1:
            return nads[0]

        return None
