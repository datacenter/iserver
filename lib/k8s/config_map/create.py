from menu.common import get_confirmation


class K8sConfigMapCreate():
    def __init__(self):
        pass

    def create_config_map_data(
            self, 
            namespace, 
            name,
            destination,
            content, 
            labels=None,
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Create Config Map', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))
            if labels is not None:
                my_output.default('- labels')
                for label in labels:
                    my_output.default('\t%s:%s' % (label, labels[label]))

        if self.is_config_map(namespace, name, cache_enabled=False):
            if my_output is not None:
                my_output.default(
                    '- already defined'
                )
            return True

        if my_output is not None:
            my_output.default('- destination: %s' % (destination))
            my_output.default(content, before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        if not self.create_config_map_data_mo(namespace, name, destination, content, labels=labels):
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if my_output is not None:
            my_output.default('Config map created', before_newline=True, after_newline=True)

        if wait:
            if my_output is not None:
                my_output.default('Wait for config map [timeout:60]...')

            if not self.wait_config_map(namespace, name, max_time=30):
                if my_output is not None:
                    my_output.error('Timed out')
                
                return False

        return True    
