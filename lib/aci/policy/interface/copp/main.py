from lib import log_helper
from lib.aci.policy.interface.copp.attachment import PolicyInterfaceCoppAttachment
from lib.aci.policy.interface.copp.protocol import PolicyInterfaceCoppProtocol


class PolicyInterfaceCopp(PolicyInterfaceCoppAttachment, PolicyInterfaceCoppProtocol):
    def __init__(self, log_id=None):
        PolicyInterfaceCoppAttachment.__init__(self)
        PolicyInterfaceCoppProtocol.__init__(self)
        self.log = log_helper.Log(log_id=log_id)
        self.mo_policy_interface_copp = None

    def initialize_policy_interface_copp(self):
        if not self.initialize_policy_interface_copp_attachment():
            return False

        if not self.initialize_policy_interface_copp_protocol():
            return False

        if self.mo_policy_interface_copp is not None:
            return True

        self.mo_policy_interface_copp = self.get_policy_interface_attributes('coppIfPol')
        if self.mo_policy_interface_copp is None:
            return False

        return True

    def get_policy_interface_copp_info(self, managed_object):
        # "annotation": "",
        # "childAction": "",
        # "descr": "",
        # "dn": "uni/infra/coppifpol-default",
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
        info['l1RsCoppIfPolCons'] = self.get_policy_interface_copp_attachments(managed_object)
        info['interfaces'] = len(
            info['l1RsCoppIfPolCons']
        )

        info['nodeInterfaces'] = self.get_policy_interface_node_interfaces(
            info['l1RsCoppIfPolCons']
        )

        info['protocol'] = self.get_policy_interface_copp_protocol()
        info['protocolCount'] = len(info['protocol'])

        return info

    def get_policy_interface_copp(self, copp_policy_name=None):
        if self.mo_policy_interface_copp is None:
            if not self.initialize_policy_interface_copp():
                self.log.error(
                    'get_policy_interface_copp',
                    'Managed objects must be initialized first'
                )
                return None

        policy = []

        for managed_object in self.mo_policy_interface_copp:
            policy_info = self.get_policy_interface_copp_info(managed_object)
            policy.append(policy_info)

        policy = sorted(
            policy,
            key=lambda i: i['name'].lower()
        )

        if copp_policy_name is not None:
            for copp_policy in policy:
                if copp_policy['name'] == copp_policy_name:
                    self.log.apic_mo(
                        'coppIfPol.info',
                        copp_policy
                    )
                    return copp_policy
            return None

        self.log.apic_mo(
            'coppIfPol.info',
            policy
        )

        return policy

    def get_policy_interface_copp_node(self, node_id, node_ports, copp_policy_name=None):
        return self.get_policy_interface_node(
            node_id,
            node_ports,
            self.get_policy_interface_copp(),
            'l1RsCoppIfPolCons',
            policy_name=copp_policy_name
        )
