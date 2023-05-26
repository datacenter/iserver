from lib import log_helper
from lib.aci.policy.interface.port_channel_member.attachment import PolicyInterfacePortChannelMemberAttachment


class PolicyInterfacePortChannelMember(PolicyInterfacePortChannelMemberAttachment):
    def __init__(self, log_id=None):
        PolicyInterfacePortChannelMemberAttachment.__init__(self)
        self.log = log_helper.Log(log_id=log_id)
        self.mo_policy_interface_port_channel_member = None

    def initialize_policy_interface_port_channel_member(self):
        if not self.initialize_policy_interface_port_channel_member_attachment():
            return False

        if self.mo_policy_interface_port_channel_member is not None:
            return True

        self.mo_policy_interface_port_channel_member = self.get_policy_interface_attributes('lacpIfPol')
        if self.mo_policy_interface_port_channel_member is None:
            return False

        return True

    def get_policy_interface_port_channel_member_info(self, managed_object):
        # "annotation": "",
        # "childAction": "",
        # "descr": "",
        # "dn": "uni/infra/lacpifp-default",
        # "extMngdBy": "",
        # "lcOwn": "local",
        # "modTs": "2020-12-09T19:07:28.202+01:00",
        # "monPolDn": "uni/fabric/monfab-default",
        # "name": "default",
        # "nameAlias": "",
        # "ownerKey": "",
        # "ownerTag": "",
        # "prio": "32768",
        # "status": "",
        # "txRate": "normal",
        # "uid": "0",
        # "userdom": ""
        keys = [
            'annotation',
            'dn',
            'name',
            'dn',
            'prio',
            'txRate',
            'relnFrom'
        ]
        info = {}
        info['__Output'] = {}

        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        if info['annotation'] == 'orchestrator:terraform':
            info['tf'] = True
            info['tfTick'] = '\u2713'
        else:
            info['tf'] = False
            info['tfTick'] = ''

        info['references'] = len(
            info['relnFrom']
        )
        info['l1RsLacpIfPolCons'] = self.get_policy_interface_port_channel_member_attachments(managed_object)
        info['interfaces'] = len(
            info['l1RsLacpIfPolCons']
        )

        info['nodeInterfaces'] = self.get_policy_interface_node_interfaces(
            info['l1RsLacpIfPolCons']
        )

        return info

    def get_policy_interface_port_channel_member(self, port_channel_member_policy_name=None):
        if self.mo_policy_interface_port_channel_member is None:
            if not self.initialize_policy_interface_port_channel_member():
                self.log.error(
                    'get_policy_interface_port_channel_member',
                    'Managed objects must be initialized first'
                )
                return None

        policy = []

        for managed_object in self.mo_policy_interface_port_channel_member:
            policy_info = self.get_policy_interface_port_channel_member_info(managed_object)
            policy.append(policy_info)

        policy = sorted(
            policy,
            key=lambda i: i['name'].lower()
        )

        if port_channel_member_policy_name is not None:
            for port_channel_member_policy in policy:
                if port_channel_member_policy['name'] == port_channel_member_policy_name:
                    self.log.apic_mo(
                        'lacpIfPol.info',
                        port_channel_member_policy
                    )
                    return port_channel_member_policy
            return None

        self.log.apic_mo(
            'lacpIfPol.info',
            policy
        )

        return policy

    def get_policy_interface_port_channel_member_node(self, node_id, node_ports, port_channel_member_policy_name=None):
        return self.get_policy_interface_node(
            node_id,
            node_ports,
            self.get_policy_interface_port_channel_member(),
            'l1RsLacpIfPolCons',
            policy_name=port_channel_member_policy_name
        )
