from lib.k8s.data_source.api import K8sDataSourceApi
from lib.k8s.data_source.info import K8sDataSourceInfo


class K8sDataSource(
        K8sDataSourceApi,
        K8sDataSourceInfo
        ):
    def __init__(self):
        K8sDataSourceApi.__init__(self)
        K8sDataSourceInfo.__init__(self)
