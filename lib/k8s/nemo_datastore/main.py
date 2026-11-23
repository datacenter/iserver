from lib.k8s.nemo_datastore.api import K8sNemoDatastoreApi
from lib.k8s.nemo_datastore.info import K8sNemoDatastoreInfo
from lib.k8s.nemo_datastore.create import K8sNemoDatastoreCreate
from lib.k8s.nemo_datastore.delete import K8sNemoDatastoreDelete
from lib.k8s.nemo_datastore.wait import K8sNemoDatastoreWait


class K8sNemoDatastore(
        K8sNemoDatastoreApi,
        K8sNemoDatastoreInfo,
        K8sNemoDatastoreCreate,
        K8sNemoDatastoreDelete,
        K8sNemoDatastoreWait
        ):
    def __init__(self):
        K8sNemoDatastoreApi.__init__(self)
        K8sNemoDatastoreInfo.__init__(self)
        K8sNemoDatastoreCreate.__init__(self)
        K8sNemoDatastoreDelete.__init__(self)
        K8sNemoDatastoreWait.__init__(self)
