class K8sClusterIssuerCreate():
    def __init__(self):
        pass

    def get_cluster_issuer_body(self, name, secret_name):
        body = {}
        body['apiVersion'] = 'cert-manager.io/v1'
        body['kind'] = 'ClusterIssuer'
        body['metadata'] = {}
        body['metadata']['name'] = name
        body['spec'] = {}
        body['spec']['ca'] = {}
        body['spec']['ca']['secretName'] = secret_name
        return body

    def create_cluster_issuer(self, name, secret_name, confirmation=False, my_output=None, wait=True):
        body = self.get_cluster_issuer_body(
            name,
            secret_name
        )

        success, _ = self.create_resource(body, object_name='cluster_issuer', my_output=my_output, confirmation=confirmation)
        if not success:
            return False

        if not wait:
            return True

        success = self.wait_cluster_issuer(
            name,
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False
        
        return True