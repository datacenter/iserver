class K8sTetragonNetworkPolicyWait():
    def __init__(self):
        pass

    def wait_tetragon_network_policy(self, name, match_properties={}, break_properties={}, my_output=None, prompt='TetragonNetworkPolicy', max_time=60):
        return self.wait_managed_object(
            'tetragon_network_policy',
            name,
            match_properties=match_properties,
            break_properties=break_properties,
            my_output=my_output,
            prompt='Wait for %s %s [timeout:%ss]' % (prompt, name, max_time),
            max_time=max_time
        )

    def wait_no_tetragon_network_policy(self, name, my_output=None, prompt='TetragonNetworkPolicy', max_time=60):
        return self.wait_no_managed_object(
            'tetragon_network_policy',
            name,
            my_output=my_output,
            prompt='Wait for no %s %s [timeout:%ss]' % (prompt, name, max_time),
            max_time=max_time
        )