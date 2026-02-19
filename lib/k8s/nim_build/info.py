from lib import filter_helper


class K8sNimBuildInfo():
    def __init__(self):
        self.nim_build = None

    def get_nim_build_info(self, managed_object):
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

    def get_nim_builds_info(self, cache_enabled=True):
        if cache_enabled:
            if self.nim_build is not None:
                return self.nim_build

        managed_objects = self.get_nim_build_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.nim_build = []
        for managed_object in managed_objects:
            nim_build_info = {}
            nim_build_info['info'] = self.get_nim_build_info(
                managed_object
            )
            nim_build_info['mo'] = managed_object
            self.nim_build.append(
                nim_build_info
            )

        return self.nim_build

    def match_nim_build(self, nim_build_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, nim_build_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, nim_build_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_nim_build',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_nim_builds(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_nim_builds = self.get_nim_builds_info(cache_enabled=cache_enabled)
        if all_nim_builds is None:
            return None

        nim_builds = []

        for nim_build_info in all_nim_builds:
            if not self.match_nim_build(nim_build_info['info'], object_filter):
                continue

            if return_mo:
                nim_builds.append(
                    nim_build_info['mo']
                )
                continue

            nim_builds.append(
                nim_build_info['info']
            )

        return nim_builds

    def is_nim_build(self, namespace, name, cache_enabled=True):
        if self.get_nim_build(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def is_any_nim_build(self, cache_enabled=True):
        policies = self.get_nim_builds(cache_enabled=cache_enabled)
        if policies is None or len(policies) == 0:
            return False
        return True

    def get_nim_build(self, namespace, name, deployment_info=False, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        nim_builds = self.get_nim_builds(
            object_filter=object_filter,
            deployment_info=deployment_info,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if nim_builds is None:
            return None

        if len(nim_builds) == 1:
            return nim_builds[0]

        return None
