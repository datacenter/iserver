class ProtocolLldpContext():
    def __init__(self):
        pass

    def add_protocol_lldp_adjacency_context(self, context, adjacency_info):
        for item in adjacency_info:
            node_name = self.get_node_name(item['node_id'].split('-')[1])
            if node_name not in context['node'][self.apic_name]:
                context['node'][self.apic_name].append(
                    node_name
                )

            interface_name = '%s:%s:%s' % (
                item['pod_id'],
                item['node_id'],
                item['interface_id']
            )
            if interface_name not in context['interface'][self.apic_name]:
                context['interface'][self.apic_name].append(
                    interface_name
                )

        return context
