from menu.common import get_confirmation


class K8sConfigMapUpdate():
    def __init__(self):
        pass

    def set_config_map_data(
            self, 
            namespace, 
            name, 
            content, 
            confirmation=False, 
            my_output=None
        ):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Change Config Map', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))

        config_map_mo = self.get_config_map(namespace, name, return_mo=True, cache_enabled=False)
        if config_map_mo is None:
            if my_output is not None:
                my_output.error('Config map not found')

            return False

        config_map_mo['data'] = content

        if my_output is not None:
            to_show = {}
            to_show['apiVersion'] = 'v1'
            to_show['kind'] = 'ConfigMap'
            to_show['metadata'] = {}
            to_show['metadata']['namespace'] = 'namespace'
            to_show['metadata']['name'] = 'name'
            to_show['data'] = content

            my_output.my_yaml(to_show, before_newline=True, wrap='~~~')
            if confirmation:
                if not get_confirmation():
                    return False

        success = self.set_config_map_mo(config_map_mo)
        if not success:
            if my_output is not None:
                my_output.error('rest api failed')
            return False
        
        if my_output is not None:
            my_output.default('Config map updated')
        return True
