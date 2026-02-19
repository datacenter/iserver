from lib.aci.profile.leaf.interface.api import ProfileLeafInterfaceApi
from lib.aci.profile.leaf.interface.info import ProfileLeafInterfaceInfo


class ProfileLeafInterface(
        ProfileLeafInterfaceApi,
        ProfileLeafInterfaceInfo
        ):
    def __init__(self):
        ProfileLeafInterfaceApi.__init__(self)
        ProfileLeafInterfaceInfo.__init__(self)
