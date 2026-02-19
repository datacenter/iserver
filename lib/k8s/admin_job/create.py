import yaml
from menu.common import get_confirmation


class K8sAdminJobCreate():
    def __init__(self):
        pass

    def create_admin_job(self, body, my_output=None, confirmation=False, wait=True):
        if my_output is None:
            confirmation = False

        namespace = body['metadata']['namespace']
        name = body['metadata']['name']
        if my_output is not None:
            my_output.default('Create admin job', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))

        if self.is_admin_job(namespace, name, cache_enabled=False):
            if my_output is not None:
                my_output.default('- already exists')
                return True
        
        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        if not self.create_admin_job_mo(body):
            if my_output is not None:
                my_output.error('admin job create failed')
            return False

        if my_output is not None:
            my_output.default('admin job created', before_newline=True, after_newline=True)

        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('Wait for admin job...')

        if not self.wait_admin_job(namespace, name, max_time=30):
            if my_output is not None:
                my_output.error('Timed out')
            
            return False

        return True    