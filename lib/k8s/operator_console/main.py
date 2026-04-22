from lib.k8s.operator_console.api import K8sOperatorConsoleApi
from lib.k8s.operator_console.info import K8sOperatorConsoleInfo
from lib.k8s.operator_console.update import K8sOperatorConsoleUpdate


class K8sOperatorConsole(
        K8sOperatorConsoleApi,
        K8sOperatorConsoleInfo,
        K8sOperatorConsoleUpdate
        ):
    def __init__(self):
        K8sOperatorConsoleApi.__init__(self)
        K8sOperatorConsoleInfo.__init__(self)
        K8sOperatorConsoleUpdate.__init__(self)
