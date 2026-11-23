from lib.k8s.splunk_monitoring_console.api import K8sSplunkMonitoringConsoleApi
from lib.k8s.splunk_monitoring_console.info import K8sSplunkMonitoringConsoleInfo


class K8sSplunkMonitoringConsole(
        K8sSplunkMonitoringConsoleApi,
        K8sSplunkMonitoringConsoleInfo
        ):
    def __init__(self):
        K8sSplunkMonitoringConsoleApi.__init__(self)
        K8sSplunkMonitoringConsoleInfo.__init__(self)
