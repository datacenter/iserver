import yaml
from menu.common import get_confirmation


class K8sKnativeServingCreate():
    def __init__(self):
        pass

    def create_knative_serving(self, body, my_output=None, confirmation=False, wait=True):
        if my_output is None:
            confirmation = False

        namespace = body['metadata']['namespace']
        name = body['metadata']['name']
        if my_output is not None:
            my_output.default('Create knative serving', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))

        if self.is_knative_serving(namespace, name, cache_enabled=False):
            if my_output is not None:
                my_output.default('- already exists')
                return True
        
        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        if not self.create_knative_serving_mo(body):
            if my_output is not None:
                my_output.error('Knative serving create failed')
            return False

        if my_output is not None:
            my_output.default('knative serving created', before_newline=True, after_newline=True)

        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('Wait for knative serving...')

        if not self.wait_knative_serving(namespace, name, max_time=30):
            if my_output is not None:
                my_output.error('Timed out')
            
            return False

        return True    