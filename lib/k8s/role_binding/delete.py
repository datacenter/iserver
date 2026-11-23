class K8sRoleBindingDelete():
    def __init__(self):
        pass

    def delete_role_binding(self, namespace, name, my_output=None, wait=True):
        success, _ = self.delete_resource(
            'RoleBinding', 
            'rbac.authorization.k8s.io/v1',
            name, 
            namespace=namespace, 
            object_name='role_binding',
            my_output=my_output
        )
        if not success:
            return False

        if wait:
            if my_output is not None:
                my_output.default('- wait for no role binding')

            if not self.wait_no_role_binding(namespace, name):
                if my_output is not None:
                    my_output.error('Timed out')
                return False

        return True

    def delete_namespaced_role_bindings(self, namespace, my_output=None, wait=True, skip = ['system:image-pullers', 'system:image-builders', 'system:deployers']):
        role_bindings = self.get_role_bindings(object_filter=['namespace:%s' % (namespace)], cache_enabled=False)
        if role_bindings is None:
            if my_output is not None:
                my_output.error('Failed to get role bindings')
            return False

        for role_binding in role_bindings:
            if role_binding['name'] in skip:
                continue
            
            success = self.delete_role_binding(
                role_binding['namespace'],
                role_binding['name'],
                my_output=my_output,
                wait=wait
            )
            if not success:
                return False

        return True