class K8sIdentityWait():
    def __init__(self):
        pass

    def wait_identity(self, name, my_output=None, prompt='Identity', max_time=60):
        return self.wait_managed_object(
            'identity',
            name,
            my_output=my_output,
            prompt='- wait for %s %s [timeout:%ss]' % (prompt, name, max_time),
            max_time=max_time
        )

    def wait_no_identity(self, name, my_output=None, prompt='Identity', max_time=60):
        return self.wait_no_managed_object(
            'identity',
            name,
            my_output=my_output,
            prompt='- wait for no %s %s [timeout:%ss]' % (prompt, name, max_time),
            max_time=max_time
        )
