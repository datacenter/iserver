class K8sClusterRoleBindingWait():
    def __init__(self):
        pass

    def wait_cluster_role_binding(self, name, my_output=None, prompt='ClusterRoleBinding', max_time=60):
        return self.wait_managed_object(
            'cluster_role_binding',
            name,
            my_output=my_output,
            prompt='- wait for %s %s [timeout:%ss]' % (prompt, name, max_time),
            max_time=max_time
        )

    def wait_no_cluster_role_binding(self, name, my_output=None, prompt='ClusterRoleBinding', max_time=60):
        return self.wait_no_managed_object(
            'cluster_role_binding',
            name,
            my_output=my_output,
            prompt='- wait for no %s %s [timeout:%ss]' % (prompt, name, max_time),
            max_time=max_time
        )
