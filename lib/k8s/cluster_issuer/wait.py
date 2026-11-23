class K8sClusterIssuerWait():
    def __init__(self):
        pass
    
    def wait_cluster_issuer(self, name, match_properties={}, break_properties={}, my_output=None, prompt='ClusterIssuer', max_time=60):
        return self.wait_managed_object(
            'cluster_issuer',
            name,
            match_properties=match_properties,
            break_properties=break_properties,
            my_output=my_output,
            prompt='Wait for %s %s [timeout:%ss]' % (prompt, name, max_time),
            max_time=max_time
        )
    
    def wait_no_cluster_issuer(self, name, max_time=60, prompt='ClusterIssuer', my_output=None):
        return self.wait_no_managed_object(
            'cluster_issuer',
            name,
            my_output=my_output,
            prompt='Wait for no %s %s [timeout:%ss]' % (prompt, name, max_time),
            max_time=max_time
        )