class InterfaceLacpStatsApi():
    def __init__(self):
        self.interface_lacp_stats_mo = {}

    def get_interface_lacp_stats_mo(self, pod_id, node_id, interface_id):
        key = '%s.%s.%s' % (pod_id, node_id, interface_id)
        if key in self.interface_lacp_stats_mo:
            return self.interface_lacp_stats_mo[key]

        distinguished_name = 'topology/pod-%s/node-%s/sys/lacp/inst/if-[%s]' % (
            pod_id,
            node_id,
            interface_id
        )
        query = 'query-target=children&target-subtree-class=lacpIfStats'

        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_interface_lacp_stats_mo',
                'API failed'
            )
            return None

        if managed_objects['totalCount'] != '1':
            self.log.error(
                'get_interface_lacp_stats_mo',
                'Unexpected object count'
            )
            return None

        self.interface_lacp_stats_mo[key] = managed_objects['imdata'][0]['lacpIfStats']['attributes']

        self.log.apic_mo(
            'lacpIfStats.%s' % (key),
            self.interface_lacp_stats_mo[key]
        )

        return self.interface_lacp_stats_mo[key]
