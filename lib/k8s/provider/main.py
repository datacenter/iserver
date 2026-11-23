from lib.k8s.provider.api import K8sProviderApi
from lib.k8s.provider.info import K8sProviderInfo
from lib.k8s.provider.create import K8sProviderCreate
from lib.k8s.provider.delete import K8sProviderDelete
from lib.k8s.provider.wait import K8sProviderWait


class K8sProvider(
        K8sProviderApi,
        K8sProviderInfo,
        K8sProviderCreate,
        K8sProviderDelete,
        K8sProviderWait
        ):
    def __init__(self):
        K8sProviderApi.__init__(self)
        K8sProviderInfo.__init__(self)
        K8sProviderCreate.__init__(self)
        K8sProviderDelete.__init__(self)
        K8sProviderWait.__init__(self)
