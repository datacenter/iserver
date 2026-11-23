from lib.k8s.dev_workspace.api import K8sDevWorkspaceApi
from lib.k8s.dev_workspace.info import K8sDevWorkspaceInfo
from lib.k8s.dev_workspace.delete import K8sDevWorkspaceDelete
from lib.k8s.dev_workspace.wait import K8sDevWorkspaceWait


class K8sDevWorkspace(
        K8sDevWorkspaceApi,
        K8sDevWorkspaceInfo,
        K8sDevWorkspaceDelete,
        K8sDevWorkspaceWait
        ):
    def __init__(self):
        K8sDevWorkspaceApi.__init__(self)
        K8sDevWorkspaceInfo.__init__(self)
        K8sDevWorkspaceDelete.__init__(self)
        K8sDevWorkspaceWait.__init__(self)
