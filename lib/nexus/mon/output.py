from lib.nexus.mon.api.output import MonApiOutput
from lib.nexus.mon.snmp.output import MonSnmpOutput
from lib.nexus.mon.telemetry.output import MonTelemetryOutput

class MonOutput(
        MonApiOutput,
        MonSnmpOutput,
        MonTelemetryOutput
    ):
    def __init__(self):
        MonApiOutput.__init__(self)
        MonSnmpOutput.__init__(self)
        MonTelemetryOutput.__init__(self)
