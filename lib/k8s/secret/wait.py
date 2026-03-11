class K8sSecretWait():
    def __init__(self):
        pass

    def wait_secret(self, namespace, name, my_output=None, prompt='Secret', max_time=60):
        return self.wait_managed_object(
            'secret',
            name,
            namespace=namespace,
            my_output=my_output,
            prompt='- wait for %s %s/%s [timeout:%ss]' % (prompt, namespace, name, max_time),
            max_time=max_time
        )
    
    def wait_no_secret(self, namespace, name, my_output=None, prompt='Secret', max_time=60):
        return self.wait_no_managed_object(
            'secret',
            name,
            namespace=namespace,
            my_output=my_output,
            prompt='- wait for no %s %s/%s [timeout:%ss]' % (prompt, namespace, name, max_time),
            max_time=max_time
        )
