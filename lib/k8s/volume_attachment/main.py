from lib.k8s.volume_attachment.api import K8sVolumeAttachmentApi
from lib.k8s.volume_attachment.info import K8sVolumeAttachmentInfo


class K8sVolumeAttachment(
        K8sVolumeAttachmentApi,
        K8sVolumeAttachmentInfo
        ):
    def __init__(self):
        K8sVolumeAttachmentApi.__init__(self)
        K8sVolumeAttachmentInfo.__init__(self)
