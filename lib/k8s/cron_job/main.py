from lib.k8s.cron_job.api import K8sCronJobApi
from lib.k8s.cron_job.info import K8sCronJobInfo
from lib.k8s.cron_job.create import K8sCronJobCreate
from lib.k8s.cron_job.delete import K8sCronJobDelete
from lib.k8s.cron_job.update import K8sCronJobUpdate
from lib.k8s.cron_job.wait import K8sCronJobWait


class K8sCronJob(
        K8sCronJobApi,
        K8sCronJobInfo,
        K8sCronJobCreate,
        K8sCronJobDelete,
        K8sCronJobUpdate,
        K8sCronJobWait
        ):
    def __init__(self):
        K8sCronJobApi.__init__(self)
        K8sCronJobInfo.__init__(self)
        K8sCronJobCreate.__init__(self)
        K8sCronJobDelete.__init__(self)
        K8sCronJobUpdate.__init__(self)
        K8sCronJobWait.__init__(self)
