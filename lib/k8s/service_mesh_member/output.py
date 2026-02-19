class K8sServiceMeshMemberOutput():
    def __init__(self):
        pass

    def print_service_mesh_members(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Service Mesh Member', 'namespace_nameT'],
                ['Service Mesh Member', 'cp_namespace_nameT'],
                ['Ready', 'readyTick'],
                ['Conditions', 'conditions']
            ]
        )