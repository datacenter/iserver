from lib.k8s.service_mesh_control_plane.api import K8sServiceMeshControlPlaneApi
from lib.k8s.service_mesh_control_plane.info import K8sServiceMeshControlPlaneInfo
from lib.k8s.service_mesh_control_plane.create import K8sServiceMeshControlPlaneCreate
from lib.k8s.service_mesh_control_plane.delete import K8sServiceMeshControlPlaneDelete
from lib.k8s.service_mesh_control_plane.wait import K8sServiceMeshControlPlaneWait


class K8sServiceMeshControlPlane(
        K8sServiceMeshControlPlaneApi,
        K8sServiceMeshControlPlaneInfo,
        K8sServiceMeshControlPlaneCreate,
        K8sServiceMeshControlPlaneDelete,
        K8sServiceMeshControlPlaneWait
        ):
    def __init__(self):
        K8sServiceMeshControlPlaneApi.__init__(self)
        K8sServiceMeshControlPlaneInfo.__init__(self)
        K8sServiceMeshControlPlaneCreate.__init__(self)
        K8sServiceMeshControlPlaneDelete.__init__(self)
        K8sServiceMeshControlPlaneWait.__init__(self)
