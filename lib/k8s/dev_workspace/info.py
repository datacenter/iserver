from lib import filter_helper


class K8sDevWorkspaceInfo():
    def __init__(self):
        self.dev_workspace = None

    def get_dev_workspace_info(self, managed_object):
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

        if 'Ready' in info['conditions']:
            info['ready'] = True
            info['readyTick'] = '\u2713'
            info['__Output']['readyT'] = 'Green'
            info['__Output']['readyTick'] = 'Green'
        else:
            info['ready'] = False
            info['readyTick'] = '\u2717'
            info['__Output']['readyT'] = 'Red'
            info['__Output']['readyTick'] = 'Red'

        return info

    def get_dev_workspaces_info(self, cache_enabled=True):
        if cache_enabled:
            if self.dev_workspace is not None:
                return self.dev_workspace

        managed_objects = self.get_dev_workspace_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.dev_workspace = []
        for managed_object in managed_objects:
            dev_workspace_info = {}
            dev_workspace_info['info'] = self.get_dev_workspace_info(
                managed_object
            )
            dev_workspace_info['mo'] = managed_object
            self.dev_workspace.append(
                dev_workspace_info
            )

        return self.dev_workspace

    def match_dev_workspace(self, dev_workspace_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, dev_workspace_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, dev_workspace_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_dev_workspace',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_dev_workspaces(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_dev_workspaces = self.get_dev_workspaces_info(cache_enabled=cache_enabled)
        if all_dev_workspaces is None:
            return None

        dev_workspaces = []

        for dev_workspace_info in all_dev_workspaces:
            if not self.match_dev_workspace(dev_workspace_info['info'], object_filter):
                continue

            if return_mo:
                dev_workspaces.append(
                    dev_workspace_info['mo']
                )
                continue

            dev_workspaces.append(
                dev_workspace_info['info']
            )

        return dev_workspaces

    def is_dev_workspace(self, namespace, name, cache_enabled=True):
        if self.get_dev_workspace(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def is_any_dev_workspace(self, cache_enabled=True):
        policies = self.get_dev_workspaces(cache_enabled=cache_enabled)
        if policies is None or len(policies) == 0:
            return False
        return True

    def get_dev_workspace(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        dev_workspaces = self.get_dev_workspaces(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if dev_workspaces is None:
            return None

        if len(dev_workspaces) == 1:
            return dev_workspaces[0]

        return None
