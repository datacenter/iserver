from lib import log_helper
from lib.aci.policy.interface.cdp.attachment import PolicyInterfaceCdpAttachment


class PolicyInterfaceCdp(PolicyInterfaceCdpAttachment):
    def __init__(self, log_id=None):
        PolicyInterfaceCdpAttachment.__init__(self)
        self.log = log_helper.Log(log_id=log_id)
        self.mo_policy_interface_cdp = None

    def initialize_policy_interface_cdp(self):
        if not self.initialize_policy_interface_cdp_attachment():
            return False

        if self.mo_policy_interface_cdp is not None:
            return True

        self.mo_policy_interface_cdp = self.get_policy_interface_attributes('cdpIfPol')
        if self.mo_policy_interface_cdp is None:
            return False

        return True

    def get_policy_interface_cdp_info(self, managed_object):
        # "adminSt": "disabled",
        # "annotation": "",
        # "childAction": "",
        # "creator": "USER",
        # "descr": "",
        # "dn": "uni/infra/cdpIfP-CDP-disable",
        # "extMngdBy": "",
        # "lcOwn": "local",
        # "modTs": "2020-12-22T18:10:36.611+01:00",
        # "monPolDn": "uni/fabric/monfab-default",
        # "name": "CDP-disable",
        # "nameAlias": "",
        # "ownerKey": "",
        # "ownerTag": "",
        # "status": "",
        # "uid": "15374",
        # "userdom": ":all:common:"
        keys = [
            'adminSt',
            'annotation',
            'creator',
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

        if info['adminSt'] == 'enabled':
            info['__Output']['adminSt'] = 'Green'
        else:
            info['__Output']['adminSt'] = 'Red'

        if info['annotation'] == 'orchestrator:terraform':
            info['tf'] = True
            info['tfTick'] = '\u2713'
        else:
            info['tf'] = False
            info['tfTick'] = ''

        info['references'] = len(
            info['relnFrom']
        )
        info['l1RsCdpIfPolCons'] = self.get_policy_interface_cdp_attachments(managed_object)
        info['interfaces'] = len(
            info['l1RsCdpIfPolCons']
        )

        info['nodeInterfaces'] = self.get_policy_interface_node_interfaces(
            info['l1RsCdpIfPolCons']
        )

        return info

    def get_policy_interface_cdp(self, cdp_policy_name=None):
        if self.mo_policy_interface_cdp is None:
            if not self.initialize_policy_interface_cdp():
                self.log.error(
                    'get_policy_interface_cdp',
                    'Managed objects must be initialized first'
                )
                return None

        policy = []

        for managed_object in self.mo_policy_interface_cdp:
            policy_info = self.get_policy_interface_cdp_info(managed_object)
            policy.append(policy_info)

        policy = sorted(
            policy,
            key=lambda i: i['name'].lower()
        )

        if cdp_policy_name is not None:
            for cdp_policy in policy:
                if cdp_policy['name'] == cdp_policy_name:
                    self.log.apic_mo(
                        'cdpIfPol.info',
                        cdp_policy
                    )
                    return cdp_policy
            return None

        self.log.apic_mo(
            'cdpIfPol.info',
            policy
        )

        return policy

    def get_policy_interface_cdp_node(self, node_id, node_ports, cdp_policy_name=None):
        return self.get_policy_interface_node(
            node_id,
            node_ports,
            self.get_policy_interface_cdp(),
            'l1RsCdpIfPolCons',
            policy_name=cdp_policy_name
        )

