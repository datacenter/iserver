from lib import filter_helper


class K8sCustomResourceDefinitionInfo():
    def __init__(self):
        self.custom_resource_definition = None

    def get_custom_resource_definition_info(self, custom_resource_definition_mo):
        if custom_resource_definition_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        return info

    def get_custom_resource_definitions_info(self, cache_enabled=True):
        if cache_enabled:
            if self.custom_resource_definition is not None:
                return self.custom_resource_definition

        managed_objects = self.get_custom_resource_definition_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.custom_resource_definition = []
        for managed_object in managed_objects:
            custom_resource_definition_info = {}
            custom_resource_definition_info['info'] = self.get_custom_resource_definition_info(
                managed_object
            )
            custom_resource_definition_info['mo'] = managed_object
            self.custom_resource_definition.append(
                custom_resource_definition_info
            )

        return self.custom_resource_definition

    def match_custom_resource_definition(self, custom_resource_definition_info, custom_resource_definition_filter):
        if custom_resource_definition_filter is None or len(custom_resource_definition_filter) == 0:
            return True

        for ap_rule in custom_resource_definition_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if not key_found:
                self.log.error(
                    'match_custom_resource_definition',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_custom_resource_definitions(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_custom_resource_definitions = self.get_custom_resource_definitions_info(cache_enabled=cache_enabled)
        if all_custom_resource_definitions is None:
            return None

        custom_resource_definitions = []

        for custom_resource_definition_info in all_custom_resource_definitions:
            if not self.match_custom_resource_definition(custom_resource_definition_info['info'], object_filter):
                continue

            if return_mo:
                custom_resource_definitions.append(
                    custom_resource_definition_info['mo']
                )
                continue

            custom_resource_definitions.append(
                custom_resource_definition_info['info']
            )

        return custom_resource_definitions
