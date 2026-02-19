from lib.k8s.admin_job.api import K8sAdminJobApi
from lib.k8s.admin_job.info import K8sAdminJobInfo
from lib.k8s.admin_job.create import K8sAdminJobCreate
from lib.k8s.admin_job.delete import K8sAdminJobDelete
from lib.k8s.admin_job.wait import K8sAdminJobWait


class K8sAdminJob(
        K8sAdminJobApi,
        K8sAdminJobInfo,
        K8sAdminJobCreate,
        K8sAdminJobDelete,
        K8sAdminJobWait
        ):
    def __init__(self):
        K8sAdminJobApi.__init__(self)
        K8sAdminJobInfo.__init__(self)
        K8sAdminJobCreate.__init__(self)
        K8sAdminJobDelete.__init__(self)
        K8sAdminJobWait.__init__(self)
