from lib.aci.l3out.external_ip.api import L3OutExternalIpApi
from lib.aci.l3out.external_ip.info import L3OutExternalIpInfo


class L3OutExternalIp(L3OutExternalIpApi, L3OutExternalIpInfo):
    def __init__(self):
        L3OutExternalIpApi.__init__(self)
        L3OutExternalIpInfo.__init__(self)
