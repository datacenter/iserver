from lib import filter_helper
from lib import output_helper


class FiOutput():
    def __init__(self, log_id):
        self.my_output = output_helper.OutputHelper(log_id=log_id)

    def print_state(self, fis, title=False):
        if title:
            self.my_output.default(
                'Fabric Interconnect State Summary [#%s]' % (len(fis)),
                underline=True,
                before_newline=True
            )

        if len(fis) == 0:
            if title:
                self.my_output.default('None')
                return

        order = [
            'Name',
            'SwitchId',
            'Model',
            'Serial',
            'ManagementMode',
            'OperabilityTick',
            'Health',
            'ManagementIp',
            'Version',
            'NumEtherPortsSummary'
        ]

        headers = [
            'Name',
            'SwitchId',
            'Model',
            'Serial',
            'Management',
            'Oper',
            'Health',
            'IP',
            'Version',
            'Ports'
        ]

        self.my_output.my_table(
            fis,
            order=order,
            headers=headers,
            remove_empty_columns=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_eth(self, info, title=False):
        if title:
            self.my_output.default(
                'Fabric Interconnect - Ethernet [%s]' % (info['Name']),
                underline=True,
                before_newline=True
            )

        if len(info['Ethernet']) == 0:
            if title:
                self.my_output.default('None')
                return

        order = [
            'Name',
            'AdminState',
            'OperState',
            'OperSpeed'
            'Mode',
            'Role',
            'SwitchId',
            'MacAddress',
            'TransceiverType',
            'PortChannelId',
            'Peer.ServerName',
            'Peer.ServerPort'
        ]

        headers = [
            'Name',
            'Admin',
            'Oper',
            'Speed'
            'Mode',
            'Role',
            'SwitchId',
            'Mac',
            'Transceiver',
            'PC',
            'Server',
            'Port'
        ]

        self.my_output.my_table(
            info['Ethernet'],
            order=order,
            headers=headers,
            remove_empty_columns=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_pc(self, info, title=False):
        if title:
            self.my_output.default(
                'Fabric Interconnect - Ethernet Port Channel [%s]' % (info['Name']),
                underline=True,
                before_newline=True
            )

        if len(info['EthernetPortChannel']) == 0:
            if title:
                self.my_output.default('None')
                return

        order = [
            'PortChannelId',
            'Name',
            'Role',
            'AdminState',
            'OperState',
            'OperSpeed',
            'MemberSummary'
        ]

        headers = [
            'PortChannelId',
            'Name',
            'Role',
            'AdminState',
            'OperState',
            'OperSpeed',
            'Members'
        ]

        self.my_output.my_table(
            info['EthernetPortChannel'],
            order=order,
            headers=headers,
            remove_empty_columns=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_fc(self, info, title=False):
        if title:
            self.my_output.default(
                'Fabric Interconnect - Fibre Channel [%s]' % (info['Name']),
                underline=True,
                before_newline=True
            )

        if 'FibreChannel' not in info or len(info['FibreChannel']) == 0:
            if title:
                self.my_output.default('None')
                return

        order = [
            'Name'
        ]

        headers = [
            'Name'
        ]

        self.my_output.my_table(
            info['FibreChannel'],
            order=order,
            headers=headers,
            remove_empty_columns=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_fpc(self, info, title=False):
        if title:
            self.my_output.default(
                'Fabric Interconnect - Fibre Port Channel [%s]' % (info['Name']),
                underline=True,
                before_newline=True
            )

        if 'FibrePortChannel' not in info or len(info['FibrePortChannel']) == 0:
            if title:
                self.my_output.default('None')
                return

        order = [
            'Name'
        ]

        headers = [
            'Name'
        ]

        self.my_output.my_table(
            info['FibrePortChannel'],
            order=order,
            headers=headers,
            remove_empty_columns=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
