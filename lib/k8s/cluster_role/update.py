class K8sClusterRoleUpdate():
    def __init__(self):
        pass

    def get_update_cluster_role_body(self, name, api_groups=[], resources=[], verbs=[]):
        body = {}
        body['apiVersion'] = 'rbac.authorization.k8s.io/v1'
        body['kind'] = 'ClusterRole'
        body['metadata'] = {}
        body['metadata']['name'] = name
        body['rules'] = []

        rule_mo = {}
        if len(api_groups) > 0:
            rule_mo['apiGroups'] = api_groups

        if len(resources) > 0:
            rule_mo['resources'] = resources

        if len(verbs) > 0:
            rule_mo['verbs'] = verbs

        body['rules'].append(rule_mo)
        return body
        
    def update_cluster_role(
            self, 
            name, 
            api_groups=[], 
            resources=[], 
            verbs=[],
            replace=True,
            confirmation=False, 
            my_output=None
        ):
        body = self.get_update_cluster_role_body(
            name, 
            api_groups=api_groups,
            resources=resources,
            verbs=verbs
        )
        if replace:
            if not self.replace_resource(body, object_name='cluster_role', my_output=my_output, confirmation=confirmation):
                return False
        else:
            if not self.patch_resource(body, object_name='cluster_role', my_output=my_output, confirmation=confirmation):
                return False

        return True    

    def get_cluster_role_body(self, name):
        crb_mo = self.get_cluster_role(name, return_mo=True, cache_enabled=False)
        if crb_mo is None:
            self.log.error(
                'get_cluster_role_body',
                'Crb not found: %s' % (name)
            )
        return crb_mo

    def add_user_subject_cluster_role(
            self, 
            name, 
            username,
            confirmation=False, 
            my_output=None
        ):
        crb_mo = self.get_cluster_role_body(name)
        if crb_mo is None:
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
        crb_mo['subjects'].append(
            subject_mo
        )

        return self.replace_resource(crb_mo, object_name='cluster_role', my_output=my_output, confirmation=confirmation)

    def del_user_subject_cluster_role(
            self, 
            name, 
            username,
            confirmation=False, 
            my_output=None
        ):
        crb_mo = self.get_cluster_role_body(name)
        if crb_mo is None:
            return False

        new_subjects = []

        for subject_mo in crb_mo['subjects']:
            if subject_mo['kind'] != 'User':
                new_subjects.append(subject_mo)
                continue

            if subject_mo['name'] != username:
                new_subjects.append(subject_mo)
                continue

        crb_mo['subjects'] = new_subjects

        return self.replace_resource(crb_mo, object_name='cluster_role', my_output=my_output, confirmation=confirmation)
