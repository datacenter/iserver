from lib.k8s.service_mesh_member.api import K8sServiceMeshMemberApi
from lib.k8s.service_mesh_member.info import K8sServiceMeshMemberInfo
from lib.k8s.service_mesh_member.create import K8sServiceMeshMemberCreate
from lib.k8s.service_mesh_member.delete import K8sServiceMeshMemberDelete
from lib.k8s.service_mesh_member.wait import K8sServiceMeshMemberWait


class K8sServiceMeshMember(
        K8sServiceMeshMemberApi,
        K8sServiceMeshMemberInfo,
        K8sServiceMeshMemberCreate,
        K8sServiceMeshMemberDelete,
        K8sServiceMeshMemberWait
        ):
    def __init__(self):
        K8sServiceMeshMemberApi.__init__(self)
        K8sServiceMeshMemberInfo.__init__(self)
        K8sServiceMeshMemberCreate.__init__(self)
        K8sServiceMeshMemberDelete.__init__(self)
        K8sServiceMeshMemberWait.__init__(self)
