import json
from lib import log_helper


class ProtocolNdNeighbor():
    def __init__(self, log_id=None):
        self.log = log_helper.Log(log_id=log_id)

    def get_protocol_nd_neighbors(self, pod_id, node_id):
        managed_objects = None

        distinguished_name = 'topology/pod-%s/node-%s/sys/nd/inst' % (pod_id, node_id)
        query = 'query-target=subtree&target-subtree-class=ndAdjEp'
        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query
        )

        if managed_objects is None:
            return None

        nd_neighbors = []
        for managed_object in managed_objects['imdata']:
            nd_neighbors.append(
                managed_object['ndAdjEp']['attributes']
            )

        return nd_neighbors

    def get_protocol_nd_neighbor_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            info[key] = managed_object[key]

        # topology/pod-1/node-201/sys/nd/inst/if-[mgmt0]/adj-1
        info['interfaceId'] = info['dn'].split('if-')[1].split(']')[0][1:]
        info['__Output']['interfaceId'] = 'Yellow'

        if info['nativeVlan'] == 'unspecified':
            info['nativeVlan'] = ''

        return info

    def get_protocol_nd_neighbors_info(self, pod_id, node_id, interface_id=None):
        managed_objects = self.get_protocol_nd_neighbors(pod_id, node_id)
        if managed_objects is None:
            return None

        info = []
        for managed_object in managed_objects:
            nbr_info = self.get_protocol_nd_neighbor_info(
                managed_object
            )

            if interface_id is None:
                info.append(
                    nbr_info
                )

            if interface_id is not None and nbr_info['interfaceId'] == interface_id:
                info.append(
                    nbr_info
                )

        info = sorted(
            info,
            key=lambda i: i['sysName']
        )

        return info
