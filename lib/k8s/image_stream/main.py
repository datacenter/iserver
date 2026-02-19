from lib.k8s.image_stream.api import K8sImageStreamApi
from lib.k8s.image_stream.info import K8sImageStreamInfo
from lib.k8s.image_stream.delete import K8sImageStreamDelete
from lib.k8s.image_stream.wait import K8sImageStreamWait


class K8sImageStream(
        K8sImageStreamApi,
        K8sImageStreamInfo,
        K8sImageStreamDelete,
        K8sImageStreamWait,
        ):
    def __init__(self):
        K8sImageStreamApi.__init__(self)
        K8sImageStreamInfo.__init__(self)
        K8sImageStreamDelete.__init__(self)
        K8sImageStreamWait.__init__(self)
