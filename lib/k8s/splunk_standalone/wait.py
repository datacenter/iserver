import time


class K8sSplunkStandaloneWait():
    def __init__(self):
        pass

    def wait_splunk_standalone(self, namespace, name, match_properties={}, break_properties={}, my_output=None, prompt='Standalone', max_time=60):
        return self.wait_managed_object(
            'splunk_standalone',
            name,
            namespace=namespace,
            match_properties=match_properties,
            break_properties=break_properties,
            my_output=my_output,
            prompt='Wait for %s %s/%s [timeout:%ss]' % (prompt, namespace, name, max_time),
            max_time=max_time
        )
    
    def wait_no_splunk_standalone(self, namespace, name, max_time=60, my_output=None, prompt='Standalone'):
        return self.wait_no_managed_object(
            'splunk_standalone',
            name,
            namespace=namespace,
            my_output=my_output,
            prompt='Wait for no %s %s/%s [timeout:%ss]' % (prompt, namespace, name, max_time),
            max_time=max_time
        )