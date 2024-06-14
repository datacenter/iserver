class AssistedInstallVersionInfo():
    def __init__(self):
        self.assisted_install_openshift_version = None
        self.assisted_install_component_version = None

    def get_assisted_install_openshift_version_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            info[key] = managed_object[key]
        info['major'] = int(info['display_name'].split('.')[0])
        info['minor'] = int(info['display_name'].split('.')[1])
        info['sub'] =int(info['display_name'].split('.')[2].split('-')[0])
        return info

    def get_assisted_install_component_version_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            info[key] = managed_object[key]

        return info

    def get_assisted_install_openshift_versions_info(self, cache_enabled=True):
        if cache_enabled and self.assisted_install_openshift_version is not None:
            return self.assisted_install_openshift_version

        managed_objects = self.get_assisted_install_openshift_version_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.assisted_install_openshift_version = []
        for key in managed_objects:
            self.assisted_install_openshift_version.append(
                self.get_assisted_install_openshift_version_info(
                    managed_objects[key]
                )
            )

        self.log.openshift_mo(
            'assisted_install_openshift_version.info',
            self.assisted_install_openshift_version
        )

        self.assisted_install_openshift_version = sorted(
            self.assisted_install_openshift_version,
            key=lambda i: (
                i['major'],
                i['minor'],
                i['sub']
            ),
            reverse=True
        )

        return self.assisted_install_openshift_version

    def get_assisted_install_component_versions_info(self, cache_enabled=True):
        if cache_enabled and self.assisted_install_component_version is not None:
            return self.assisted_install_component_version

        managed_objects = self.get_assisted_install_component_version_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.assisted_install_component_version = self.get_assisted_install_component_version_info(
            managed_objects['versions']
        )
        self.assisted_install_component_version['release_tag'] = managed_objects['release_tag']

        self.log.openshift_mo(
            'assisted_install_component_version.info',
            self.assisted_install_component_version
        )

        return self.assisted_install_component_version

    def match_assisted_install_openshift_version(self, assisted_install_openshift_version_info, assisted_install_openshift_version_filter):
        if assisted_install_openshift_version_filter is None or len(assisted_install_openshift_version_filter) == 0:
            return True

        for ap_rule in assisted_install_openshift_version_filter:
            (key, value) = ap_rule.split(':')

            key_found = False

            if not key_found:
                self.log.error(
                    'match_assisted_install_openshift_version',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_assisted_install_versions(self, cache_enabled=True):
        versions = {}
        versions['openshift'] = self.get_assisted_install_openshift_versions_info(cache_enabled=cache_enabled)
        versions['component'] = self.get_assisted_install_component_versions_info(cache_enabled=cache_enabled)
        return versions

    def get_assisted_install_versions_latest(self, support_level='production', cache_enabled=True):
        versions = self.get_assisted_install_openshift_versions_info(cache_enabled=cache_enabled)
        if len(versions) == 0:
            return None

        if support_level == 'any':
            return versions[0]

        for version in versions:
            if version['support_level'] == support_level:
                return version['display_name']

        return None
