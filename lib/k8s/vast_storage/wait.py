class K8sVastStorageWait():
    def __init__(self):
        pass

    def wait_vast_storage(self, namespace, name, match_properties={}, break_properties={}, my_output=None, prompt='VastStorage', max_time=60):
        return self.wait_managed_object(
            'vast_storage',
            name,
            namespace=namespace,
            match_properties=match_properties,
            break_properties=break_properties,
            my_output=my_output,
            prompt='- wait for %s %s/%s [timeout:%ss]' % (prompt, namespace, name, max_time),
            max_time=max_time
        )

    def wait_no_vast_storage(self, namespace, name, max_time=60, my_output=None, prompt='VastStorage'):
        return self.wait_no_managed_object(
            'vast_storage',
            name,
            namespace=namespace,
            my_output=my_output,
            prompt='- wait for no %s %s/%s [timeout:%ss]' % (prompt, namespace, name, max_time),
            max_time=max_time
        )
