class K8sAuthenticationUpdate():
    def __init__(self):
        pass

    def set_authentication_log_level(self, level, name='cluster', my_output=None, confirmation=False):
        body = {}
        body['apiVersion'] = 'operator.openshift.io/v1'
        body['kind'] = 'Authentication'
        body['metadata'] = {}
        body['metadata']['name'] = name
        body['spec'] = dict(logLevel=level)

        if not self.patch_resource(body, object_name='authentication', my_output=my_output, confirmation=confirmation):
            return False

        return True
