from lib.nexus.pc.database.api import PcDatabaseApi
from lib.nexus.pc.database.info import PcDatabaseInfo


class PcDatabase(
        PcDatabaseApi,
        PcDatabaseInfo
        ):
    def __init__(self):
        PcDatabaseApi.__init__(self)
        PcDatabaseInfo.__init__(self)
