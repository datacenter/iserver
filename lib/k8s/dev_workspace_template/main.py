from lib.k8s.dev_workspace_template.api import K8sDevWorkspaceTemplateApi
from lib.k8s.dev_workspace_template.info import K8sDevWorkspaceTemplateInfo
from lib.k8s.dev_workspace_template.delete import K8sDevWorkspaceTemplateDelete
from lib.k8s.dev_workspace_template.wait import K8sDevWorkspaceTemplateWait


class K8sDevWorkspaceTemplate(
        K8sDevWorkspaceTemplateApi,
        K8sDevWorkspaceTemplateInfo,
        K8sDevWorkspaceTemplateDelete,
        K8sDevWorkspaceTemplateWait
        ):
    def __init__(self):
        K8sDevWorkspaceTemplateApi.__init__(self)
        K8sDevWorkspaceTemplateInfo.__init__(self)
        K8sDevWorkspaceTemplateDelete.__init__(self)
        K8sDevWorkspaceTemplateWait.__init__(self)
