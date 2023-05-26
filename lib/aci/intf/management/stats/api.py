class InterfaceManagementStatsApi():
    def __init__(self):
        self.interface_mgmt_stats_mo = {}

    def get_interface_management_stats_mo(self, pod_id, node_id, interface_id):
        key = '%s.%s.%s' % (
            pod_id,
            node_id,
            interface_id
        )
        if key in self.interface_mgmt_stats_mo:
            return self.interface_mgmt_stats_mo[key]

        distinguished_name = 'topology/pod-%s/node-%s/sys/ipv4/inst/dom-management/if-[%s]' % (
            pod_id,
            node_id,
            interface_id
        )
        query = 'query-target=children&target-subtree-class=ipv4Addr'

        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_interface_management_stats_mo',
                'API failed'
            )
            return None

        if managed_objects['totalCount'] != '1':
            self.log.error(
                'get_interface_management_stats_mo',
                'Unexpected object count'
            )
            return None

        self.interface_mgmt_stats_mo[key] = managed_objects['imdata'][0]['ipv4Addr']['attributes']

        self.log.apic_mo(
            'mgmtStats.%s' % (key),
            self.interface_mgmt_stats_mo[key]
        )

        return self.interface_mgmt_stats_mo[key]
