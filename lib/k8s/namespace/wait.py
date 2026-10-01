class K8sNamespaceWait():
    def __init__(self):
        pass

    def wait_namespace(self, name, match_properties={}, break_properties={}, my_output=None, prompt='Namespace', max_time=60):
        return self.wait_managed_object(
            'namespace',
            name,
            match_properties=match_properties,
            break_properties=break_properties,
            my_output=my_output,
            prompt='Wait for %s %s [timeout:%ss]' % (prompt, name, max_time),
            max_time=max_time
        )

    def wait_no_namespace(self, name, my_output=None, prompt='Namespace', max_time=60):
        return self.wait_no_managed_object(
            'namespace',
            name,
            my_output=my_output,
            prompt='Wait for no %s %s [timeout:%ss]' % (prompt, name, max_time),
            max_time=max_time
        )