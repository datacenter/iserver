class K8sForkliftControllerWait():
    def __init__(self):
        pass

    def wait_forklift_controller(self, namespace, name, match_properties={}, break_properties={}, my_output=None, prompt='ForkliftController', max_time=60):
        return self.wait_managed_object(
            'forklift_controller',
            name,
            namespace=namespace,
            match_properties=match_properties,
            break_properties=break_properties,
            my_output=my_output,
            prompt='Wait for %s %s/%s [timeout:%ss]' % (prompt, namespace, name, max_time),
            max_time=max_time
        )

    def wait_no_forklift_controller(self, namespace, name, max_time=360, my_output=None, prompt='ForkliftController'):
        return self.wait_no_managed_object(
            'forklift_controller',
            name,
            namespace=namespace,
            my_output=my_output,
            prompt='Wait for no %s %s/%s [timeout:%ss]' % (prompt, namespace, name, max_time),
            max_time=max_time
        )
        
    def wait_forklift_controller_ready(self, namespace, name, my_output=None, prompt='ForkliftController', max_time=60):
        return self.wait_forklift_controller(
            namespace, 
            name, 
            match_properties={'ready': True}, 
            my_output=my_output, 
            prompt=prompt, 
            max_time=max_time
        )