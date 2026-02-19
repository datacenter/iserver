import yaml
from menu.common import get_confirmation


class K8sNemoGuardrailCreate():
    def __init__(self):
        pass

    def create_nemo_guardrail(self, body, my_output=None, confirmation=False, wait=True):
        if my_output is None:
            confirmation = False

        namespace = body['metadata']['namespace']
        name = body['metadata']['name']
        if my_output is not None:
            my_output.default('Create nim build', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))

        if self.is_nemo_guardrail(namespace, name, cache_enabled=False):
            if my_output is not None:
                my_output.default('- already exists')
                return True
        
        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        if not self.create_nemo_guardrail_mo(body):
            if my_output is not None:
                my_output.error('nim build create failed')
            return False

        if my_output is not None:
            my_output.default('nim build created', before_newline=True, after_newline=True)

        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('Wait for nim build...')

        if not self.wait_nemo_guardrail(namespace, name, max_time=30):
            if my_output is not None:
                my_output.error('Timed out')
            
            return False

        return True    