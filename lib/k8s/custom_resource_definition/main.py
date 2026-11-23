from lib.k8s.custom_resource_definition.api import K8sCustomResourceDefinitionApi
from lib.k8s.custom_resource_definition.info import K8sCustomResourceDefinitionInfo
from lib.k8s.custom_resource_definition.delete import K8sCustomResourceDefinitionDelete
from lib.k8s.custom_resource_definition.wait import K8sCustomResourceDefinitionWait


class K8sCustomResourceDefinition(
        K8sCustomResourceDefinitionApi,
        K8sCustomResourceDefinitionInfo,
        K8sCustomResourceDefinitionDelete,
        K8sCustomResourceDefinitionWait
        ):
    def __init__(self):
        K8sCustomResourceDefinitionApi.__init__(self)
        K8sCustomResourceDefinitionInfo.__init__(self)
        K8sCustomResourceDefinitionDelete.__init__(self)
        K8sCustomResourceDefinitionWait.__init__(self)
