from lib.nexus.mon.api.main import MonApi
from lib.nexus.mon.snmp.main import MonSnmp
from lib.nexus.mon.telemetry.main import MonTelemetry


class Mon(
        MonApi,
        MonSnmp,
        MonTelemetry
        ):
    def __init__(self):
        MonApi.__init__(self)
        MonSnmp.__init__(self)
        MonTelemetry.__init__(self)
