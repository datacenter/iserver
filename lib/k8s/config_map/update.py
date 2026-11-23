from lib import filter_helper


class K8sConfigMapUpdate():
    def __init__(self):
        pass

    def update_config_map(
            self, 
            namespace, 
            name, 
            content, 
            confirmation=False, 
            my_output=None
        ):
        config_map_mo = self.get_config_map(namespace, name, return_mo=True, cache_enabled=False)
        if config_map_mo is None:
            if my_output is not None:
                my_output.error('Config map not found')
            return False

        if filter_helper.compare_dict(config_map_mo['data'], content):
            if my_output is not None:
                my_output.default('Config map data the same, no update required')
            return True
        
        config_map_mo['data'] = content
        config_map_mo = self.cleanup_managed_object(config_map_mo, exclude=['resourceVersion'])
        return self.replace_resource(config_map_mo, object_name='config_map', my_output=my_output, confirmation=confirmation)
