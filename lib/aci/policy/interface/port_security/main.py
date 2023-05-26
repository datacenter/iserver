from lib import log_helper
from lib.aci.policy.interface.port_security.attachment import PolicyInterfacePortSecurityAttachment


class PolicyInterfacePortSecurity(PolicyInterfacePortSecurityAttachment):
    def __init__(self, log_id=None):
        PolicyInterfacePortSecurityAttachment.__init__(self)
        self.log = log_helper.Log(log_id=log_id)
        self.mo_policy_interface_port_security = None

    def initialize_policy_interface_port_security(self):
        if not self.initialize_policy_interface_port_security_attachment():
            return False

        if self.mo_policy_interface_port_security is not None:
            return True

        self.mo_policy_interface_port_security = self.get_policy_interface_attributes('l2PortSecurityPol')
        if self.mo_policy_interface_port_security is None:
            return False

        return True

    def get_policy_interface_port_security_info(self, managed_object):
        # "annotation": "",
        # "childAction": "",
        # "descr": "",
        # "dn": "uni/infra/portsecurityP-default",
        # "extMngdBy": "",
        # "lcOwn": "local",
        # "maximum": "0",
        # "modTs": "2020-12-09T19:07:28.202+01:00",
        # "name": "default",
        # "nameAlias": "",
        # "ownerKey": "",
        # "ownerTag": "",
        # "status": "",
        # "timeout": "60",
        # "uid": "0",
        # "userdom": "",
        # "violation": "protect"
        keys = [
            'annotation',
            'dn',
            'maximum',
            'name',
            'timeout',
            'violation',
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
        info['l1RsL2PortSecurityCons'] = self.get_policy_interface_port_security_attachments(managed_object)
        info['interfaces'] = len(
            info['l1RsL2PortSecurityCons']
        )

        info['nodeInterfaces'] = self.get_policy_interface_node_interfaces(
            info['l1RsL2PortSecurityCons']
        )

        return info

    def get_policy_interface_port_security(self, port_security_policy_name=None):
        if self.mo_policy_interface_port_security is None:
            if not self.initialize_policy_interface_port_security():
                self.log.error(
                    'get_policy_interface_port_security',
                    'Managed objects must be initialized first'
                )
                return None

        policy = []

        for managed_object in self.mo_policy_interface_port_security:
            policy_info = self.get_policy_interface_port_security_info(managed_object)
            policy.append(policy_info)

        policy = sorted(
            policy,
            key=lambda i: i['name'].lower()
        )

        if port_security_policy_name is not None:
            for port_security_policy in policy:
                if port_security_policy['name'] == port_security_policy_name:
                    self.log.apic_mo(
                        'l2PortSecurityPol.info',
                        port_security_policy
                    )
                    return port_security_policy
            return None

        self.log.apic_mo(
            'l2PortSecurityPol.info',
            policy
        )

        return policy

    def get_policy_interface_port_security_node(self, node_id, node_ports, port_security_policy_name=None):
        return self.get_policy_interface_node(
            node_id,
            node_ports,
            self.get_policy_interface_port_security(),
            'l1RsL2PortSecurityCons',
            policy_name=port_security_policy_name
        )
