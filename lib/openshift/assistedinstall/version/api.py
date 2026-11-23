class AssistedInstallVersionApi():
    def __init__(self):
        self.assisted_install_openshift_version_mo = None
        self.assisted_install_component_version_mo = None

        self.assisted_install_version_api_version = 'v2'
        self.assisted_install_openshift_version_url = '%s/openshift-versions' % (
            self.assisted_install_version_api_version
        )
        self.assisted_install_component_version_url = '%s/component-versions' % (
            self.assisted_install_version_api_version
        )

    def get_assisted_install_openshift_version_mo(self, cache_enabled=True):
        if cache_enabled and self.assisted_install_openshift_version_mo is not None:
            return self.assisted_install_openshift_version_mo

        self.assisted_install_openshift_version_mo = self.get_assisted_install_mo(
            self.assisted_install_openshift_version_url
        )
        return self.assisted_install_openshift_version_mo

    def get_assisted_install_component_version_mo(self, cache_enabled=True):
        if cache_enabled and self.assisted_install_component_version_mo is not None:
            return self.assisted_install_component_version_mo

        self.assisted_install_component_version_mo = self.get_assisted_install_mo(
            self.assisted_install_component_version_url
        )
        return self.assisted_install_component_version_mo
