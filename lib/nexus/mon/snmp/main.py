from lib.nexus.mon.snmp.api import MonSnmpApi
from lib.nexus.mon.snmp.info import MonSnmpInfo


class MonSnmp(
        MonSnmpApi,
        MonSnmpInfo
        ):
    def __init__(self):
        MonSnmpApi.__init__(self)
        MonSnmpInfo.__init__(self)
