import copy

from lib.aci.policy.interface.auth.output import PolicyInterfaceAuthOutput
from lib.aci.policy.interface.cdp.output import PolicyInterfaceCdpOutput
from lib.aci.policy.interface.copp.output import PolicyInterfaceCoppOutput
from lib.aci.policy.interface.dpp.output import PolicyInterfaceDppOutput
from lib.aci.policy.interface.fc.output import PolicyInterfaceFcOutput
from lib.aci.policy.interface.l2.output import PolicyInterfaceL2Output
from lib.aci.policy.interface.link_flap.output import PolicyInterfaceLinkFlapOutput
from lib.aci.policy.interface.link_level.output import PolicyInterfaceLinkLevelOutput
from lib.aci.policy.interface.link_level_fc.output import PolicyInterfaceLinkLevelFcOutput
from lib.aci.policy.interface.lldp.output import PolicyInterfaceLldpOutput
from lib.aci.policy.interface.mcp.output import PolicyInterfaceMcpOutput
from lib.aci.policy.interface.pfc.output import PolicyInterfacePfcOutput
from lib.aci.policy.interface.port_channel.output import PolicyInterfacePortChannelOutput
from lib.aci.policy.interface.port_channel_member.output import PolicyInterfacePortChannelMemberOutput
from lib.aci.policy.interface.port_security.output import PolicyInterfacePortSecurityOutput
from lib.aci.policy.interface.slow_drain.output import PolicyInterfaceSlowDrainOutput
from lib.aci.policy.interface.storm_control.output import PolicyInterfaceStormControlOutput
from lib.aci.policy.interface.stp.output import PolicyInterfaceStpOutput
from lib.aci.policy.interface.synce.output import PolicyInterfaceSynceOutput
from lib.aci.policy.interface.transceiver.output import PolicyInterfaceTransceiverOutput


class PolicyInterfaceOutput(
    PolicyInterfaceAuthOutput,
    PolicyInterfaceCdpOutput,
    PolicyInterfaceCoppOutput,
    PolicyInterfaceDppOutput,
    PolicyInterfaceFcOutput,
    PolicyInterfaceL2Output,
    PolicyInterfaceLinkFlapOutput,
    PolicyInterfaceLinkLevelOutput,
    PolicyInterfaceLinkLevelFcOutput,
    PolicyInterfaceLldpOutput,
    PolicyInterfaceMcpOutput,
    PolicyInterfacePfcOutput,
    PolicyInterfacePortChannelOutput,
    PolicyInterfacePortChannelMemberOutput,
    PolicyInterfacePortSecurityOutput,
    PolicyInterfaceSlowDrainOutput,
    PolicyInterfaceStormControlOutput,
    PolicyInterfaceStpOutput,
    PolicyInterfaceSynceOutput,
    PolicyInterfaceTransceiverOutput
    ):
    def __init__(self):
        PolicyInterfaceAuthOutput.__init__(self)
        PolicyInterfaceCdpOutput.__init__(self)
        PolicyInterfaceCoppOutput.__init__(self)
        PolicyInterfaceDppOutput.__init__(self)
        PolicyInterfaceFcOutput.__init__(self)
        PolicyInterfaceL2Output.__init__(self)
        PolicyInterfaceLinkFlapOutput.__init__(self)
        PolicyInterfaceLinkLevelOutput.__init__(self)
        PolicyInterfaceLinkLevelFcOutput.__init__(self)
        PolicyInterfaceLldpOutput.__init__(self)
        PolicyInterfaceMcpOutput.__init__(self)
        PolicyInterfacePfcOutput.__init__(self)
        PolicyInterfacePortChannelOutput.__init__(self)
        PolicyInterfacePortChannelMemberOutput.__init__(self)
        PolicyInterfacePortSecurityOutput.__init__(self)
        PolicyInterfaceSlowDrainOutput.__init__(self)
        PolicyInterfaceStormControlOutput.__init__(self)
        PolicyInterfaceStpOutput.__init__(self)
        PolicyInterfaceSynceOutput.__init__(self)
        PolicyInterfaceTransceiverOutput.__init__(self)

    def print_policy_interface_reln_from(self, info):
        order = [
            'policyType',
            'policyName'
        ]

        headers = [
            'Policy Type',
            'Policy Name'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_policy_interface_node_interfaces(self, info, verbose):
        if verbose:
            node_ports = []
            for node in info:
                node_ports = node_ports + node['interfaces']

            order = [
                'port.podId',
                'port.nodeName',
                'port.id',
                'port.adminSt',
                'port.stats.operSt',
                'port.portT',
                'port.stats.bundleIndex'
            ]

            headers = [
                'Pod',
                'Node',
                'Port',
                'Admin State',
                'Oper State',
                'Port Type',
                'Port Channel'
            ]

            self.my_output.my_table(
                node_ports,
                order=order,
                headers=headers,
                allow_order_subkeys=True,
                underline=True,
                table=True
            )

        if not verbose:
            order = [
                'pod_id',
                'node_name',
                'interfacesCount'
            ]

            headers = [
                'Pod',
                'Node',
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

    def print_policy_interface(self, info, title, order, headers, verbose):
        self.my_output.dictionary(
            info,
            title=title,
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

        if 'relnFrom' in info:
            self.print_policy_interface_reln_from(info['relnFrom'])

        if 'nodeInterfaces' in info:
            self.print_policy_interface_node_interfaces(info['nodeInterfaces'], verbose)

    def print_policies_interface(self, info, order, headers, verbose, expand_lists=None):
        if not verbose:
            order.append('interfaces')
            headers.append('Interfaces')
            order.append('references')
            headers.append('Ref Policies')

            if expand_lists is not None:
                self.my_output.my_table(
                    self.my_output.expand_lists(
                        info,
                        order,
                        expand_lists
                    ),
                    order=order,
                    headers=headers,
                    allow_order_subkeys=True,
                    underline=True,
                    table=True
                )
            else:
                self.my_output.my_table(
                    info,
                    order=order,
                    headers=headers,
                    allow_order_subkeys=True,
                    underline=True,
                    table=True
                )

        if verbose:
            order.append('nodeInterfaces.node_name')
            headers.append('Node Name')
            order.append('nodeInterfaces.interfacesCount')
            headers.append('Interfaces')
            order.append('relnFrom.policyType')
            headers.append('Ref Policy Type')
            order.append('relnFrom.policyName')
            headers.append('Ref Policy Name')

            if expand_lists is not None:
                expand_lists = expand_lists + ['relnFrom', 'nodeInterfaces']
            else:
                expand_lists = ['relnFrom', 'nodeInterfaces']

            self.my_output.my_table(
                self.my_output.expand_lists(
                    info,
                    order,
                    expand_lists
                ),
                order=order,
                headers=headers,
                allow_order_subkeys=True,
                underline=True,
                table=True
            )

    def print_policy_interface_node(self, info, order, headers, include_no_policy=False, expand_lists=None):
        if not include_no_policy:
            info_filtered = []
            for item in info:
                if 'policy' not in item:
                    continue

                if len(item['policy']) == 0:
                    continue

                info_filtered.append(item)

            info = copy.deepcopy(info_filtered)

        base_order = [
            'port.id',
            'port.adminSt',
            'port.stats.operSt',
            'port.portT',
            'port.stats.bundleIndex'
        ]
        order = base_order + order

        base_headers = [
            'Port',
            'Admin State',
            'Oper State',
            'Port Type',
            'Port Channel'
        ]
        headers = base_headers + headers

        if expand_lists is not None:
            self.my_output.my_table(
                self.my_output.expand_lists(
                    info,
                    order,
                    expand_lists
                ),
                order=order,
                headers=headers,
                allow_order_subkeys=True,
                underline=True,
                table=True
            )
        else:
            self.my_output.my_table(
                info,
                order=order,
                headers=headers,
                allow_order_subkeys=True,
                underline=True,
                table=True
            )
