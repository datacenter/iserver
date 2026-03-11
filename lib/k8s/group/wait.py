class K8sGroupWait():
    def __init__(self):
        pass

    def wait_group(self, name, my_output=None, prompt='Group', max_time=60):
        return self.wait_managed_object(
            'group',
            name,
            my_output=my_output,
            prompt='- wait for %s %s [timeout:%ss]' % (prompt, name, max_time),
            max_time=max_time
        )

    def wait_no_group(self, name, my_output=None, prompt='Group', max_time=60):
        return self.wait_no_managed_object(
            'group',
            name,
            my_output=my_output,
            prompt='- wait for no %s %s [timeout:%ss]' % (prompt, name, max_time),
            max_time=max_time
        )
