from lib.k8s.bfd_profile.api import K8sBfdProfileApi
from lib.k8s.bfd_profile.info import K8sBfdProfileInfo
from lib.k8s.bfd_profile.create import K8sBfdProfileCreate
from lib.k8s.bfd_profile.delete import K8sBfdProfileDelete
from lib.k8s.bfd_profile.update import K8sBfdProfileUpdate
from lib.k8s.bfd_profile.wait import K8sBfdProfileWait


class K8sBfdProfile(
        K8sBfdProfileApi,
        K8sBfdProfileInfo,
        K8sBfdProfileCreate,
        K8sBfdProfileDelete,
        K8sBfdProfileUpdate,
        K8sBfdProfileWait
        ):
    def __init__(self):
        K8sBfdProfileApi.__init__(self)
        K8sBfdProfileInfo.__init__(self)
        K8sBfdProfileCreate.__init__(self)
        K8sBfdProfileDelete.__init__(self)
        K8sBfdProfileUpdate.__init__(self)
        K8sBfdProfileWait.__init__(self)
