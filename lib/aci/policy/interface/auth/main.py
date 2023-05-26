from lib import log_helper
from lib.aci.policy.interface.auth.attachment import PolicyInterfaceAuthAttachment


class PolicyInterfaceAuth(PolicyInterfaceAuthAttachment):
    def __init__(self, log_id=None):
        PolicyInterfaceAuthAttachment.__init__(self)
        self.log = log_helper.Log(log_id=log_id)
        self.mo_policy_interface_auth = None

    def initialize_policy_interface_auth(self):
        if not self.initialize_policy_interface_auth_attachment():
            return False

        if self.mo_policy_interface_auth is not None:
            return True

        self.mo_policy_interface_auth = self.get_policy_interface_attributes('l2PortAuthPol')
        if self.mo_policy_interface_auth is None:
            return False

        return True

    def get_policy_interface_auth_info(self, managed_object):
        # "adminSt": "disabled",
        # "annotation": "",
        # "childAction": "",
        # "descr": "",
        # "dn": "uni/infra/portauthpol-default",
        # "extMngdBy": "",
        # "hostMode": "single-host",
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
            'hostMode',
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
        info['l1RsL2PortAuthCons'] = self.get_policy_interface_auth_attachments(managed_object)
        info['interfaces'] = len(
            info['l1RsL2PortAuthCons']
        )

        info['nodeInterfaces'] = self.get_policy_interface_node_interfaces(
            info['l1RsL2PortAuthCons']
        )

        return info

    def get_policy_interface_auth(self, auth_policy_name=None):
        if self.mo_policy_interface_auth is None:
            if not self.initialize_policy_interface_auth():
                self.log.error(
                    'get_policy_interface_auth',
                    'Managed objects must be initialized first'
                )
                return None

        policy = []

        for managed_object in self.mo_policy_interface_auth:
            policy_info = self.get_policy_interface_auth_info(managed_object)
            policy.append(policy_info)

        policy = sorted(
            policy,
            key=lambda i: i['name'].lower()
        )

        if auth_policy_name is not None:
            for auth_policy in policy:
                if auth_policy['name'] == auth_policy_name:
                    self.log.apic_mo(
                        'l2PortAuthPol.info',
                        auth_policy
                    )
                    return auth_policy
            return None

        self.log.apic_mo(
            'l2PortAuthPol.info',
            policy
        )

        return policy

    def get_policy_interface_auth_node(self, node_id, node_ports, auth_policy_name=None):
        return self.get_policy_interface_node(
            node_id,
            node_ports,
            self.get_policy_interface_auth(),
            'l1RsL2PortAuthCons',
            policy_name=auth_policy_name
        )

    def print_policy_interface_auth(self, info, verbose=False):
        order = [
            'name',
            'tf',
            'adminSt',
            'hostMode',
            'interfaces',
            'references'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Admin State',
            'Host Mode',
            'Interfaces',
            'Ref Policies'
        ]

        self.print_policy_interface(
            info,
            '802.1x Policy Properties',
            order,
            headers,
            verbose
        )

    def print_policies_interface_auth(self, info, verbose=False):
        order = [
            'name',
            'tfTick',
            'adminSt',
            'hostMode'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Admin State',
            'Host Mode'
        ]

        self.print_policies_interface(
            info,
            order,
            headers,
            verbose
        )

    def print_policy_interface_auth_node(self, info):
        order = [
            'policy.name',
            'policy.adminSt',
            'policy.hostMode'
        ]

        headers = [
            '802.1x Policy Name',
            '802.1x Admin State',
            '802.1x Host Mode'
        ]

        self.print_policy_interface_node(
            info,
            order,
            headers
        )
