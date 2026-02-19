from lib.k8s.nemo_guardrail.api import K8sNemoGuardrailApi
from lib.k8s.nemo_guardrail.info import K8sNemoGuardrailInfo
from lib.k8s.nemo_guardrail.create import K8sNemoGuardrailCreate
from lib.k8s.nemo_guardrail.delete import K8sNemoGuardrailDelete
from lib.k8s.nemo_guardrail.wait import K8sNemoGuardrailWait


class K8sNemoGuardrail(
        K8sNemoGuardrailApi,
        K8sNemoGuardrailInfo,
        K8sNemoGuardrailCreate,
        K8sNemoGuardrailDelete,
        K8sNemoGuardrailWait
        ):
    def __init__(self):
        K8sNemoGuardrailApi.__init__(self)
        K8sNemoGuardrailInfo.__init__(self)
        K8sNemoGuardrailCreate.__init__(self)
        K8sNemoGuardrailDelete.__init__(self)
        K8sNemoGuardrailWait.__init__(self)
