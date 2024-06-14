from lib import filter_helper


class K8sNodeNetworkConfigurationEnactmentInfo():
    def __init__(self):
        self.node_network_configuration_enactment = None

    def get_node_network_configuration_enactment_info(self, node_network_configuration_enactment_mo):
        if node_network_configuration_enactment_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            node_network_configuration_enactment_mo
        )
        info.update(metadata_info)

        return info

    def get_node_network_configuration_enactments_info(self, cache_enabled=True):
        if cache_enabled:
            if self.node_network_configuration_enactment is not None:
                return self.node_network_configuration_enactment

        managed_objects = self.get_node_network_configuration_enactment_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.node_network_configuration_enactment = []
        for managed_object in managed_objects:
            node_network_configuration_enactment_info = {}
            node_network_configuration_enactment_info['info'] = self.get_node_network_configuration_enactment_info(
                managed_object
            )
            node_network_configuration_enactment_info['mo'] = managed_object
            self.node_network_configuration_enactment.append(
                node_network_configuration_enactment_info
            )

        return self.node_network_configuration_enactment

    def match_node_network_interface_state_state(self, node_network_interface_state_state_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True

            if not key_found:
                self.log.error(
                    'match_node_network_interface_state_state',
                    'Unsupported key: %s' % (key)
                )

        return True

    def match_node_network_configuration_enactment(self, node_network_configuration_enactment_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, node_network_configuration_enactment_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_node_network_configuration_enactment',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_node_network_configuration_enactments(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_node_network_configuration_enactments = self.get_node_network_configuration_enactments_info(cache_enabled=cache_enabled)
        if all_node_network_configuration_enactments is None:
            return None

        node_network_configuration_enactments = []

        for node_network_configuration_enactment_info in all_node_network_configuration_enactments:
            if not self.match_node_network_configuration_enactment(node_network_configuration_enactment_info['info'], object_filter):
                continue

            if return_mo:
                node_network_configuration_enactments.append(
                    node_network_configuration_enactment_info['mo']
                )
                continue

            node_network_configuration_enactments.append(
                node_network_configuration_enactment_info['info']
            )

        return node_network_configuration_enactments

    def is_node_network_configuration_enactment(self, name, cache_enabled=True):
        if self.get_node_network_configuration_enactment(name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_node_network_configuration_enactment(self, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'name:%s' % (name)
        )
        node_network_configuration_enactments = self.get_node_network_configuration_enactments(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if node_network_configuration_enactments is None:
            return None

        if len(node_network_configuration_enactments) == 1:
            return node_network_configuration_enactments[0]

        return None
