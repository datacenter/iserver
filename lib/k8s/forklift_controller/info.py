from lib import filter_helper


class K8sForkliftControllerInfo():
    def __init__(self):
        self.forklift_controller = None

    def get_forklift_controller_info(self, managed_object):
        if managed_object is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            managed_object
        )
        info.update(metadata_info)

        info['spec'] = self.get(managed_object, 'spec')
        info['status'] = self.get(managed_object, 'status')

        info['conditions'] = self.get_conditions(
            self.get(managed_object, 'status:conditions')
        )

        info['ready'] = False
        info['readyTick'] = '\u2717'
        info['__Output']['readyTick'] = 'Red'

        if 'Running' in info['conditions']:
            info['ready'] = True 
            info['readyTick'] = '\u2713'
            info['__Output']['readyTick'] = 'Green'

        return info
    
    def get_forklift_controllers_info(self, cache_enabled=True):
        if cache_enabled:
            if self.forklift_controller is not None:
                return self.forklift_controller

        managed_objects = self.get_forklift_controller_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.forklift_controller = []
        for managed_object in managed_objects:
            forklift_controller_info = {}
            forklift_controller_info['info'] = self.get_forklift_controller_info(
                managed_object
            )
            forklift_controller_info['mo'] = managed_object
            self.forklift_controller.append(
                forklift_controller_info
            )

        return self.forklift_controller

    def match_forklift_controller(self, forklift_controller_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, forklift_controller_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_namespace_name(value, '%s/%s' % (forklift_controller_info['namespace'], forklift_controller_info['name'])):
                    return False

            if not key_found:
                self.log.error(
                    'match_forklift_controller',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_forklift_controllers(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_forklift_controllers = self.get_forklift_controllers_info(cache_enabled=cache_enabled)
        if all_forklift_controllers is None:
            return None

        forklift_controllers = []

        for forklift_controller_info in all_forklift_controllers:
            if not self.match_forklift_controller(forklift_controller_info['info'], object_filter):
                continue

            if return_mo:
                forklift_controllers.append(
                    forklift_controller_info['mo']
                )
                continue

            forklift_controllers.append(
                forklift_controller_info['info']
            )

        return forklift_controllers

    def is_any_forklift_controller(self, cache_enabled=True):
        controllers = self.get_forklift_controllers(cache_enabled=cache_enabled)
        if controllers is None or len(controllers) == 0:
            return False
        return True
    
    def is_forklift_controller(self, namespace, name, cache_enabled=True):
        if self.get_forklift_controller(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_forklift_controller(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        forklift_controllers = self.get_forklift_controllers(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if forklift_controllers is None:
            return None

        if len(forklift_controllers) == 1:
            return forklift_controllers[0]

        return None
