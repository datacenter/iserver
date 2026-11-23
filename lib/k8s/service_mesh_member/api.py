class K8sServiceMeshMemberApi():
    def __init__(self):
        self.service_mesh_member_mo = None
        self.service_mesh_member_namespace_mo = {}

    def get_service_mesh_member_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.service_mesh_member_mo,
            self.service_mesh_member_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.service_mesh_member_mo, self.service_mesh_member_namespace_mo = self.get_namespaced_resources(
            'ServiceMeshMember', 
            'maistra.io/v1', 
            self.service_mesh_member_mo,
            self.service_mesh_member_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def delete_service_mesh_member_mo(self, namespace, name):
        success, _ = self.delete_resource('AdminServiceMeshMemberJob', 'maistra.io/v1', name, namespace=namespace)
        return success