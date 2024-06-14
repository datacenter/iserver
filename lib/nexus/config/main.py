from lib.nexus.config.api import ConfigApi
from lib.nexus.config.info import ConfigInfo


class Config(
        ConfigApi,
        ConfigInfo
        ):
    def __init__(self):
        ConfigApi.__init__(self)
        ConfigInfo.__init__(self)
