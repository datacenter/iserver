class K8sCustomResourceDefinitionWait():
    def __init__(self):
        pass

    def wait_custom_resource_definition_established(self, name, match_properties={'established':True}, break_properties={}, my_output=None, prompt='CustomResourceDefinition', max_time=360):
        return self.wait_managed_object(
            'custom_resource_definition',
            name,
            match_properties=match_properties,
            break_properties=break_properties,
            my_output=my_output,
            prompt='Wait for %s %s [timeout:%ss]' % (prompt, name, max_time),
            max_time=max_time
        )

    def wait_custom_resource_definition(self, name, my_output=None, prompt='CustomResourceDefinition', max_time=60):
        return self.wait_managed_object(
            'custom_resource_definition',
            name,
            my_output=my_output,
            prompt='Wait for %s %s [timeout:%ss]' % (prompt, name, max_time),
            max_time=max_time
        )

    def wait_no_custom_resource_definition(self, name, max_time=180, prompt='CustomResourceDefinition', optional=False, my_output=None, log_error_on_timeout=False):
        return self.wait_no_managed_object(
            'custom_resource_definition',
            name,
            my_output=my_output,
            prompt='Wait for no %s %s [timeout:%ss]' % (prompt, name, max_time),
            max_time=max_time,
            optional=optional,
            log_error_on_timeout=log_error_on_timeout
        )
