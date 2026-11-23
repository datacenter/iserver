from lib.k8s.data_import_cron.api import K8sDataImportCronApi
from lib.k8s.data_import_cron.info import K8sDataImportCronInfo


class K8sDataImportCron(
        K8sDataImportCronApi,
        K8sDataImportCronInfo
        ):
    def __init__(self):
        K8sDataImportCronApi.__init__(self)
        K8sDataImportCronInfo.__init__(self)
