from menu.common import get_confirmation


class K8sSecretCreate():
    def __init__(self):
        pass

    def create_secret_kv(
            self, 
            namespace, 
            name,
            content, 
            secret_type='Opaque',
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Create Secret', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))

        if self.is_secret(namespace, name, cache_enabled=False):
            if my_output is not None:
                my_output.default(
                    '- already defined'
                )
            return True

        if confirmation:
            if not get_confirmation():
                return False

        if not self.create_secret_kv_mo(namespace, name, content, secret_type=secret_type):
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if my_output is not None:
            my_output.default('Secret created', before_newline=True, after_newline=True)

        if wait:
            if my_output is not None:
                my_output.default('Wait for secret [timeout:60]...')

            if not self.wait_secret(namespace, name, max_time=30):
                if my_output is not None:
                    my_output.error('Timed out')
                
                return False

        return True    
