import json
import copy
from lib import log_helper

from lib.aci.proto.nd.interface_stats import ProtocolNdInterfaceStats


class ProtocolNdInterface(ProtocolNdInterfaceStats):
    def __init__(self, log_id=None):
        ProtocolNdInterfaceStats.__init__(self, log_id=log_id)
        self.log = log_helper.Log(log_id=log_id)

    def get_nd_active_interface_count(self, interfaces):
        count = 0
        for interface in interfaces:
            if 'neighborCount' in interface and interface['neighborCount'] > 0:
                count = count + 1
        return count

    def add_protocol_nd_interface_neighbor_info(self, interfaces, neighbors, remove_no_neighbors=False):
        for interface in interfaces:
            interface['neighborCount'] = 0
            interface_neighbors = []

            for neighbor in neighbors:
                if neighbor['interfaceId'] == interface['id']:
                    interface['neighborCount'] = interface['neighborCount'] + 1
                    interface_neighbors.append(
                        neighbor['sysName']
                    )

            interface['neighborList'] = ', '.join(interface_neighbors)

        if remove_no_neighbors:
            new_interfaces = []
            for interface in interfaces:
                if interface['neighborCount'] > 0:
                    new_interfaces.append(
                        interface
                    )

            interfaces = copy.deepcopy(new_interfaces)

        return interfaces

    def get_protocol_nd_interfaces(self, pod_id, node_id):
        managed_objects = None

        # url: https://apic11o-eu-spdc.cisco.com/api/node/class/topology/pod-1/node-201/ndIf.json?rsp-subtree=children&rsp-subtree-class=ndIf,ndIfStats&rsp-subtree-include=required
        class_name = 'topology/pod-%s/node-%s/ndIf' % (pod_id, node_id)
        query = 'rsp-subtree=children&rsp-subtree-class=ndIf,ndIfStats&rsp-subtree-include=required'
        managed_objects = self.get_class(
            class_name,
            query=query
        )

        if managed_objects is None:
            return None

        nd_interfaces = []
        for managed_object in managed_objects['imdata']:
            if 'ndIf' in managed_object:
                nd_interface = managed_object['ndIf']['attributes']
                for child in managed_object['ndIf']['children']:
                    if 'ndIfStats' in child:
                        nd_interface['stats'] = child['ndIfStats']['attributes']

                nd_interfaces.append(
                    nd_interface
                )

        return nd_interfaces

    def get_protocol_nd_interface_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            if key == 'stats':
                info[key] = self.get_protocol_nd_interface_stats_info(managed_object[key])
                for output_key in info[key]['__Output']:
                    info['__Output']['stats.%s' % (output_key)] = info[key]['__Output'][output_key]
            else:
                info[key] = managed_object[key]

        # topology/pod-1/node-201/sys/nd/inst/dom-cvim4a:cvim4a_VRF/if-[vlan161]
        info['domainName'] = info['dn'].split('/')[6][4:]

        info['__Output']['id'] = 'Yellow'
        if info['adminSt'] == 'enabled':
            info['__Output']['adminSt'] = 'Green'
        else:
            info['__Output']['adminSt'] = 'Red'

        return info

    def get_protocol_nd_interfaces_info(self, pod_id, node_id, interface_id=None):
        managed_objects = self.get_protocol_nd_interfaces(pod_id, node_id)

        info = []
        for managed_object in managed_objects:
            nd_interface_info = self.get_protocol_nd_interface_info(
                managed_object
            )

            if interface_id is None:
                info.append(
                    nd_interface_info
                )

            if interface_id is not None and nd_interface_info['id'] == interface_id:
                return nd_interface_info

        info = sorted(
            info,
            key=lambda i: i['id']
        )

        return info
