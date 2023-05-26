from lib import log_helper
from lib.aci.policy.interface.port_channel.attachment import PolicyInterfacePortChannelAttachment


class PolicyInterfacePortChannel(PolicyInterfacePortChannelAttachment):
    def __init__(self, log_id=None):
        PolicyInterfacePortChannelAttachment.__init__(self)
        self.log = log_helper.Log(log_id=log_id)
        self.mo_policy_interface_port_channel = None

    def initialize_policy_interface_port_channel(self):
        if self.mo_policy_interface_port_channel is not None:
            return True

        self.mo_policy_interface_port_channel = self.get_policy_interface_attributes('lacpLagPol')
        if self.mo_policy_interface_port_channel is None:
            return False

        if not self.initialize_policy_interface_port_channel_attachment():
            return False

        return True

    def get_policy_interface_port_channel_info(self, managed_object):
        # "annotation": "",
        # "childAction": "",
        # "creator": "USER",
        # "ctrl": "fast-sel-hot-stdby,graceful-conv,susp-individual",
        # "descr": "",
        # "dn": "uni/infra/lacplagp-LACP-passive",
        # "extMngdBy": "",
        # "lcOwn": "local",
        # "maxLinks": "16",
        # "minLinks": "1",
        # "modTs": "2020-12-22T18:45:43.441+01:00",
        # "mode": "passive",
        # "monPolDn": "uni/fabric/monfab-default",
        # "name": "LACP-passive",
        # "nameAlias": "",
        # "ownerKey": "",
        # "ownerTag": "",
        # "status": "",
        # "uid": "15374",
        # "userdom": ":all:common:"
        keys = [
            'annotation',
            'ctrl',
            'dn',
            'maxLinks',
            'minLinks',
            'mode',
            'name',
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

        info['ctrlT'] = []
        if 'fast-sel-hot-stdby' in info['ctrl'].split(','):
            info['ctrlT'].append('Fast Select Hot Standby Ports')
        if 'graceful-conv' in info['ctrl'].split(','):
            info['ctrlT'].append('Graceful Convergence')
        if 'susp-individual' in info['ctrl'].split(','):
            info['ctrlT'].append('Suspend Individual Ports')

        info['references'] = len(
            info['relnFrom']
        )
        info['l1RsLacpIfPolCons'] = self.get_policy_interface_port_channel_attachments(managed_object)
        info['interfaces'] = len(
            info['l1RsLacpIfPolCons']
        )

        info['nodeInterfaces'] = self.get_policy_interface_node_interfaces(
            info['l1RsLacpIfPolCons']
        )

        return info

    def get_policy_interface_port_channel(self, port_channel_policy_name=None):
        if self.mo_policy_interface_port_channel is None:
            if not self.initialize_policy_interface_port_channel():
                self.log.error(
                    'get_policy_interface_port_channel',
                    'Managed objects must be initialized first'
                )
                return None

        policy = []

        for managed_object in self.mo_policy_interface_port_channel:
            policy_info = self.get_policy_interface_port_channel_info(managed_object)
            policy.append(policy_info)

        policy = sorted(
            policy,
            key=lambda i: i['name'].lower()
        )

        if port_channel_policy_name is not None:
            for port_channel_policy in policy:
                if port_channel_policy['name'] == port_channel_policy_name:
                    self.log.apic_mo(
                        'lacpLagPol.info',
                        port_channel_policy
                    )
                    return port_channel_policy
            return None

        self.log.apic_mo(
            'lacpLagPol.info',
            policy
        )

        return policy

    def get_policy_interface_port_channel_node(self, node_id, node_ports, port_channel_policy_name=None):
        return self.get_policy_interface_node(
            node_id,
            node_ports,
            self.get_policy_interface_port_channel(),
            'l1RsLacpIfPolCons',
            policy_name=port_channel_policy_name
        )
