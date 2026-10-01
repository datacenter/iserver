class K8sKnativeServingWait():
    def __init__(self):
        pass

    def wait_knative_serving(self, namespace, name, match_properties={}, break_properties={}, my_output=None, prompt='KnativeServing', max_time=60):
        return self.wait_managed_object(
            'knative_serving',
            name,
            namespace=namespace,
            match_properties=match_properties,
            break_properties=break_properties,
            my_output=my_output,
            prompt='Wait for %s %s/%s [timeout:%ss]' % (prompt, namespace, name, max_time),
            max_time=max_time
        )

    def wait_no_knative_serving(self, namespace, name, max_time=60, my_output=None, prompt='KnativeServing'):
        return self.wait_no_managed_object(
            'knative_serving',
            name,
            namespace=namespace,
            my_output=my_output,
            prompt='Wait for no %s %s/%s [timeout:%ss]' % (prompt, namespace, name, max_time),
            max_time=max_time
        )