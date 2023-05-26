from lib import log_helper
from lib.aci.policy.interface.link_flap.attachment import PolicyInterfaceLinkFlapAttachment


class PolicyInterfaceLinkFlap(PolicyInterfaceLinkFlapAttachment):
    def __init__(self, log_id=None):
        PolicyInterfaceLinkFlapAttachment.__init__(self)
        self.log = log_helper.Log(log_id=log_id)
        self.mo_policy_interface_link_flap = None

    def initialize_policy_interface_link_flap(self):
        if not self.initialize_policy_interface_link_flap_attachment():
            return False

        if self.mo_policy_interface_link_flap is not None:
            return True

        self.mo_policy_interface_link_flap = self.get_policy_interface_attributes('fabricLinkFlapPol')
        if self.mo_policy_interface_link_flap is None:
            return False

        return True

    def get_policy_interface_link_flap_info(self, managed_object):
        # "annotation": "",
        # "childAction": "",
        # "descr": "",
        # "dn": "uni/infra/linkflappol-default",
        # "extMngdBy": "",
        # "lcOwn": "local",
        # "linkFlapErrorMax": "30",
        # "linkFlapErrorSeconds": "420",
        # "modTs": "2020-12-09T19:07:28.202+01:00",
        # "monPolDn": "uni/fabric/monfab-default",
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
            'linkFlapErrorMax',
            'linkFlapErrorSeconds',
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
        info['l1RsFLinkFlapPolCons'] = self.get_policy_interface_link_flap_attachments(managed_object)
        info['interfaces'] = len(
            info['l1RsFLinkFlapPolCons']
        )

        info['nodeInterfaces'] = self.get_policy_interface_node_interfaces(
            info['l1RsFLinkFlapPolCons']
        )

        return info

    def get_policy_interface_link_flap(self, link_flap_policy_name=None):
        if self.mo_policy_interface_link_flap is None:
            if not self.initialize_policy_interface_link_flap():
                self.log.error(
                    'get_policy_interface_link_flap',
                    'Managed objects must be initialized first'
                )
                return None

        policy = []

        for managed_object in self.mo_policy_interface_link_flap:
            policy_info = self.get_policy_interface_link_flap_info(managed_object)
            policy.append(policy_info)

        policy = sorted(
            policy,
            key=lambda i: i['name'].lower()
        )

        if link_flap_policy_name is not None:
            for link_flap_policy in policy:
                if link_flap_policy['name'] == link_flap_policy_name:
                    self.log.apic_mo(
                        'fabricLinkFlapPol.info',
                        link_flap_policy
                    )
                    return link_flap_policy
            return None

        self.log.apic_mo(
            'fabricLinkFlapPol.info',
            policy
        )

        return policy

    def get_policy_interface_link_flap_node(self, node_id, node_ports, link_flap_policy_name=None):
        return self.get_policy_interface_node(
            node_id,
            node_ports,
            self.get_policy_interface_link_flap(),
            'l1RsFLinkFlapPolCons',
            policy_name=link_flap_policy_name
        )
