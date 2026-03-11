class K8sUserWait():
    def __init__(self):
        pass

    def wait_user(self, name, my_output=None, prompt='User', max_time=60):
        return self.wait_managed_object(
            'user',
            name,
            my_output=my_output,
            prompt='- wait for %s %s [timeout:%ss]' % (prompt, name, max_time),
            max_time=max_time
        )

    def wait_no_user(self, name, my_output=None, prompt='User', max_time=60):
        return self.wait_no_managed_object(
            'user',
            name,
            my_output=my_output,
            prompt='- wait for no %s %s [timeout:%ss]' % (prompt, name, max_time),
            max_time=max_time
        )
