class NodeOutput():
    def __init__(self):
        pass

    def print_nodes(self, nodes):
        if len(nodes) == 0:
            return

        order = []
        if self.is_apic:
            order = ['apic']

        order = order + [
            'pod_node_name',
            'id',
            'podId',
            'address',
            'adSt',
            'fabricSt',
            'roleUi',
            'model',
            'serial',
            'version'
        ]

        headers = []
        if self.is_apic:
            headers = ['Apic']

        headers = headers + [
            'Node Name',
            'Node ID',
            'Pod ID',
            'IP Address',
            'Admin State',
            'Fabric State',
            'Role',
            'Model',
            'Serial',
            'Version'
        ]

        self.my_output.my_table(
            nodes,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_nodes_power(self, nodes):
        if len(nodes) == 0:
            return

        power = []
        for node in nodes:
            power = power + node['power']

        order = []
        if self.is_apic:
            order = ['apic']

        order = order + [
            'pod_node_name',
            'slotId',
            'descr',
            'drawnAvg',
            'drawnLast',
            'drawnMax',
            'drawnMin',
            'suppliedAvg',
            'suppliedLast',
            'suppliedMax',
            'suppliedMin'
        ]

        headers = []
        if self.is_apic:
            headers = ['Apic']

        headers = headers + [
            'Node',
            'PSU Slot ID',
            'Description',
            'Drawn Avg',
            'Drawn Last',
            'Drawn Max',
            'Drawn Min',
            'Supplied Avg',
            'Supplied Last',
            'Supplied Max',
            'Supplied Min'
        ]

        self.my_output.my_table(
            power,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_nodes_psu(self, nodes):
        if len(nodes) == 0:
            return

        psu = []
        for node in nodes:
            psu = psu + node['psu']

        order = []
        if self.is_apic:
            order = ['apic']

        order = order + [
            'pod_node_name',
            'slotId',
            'descr',
            'model',
            'ser',
            'drawnCurr',
            'volt',
            'operSt'
        ]

        headers = []
        if self.is_apic:
            headers = ['Apic']

        headers = headers + [
            'Node',
            'PSU Slot ID',
            'Description',
            'Model',
            'Serial Number',
            'Current',
            'Voltage',
            'Oper State'
        ]

        self.my_output.my_table(
            psu,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_nodes_sensor(self, nodes):
        if len(nodes) == 0:
            return

        sensor = []
        for node in nodes:
            sensor = sensor + node['sensor']

        order = []
        if self.is_apic:
            order = ['apic']

        order = order + [
            'pod_node_name',
            'descr',
            'type',
            'value',
            'minorThresh',
            'majorThresh',
            'operSt'
        ]

        headers = []
        if self.is_apic:
            headers = ['Apic']

        headers = headers + [
            'Node',
            'Sensor',
            'Type',
            'Value',
            'Min',
            'Max',
            'Oper State'
        ]

        self.my_output.my_table(
            sensor,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_nodes_system(self, nodes):
        if len(nodes) == 0:
            return

        order = []
        if self.is_apic:
            order = ['apic']

        order = order + [
            'pod_node_name',
            'address',
            'system.inbMgmtCidr',
            'system.inbMgmtGateway',
            'system.oobMgmtCidr',
            'system.oobMgmtGateway',
        ]

        headers = []
        if self.is_apic:
            headers = ['Apic']

        headers = headers + [
            'Node Name',
            'IP Address',
            'Inband IP Address',
            'Inband Gateway',
            'Out of band IP Address',
            'Out of band Gateway'
        ]

        self.my_output.my_table(
            nodes,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_nodes_temp(self, nodes):
        if len(nodes) == 0:
            return

        temp = []
        for node in nodes:
            temp = temp + node['temp']

        order = []
        if self.is_apic:
            order = ['apic']

        order = order + [
            'pod_node_name',
            'sensorName',
            'currentAvg',
            'currentLast',
            'currentMax',
            'currentMax'
        ]

        headers = []
        if self.is_apic:
            headers = ['Apic']

        headers = headers + [
            'Node',
            'Sensor',
            'Avg',
            'Last',
            'Max',
            'Min'
        ]

        self.my_output.my_table(
            temp,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_nodes_intf(self, nodes):
        if len(nodes) == 0:
            return

        order = []
        if self.is_apic:
            order = ['apic']

        order = order + [
            'pod_node_name',
            'interfaces_summary.portSummary',
            'interfaces_summary.uplinkSummary',
            'interfaces_summary.downlinkSummary',
            'interfaces_summary.100MSummary',
            'interfaces_summary.1GSummary',
            'interfaces_summary.10GSummary',
            'interfaces_summary.25GSummary',
            'interfaces_summary.40GSummary',
            'interfaces_summary.100GSummary',
            'interfaces_summary.400GSummary',
        ]

        headers = []
        if self.is_apic:
            headers = ['Apic']

        headers = headers + [
            'Node Name',
            'Ports (Up/Down/Total)',
            'Uplink',
            'Downlink',
            '100M',
            '1G',
            '10G',
            '25G',
            '40G',
            '100G',
            '400G'
        ]

        self.my_output.my_table(
            nodes,
            order=order,
            headers=headers,
            merge=True,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )
