class K8sClusterRoleBindingUpdate():
    def __init__(self):
        pass

    def update_service_account_cluster_role_binding(
            self, 
            name, 
            cluster_role_name, 
            sa_name, 
            sa_namespace,
            confirmation=False, 
            my_output=None
        ):
        body = self.get_create_cluster_role_binding_service_account_body(
            name,
            cluster_role_name, 
            sa_namespace,
            sa_name
        )
        return self.replace_resource(body, object_name='cluster_role_binding', my_output=my_output, confirmation=confirmation)

    def add_user_subject_cluster_role_binding(
            self, 
            name, 
            username,
            confirmation=False, 
            my_output=None
        ):
        if my_output is not None:
            my_output.default('Add user subject to cluster role binding', before_newline=True, underline=True)
            my_output.default('- cluster role binding: %s' % (name))
            my_output.default('- user: %s' % (username))

        crb_mo = self.get_cluster_role_binding(name, return_mo=True, cache_enabled=False)
        if crb_mo is None:
            if my_output is not None:
                my_output.error('cluster role binding not found')

            self.log.error(
                'add_user_subject_cluster_role_binding',
                'Crb not found: %s' % (name)
            )
            return False

        for subject_mo in crb_mo['subjects']:
            if subject_mo['kind'] != 'User':
                continue

            if subject_mo['name'] == username:
                return True

        subject_mo = {}
        subject_mo['apiGroup'] = 'rbac.authorization.k8s.io'
        subject_mo['kind'] = 'User'
        subject_mo['name'] = username

        crb_mo = self.cleanup_managed_object(crb_mo, exclude=['resourceVersion'])
        crb_mo['subjects'].append(
            subject_mo
        )

        return self.replace_resource(crb_mo, object_name='cluster_role_binding', my_output=my_output, confirmation=confirmation)
