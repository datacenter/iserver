from lib import log_helper


class LacpAdjEp():
    def __init__(self, log_id=None):
        self.log = log_helper.Log(log_id=log_id)
        self.mo_lacp_adj_ep_class = 'lacpAdjEp'
        self.mo_lacp_adj_ep_filter = None
        self.mo_lacp_adj_ep = None

    def initialize_lacp_adjacency_endpoint(self, pod_id, node_id):
        distinguished_name = 'topology/pod-%s/node-%s/sys/lacp/inst' % (
            pod_id,
            node_id
        )

        query = 'query-target=subtree&target-subtree-class=%s' % (
            self.mo_lacp_adj_ep_class
        )

        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query

        )

        if managed_objects is None:
            return False

        self.mo_lacp_adj_ep = []
        for managed_object in managed_objects['imdata']:
            self.mo_lacp_adj_ep.append(
                managed_object[self.mo_lacp_adj_ep_class]['attributes']
            )

        return True

    def get_lacp_adjacency_endpoint_info(self, managed_object):
        keys = [
            'activityFlags',
            'dn',
            'key',
            'name',
            'port',
            'portPrio',
            'status',
            'sysId',
            'sysPrio'
        ]

        info = {}
        info['__Output'] = {}
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        return info

    def get_lacp_adjacency_endpoint(self, pod_id, node_id, interface_id, allow_multiple=True):
        if self.mo_lacp_adj_ep is None:
            if not self.initialize_lacp_adjacency_endpoint(pod_id, node_id):
                self.log.error(
                    'get_lacp_adjacency_endpoint',
                    'Lacp adjacency managed objects must be initialized first'
                )
                return None

        endpoints = []
        for managed_object in self.mo_lacp_adj_ep:
            endpoint_info = self.get_lacp_adjacency_endpoint_info(
                managed_object
            )

            endpoint_info['pod_id'] = pod_id
            endpoint_info['node_id'] = node_id
            endpoint_info['port_id'] = interface_id

            endpoints.append(
                endpoint_info
            )

        if allow_multiple:
            return endpoints

        if len(endpoints) == 0:
            return None

        return endpoints[0]
