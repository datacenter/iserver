class InterfacePhyEpgStatsApi():
    def __init__(self):
        self.interface_phy_epg_stats_mo = {}

    def get_interface_phy_epg_stats_mo(self, pod_id, node_id, interface_id):
        key = '%s.%s.%s' % (
            pod_id,
            node_id,
            '.'.join(interface_id.split('/'))
        )
        if key in self.interface_phy_epg_stats_mo:
            return self.interface_phy_epg_stats_mo[key]

        cache = self.get_object_cache(
            'l1EthIfToEPg',
            object_selector=key
        )
        if cache is not None:
            self.interface_phy_epg_stats_mo[key] = cache
            self.log.apic_mo(
                'l1EthIfToEPg.%s' % (key),
                self.interface_phy_epg_stats_mo[key]
            )
            return self.interface_phy_epg_stats_mo[key]

        distinguished_name = 'topology/pod-%s/node-%s/sys/phys-[%s]' % (
            pod_id,
            node_id,
            interface_id
        )
        query = 'rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg'

        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_interface_phy_epg_stats_mo',
                'API failed'
            )
            return None

        self.interface_phy_epg_stats_mo[key] = []
        for managed_object in managed_objects['imdata']:
            if 'children' in managed_object['l1PhysIf']:
                for deploy_child in managed_object['l1PhysIf']['children']:
                    for resource_child in deploy_child['pconsCtrlrDeployCtx']['children']:
                        epg_info = self.get_epg(
                            resource_child['pconsResourceCtx']['attributes']['ctxDn']
                        )
                        if epg_info is not None:
                            self.interface_phy_epg_stats_mo[key].append(
                                epg_info
                            )

        self.interface_phy_epg_stats_mo[key] = sorted(
            self.interface_phy_epg_stats_mo[key],
            key=lambda i: i['name'].lower()
        )

        self.log.apic_mo(
            'l1EthIfToEPg.%s' % (key),
            self.interface_phy_epg_stats_mo[key]
        )

        self.set_object_cache(
            'l1EthIfToEPg',
            self.interface_phy_epg_stats_mo[key],
            object_selector=key
        )

        return self.interface_phy_epg_stats_mo[key]
