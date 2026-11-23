class K8sJobWait():
    def __init__(self):
        pass

    def wait_no_job(self, namespace, name, max_time=60, prompt='Job', my_output=None):
        return self.wait_no_managed_object(
            'job',
            name,
            namespace=namespace,
            my_output=my_output,
            prompt='Wait for no %s %s/%s [timeout:%ss]' % (prompt, namespace, name, max_time),
            max_time=max_time
        )