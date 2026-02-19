from lib.k8s.nemo_entitystore.api import K8sNemoEntitystoreApi
from lib.k8s.nemo_entitystore.info import K8sNemoEntitystoreInfo
from lib.k8s.nemo_entitystore.create import K8sNemoEntitystoreCreate
from lib.k8s.nemo_entitystore.delete import K8sNemoEntitystoreDelete
from lib.k8s.nemo_entitystore.wait import K8sNemoEntitystoreWait


class K8sNemoEntitystore(
        K8sNemoEntitystoreApi,
        K8sNemoEntitystoreInfo,
        K8sNemoEntitystoreCreate,
        K8sNemoEntitystoreDelete,
        K8sNemoEntitystoreWait
        ):
    def __init__(self):
        K8sNemoEntitystoreApi.__init__(self)
        K8sNemoEntitystoreInfo.__init__(self)
        K8sNemoEntitystoreCreate.__init__(self)
        K8sNemoEntitystoreDelete.__init__(self)
        K8sNemoEntitystoreWait.__init__(self)
