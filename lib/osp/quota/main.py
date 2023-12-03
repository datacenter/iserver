from lib.osp.quota.api import OspQuotaApi
from lib.osp.quota.info import OspQuotaInfo


class OspQuota(
        OspQuotaApi,
        OspQuotaInfo
        ):
    def __init__(self):
        OspQuotaApi.__init__(self)
        OspQuotaInfo.__init__(self)
