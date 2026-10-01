class K8sImageStreamWait():
    def __init__(self):
        pass

    def wait_image_stream(self, namespace, name, match_properties={}, break_properties={}, my_output=None, prompt='ImageStream', max_time=60):
        return self.wait_managed_object(
            'image_stream',
            name,
            namespace=namespace,
            match_properties=match_properties,
            break_properties=break_properties,
            my_output=my_output,
            prompt='Wait for %s %s/%s [timeout:%ss]' % (prompt, namespace, name, max_time),
            max_time=max_time
        )

    def wait_no_image_stream(self, namespace, name, max_time=60, my_output=None, prompt='ImageStream'):
        return self.wait_no_managed_object(
            'image_stream',
            name,
            namespace=namespace,
            my_output=my_output,
            prompt='Wait for no %s %s/%s [timeout:%ss]' % (prompt, namespace, name, max_time),
            max_time=max_time
        )