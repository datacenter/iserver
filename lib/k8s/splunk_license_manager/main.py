from lib.k8s.splunk_license_manager.api import K8sSplunkLicenseManagerApi
from lib.k8s.splunk_license_manager.info import K8sSplunkLicenseManagerInfo


class K8sSplunkLicenseManager(
        K8sSplunkLicenseManagerApi,
        K8sSplunkLicenseManagerInfo
        ):
    def __init__(self):
        K8sSplunkLicenseManagerApi.__init__(self)
        K8sSplunkLicenseManagerInfo.__init__(self)
