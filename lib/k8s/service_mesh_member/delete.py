class K8sServiceMeshMemberDelete():
    def __init__(self):
        self.service_mesh_member = None

    def delete_service_mesh_members(self, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete Knative Serving', before_newline=True, underline=True)

        servings = self.get_service_mesh_members(
            cache_enabled=False
        )
        if servings is None:
            if my_output is not None:
                my_output.error('Failed to get service mesh member')
            return False

        if len(servings) == 0:
            if my_output is not None:
                my_output.default('- no service mesh member found')
            return True
        
        for serving in servings:
            if my_output is not None:
                my_output.default('- %s' % (serving['namespace_name']))

            success = self.delete_service_mesh_member_mo(
                serving['namespace'],
                serving['name']
            )
            if not success:
                if my_output is not None:
                    my_output.error('service mesh member delete failed')

                return False

            if wait:
                if my_output is not None:
                    my_output.default('- wait for no service mesh member')

                if not self.wait_no_service_mesh_member(serving['namespace'], serving['name']):
                    if my_output is not None:
                        my_output.error('Time out')
                    return False
            
        return True
