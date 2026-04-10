class K8sMetalLbWait():
    def __init__(self):
        pass

    def wait_metallb(self, namespace, name, match_properties={}, break_properties={}, my_output=None, prompt='MetalLB', max_time=60):
        return self.wait_managed_object(
            'metallb',
            name,
            namespace=namespace,
            match_properties=match_properties,
            break_properties=break_properties,
            my_output=my_output,
            prompt='- wait for %s %s/%s [timeout:%ss]' % (prompt, namespace, name, max_time),
            max_time=max_time
        )


    def wait_no_metallb(self, namespace, name, max_time=60, my_output=None, prompt='MetalLB'):
        return self.wait_no_managed_object(
            'metallb',
            name,
            namespace=namespace,
            my_output=my_output,
            prompt='- wait for no %s %s/%s [timeout:%ss]' % (prompt, namespace, name, max_time),
            max_time=max_time
        )
