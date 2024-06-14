class InterfacePortChannelRelationsApi():
    def __init__(self):
        self.interface_pc_relations_mo = {}

    def get_interface_port_channel_relations_mo(self, pod_id, node_id, port_channel_id):
        key = '%s.%s.%s' % (
            pod_id,
            node_id,
            port_channel_id
        )
        if key in self.interface_pc_relations_mo:
            return self.interface_pc_relations_mo[key]

        cache = self.get_object_cache(
            'pcAggrIfRelations',
            object_selector=key
        )
        if cache is not None:
            self.interface_pc_relations_mo[key] = cache
            self.log.apic_mo(
                'pcAggrIfRelations.%s' % (key),
                self.interface_pc_relations_mo[key]
            )
            return self.interface_pc_relations_mo[key]

        distinguished_name = 'topology/pod-%s/node-%s/sys/aggr-[%s]' % (pod_id, node_id, port_channel_id)
        query = 'rsp-subtree-include=relations'

        managed_object = self.get_managed_object(
            distinguished_name,
            query=query
        )

        if managed_object is None:
            self.log.error(
                'get_interface_port_channel_relations',
                'API failed'
            )
            return None

        self.interface_pc_relations_mo[key] = {}
        for section in managed_object['imdata']:
            for section_key in section:
                self.interface_pc_relations_mo[key][section_key] = {}
                for attribute in section[section_key]['attributes']:
                    self.interface_pc_relations_mo[key][section_key][attribute] = section[section_key]['attributes'][attribute]

        self.log.apic_mo(
            'pcAggrIfRelations.%s' % (key),
            self.interface_pc_relations_mo[key]
        )

        self.set_object_cache(
            'pcAggrIfRelations',
            self.interface_pc_relations_mo[key],
            object_selector=key
        )

        return self.interface_pc_relations_mo[key]
