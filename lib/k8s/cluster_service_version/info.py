from lib import filter_helper


class K8sClusterServiceVersionInfo():
    def __init__(self):
        self.cluster_service_version = None

    def get_cluster_service_version_info(self, cluster_service_version_mo):
        if cluster_service_version_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            cluster_service_version_mo
        )
        info.update(metadata_info)

        info['phase'] = self.get(cluster_service_version_mo, 'status:phase')
        if info['phase'] is not None and info['phase'] == 'Succeeded':
            info['__Output']['phase'] = 'Green'
        else:
            info['__Output']['phase'] = 'Red'

        info['display_name'] = self.get(cluster_service_version_mo, 'spec:displayName')
        info['provider_name'] = self.get(cluster_service_version_mo, 'spec:provider:name')
        info['maturity'] = self.get(cluster_service_version_mo, 'spec:maturity')
        info['maturityT'] = info['maturity']
        if info['maturityT'] is None:
            info['maturityT'] = '--'
        info['replaces'] = self.get(cluster_service_version_mo, 'spec:replaces')
        info['version'] = self.get(cluster_service_version_mo, 'spec:version')

        return info

    def get_cluster_service_versions_info(self, cache_enabled=True):
        if cache_enabled:
            if self.cluster_service_version is not None:
                return self.cluster_service_version

        managed_objects = self.get_cluster_service_version_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.cluster_service_version = []
        for managed_object in managed_objects:
            cluster_service_version_info = {}
            cluster_service_version_info['info'] = self.get_cluster_service_version_info(
                managed_object
            )
            cluster_service_version_info['mo'] = managed_object
            self.cluster_service_version.append(
                cluster_service_version_info
            )

        return self.cluster_service_version

    def match_cluster_service_version(self, cluster_service_version_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, cluster_service_version_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_namespace_name(value, '%s/%s' % (cluster_service_version_info['namespace'], cluster_service_version_info['name'])):
                    return False

            if not key_found:
                self.log.error(
                    'match_cluster_service_version',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_cluster_service_versions(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_cluster_service_versions = self.get_cluster_service_versions_info(cache_enabled=cache_enabled)
        if all_cluster_service_versions is None:
            return None

        cluster_service_versions = []

        for cluster_service_version_info in all_cluster_service_versions:
            if not self.match_cluster_service_version(cluster_service_version_info['info'], object_filter):
                continue

            if return_mo:
                cluster_service_versions.append(
                    cluster_service_version_info['mo']
                )
                continue

            cluster_service_versions.append(
                cluster_service_version_info['info']
            )

        return cluster_service_versions

    def is_cluster_service_version(self, namespace, name, cache_enabled=True):
        if self.get_cluster_service_version(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_cluster_service_version(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        cluster_service_versions = self.get_cluster_service_versions(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if cluster_service_versions is None:
            return None

        if len(cluster_service_versions) == 1:
            return cluster_service_versions[0]

        return None
