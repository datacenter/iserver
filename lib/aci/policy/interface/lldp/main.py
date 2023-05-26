from lib import log_helper
from lib.aci.policy.interface.lldp.attachment import PolicyInterfaceLldpAttachment


class PolicyInterfaceLldp(PolicyInterfaceLldpAttachment):
    def __init__(self, log_id=None):
        PolicyInterfaceLldpAttachment.__init__(self)
        self.log = log_helper.Log(log_id=log_id)
        self.mo_policy_interface_lldp = None

    def initialize_policy_interface_lldp(self):
        if not self.initialize_policy_interface_lldp_attachment():
            return False

        if self.mo_policy_interface_lldp is not None:
            return True

        self.mo_policy_interface_lldp = self.get_policy_interface_attributes('lldpIfPol')
        if self.mo_policy_interface_lldp is None:
            return False

        return True

    def get_policy_interface_lldp_info(self, managed_object):
        # "adminRxSt": "enabled",
        # "adminTxSt": "enabled",
        # "annotation": "",
        # "childAction": "",
        # "creator": "USER",
        # "descr": "",
        # "dn": "uni/fabric/lldpIfP-default",
        # "extMngdBy": "",
        # "lcOwn": "local",
        # "modTs": "2020-12-09T19:07:28.320+01:00",
        # "monPolDn": "uni/fabric/monfab-default",
        # "name": "default",
        # "nameAlias": "",
        # "ownerKey": "",
        # "ownerTag": "",
        # "status": "",
        # "uid": "0",
        # "userdom": ""
        keys = [
            'adminRxSt',
            'adminTxSt',
            'annotation',
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

        if info['adminRxSt'] == 'enabled':
            info['__Output']['adminRxSt'] = 'Green'
        else:
            info['__Output']['adminRxSt'] = 'Red'

        if info['adminTxSt'] == 'enabled':
            info['__Output']['adminTxSt'] = 'Green'
        else:
            info['__Output']['adminTxSt'] = 'Red'

        info['references'] = len(
            info['relnFrom']
        )
        info['l1RsLldpIfPolCons'] = self.get_policy_interface_lldp_attachments(managed_object)
        info['interfaces'] = len(
            info['l1RsLldpIfPolCons']
        )

        info['nodeInterfaces'] = self.get_policy_interface_node_interfaces(
            info['l1RsLldpIfPolCons']
        )

        return info

    def get_policy_interface_lldp(self, lldp_policy_name=None):
        if self.mo_policy_interface_lldp is None:
            if not self.initialize_policy_interface_lldp():
                self.log.error(
                    'get_policy_interface_lldp',
                    'Managed objects must be initialized first'
                )
                return None

        policy = []

        for managed_object in self.mo_policy_interface_lldp:
            policy_info = self.get_policy_interface_lldp_info(managed_object)
            policy.append(policy_info)

        policy = sorted(
            policy,
            key=lambda i: i['name'].lower()
        )

        if lldp_policy_name is not None:
            for lldp_policy in policy:
                if lldp_policy['name'] == lldp_policy_name:
                    self.log.apic_mo(
                        'lldpIfPol.info',
                        lldp_policy
                    )
                    return lldp_policy
            return None

        self.log.apic_mo(
            'lldpIfPol.info',
            policy
        )

        return policy

    def get_policy_interface_lldp_node(self, node_id, node_ports, lldp_policy_name=None):
        return self.get_policy_interface_node(
            node_id,
            node_ports,
            self.get_policy_interface_lldp(),
            'l1RsLldpIfPolCons',
            policy_name=lldp_policy_name
        )
