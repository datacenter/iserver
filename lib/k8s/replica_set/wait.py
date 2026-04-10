class K8sReplicaSetWait():
    def __init__(self):
        pass

    def wait_replica_set(self, namespace, name, my_output=None, prompt='ReplicaSet', max_time=60):
        return self.wait_managed_object(
            'replica_set',
            name,
            namespace=namespace,
            my_output=my_output,
            prompt='- wait for %s %s/%s [timeout:%ss]' % (prompt, namespace, name, max_time),
            max_time=max_time
        )

    def wait_no_replica_set(self, namespace, name, max_time=600, prompt='ReplicaSet', optional=False, my_output=None, log_error_on_timeout=False):
        return self.wait_no_managed_object(
            'replica_set',
            name,
            namespace=namespace,
            my_output=my_output,
            prompt='- wait for %s %s/%s [timeout:%ss]' % (prompt, namespace, name, max_time),
            max_time=max_time,
            optional=optional,
            log_error_on_timeout=log_error_on_timeout
        )