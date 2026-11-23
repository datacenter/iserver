from lib.k8s.knative_serving.api import K8sKnativeServingApi
from lib.k8s.knative_serving.info import K8sKnativeServingInfo
from lib.k8s.knative_serving.create import K8sKnativeServingCreate
from lib.k8s.knative_serving.delete import K8sKnativeServingDelete
from lib.k8s.knative_serving.wait import K8sKnativeServingWait


class K8sKnativeServing(
        K8sKnativeServingApi,
        K8sKnativeServingInfo,
        K8sKnativeServingCreate,
        K8sKnativeServingDelete,
        K8sKnativeServingWait
        ):
    def __init__(self):
        K8sKnativeServingApi.__init__(self)
        K8sKnativeServingInfo.__init__(self)
        K8sKnativeServingCreate.__init__(self)
        K8sKnativeServingDelete.__init__(self)
        K8sKnativeServingWait.__init__(self)
