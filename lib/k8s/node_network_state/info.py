from lib import filter_helper
from lib.workflow.ocp_interface_state_up import get as ocp_workflow


class K8sNodeNetworkStateInfo():
    def __init__(self):
        self.node_network_state = None
        self.node_network_state_interface_up = None

    def get_node_network_state_info(self, managed_object):
        if managed_object is None:
            return None

        info = self.get_base_info(managed_object)
        info.update(self.get_node_network_state_interfaces_info(managed_object))
        info['dns'] = self.get_node_network_state_dns_info(managed_object)
        info['route'] = self.get_node_network_state_route_info(managed_object)
        return info

    def get_node_network_states_info(self, cache_enabled=True):
        if cache_enabled:
            if self.node_network_state is not None:
                return self.node_network_state

        managed_objects = self.get_node_network_state_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.node_network_state = []
        for managed_object in managed_objects:
            node_network_state_info = {}
            node_network_state_info['info'] = self.get_node_network_state_info(
                managed_object
            )
            node_network_state_info['mo'] = managed_object
            self.node_network_state.append(
                node_network_state_info
            )

        return self.node_network_state

    def match_node_network_state(self, node_network_state_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, node_network_state_info['name']):
                    return False

            if key.startswith('interface-'):
                key_found = True

            if not key_found:
                self.log.error(
                    'match_node_network_state',
                    'Unsupported key: %s' % (key)
                )

        return True

    def match_node_network_state_interface(self, node_network_state_interface_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True

            if key == 'interface-type':
                key_found = True
                if not filter_helper.match_string(value, node_network_state_interface_info['interface']):
                    return False

            if not key_found:
                self.log.error(
                    'match_node_network_state_interface',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_node_network_states(self, object_filter=None, return_mo=False, cluster_name=None, fixup=False, cache_enabled=True):
        if fixup and cluster_name is not None:
            if cache_enabled and self.node_network_state_interface_up is None or not cache_enabled:
                params = {}
                params['cluster'] = self.cluster_name
                self.node_network_state_interface_up = ocp_workflow.run(params, log_id=self.log_id)

        all_node_network_states = self.get_node_network_states_info(cache_enabled=cache_enabled)
        if all_node_network_states is None:
            return None

        node_network_states = []

        for node_network_state_info in all_node_network_states:
            if not self.match_node_network_state(node_network_state_info['info'], object_filter):
                continue

            if return_mo:
                node_network_states.append(
                    node_network_state_info['mo']
                )
                continue

            interfaces_info = []
            for node_network_state_interface_info in node_network_state_info['info']['interface']:
                if not self.match_node_network_state_interface(node_network_state_interface_info, object_filter):
                    continue

                interfaces_info.append(
                    node_network_state_interface_info
                )

            node_network_state_info['info']['interface'] = interfaces_info

            node_network_states.append(
                node_network_state_info['info']
            )

        return node_network_states

    def is_node_network_state(self, name, cache_enabled=True):
        if self.get_node_network_state(name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_node_network_state(self, node_name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'name:%s' % (node_name)
        )
        node_network_states = self.get_node_network_states(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if node_network_states is None:
            return None

        if len(node_network_states) == 1:
            return node_network_states[0]

        return None
