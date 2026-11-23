from lib import filter_helper


class K8sHookInfo():
    def __init__(self):
        self.hook = None

    def get_hook_info(self, hook_mo):
        if hook_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            hook_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(hook_mo, 'spec')
        info['status'] = self.get(hook_mo, 'status')
        return info
    
    def get_hooks_info(self, cache_enabled=True):
        if cache_enabled:
            if self.hook is not None:
                return self.hook

        managed_objects = self.get_hook_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.hook = []
        for managed_object in managed_objects:
            hook_info = {}
            hook_info['info'] = self.get_hook_info(
                managed_object
            )
            hook_info['mo'] = managed_object
            self.hook.append(
                hook_info
            )

        return self.hook

    def match_hook(self, hook_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, hook_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_namespace_name(value, '%s/%s' % (hook_info['namespace'], hook_info['name'])):
                    return False

            if not key_found:
                self.log.error(
                    'match_hook',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_hooks(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_hooks = self.get_hooks_info(cache_enabled=cache_enabled)
        if all_hooks is None:
            return None

        hooks = []

        for hook_info in all_hooks:
            if not self.match_hook(hook_info['info'], object_filter):
                continue

            if return_mo:
                hooks.append(
                    hook_info['mo']
                )
                continue

            hooks.append(
                hook_info['info']
            )

        return hooks

    def is_hook(self, namespace, name, cache_enabled=True):
        if self.get_hook(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_hook(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        hooks = self.get_hooks(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if hooks is None:
            return None

        if len(hooks) == 1:
            return hooks[0]

        return None
