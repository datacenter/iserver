from lib.nexus.version.api import VersionApi
from lib.nexus.version.info import VersionInfo


class Version(
        VersionApi,
        VersionInfo
        ):
    def __init__(self):
        VersionApi.__init__(self)
        VersionInfo.__init__(self)
