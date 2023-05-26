class PolicyInterfaceTransceiverOutput():
    def __init__(self):
        pass

    def print_policy_interface_transceiver(self, info, verbose=False):
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

        self.print_policy_interface(
            info,
            'Transceiver Policy Properties',
            order,
            headers,
            verbose
        )

    def print_policies_interface_transceiver(self, info, verbose=False):
        order = [
            'name',
            'tfTick',
            'adminSt',
            'typeT'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Admin State',
            'Type'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
