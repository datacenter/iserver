from lib.k8s.trident_orchestrator.api import K8sTridentOrchestratorApi
from lib.k8s.trident_orchestrator.info import K8sTridentOrchestratorInfo
from lib.k8s.trident_orchestrator.create import K8sTridentOrchestratorCreate
from lib.k8s.trident_orchestrator.delete import K8sTridentOrchestratorDelete
from lib.k8s.trident_orchestrator.wait import K8sTridentOrchestratorWait


class K8sTridentOrchestrator(
        K8sTridentOrchestratorApi,
        K8sTridentOrchestratorInfo,
        K8sTridentOrchestratorCreate,
        K8sTridentOrchestratorDelete,
        K8sTridentOrchestratorWait
        ):
    def __init__(self):
        K8sTridentOrchestratorApi.__init__(self)
        K8sTridentOrchestratorInfo.__init__(self)
        K8sTridentOrchestratorCreate.__init__(self)
        K8sTridentOrchestratorDelete.__init__(self)
        K8sTridentOrchestratorWait.__init__(self)
