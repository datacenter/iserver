from lib.k8s.network_attachment_definition.api import K8sNetworkAttachmentDefinitionApi
from lib.k8s.network_attachment_definition.info import K8sNetworkAttachmentDefinitionInfo
from lib.k8s.network_attachment_definition.bridge import K8sNetworkAttachmentDefinitionBridge
from lib.k8s.network_attachment_definition.delete import K8sNetworkAttachmentDefinitionDelete
from lib.k8s.network_attachment_definition.ipvlan import K8sNetworkAttachmentDefinitionIpVlan
from lib.k8s.network_attachment_definition.macvlan import K8sNetworkAttachmentDefinitionMacVlan
from lib.k8s.network_attachment_definition.vlan import K8sNetworkAttachmentDefinitionVlan
from lib.k8s.network_attachment_definition.wait import K8sNetworkAttachmentDefinitionWait


class K8sNetworkAttachmentDefinition(
        K8sNetworkAttachmentDefinitionApi,
        K8sNetworkAttachmentDefinitionInfo,
        K8sNetworkAttachmentDefinitionBridge,
        K8sNetworkAttachmentDefinitionDelete,
        K8sNetworkAttachmentDefinitionIpVlan,
        K8sNetworkAttachmentDefinitionMacVlan,
        K8sNetworkAttachmentDefinitionVlan,
        K8sNetworkAttachmentDefinitionWait
        ):
    def __init__(self):
        K8sNetworkAttachmentDefinitionApi.__init__(self)
        K8sNetworkAttachmentDefinitionInfo.__init__(self)
        K8sNetworkAttachmentDefinitionBridge.__init__(self)
        K8sNetworkAttachmentDefinitionDelete.__init__(self)
        K8sNetworkAttachmentDefinitionIpVlan.__init__(self)
        K8sNetworkAttachmentDefinitionMacVlan.__init__(self)
        K8sNetworkAttachmentDefinitionVlan.__init__(self)
        K8sNetworkAttachmentDefinitionWait.__init__(self)
