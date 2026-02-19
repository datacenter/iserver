from lib.k8s.nemo_evaluator.api import K8sNemoEvaluatorApi
from lib.k8s.nemo_evaluator.info import K8sNemoEvaluatorInfo
from lib.k8s.nemo_evaluator.create import K8sNemoEvaluatorCreate
from lib.k8s.nemo_evaluator.delete import K8sNemoEvaluatorDelete
from lib.k8s.nemo_evaluator.wait import K8sNemoEvaluatorWait


class K8sNemoEvaluator(
        K8sNemoEvaluatorApi,
        K8sNemoEvaluatorInfo,
        K8sNemoEvaluatorCreate,
        K8sNemoEvaluatorDelete,
        K8sNemoEvaluatorWait
        ):
    def __init__(self):
        K8sNemoEvaluatorApi.__init__(self)
        K8sNemoEvaluatorInfo.__init__(self)
        K8sNemoEvaluatorCreate.__init__(self)
        K8sNemoEvaluatorDelete.__init__(self)
        K8sNemoEvaluatorWait.__init__(self)
