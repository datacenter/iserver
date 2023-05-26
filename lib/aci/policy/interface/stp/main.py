from lib import log_helper
from lib.aci.policy.interface.stp.attachment import PolicyInterfaceStpAttachment


class PolicyInterfaceStp(PolicyInterfaceStpAttachment):
    def __init__(self, log_id=None):
        PolicyInterfaceStpAttachment.__init__(self)
        self.log = log_helper.Log(log_id=log_id)
        self.mo_policy_interface_stp = None

    def initialize_policy_interface_stp(self):
        if not self.initialize_policy_interface_stp_attachment():
            return False

        if self.mo_policy_interface_stp is not None:
            return True

        self.mo_policy_interface_stp = self.get_policy_interface_attributes('stpIfPol')
        if self.mo_policy_interface_stp is None:
            return False

        return True

    def get_policy_interface_stp_info(self, managed_object):
        # "annotation": "",
        # "childAction": "",
        # "ctrl": "bpdu-filter,bpdu-guard",
        # "descr": "",
        # "dn": "uni/infra/ifPol-test",
        # "extMngdBy": "",
        # "lcOwn": "local",
        # "modTs": "2023-02-06T14:52:55.014+01:00",
        # "monPolDn": "uni/fabric/monfab-default",
        # "name": "test",
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

        info['bpduFilter'] = False
        info['bpduFilterTick'] = '\u2717'
        info['bpduGuard'] = False
        info['bpduGuardTick'] = '\u2717'

        if info['ctrl'] is not None:
            if 'bpdu-filter' in info['ctrl'].split(','):
                info['bpduFilter'] = True
                info['bpduFilterTick'] = '\u2713'

            if 'bpdu-guard' in info['ctrl'].split(','):
                info['bpduGuard'] = True
                info['bpduGuardTick'] = '\u2713'

        info['references'] = 0
        if info['relnFrom'] is not None:
            info['references'] = len(
                info['relnFrom']
            )

        info['l1RsFLinkFlapPolCons'] = self.get_policy_interface_stp_attachments(managed_object)
        info['interfaces'] = len(
            info['l1RsFLinkFlapPolCons']
        )

        info['nodeInterfaces'] = self.get_policy_interface_node_interfaces(
            info['l1RsFLinkFlapPolCons']
        )

        return info

    def get_policy_interface_stp(self, stp_policy_name=None):
        if self.mo_policy_interface_stp is None:
            if not self.initialize_policy_interface_stp():
                self.log.error(
                    'get_policy_interface_stp',
                    'Managed objects must be initialized first'
                )
                return None

        policy = []

        for managed_object in self.mo_policy_interface_stp:
            policy_info = self.get_policy_interface_stp_info(managed_object)
            policy.append(policy_info)

        policy = sorted(
            policy,
            key=lambda i: i['name'].lower()
        )

        if stp_policy_name is not None:
            for stp_policy in policy:
                if stp_policy['name'] == stp_policy_name:
                    self.log.apic_mo(
                        'stpIfPol.info',
                        stp_policy
                    )
                    return stp_policy
            return None

        self.log.apic_mo(
            'stpIfPol.info',
            policy
        )

        return policy

    def get_policy_interface_stp_node(self, node_id, node_ports, stp_policy_name=None):
        return self.get_policy_interface_node(
            node_id,
            node_ports,
            self.get_policy_interface_stp(),
            'l1RsFLinkFlapPolCons',
            policy_name=stp_policy_name
        )
