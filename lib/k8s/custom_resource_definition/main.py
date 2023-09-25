from lib.k8s.custom_resource_definition.api import K8sCustomResourceDefinitionApi
from lib.k8s.custom_resource_definition.info import K8sCustomResourceDefinitionInfo


class K8sCustomResourceDefinition(
        K8sCustomResourceDefinitionApi,
        K8sCustomResourceDefinitionInfo
        ):
    def __init__(self):
        K8sCustomResourceDefinitionApi.__init__(self)
        K8sCustomResourceDefinitionInfo.__init__(self)
