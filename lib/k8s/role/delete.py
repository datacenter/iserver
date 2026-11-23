class K8sRoleDelete():
    def __init__(self):
        pass

    def delete_role(self, namespace, name, my_output=None, wait=True):
        success, _ = self.delete_resource(
            'Role', 
            'rbac.authorization.k8s.io/v1',
            name, 
            namespace=namespace, 
            object_name='role',
            my_output=my_output
        )
        if not success:
            return False

        if wait:
            if my_output is not None:
                my_output.default('- wait for no role')

            if not self.wait_no_role(namespace, name):
                if my_output is not None:
                    my_output.error('Timed out')
                return False

        return True

    def delete_namespaced_roles(self, namespace, my_output=None, wait=True):
        roles = self.get_roles(object_filter=['namespace:%s' % (namespace)], cache_enabled=False)
        if roles is None:
            if my_output is not None:
                my_output.error('Failed to get role')
            return False

        for role in roles:
            success = self.delete_role(
                role['namespace'],
                role['name'],
                my_output=my_output,
                wait=wait
            )
            if not success:
                return False

        return True