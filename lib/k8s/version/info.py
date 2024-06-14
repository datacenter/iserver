import json
from lib import filter_helper


class K8sVersionInfo():
    def __init__(self):
        self.version = None

    def get_version_info(self, version_mo):
        if version_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        info['version'] = self.get(version_mo, 'k8s:git_version')
        info['build_date'] = self.get(version_mo, 'k8s:build_date')
        info['platform'] = self.get(version_mo, 'k8s:platform')
        info['ocp'] = self.get(version_mo, 'ocp:status:desired:version', on_error='--', on_none='--')

        return info

    def get_versions_info(self, cache_enabled=True):
        if cache_enabled:
            if self.version is not None:
                return self.version

        managed_objects = self.get_version_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.version = []
        for managed_object in managed_objects:
            version_info = {}
            version_info['info'] = self.get_version_info(
                managed_object
            )
            version_info['mo'] = managed_object
            self.version.append(
                version_info
            )

        return self.version

    def match_version(self, version_info, version_filter):
        if version_filter is None or len(version_filter) == 0:
            return True

        for ap_rule in version_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if not key_found:
                self.log.error(
                    'match_version',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_versions(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_versions = self.get_versions_info(cache_enabled=cache_enabled)
        if all_versions is None:
            return None

        versions = []

        for version_info in all_versions:
            if not self.match_version(version_info['info'], object_filter):
                continue

            if return_mo:
                versions.append(
                    version_info['mo']
                )
                continue

            versions.append(
                version_info['info']
            )

        return versions

    def get_version(self):
        versions = self.get_versions()
        if versions is None or len(versions) != 1:
            return None
        return versions[0]
