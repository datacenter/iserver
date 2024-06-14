from lib.osp.security_group.api import OspSecurityGroupApi
from lib.osp.security_group.info import OspSecurityGroupInfo


class OspSecurityGroup(
        OspSecurityGroupApi,
        OspSecurityGroupInfo
        ):
    def __init__(self):
        OspSecurityGroupApi.__init__(self)
        OspSecurityGroupInfo.__init__(self)
