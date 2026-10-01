class K8sNodeNetworkStateWait():
    def __init__(self):
        pass
    
    def wait_node_network_state(self, name, match_properties={}, break_properties={}, my_output=None, prompt='nodNodeNetworkState', max_time=360):
        return self.wait_managed_object(
            'node_network_state',
            name,
            match_properties=match_properties,
            break_properties=break_properties,
            my_output=my_output,
            prompt='Wait for %s %s [timeout:%ss]' % (prompt, name, max_time),
            max_time=max_time
        )