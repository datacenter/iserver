from lib.nexus.mon.telemetry.api import MonTelemetryApi
from lib.nexus.mon.telemetry.info import MonTelemetryInfo


class MonTelemetry(
        MonTelemetryApi,
        MonTelemetryInfo
        ):
    def __init__(self):
        MonTelemetryApi.__init__(self)
        MonTelemetryInfo.__init__(self)
