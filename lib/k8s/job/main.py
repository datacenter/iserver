from lib.k8s.job.api import K8sJobApi
from lib.k8s.job.info import K8sJobInfo
from lib.k8s.job.delete import K8sJobDelete
from lib.k8s.job.wait import K8sJobWait


class K8sJob(
        K8sJobApi,
        K8sJobInfo,
        K8sJobDelete,
        K8sJobWait
        ):
    def __init__(self):
        K8sJobApi.__init__(self)
        K8sJobInfo.__init__(self)
        K8sJobDelete.__init__(self)
        K8sJobWait.__init__(self)
