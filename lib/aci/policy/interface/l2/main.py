from lib import log_helper
from lib.aci.policy.interface.l2.attachment import PolicyInterfaceL2Attachment


class PolicyInterfaceL2(PolicyInterfaceL2Attachment):
    def __init__(self, log_id=None):
        PolicyInterfaceL2Attachment.__init__(self)
        self.log = log_helper.Log(log_id=log_id)
        self.mo_policy_interface_l2 = None

    def initialize_policy_interface_l2(self):
        if not self.initialize_policy_interface_l2_attachment():
            return False

        if self.mo_policy_interface_l2 is not None:
            return True

        self.mo_policy_interface_l2 = self.get_policy_interface_attributes('l2IfPol')
        if self.mo_policy_interface_l2 is None:
            return False

        return True

    def get_policy_interface_l2_info(self, managed_object):
        # "annotation": "",
        # "childAction": "",
        # "descr": "",
        # "dn": "uni/infra/l2IfP-default",
        # "extMngdBy": "",
        # "lcOwn": "local",
        # "modTs": "2020-12-09T19:07:28.202+01:00",
        # "name": "default",
        # "nameAlias": "",
        # "ownerKey": "",
        # "ownerTag": "",
        # "qinq": "disabled",
        # "status": "",
        # "uid": "0",
        # "userdom": "",
        # "vepa": "disabled",
        # "vlanScope": "global"
        keys = [
            'annotation',
            'dn',
            'name',
            'qinq',
            'relnFrom',
            'vepa',
            'vlanScope'
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

        if info['qinq'] == 'enabled':
            info['__Output']['qinq'] = 'Green'
        else:
            info['__Output']['qinq'] = 'Red'

        if info['vepa'] == 'enabled':
            info['__Output']['vepa'] = 'Green'
        else:
            info['__Output']['vepa'] = 'Red'

        info['vlanScopeT'] = ''
        if info['vlanScope'] == 'global':
            info['vlanScopeT'] = 'Global scope'
        if info['vlanScope'] == 'portlocal':
            info['vlanScopeT'] = 'Port Local scope'

        info['references'] = len(
            info['relnFrom']
        )
        info['l1RsL2IfPolCons'] = self.get_policy_interface_l2_attachments(managed_object)
        info['interfaces'] = len(
            info['l1RsL2IfPolCons']
        )

        info['nodeInterfaces'] = self.get_policy_interface_node_interfaces(
            info['l1RsL2IfPolCons']
        )

        return info

    def get_policy_interface_l2(self, l2_policy_name=None):
        if self.mo_policy_interface_l2 is None:
            if not self.initialize_policy_interface_l2():
                self.log.error(
                    'get_policy_interface_l2',
                    'Managed objects must be initialized first'
                )
                return None

        policy = []

        for managed_object in self.mo_policy_interface_l2:
            policy_info = self.get_policy_interface_l2_info(managed_object)
            policy.append(policy_info)

        policy = sorted(
            policy,
            key=lambda i: i['name'].lower()
        )

        if l2_policy_name is not None:
            for l2_policy in policy:
                if l2_policy['name'] == l2_policy_name:
                    self.log.apic_mo(
                        'l2IfPol.info',
                        l2_policy
                    )
                    return l2_policy
            return None

        self.log.apic_mo(
            'l2IfPol.info',
            policy
        )

        return policy

    def get_policy_interface_l2_node(self, node_id, node_ports, l2_policy_name=None):
        return self.get_policy_interface_node(
            node_id,
            node_ports,
            self.get_policy_interface_l2(),
            'l1RsL2IfPolCons',
            policy_name=l2_policy_name
        )
