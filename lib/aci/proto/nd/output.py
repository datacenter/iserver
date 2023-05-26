import json


class ProtocolNdOutput():
    def __init__(self):
        pass

    def print_proto_nd(self, info):
        self.print_proto_nd_instance(
            info['instance']
        )

        self.print_protocol_nd_domains(
            info['domains']
        )

        self.print_proto_nd_neighbors(
            info['neighbors']
        )

        self.print_proto_nd_interfaces(
            info['interfaces']
        )

    def print_protocol_nd_domains(self, info):
        order = [
            'name',
            'interfacesCount',
            'neighborsCount'
        ]

        headers = [
            'VRF',
            'Interfaces',
            'Neighbors'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_protocol_nd_domain(self, info):
        order = [
            'name',
            'interfacesCount',
            'neighborsCount'
        ]

        headers = [
            'VRF',
            'Interfaces',
            'Neighbors'
        ]

        self.my_output.dictionary(
            info,
            title='Neighbor Discovery VRF',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

    def print_proto_nd_instance(self, info):
        order = [
            'pod_node_name',
            'adminSt',
            'agingIntvl',
            'neighborCount',
            'activeInterfaceCount'
        ]

        headers = [
            'Node',
            'Admin State',
            'Aging Interval',
            'Neighbor Count',
            'Active Interface Count'
        ]

        self.my_output.dictionary(
            info,
            title='Neighbor Discovery Instance',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

    def print_proto_nd_instances(self, info):
        order = [
            'instance.pod_node_name',
            'instance.adminSt',
            'instance.agingIntvl',
            'instance.neighborCount',
            'instance.activeInterfaceCount'
        ]

        headers = [
            'Node',
            'Admin State',
            'Aging Interval',
            'Neighbor Count',
            'Active Interface Count'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_protocol_nd_interface_stats(self, info):
        print(info)

    def print_proto_nd_interfaces(self, info):
        if len(info) > 0:
            self.my_output.default(
                json.dumps(
                    info,
                    indent=4
                )
            )

    def print_proto_nd_neighbors(self, info):
        if len(info) > 0:
            self.my_output.default(
                json.dumps(
                    info,
                    indent=4
                )
            )
