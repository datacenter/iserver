import json


class ProtocolHsrpOutput():
    def __init__(self):
        pass

    def print_proto_hsrp(self, info):
        self.print_proto_hsrp_instance(
            info['instance']
        )

        self.print_proto_hsrp_domains(
            info['domains']
        )

    def print_proto_hsrp_domains(self, info):
        if len(info) == 0:
            return

        order = [
            'pod_node_name',
            'name',
            'interfacesCount'
        ]

        headers = [
            'Node',
            'VRF',
            'Interfaces'
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

    def print_proto_hsrp_domain(self, info):
        order = [
            'name',
            'interfacesCount'
        ]

        headers = [
            'VRF',
            'Interfaces'
        ]

        self.my_output.dictionary(
            info,
            title='HSRP VRF',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

    def print_proto_hsrp_instances(self, info):
        if len(info) == 0:
            return

        order = [
            'instance.pod_node_name',
            'instance.adminSt',
            'instance.operSt'
        ]

        headers = [
            'Node',
            'Admin State',
            'Oper State'
        ]

        self.my_output.my_table(
            info,
            merge=True,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_proto_hsrp_instance(self, info):
        order = [
            'adminSt',
            'operSt'
        ]

        headers = [
            'Admin State',
            'Oper State'
        ]

        self.my_output.dictionary(
            info,
            title='HSRP Instance',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

    def print_proto_hsrp_interfaces(self, info):
        if len(info) == 0:
            return

        self.my_output.default(
            json.dumps(
                info,
                indent=4
            )
        )
