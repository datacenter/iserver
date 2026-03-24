class K8sUserDefinedNetworkWait():
    def __init__(self):
        pass

    def wait_user_defined_network(self, namespace, name, match_properties={}, break_properties={}, my_output=None, prompt='UserDefinedNetwork', max_time=60):
        return self.wait_managed_object(
            'user_defined_network',
            name,
            namespace=namespace,
            match_properties=match_properties,
            break_properties=break_properties,
            my_output=my_output,
            prompt='- wait for %s %s/%s [timeout:%ss]' % (prompt, namespace, name, max_time),
            max_time=max_time
        )

    def wait_no_user_defined_network(self, namespace, name, max_time=60, my_output=None, prompt='UserDefinedNetwork'):
        return self.wait_no_managed_object(
            'user_defined_network',
            name,
            namespace=namespace,
            my_output=my_output,
            prompt='- wait for no %s %s/%s [timeout:%ss]' % (prompt, namespace, name, max_time),
            max_time=max_time
        )
