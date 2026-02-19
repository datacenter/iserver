from lib.k8s.job.api import K8sJobApi
from lib.k8s.job.info import K8sJobInfo


class K8sJob(
        K8sJobApi,
        K8sJobInfo
        ):
    def __init__(self):
        K8sJobApi.__init__(self)
        K8sJobInfo.__init__(self)
