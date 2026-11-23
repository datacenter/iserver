from lib.k8s.private_network_node_attachment.api import K8sPrivateNetworkNodeAttachmentApi
from lib.k8s.private_network_node_attachment.info import K8sPrivateNetworkNodeAttachmentInfo


class K8sPrivateNetworkNodeAttachment(
        K8sPrivateNetworkNodeAttachmentApi,
        K8sPrivateNetworkNodeAttachmentInfo
        ):
    def __init__(self):
        K8sPrivateNetworkNodeAttachmentApi.__init__(self)
        K8sPrivateNetworkNodeAttachmentInfo.__init__(self)