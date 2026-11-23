from lib import filter_helper


class K8sDevWorkspaceTemplateInfo():
    def __init__(self):
        self.dev_workspace_template = None

    def get_dev_workspace_template_info(self, managed_object):
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
        return info

    def get_dev_workspace_templates_info(self, cache_enabled=True):
        if cache_enabled:
            if self.dev_workspace_template is not None:
                return self.dev_workspace_template

        managed_objects = self.get_dev_workspace_template_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.dev_workspace_template = []
        for managed_object in managed_objects:
            dev_workspace_template_info = {}
            dev_workspace_template_info['info'] = self.get_dev_workspace_template_info(
                managed_object
            )
            dev_workspace_template_info['mo'] = managed_object
            self.dev_workspace_template.append(
                dev_workspace_template_info
            )

        return self.dev_workspace_template

    def match_dev_workspace_template(self, dev_workspace_template_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, dev_workspace_template_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, dev_workspace_template_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_dev_workspace_template',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_dev_workspace_templates(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_dev_workspace_templates = self.get_dev_workspace_templates_info(cache_enabled=cache_enabled)
        if all_dev_workspace_templates is None:
            return None

        dev_workspace_templates = []

        for dev_workspace_template_info in all_dev_workspace_templates:
            if not self.match_dev_workspace_template(dev_workspace_template_info['info'], object_filter):
                continue

            if return_mo:
                dev_workspace_templates.append(
                    dev_workspace_template_info['mo']
                )
                continue

            dev_workspace_templates.append(
                dev_workspace_template_info['info']
            )

        return dev_workspace_templates

    def is_dev_workspace_template(self, namespace, name, cache_enabled=True):
        if self.get_dev_workspace_template(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def is_any_dev_workspace_template(self, cache_enabled=True):
        policies = self.get_dev_workspace_templates(cache_enabled=cache_enabled)
        if policies is None or len(policies) == 0:
            return False
        return True

    def get_dev_workspace_template(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        dev_workspace_templates = self.get_dev_workspace_templates(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if dev_workspace_templates is None:
            return None

        if len(dev_workspace_templates) == 1:
            return dev_workspace_templates[0]

        return None
