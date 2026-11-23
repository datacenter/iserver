class K8sServiceMeshMemberRollApi():
    def __init__(self):
        self.service_mesh_member_roll_mo = None
        self.service_mesh_member_roll_namespace_mo = {}

    def get_service_mesh_member_roll_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.service_mesh_member_roll_mo,
            self.service_mesh_member_roll_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.service_mesh_member_roll_mo, self.service_mesh_member_roll_namespace_mo = self.get_namespaced_resources(
            'ServiceMeshMemberRoll', 
            'maistra.io/v1', 
            self.service_mesh_member_roll_mo,
            self.service_mesh_member_roll_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response