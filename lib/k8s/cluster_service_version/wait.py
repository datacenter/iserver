class K8sClusterServiceVersionWait():
    def __init__(self):
        pass

    def wait_no_cluster_service_version(self, namespace, name, my_output=None, prompt='ClusterServiceVersion', max_time=60):
        return self.wait_no_managed_object(
            'cluster_service_version',
            name,
            namespace=namespace,
            my_output=my_output,
            prompt='- wait for no %s %s [timeout:%ss]' % (prompt, name, max_time),
            max_time=max_time
        )