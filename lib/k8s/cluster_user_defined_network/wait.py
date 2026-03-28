class K8sClusterUserDefinedNetworkWait():
    def __init__(self):
        pass

    def wait_cluster_user_defined_network(self, name, match_properties={}, break_properties={}, my_output=None, prompt='ClusterUserDefinedNetwork', max_time=60):
        return self.wait_managed_object(
            'cluster_user_defined_network',
            name,
            match_properties=match_properties,
            break_properties=break_properties,
            my_output=my_output,
            prompt='- wait for %s %s [timeout:%ss]' % (prompt, name, max_time),
            max_time=max_time
        )

    def wait_no_cluster_user_defined_network(self, name, max_time=60, my_output=None, prompt='ClusterUserDefinedNetwork'):
        return self.wait_no_managed_object(
            'cluster_user_defined_network',
            name,
            my_output=my_output,
            prompt='- wait for no %s %s [timeout:%ss]' % (prompt, name, max_time),
            max_time=max_time
        )
