from lib import log_helper
from lib.aci.policy.interface.link_level.attachment import PolicyInterfaceLinkLevelAttachment


class PolicyInterfaceLinkLevel(PolicyInterfaceLinkLevelAttachment):
    def __init__(self, log_id=None):
        PolicyInterfaceLinkLevelAttachment.__init__(self)
        self.log = log_helper.Log(log_id=log_id)
        self.mo_policy_interface_link_level = None

    def initialize_policy_interface_link_level(self):
        if not self.initialize_policy_interface_link_level_attachment():
            return False

        if self.mo_policy_interface_link_level is not None:
            return True

        self.mo_policy_interface_link_level = self.get_policy_interface_attributes('fabricHIfPol')
        if self.mo_policy_interface_link_level is None:
            return False

        return True

    def get_policy_interface_link_level_info(self, managed_object):
        # "annotation": "",
        # "autoNeg": "on",
        # "childAction": "",
        # "creator": "USER",
        # "descr": "Auto Speed and Auto FEC",
        # "dfeDelayMs": "0",
        # "dn": "uni/infra/hintfpol-25G-auto",
        # "emiRetrain": "disable",
        # "extMngdBy": "",
        # "fecMode": "auto-fec",
        # "lcOwn": "local",
        # "linkDebounce": "100",
        # "modTs": "2022-01-28T14:41:55.292+01:00",
        # "monPolDn": "uni/fabric/monfab-default",
        # "name": "25G-auto",
        # "nameAlias": "",
        # "ownerKey": "",
        # "ownerTag": "",
        # "portPhyMediaType": "auto",
        # "speed": "inherit",
        # "status": "",
        # "uid": "15374",
        # "userdom": ":all:common:"
        keys = [
            'annotation',
            'autoNeg',
            'creator',
            'descr',
            'dfeDelayMs',
            'dn',
            'emiRetrain',
            'fecMode',
            'linkDebounce',
            'name',
            'portPhyMediaType',
            'speed',
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
        info['l1RsHIfPolCons'] = self.get_policy_interface_link_level_attachments(managed_object)
        info['interfaces'] = len(
            info['l1RsHIfPolCons']
        )

        info['nodeInterfaces'] = self.get_policy_interface_node_interfaces(
            info['l1RsHIfPolCons']
        )

        return info

    def get_policy_interface_link_level(self, link_level_policy_name=None):
        if self.mo_policy_interface_link_level is None:
            if not self.initialize_policy_interface_link_level():
                self.log.error(
                    'get_policy_interface_link_level',
                    'Managed objects must be initialized first'
                )
                return None

        policy = []

        for managed_object in self.mo_policy_interface_link_level:
            policy_info = self.get_policy_interface_link_level_info(managed_object)
            policy.append(policy_info)

        policy = sorted(
            policy,
            key=lambda i: i['name'].lower()
        )

        if link_level_policy_name is not None:
            for link_level_policy in policy:
                if link_level_policy['name'] == link_level_policy_name:
                    self.log.apic_mo(
                        'fabricHIfPol.info',
                        link_level_policy
                    )
                    return link_level_policy
            return None

        self.log.apic_mo(
            'fabricHIfPol.info',
            policy
        )

        return policy

    def get_policy_interface_link_level_node(self, node_id, node_ports, link_level_policy_name=None):
        return self.get_policy_interface_node(
            node_id,
            node_ports,
            self.get_policy_interface_link_level(),
            'l1RsHIfPolCons',
            policy_name=link_level_policy_name
        )
