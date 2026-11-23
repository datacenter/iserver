from lib.k8s.nemo_customizer.api import K8sNemoCustomizerApi
from lib.k8s.nemo_customizer.info import K8sNemoCustomizerInfo
from lib.k8s.nemo_customizer.create import K8sNemoCustomizerCreate
from lib.k8s.nemo_customizer.delete import K8sNemoCustomizerDelete
from lib.k8s.nemo_customizer.wait import K8sNemoCustomizerWait


class K8sNemoCustomizer(
        K8sNemoCustomizerApi,
        K8sNemoCustomizerInfo,
        K8sNemoCustomizerCreate,
        K8sNemoCustomizerDelete,
        K8sNemoCustomizerWait
        ):
    def __init__(self):
        K8sNemoCustomizerApi.__init__(self)
        K8sNemoCustomizerInfo.__init__(self)
        K8sNemoCustomizerCreate.__init__(self)
        K8sNemoCustomizerDelete.__init__(self)
        K8sNemoCustomizerWait.__init__(self)
