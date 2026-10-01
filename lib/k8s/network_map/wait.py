import time


class K8sNetworkMapWait():
    def __init__(self):
        pass

    def wait_network_map(self, namespace, name, match_properties={}, break_properties={}, my_output=None, prompt='NetworkMap', max_time=60):
        return self.wait_managed_object(
            'network_map',
            name,
            namespace=namespace,
            match_properties=match_properties,
            break_properties=break_properties,
            my_output=my_output,
            prompt='Wait for %s %s/%s [timeout:%ss]' % (prompt, namespace, name, max_time),
            max_time=max_time
        )

    def wait_no_network_map(self, namespace, name, max_time=60, my_output=None, prompt='NetworkMap'):
        return self.wait_no_managed_object(
            'network_map',
            name,
            namespace=namespace,
            my_output=my_output,
            prompt='Wait for no %s %s/%s [timeout:%ss]' % (prompt, namespace, name, max_time),
            max_time=max_time
        )
        
    def wait_network_map_ready(self, namespace, name, max_time=60, my_output=None, prompt='NetworkMap'):
        return self.wait_network_map(
            namespace, 
            name, 
            match_properties={'ready': True}, 
            break_properties={'invalid': True}, 
            my_output=my_output, 
            prompt=prompt, 
            max_time=max_time
        )