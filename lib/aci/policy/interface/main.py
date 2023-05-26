import copy

from lib.aci.policy.interface.auth.main import PolicyInterfaceAuth
from lib.aci.policy.interface.cdp.main import PolicyInterfaceCdp
from lib.aci.policy.interface.copp.main import PolicyInterfaceCopp
from lib.aci.policy.interface.dpp.main import PolicyInterfaceDpp
from lib.aci.policy.interface.fc.main import PolicyInterfaceFc
from lib.aci.policy.interface.l2.main import PolicyInterfaceL2
from lib.aci.policy.interface.link_flap.main import PolicyInterfaceLinkFlap
from lib.aci.policy.interface.link_level.main import PolicyInterfaceLinkLevel
from lib.aci.policy.interface.link_level_fc.main import PolicyInterfaceLinkLevelFc
from lib.aci.policy.interface.lldp.main import PolicyInterfaceLldp
from lib.aci.policy.interface.mcp.main import PolicyInterfaceMcp
from lib.aci.policy.interface.pfc.main import PolicyInterfacePfc
from lib.aci.policy.interface.port_channel.main import PolicyInterfacePortChannel
from lib.aci.policy.interface.port_channel_member.main import PolicyInterfacePortChannelMember
from lib.aci.policy.interface.port_security.main import PolicyInterfacePortSecurity
from lib.aci.policy.interface.slow_drain.main import PolicyInterfaceSlowDrain
from lib.aci.policy.interface.storm_control.main import PolicyInterfaceStormControl
from lib.aci.policy.interface.stp.main import PolicyInterfaceStp
from lib.aci.policy.interface.synce.main import PolicyInterfaceSyncE
from lib.aci.policy.interface.transceiver.main import PolicyInterfaceTransceiver


class PolicyInterface(
    PolicyInterfaceAuth,
    PolicyInterfaceCdp,
    PolicyInterfaceCopp,
    PolicyInterfaceDpp,
    PolicyInterfaceFc,
    PolicyInterfaceL2,
    PolicyInterfaceLinkFlap,
    PolicyInterfaceLinkLevel,
    PolicyInterfaceLinkLevelFc,
    PolicyInterfaceLldp,
    PolicyInterfaceMcp,
    PolicyInterfacePfc,
    PolicyInterfacePortChannel,
    PolicyInterfacePortChannelMember,
    PolicyInterfacePortSecurity,
    PolicyInterfaceSlowDrain,
    PolicyInterfaceStormControl,
    PolicyInterfaceStp,
    PolicyInterfaceSyncE,
    PolicyInterfaceTransceiver
    ):
    def __init__(self, log_id=None):
        PolicyInterfaceAuth.__init__(self, log_id=log_id)
        PolicyInterfaceCdp.__init__(self, log_id=log_id)
        PolicyInterfaceCopp.__init__(self, log_id=log_id)
        PolicyInterfaceDpp.__init__(self, log_id=log_id)
        PolicyInterfaceFc.__init__(self, log_id=log_id)
        PolicyInterfaceL2.__init__(self, log_id=log_id)
        PolicyInterfaceLinkFlap.__init__(self, log_id=log_id)
        PolicyInterfaceLinkLevel.__init__(self, log_id=log_id)
        PolicyInterfaceLinkLevelFc.__init__(self, log_id=log_id)
        PolicyInterfaceLldp.__init__(self, log_id=log_id)
        PolicyInterfaceMcp.__init__(self, log_id=log_id)
        PolicyInterfacePfc.__init__(self, log_id=log_id)
        PolicyInterfacePortChannel.__init__(self, log_id=log_id)
        PolicyInterfacePortChannelMember.__init__(self, log_id=log_id)
        PolicyInterfacePortSecurity.__init__(self, log_id=log_id)
        PolicyInterfaceSlowDrain.__init__(self, log_id=log_id)
        PolicyInterfaceStormControl.__init__(self, log_id=log_id)
        PolicyInterfaceStp.__init__(self, log_id=log_id)
        PolicyInterfaceSyncE.__init__(self, log_id=log_id)
        PolicyInterfaceTransceiver.__init__(self, log_id=log_id)

    def get_policy_interface_attributes(self, class_name, dn_filter=None, include_reln=True):
        query = ''
        if include_reln:
            query = 'rsp-subtree=children&rsp-subtree-class=relnFrom'

        managed_objects = self.get_class(
            class_name,
            query=query
        )
        if managed_objects is None:
            return None

        self.log.apic_mo(
            class_name,
            managed_objects['imdata']
        )

        attributes = []

        for managed_object in managed_objects['imdata']:
            managed_object_attributes = managed_object[class_name]['attributes']
            if dn_filter is not None and not managed_object_attributes['dn'].startswith(dn_filter):
                continue

            if include_reln:
                managed_object_attributes['relnFrom'] = self.get_policy_interface_reln(managed_object, class_name)

            attributes.append(
                managed_object_attributes
            )

        self.log.apic_mo(
            '%s.attributes' % (class_name),
            attributes
        )

        return attributes

    def get_policy_interface_attachment_attributes(self, class_name):
        managed_objects = self.get_class(
            class_name
        )
        if managed_objects is None:
            return None

        self.log.apic_mo(
            class_name,
            managed_objects['imdata']
        )

        attributes = []

        for managed_object in managed_objects['imdata']:
            managed_object_attributes = managed_object[class_name]['attributes']
            attributes.append(
                managed_object_attributes
            )

        self.log.apic_mo(
            '%s.attributes' % (class_name),
            attributes
        )

        return attributes

    def get_policy_interface_reference_attributes(self, managed_object):
        # "annotation": "",
        # "childAction": "",
        # "extMngdBy": "",
        # "forceResolve": "yes",
        # "lcOwn": "local",
        # "modTs": "2021-05-19T18:26:53.317+01:00",
        # "monPolDn": "uni/fabric/monfab-default",
        # "rType": "mo",
        # "rn": "rsstormctrlIfPol",
        # "state": "formed",
        # "stateQual": "default-target",
        # "status": "",
        # "tCl": "stormctrlIfPol",
        # "tContextDn": "",
        # "tDn": "uni/infra/stormctrlifp-default",
        # "tRn": "stormctrlifp-default",
        # "tType": "name",
        # "tnStormctrlIfPolName": "",
        # "uid": "0",
        # "userdom": "all"
        keys = [
            'state',
            'tDn',
            'tRn'
        ]
        info = {}
        info['__Output'] = {}

        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        info['name'] = '-'.join(info['tRn'].split('-')[1:])

        return info

    def get_policy_interface_attachment(self, managed_object, managed_objects, interface_type='phys'):
        if managed_objects is None:
            return None

        attachments = []
        for attachment in managed_objects:
            if attachment['tDn'] == managed_object['dn']:
                if attachment['dn'].startswith('topology'):
                    info = {}
                    info['podId'] = attachment['dn'].split('/')[1].split('-')[1]
                    info['nodeId'] = attachment['dn'].split('/')[2].split('-')[1]
                    if 'sys/%s-' % (interface_type) in attachment['dn']:
                        info['portId'] = attachment['dn'].split('sys/%s-[' % (interface_type))[1].split(']')[0]
                        attachments.append(
                            info
                        )

        if interface_type == 'phys':
            attachments = sorted(
                attachments,
                key=lambda i: (
                    i['podId'],
                    int(i['nodeId']),
                    int(i['portId'].split('/')[1])
                )
            )

        if interface_type == 'aggr':
            attachments = sorted(
                attachments,
                key=lambda i: (
                    i['podId'],
                    int(i['nodeId']),
                    int(i['portId'].split('po')[1])
                )
            )

        return attachments

    def get_policy_interface_reln(self, managed_object, interface_class_name):
        attributes = []
        if 'children' in managed_object[interface_class_name]:
            for child in managed_object[interface_class_name]['children']:
                for class_name in child:
                    entry = {}
                    entry['class'] = class_name
                    entry['rn'] = child[class_name]['attributes']['rn']
                    entry['tCl'] = child[class_name]['attributes']['tCl']
                    entry['tDn'] = child[class_name]['attributes']['tDn']
                    entry['policyType'] = self.get_policy_type_from_tcl(
                        child[class_name]['attributes']['tCl']
                    )
                    entry['policyName'] = self.get_policy_name_from_tdn(
                        child[class_name]['attributes']['tDn']
                    )
                    attributes.append(
                        entry
                    )

        attributes = sorted(
            attributes,
            key=lambda i: (
                i['policyType'],
                i['policyName']
            )
        )

        return attributes

    def get_policy_interface_node(self, node_id, node_ports, policy, attachment_class_name, policy_name=None):
        if policy is None:
            return None

        node_ports_policy = []
        for node_port in node_ports:
            info = {}
            info['__Output'] = {}
            info['port'] = node_port
            for key in node_port['__Output']:
                info['__Output']['port.%s' % (key)] = node_port['__Output'][key]
            info['policy'] = {}

            for policy_instance in policy:
                for policy_instance_port in policy_instance[attachment_class_name]:
                    if policy_instance_port['nodeId'] == node_id:
                        if policy_instance_port['portId'].startswith('eth'):
                            if policy_instance_port['portId'] == node_port['id']:
                                info['policy'] = policy_instance
                                for key in policy_instance['__Output']:
                                    info['__Output']['policy.%s' % (key)] = policy_instance['__Output'][key]

                        if policy_instance_port['portId'].startswith('po'):
                            if 'stats' in node_port and node_port['stats'] is not None and 'bundleIndex' in node_port['stats']:
                                if policy_instance_port['portId'] == node_port['stats']['bundleIndex']:
                                    info['policy'] = policy_instance
                                    for key in policy_instance['__Output']:
                                        info['__Output']['policy.%s' % (key)] = policy_instance['__Output'][key]

            if policy_name is None or 'name' in info['policy'] and info['policy']['name'] == policy_name:
                node_ports_policy.append(info)

        node_ports_policy = sorted(
            node_ports_policy,
            key=lambda i: int(i['port']['id'].split('/')[1])
        )

        return node_ports_policy

    def get_policy_interface_node_interfaces(self, managed_objects):
        pod_nodes = {}
        for managed_object in managed_objects:
            if managed_object['podId'] not in pod_nodes:
                pod_nodes[managed_object['podId']] = {}

            if managed_object['nodeId'] not in pod_nodes[managed_object['podId']]:
                pod_nodes[managed_object['podId']][managed_object['nodeId']] = 0
            pod_nodes[managed_object['podId']][managed_object['nodeId']] = pod_nodes[managed_object['podId']][managed_object['nodeId']] + 1

        node_interfaces = []
        for pod_id in pod_nodes:
            for node_id in pod_nodes[pod_id]:
                node_info = {}
                node_info['pod_id'] = pod_id
                node_info['node_id'] = node_id
                node_info['node_name'] = self.get_node_name(node_id)
                node_info['interfacesCount'] = pod_nodes[pod_id][node_id]
                node_interfaces.append(node_info)

        node_interfaces = sorted(
            node_interfaces,
            key=lambda i: (
                i['pod_id'],
                i['node_name']
            )
        )

        return node_interfaces

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
