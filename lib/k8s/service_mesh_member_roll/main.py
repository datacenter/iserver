from lib.k8s.service_mesh_member_roll.api import K8sServiceMeshMemberRollApi
from lib.k8s.service_mesh_member_roll.info import K8sServiceMeshMemberRollInfo
from lib.k8s.service_mesh_member_roll.wait import K8sServiceMeshMemberRollWait


class K8sServiceMeshMemberRoll(
        K8sServiceMeshMemberRollApi,
        K8sServiceMeshMemberRollInfo,
        K8sServiceMeshMemberRollWait
        ):
    def __init__(self):
        K8sServiceMeshMemberRollApi.__init__(self)
        K8sServiceMeshMemberRollInfo.__init__(self)
        K8sServiceMeshMemberRollWait.__init__(self)
