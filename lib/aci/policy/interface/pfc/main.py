from lib import log_helper
from lib.aci.policy.interface.pfc.attachment import PolicyInterfacePfcAttachment


class PolicyInterfacePfc(PolicyInterfacePfcAttachment):
    def __init__(self, log_id=None):
        PolicyInterfacePfcAttachment.__init__(self)
        self.log = log_helper.Log(log_id=log_id)
        self.mo_policy_interface_pfc = None

    def initialize_policy_interface_pfc(self):
        if not self.initialize_policy_interface_pfc_attachment():
            return False

        if self.mo_policy_interface_pfc is not None:
            return True

        self.mo_policy_interface_pfc = self.get_policy_interface_attributes('qosPfcIfPol')
        if self.mo_policy_interface_pfc is None:
            return False

        return True

    def get_policy_interface_pfc_info(self, managed_object):
        # "adminSt": "auto",
        # "annotation": "",
        # "childAction": "",
        # "descr": "",
        # "dn": "uni/infra/pfc-default",
        # "extMngdBy": "",
        # "lcOwn": "local",
        # "modTs": "2020-12-09T19:07:28.202+01:00",
        # "name": "default",
        # "nameAlias": "",
        # "ownerKey": "",
        # "ownerTag": "",
        # "status": "",
        # "uid": "0",
        # "userdom": ""
        keys = [
            'adminSt',
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

        info['references'] = len(
            info['relnFrom']
        )
        info['l1RsQosPfcIfPolCons'] = self.get_policy_interface_pfc_attachments(managed_object)
        info['interfaces'] = len(
            info['l1RsQosPfcIfPolCons']
        )

        info['nodeInterfaces'] = self.get_policy_interface_node_interfaces(
            info['l1RsQosPfcIfPolCons']
        )

        return info

    def get_policy_interface_pfc(self, pfc_policy_name=None):
        if self.mo_policy_interface_pfc is None:
            if not self.initialize_policy_interface_pfc():
                self.log.error(
                    'get_policy_interface_pfc',
                    'Managed objects must be initialized first'
                )
                return None

        policy = []

        for managed_object in self.mo_policy_interface_pfc:
            policy_info = self.get_policy_interface_pfc_info(managed_object)
            policy.append(policy_info)

        policy = sorted(
            policy,
            key=lambda i: i['name'].lower()
        )

        if pfc_policy_name is not None:
            for pfc_policy in policy:
                if pfc_policy['name'] == pfc_policy_name:
                    self.log.apic_mo(
                        'qosPfcIfPol.info',
                        pfc_policy
                    )
                    return pfc_policy
            return None

        self.log.apic_mo(
            'qosPfcIfPol.info',
            policy
        )

        return policy

    def get_policy_interface_pfc_node(self, node_id, node_ports, pfc_policy_name=None):
        return self.get_policy_interface_node(
            node_id,
            node_ports,
            self.get_policy_interface_pfc(),
            'l1RsQosPfcIfPolCons',
            policy_name=pfc_policy_name
        )
