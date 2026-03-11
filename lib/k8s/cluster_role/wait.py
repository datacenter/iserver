class K8sClusterRoleWait():
    def __init__(self):
        pass

    def wait_cluster_role(self, name, my_output=None, prompt='ClusterRole', max_time=60):
        return self.wait_managed_object(
            'cluster_role',
            name,
            my_output=my_output,
            prompt='- wait for %s %s [timeout:%ss]' % (prompt, name, max_time),
            max_time=max_time
        )

    def wait_no_cluster_role(self, name, my_output=None, prompt='ClusterRole', max_time=60):
        return self.wait_no_managed_object(
            'cluster_role',
            name,
            my_output=my_output,
            prompt='- wait for no %s %s [timeout:%ss]' % (prompt, name, max_time),
            max_time=max_time
        )
