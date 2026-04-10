from lib.k8s.community.api import K8sCommunityApi
from lib.k8s.community.info import K8sCommunityInfo
from lib.k8s.community.create import K8sCommunityCreate
from lib.k8s.community.delete import K8sCommunityDelete
from lib.k8s.community.update import K8sCommunityUpdate
from lib.k8s.community.wait import K8sCommunityWait


class K8sCommunity(
        K8sCommunityApi,
        K8sCommunityInfo,
        K8sCommunityCreate,
        K8sCommunityDelete,
        K8sCommunityUpdate,
        K8sCommunityWait
        ):
    def __init__(self):
        K8sCommunityApi.__init__(self)
        K8sCommunityInfo.__init__(self)
        K8sCommunityCreate.__init__(self)
        K8sCommunityDelete.__init__(self)
        K8sCommunityUpdate.__init__(self)
        K8sCommunityWait.__init__(self)
