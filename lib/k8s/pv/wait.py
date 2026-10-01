class K8sPvWait():
    def __init__(self):
        pass

    def wait_no_pv(self, name, max_time=30, my_output=None, prompt='PersistentVolume'):
        return self.wait_no_managed_object(
            'pv',
            name,
            my_output=my_output,
            prompt='Wait for no %s %s [timeout:%ss]' % (prompt, name, max_time),
            max_time=max_time
        )