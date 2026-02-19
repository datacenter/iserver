from lib import filter_helper


class K8sNimServiceInfo():
    def __init__(self):
        self.nim_service = None

    def get_nim_service_info(self, managed_object):
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

    def get_nim_services_info(self, cache_enabled=True):
        if cache_enabled:
            if self.nim_service is not None:
                return self.nim_service

        managed_objects = self.get_nim_service_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.nim_service = []
        for managed_object in managed_objects:
            nim_service_info = {}
            nim_service_info['info'] = self.get_nim_service_info(
                managed_object
            )
            nim_service_info['mo'] = managed_object
            self.nim_service.append(
                nim_service_info
            )

        return self.nim_service

    def match_nim_service(self, nim_service_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, nim_service_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, nim_service_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_nim_service',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_nim_services(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_nim_services = self.get_nim_services_info(cache_enabled=cache_enabled)
        if all_nim_services is None:
            return None

        nim_services = []

        for nim_service_info in all_nim_services:
            if not self.match_nim_service(nim_service_info['info'], object_filter):
                continue

            if return_mo:
                nim_services.append(
                    nim_service_info['mo']
                )
                continue

            nim_services.append(
                nim_service_info['info']
            )

        return nim_services

    def is_nim_service(self, namespace, name, cache_enabled=True):
        if self.get_nim_service(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def is_any_nim_service(self, cache_enabled=True):
        policies = self.get_nim_services(cache_enabled=cache_enabled)
        if policies is None or len(policies) == 0:
            return False
        return True

    def get_nim_service(self, namespace, name, deployment_info=False, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        nim_services = self.get_nim_services(
            object_filter=object_filter,
            deployment_info=deployment_info,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if nim_services is None:
            return None

        if len(nim_services) == 1:
            return nim_services[0]

        return None
