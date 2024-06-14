from lib.k8s.network_attachment_definition.api import K8sNetworkAttachmentDefinitionApi
from lib.k8s.network_attachment_definition.info import K8sNetworkAttachmentDefinitionInfo


class K8sNetworkAttachmentDefinition(
        K8sNetworkAttachmentDefinitionApi,
        K8sNetworkAttachmentDefinitionInfo
        ):
    def __init__(self):
        K8sNetworkAttachmentDefinitionApi.__init__(self)
        K8sNetworkAttachmentDefinitionInfo.__init__(self)
