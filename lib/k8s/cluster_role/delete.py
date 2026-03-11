class K8sClusterRoleDelete():
    def __init__(self):
        pass

    def delete_cluster_role(self, name, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete Cluster Role', before_newline=True, underline=True)
            my_output.default('- name: %s' % (name))

        if not self.is_cluster_role(name, cache_enabled=False):
            if my_output is not None:
                my_output.default('- already deleted')
            return True
        
        if not self.delete_cluster_role_mo(name):
            if my_output is not None:
                my_output.error('Failed to delete cluster role')
            return False

        if wait:
            if my_output is not None:
                my_output.default('- wait for no cluster role')

            if not self.wait_no_cluster_role(name):
                if my_output is not None:
                    my_output.error('Time out')
                return False
            
        return True
    