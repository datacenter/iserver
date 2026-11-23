from lib.k8s.vast_driver.api import K8sVastDriverApi
from lib.k8s.vast_driver.info import K8sVastDriverInfo
from lib.k8s.vast_driver.create import K8sVastDriverCreate
from lib.k8s.vast_driver.delete import K8sVastDriverDelete
from lib.k8s.vast_driver.wait import K8sVastDriverWait


class K8sVastDriver(
        K8sVastDriverApi,
        K8sVastDriverInfo,
        K8sVastDriverCreate,
        K8sVastDriverDelete,
        K8sVastDriverWait
        ):
    def __init__(self):
        K8sVastDriverApi.__init__(self)
        K8sVastDriverInfo.__init__(self)
        K8sVastDriverCreate.__init__(self)
        K8sVastDriverDelete.__init__(self)
        K8sVastDriverWait.__init__(self)
