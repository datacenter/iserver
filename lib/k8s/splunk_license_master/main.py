from lib.k8s.splunk_license_master.api import K8sSplunkLicenseMasterApi
from lib.k8s.splunk_license_master.info import K8sSplunkLicenseMasterInfo


class K8sSplunkLicenseMaster(
        K8sSplunkLicenseMasterApi,
        K8sSplunkLicenseMasterInfo
        ):
    def __init__(self):
        K8sSplunkLicenseMasterApi.__init__(self)
        K8sSplunkLicenseMasterInfo.__init__(self)
