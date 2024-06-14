class PolicyInterfaceTransceiverOutput():
    def __init__(self):
        pass

    def print_policy_interface_transceiver(self, info):
        self.print_policy_interface_transceiver_properties(
            info
        )

        self.print_policy_interface_transceiver_interfaces(
            info['l1RsSynceEthIfPolCons']
        )

    def print_policy_interface_transceiver_properties(self, info):
        order = [
            'name',
            'tf',
            'adminSt',
            'typeT',
            'cdMin',
            'cdMax',
            'dacRate',
            'dwdmCarrier',
            'fecMode',
            'frequency100MHz',
            'frequency50GHz',
            'ituChannel50GHz',
            'modulation',
            'muxponder',
            'transmitPower',
            'wavelength50GHz'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Admin State',
            'Type',
            'Chromatic Dispersion Minimum',
            'Chromatic Dispersion Maximum',
            'DAC Rate',
            'DWDM Carrier Grid Selector',
            'FEC Mode',
            '100MHz Frequency',
            '50GHz Frequency',
            '50GHz ITU Channel',
            'Modulation',
            'Muxponder Mode',
            'Transmit Power',
            '50GHz Wavelength'
        ]

        self.my_output.dictionary(
            info,
            title='Transceiver Policy Properties',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

    def print_policy_interface_transceiver_interfaces(self, info):
        if info is None or len(info) == 0:
            return

        order = [
            'pod_node_name',
            'interfaceId'
        ]

        headers = [
            'Node',
            'Interface'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_policies_interface_transceiver_summary(self, info):
        order = [
            'name',
            'tfTick',
            'adminSt',
            'typeT',
            'interfaces'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Admin State',
            'Type',
            'Interfaces'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_policies_interface_transceiver_usage(self, info):
        order = [
            'name',
            'typeT',
            'nodeInterfaces.pod_node_name',
            'nodeInterfaces.interfaces'
        ]

        headers = [
            'Policy Name',
            'Type',
            'Node',
            'Interface Count'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['nodeInterfaces']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_policies_interface_transceiver_interfaces(self, info):
        order = [
            'name',
            'typeT',
            'l1RsSynceEthIfPolCons.pod_node_name',
            'l1RsSynceEthIfPolCons.interfaceId'
        ]

        headers = [
            'Policy Name',
            'Type',
            'Node',
            'Interface'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['l1RsSynceEthIfPolCons']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
