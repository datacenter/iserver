class K8sNetworkOperatorWait():
    def __init__(self):
        pass

    def wait_network_operator(self, name, match_properties={}, break_properties={}, my_output=None, prompt='Network', max_time=60):
        return self.wait_managed_object(
            'network_operator',
            name,
            match_properties=match_properties,
            break_properties=break_properties,
            my_output=my_output,
            prompt='- wait for %s %s [timeout:%ss]' % (prompt, name, max_time),
            max_time=max_time
        )
