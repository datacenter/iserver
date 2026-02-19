from lib.k8s.nim_pipeline.api import K8sNimPipelineApi
from lib.k8s.nim_pipeline.info import K8sNimPipelineInfo
from lib.k8s.nim_pipeline.create import K8sNimPipelineCreate
from lib.k8s.nim_pipeline.delete import K8sNimPipelineDelete
from lib.k8s.nim_pipeline.wait import K8sNimPipelineWait


class K8sNimPipeline(
        K8sNimPipelineApi,
        K8sNimPipelineInfo,
        K8sNimPipelineCreate,
        K8sNimPipelineDelete,
        K8sNimPipelineWait
        ):
    def __init__(self):
        K8sNimPipelineApi.__init__(self)
        K8sNimPipelineInfo.__init__(self)
        K8sNimPipelineCreate.__init__(self)
        K8sNimPipelineDelete.__init__(self)
        K8sNimPipelineWait.__init__(self)
