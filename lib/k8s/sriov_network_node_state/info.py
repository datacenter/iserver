import json

from lib import filter_helper


class K8sSriovNetworkNodeStateInfo():
    def __init__(self):
        self.sriov_network_node_state = None

    def get_sriov_network_node_state_info(self, sriov_network_node_state_mo):
        if sriov_network_node_state_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            sriov_network_node_state_mo
        )
        info.update(metadata_info)

        info['syncStatus'] = self.get(sriov_network_node_state_mo, 'status:syncStatus')
        if info['syncStatus'] == 'Succeeded':
            info['syncStatusTick'] = '\u2713'
            info['__Output']['syncStatusTick'] = 'Green'
        else:
            info['syncStatusTick'] = '\u2717'
            info['__Output']['syncStatusTick'] = 'Red'

        info['interface'] = []

        interfaces_state_mo = self.get(sriov_network_node_state_mo, 'status:interfaces', on_error=[], on_none=[])
        for interface_state_mo in interfaces_state_mo:
            interface_info = {}
            interface_info['name'] = self.get(interface_state_mo, 'name')
            interface_info['numVfs'] = self.get(interface_state_mo, 'totalvfs')
            interface_info['pciAddress'] = self.get(interface_state_mo, 'pciAddress')

            interface_vfs_mo = self.get(interface_state_mo, 'Vfs', on_error=[], on_none=[])
            interface_info['vfs'] = []
            for interface_vf_mo in interface_vfs_mo:
                vf_info = {}
                vf_info['deviceId'] = self.get(interface_vf_mo, 'deviceID')
                vf_info['driver'] = self.get(interface_vf_mo, 'driver')
                vf_info['mac'] = self.get(interface_vf_mo, 'mac')
                vf_info['macT'] = vf_info['mac']
                if vf_info['mac'] is None:
                    vf_info['macT'] = '--'
                vf_info['mtu'] = self.get(interface_vf_mo, 'mtu')
                vf_info['mtuT'] = vf_info['mtu']
                if vf_info['mtu'] is None:
                    vf_info['mtuT'] = '--'
                vf_info['name'] = self.get(interface_vf_mo, 'name')
                vf_info['nameT'] = vf_info['name']
                if vf_info['name'] is None:
                    vf_info['nameT'] = '--'
                vf_info['pciAddress'] = self.get(interface_vf_mo, 'pciAddress')
                vf_info['vendor'] = self.get(interface_vf_mo, 'vendor')
                vf_info['vfId'] = self.get(interface_vf_mo, 'vfID')
                interface_info['vfs'].append(
                    vf_info
                )

            interface_info['vfs'] = sorted(
                interface_info['vfs'],
                key=lambda i: i['vfId']
            )

            interface_info['driver'] = self.get(interface_state_mo, 'driver')
            interface_info['linkSpeed'] = self.get(interface_state_mo, 'linkSpeed')
            interface_info['linkType'] = self.get(interface_state_mo, 'linkType')
            interface_info['mac'] = self.get(interface_state_mo, 'mac')
            interface_info['mtu'] = self.get(interface_state_mo, 'mtu')
            interface_info['totalVfs'] = self.get(interface_state_mo, 'totalvfs')
            interface_info['vendor'] = self.get(interface_state_mo, 'vendor')
            interface_info['vendorT'] = interface_info['vendor']
            if interface_info['vendor'] in self.network_vendor:
                interface_info['vendorT'] = '%s (%s)' % (
                    self.network_vendor[interface_info['vendor']],
                    interface_info['vendor']
                )
            interface_info['deviceId'] = self.get(interface_state_mo, 'deviceID')
            interface_info['deviceIdT'] = interface_info['deviceId']
            if interface_info['vendor'] in self.network_vendor_device:
                if interface_info['deviceId'] in self.network_vendor_device[interface_info['vendor']]:
                    interface_info['deviceIdT'] = '%s (%s)' % (
                        self.network_vendor_device[interface_info['vendor']][interface_info['deviceId']],
                        interface_info['deviceId']
                    )

            interface_info['vfUsed'] = len(
                interface_info['vfs']
            )
            interface_info['vfUsage'] = '%s/%s' % (
                interface_info['vfUsed'],
                interface_info['numVfs']
            )

            interface_info['vfGroups'] = []

            info['interface'].append(
                interface_info
            )

        interfaces_mo = self.get(sriov_network_node_state_mo, 'spec:interfaces', on_error=[], on_none=[])
        for interface_mo in interfaces_mo:
            for interface_info in info['interface']:
                if self.get(interface_mo, 'name') == interface_info['name']:
                    interface_info['vfGroups'] = self.get(interface_mo, 'vfGroups')
                    interface_info['vfGroupsT'] = json.dumps(interface_info['vfGroups'], indent=4).split('\n')

        info['interface'] = sorted(
            info['interface'],
            key=lambda i: i['name']
        )

        return info

    def get_sriov_network_node_states_info(self, cache_enabled=True):
        if cache_enabled:
            if self.sriov_network_node_state is not None:
                return self.sriov_network_node_state

        managed_objects = self.get_sriov_network_node_state_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.sriov_network_node_state = []
        for managed_object in managed_objects:
            sriov_network_node_state_info = {}
            sriov_network_node_state_info['info'] = self.get_sriov_network_node_state_info(
                managed_object
            )
            sriov_network_node_state_info['mo'] = managed_object
            self.sriov_network_node_state.append(
                sriov_network_node_state_info
            )

        return self.sriov_network_node_state

    def match_sriov_network_node_interface_state(self, sriov_network_node_interface_state_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True

            if key == 'name':
                key_found = True

            if key == 'interface':
                key_found = True
                if not filter_helper.match_string(value, sriov_network_node_interface_state_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_sriov_network_node_interface_state',
                    'Unsupported key: %s' % (key)
                )

        return True

    def match_sriov_network_node_interfaces_state(self, sriov_network_node_state_info, object_filter):
        interface = []

        for interface_info in sriov_network_node_state_info['interface']:
            if self.match_sriov_network_node_interface_state(interface_info, object_filter):
                interface.append(
                    interface_info
                )

        return interface

    def match_sriov_network_node_state(self, sriov_network_node_state_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, sriov_network_node_state_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_namespace_name(value, '%s/%s' % (sriov_network_node_state_info['namespace'], sriov_network_node_state_info['name'])):
                    return False

            if key == 'interface':
                key_found = True
                found = False
                for interface_info in sriov_network_node_state_info['interface']:
                    if filter_helper.match_string(value, interface_info['name']):
                        found = True
                        break

                if not found:
                    return False

            if not key_found:
                self.log.error(
                    'match_sriov_network_node_state',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_sriov_network_node_states(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_sriov_network_node_states = self.get_sriov_network_node_states_info(cache_enabled=cache_enabled)
        if all_sriov_network_node_states is None:
            return None

        sriov_network_node_states = []

        for sriov_network_node_state_info in all_sriov_network_node_states:
            if not self.match_sriov_network_node_state(sriov_network_node_state_info['info'], object_filter):
                continue

            sriov_network_node_state_info['info']['interface'] = self.match_sriov_network_node_interfaces_state(
                sriov_network_node_state_info['info'],
                object_filter
            )
            if len(sriov_network_node_state_info['info']['interface']) == 0:
                continue

            if return_mo:
                sriov_network_node_states.append(
                    sriov_network_node_state_info['mo']
                )
                continue

            sriov_network_node_states.append(
                sriov_network_node_state_info['info']
            )

        return sriov_network_node_states

    def is_sriov_network_node_state(self, name, namespace='openshift-sriov-network-operator', cache_enabled=True):
        if self.get_sriov_network_node_state(name, namespace=namespace, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_sriov_network_node_state(self, name, namespace='openshift-sriov-network-operator', return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        sriov_network_node_states = self.get_sriov_network_node_states(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if sriov_network_node_states is None:
            return None

        if len(sriov_network_node_states) == 1:
            return sriov_network_node_states[0]

        return None

    def get_sriov_network_node_state_with_node_interface(self, node_name, interface_name):
        object_filter = []
        object_filter.append(
            'name:%s' % (node_name)
        )
        object_filter.append(
            'interface:%s' % (interface_name)
        )
        state = self.get_sriov_network_node_states(
            object_filter=object_filter
        )
        return state
