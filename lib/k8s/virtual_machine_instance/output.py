class K8sVirtualMachineInstanceOutput():
    def __init__(self):
        pass

    def print_virtual_machine_instances_state(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['VM Instance', 'namespace_nameT'],
                ['Node', 'node_name'],
                ['CPU', 'cores'],
                ['Mem', 'memory'],
                ['Disk', 'disk.info'],
                ['PVC', 'disk.pvc_name'],
                ['Interface', 'interface.info'],
                ['Svc', 'serviceCount'],
                ['State', 'phaseT'],
                ['Age', 'age']
            ]
        )

    def print_virtual_machine_instances_metadata(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['VM Instance', 'namespace_nameT'],
                ['Owner', 'ownerT'],
                ['Label', 'labelT'],
                ['Annotation', 'annotationT']
            ]
        )

    def print_virtual_machine_instances_phase(self, info, title=False):
        if title:
            self.my_output.default(
                'Virtual Machine Instance - Phase Transitions [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'namespace_name',
            'phaseT',
            'phase_transitions.phase',
            'phase_transitions.phaseTransitionTimestamp',
            'age'
        ]

        headers = [
            'VMI',
            'State',
            'Phase',
            'Timestamp',
            'Age'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['phase_transitions']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_virtual_machine_instances_net(self, info):
        interfaces = []
        for item in info:
            for item_interface in item['interface']:
                interface = {}
                interface['namespace_name'] = item['namespace_name']
                for key in ['info', 'mac', 'network_name', 'resource_name', 'vlanT']:
                    interface[key] = '--'
                    if key in item_interface:
                        interface[key] = item_interface[key]
                        if interface[key] is None:
                            interface[key] = '--'

                for key in ['ipamT']:
                    interface[key] = ['--']
                    if key in item_interface:
                        interface[key] = item_interface[key]

                interfaces.append(interface)

        order = [
            'namespace_name',
            'info',
            'mac',
            'network_name',
            'resource_name',
            'vlanT',
            'ipamT'
        ]

        headers = [
            'VMI',
            'Interface',
            'MAC',
            'Multus Network',
            'Resource Name',
            'VLAN',
            'IPAM'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                interfaces,
                order,
                ['ipamT']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_virtual_machine_instances_svc(self, info):
        order = [
            'namespace_name',
            'service.namespace_name',
            'service.type',
            'service.cluster_ip',
            'service.ports'
        ]

        headers = [
            'VMI',
            'Service',
            'Type',
            'Cluster IP',
            'Ports'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['service']
            ),
            order=order,
            headers=headers,
            row_separator=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
