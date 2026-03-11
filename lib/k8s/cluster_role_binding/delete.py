class K8sClusterRoleBindingDelete():
    def __init__(self):
        pass

    def delete_cluster_role_binding(self, name, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete Cluster Role Binding', before_newline=True, underline=True)
            my_output.default('- name: %s' % (name))

        if not self.is_cluster_role_binding(name, cache_enabled=False):
            if my_output is not None:
                my_output.default('- already deleted')
            return True
        
        if not self.delete_cluster_role_binding_mo(name):
            if my_output is not None:
                my_output.error('Failed to delete cluster role binding')
            return False

        if wait:
            if my_output is not None:
                my_output.default('- wait for no cluster role binding')

            if not self.wait_no_cluster_role_binding(name):
                if my_output is not None:
                    my_output.error('Time out')
                return False
            
        return True
    
    def del_user_subject_cluster_role_binding(
            self, 
            name, 
            username,
            confirmation=False, 
            my_output=None
        ):
        if my_output is not None:
            my_output.default('Remove user subject from cluster role binding', before_newline=True, underline=True)
            my_output.default('- cluster role binding: %s' % (name))
            my_output.default('- user: %s' % (username))

        crb_mo = self.get_cluster_role_binding(name, return_mo=True, cache_enabled=False)
        if crb_mo is None:
            if my_output is not None:
                my_output.error('cluster role binding not found')

            self.log.error(
                'del_user_subject_cluster_role_binding',
                'Crb not found: %s' % (name)
            )
            return False

        new_subjects = []

        found = False
        for subject_mo in crb_mo['subjects']:
            if subject_mo['kind'] != 'User':
                new_subjects.append(subject_mo)
                continue

            if subject_mo['name'] != username:
                new_subjects.append(subject_mo)
                continue
            
            found = True

        if not found:
            if my_output is not None:
                my_output.default('- already deleted')
            return True
        
        crb_mo = self.cleanup_managed_object(crb_mo, exclude=['resourceVersion'])
        crb_mo['subjects'] = new_subjects
        return self.replace_resource(crb_mo, object_name='cluster_role_binding', my_output=my_output, confirmation=confirmation)
