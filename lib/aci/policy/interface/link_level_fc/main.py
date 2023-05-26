from lib import log_helper
from lib.aci.policy.interface.link_level_fc.attachment import PolicyInterfaceLinkLevelFcAttachment


class PolicyInterfaceLinkLevelFc(PolicyInterfaceLinkLevelFcAttachment):
    def __init__(self, log_id=None):
        PolicyInterfaceLinkLevelFcAttachment.__init__(self)
        self.log = log_helper.Log(log_id=log_id)
        self.mo_policy_interface_link_level_fc = None

    def initialize_policy_interface_link_level_fc(self):
        if not self.initialize_policy_interface_link_level_fc_attachment():
            return False

        if self.mo_policy_interface_link_level_fc is not None:
            return True

        self.mo_policy_interface_link_level_fc = self.get_policy_interface_attributes('qosLlfcIfPol')
        if self.mo_policy_interface_link_level_fc is None:
            return False

        return True

    def get_policy_interface_link_level_fc_info(self, managed_object):
        # "annotation": "",
        # "childAction": "",
        # "descr": "",
        # "dn": "uni/infra/llfc-default",
        # "extMngdBy": "",
        # "lcOwn": "local",
        # "llfcRcvAdminSt": "off",
        # "llfcSendAdminSt": "off",
        # "modTs": "2021-03-17T04:02:25.117+01:00",
        # "name": "default",
        # "nameAlias": "",
        # "ownerKey": "",
        # "ownerTag": "",
        # "status": "",
        # "uid": "0",
        # "userdom": "all"
        keys = [
            'annotation',
            'dn',
            'llfcRcvAdminSt',
            'llfcSendAdminSt',
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
        info['l1RsQosLlfcIfPolCons'] = self.get_policy_interface_link_level_fc_attachments(managed_object)
        info['interfaces'] = len(
            info['l1RsQosLlfcIfPolCons']
        )

        info['nodeInterfaces'] = self.get_policy_interface_node_interfaces(
            info['l1RsQosLlfcIfPolCons']
        )

        return info

    def get_policy_interface_link_level_fc(self, link_level_fc_policy_name=None):
        if self.mo_policy_interface_link_level_fc is None:
            if not self.initialize_policy_interface_link_level_fc():
                self.log.error(
                    'get_policy_interface_link_level_fc',
                    'Managed objects must be initialized first'
                )
                return None

        policy = []

        for managed_object in self.mo_policy_interface_link_level_fc:
            policy_info = self.get_policy_interface_link_level_fc_info(managed_object)
            policy.append(policy_info)

        policy = sorted(
            policy,
            key=lambda i: i['name'].lower()
        )

        if link_level_fc_policy_name is not None:
            for link_level_fc_policy in policy:
                if link_level_fc_policy['name'] == link_level_fc_policy_name:
                    self.log.apic_mo(
                        'qosLlfcIfPol.info',
                        link_level_fc_policy
                    )
                    return link_level_fc_policy
            return None

        self.log.apic_mo(
            'qosLlfcIfPol.info',
            policy
        )

        return policy

    def get_policy_interface_link_level_fc_node(self, node_id, node_ports, link_level_fc_policy_name=None):
        return self.get_policy_interface_node(
            node_id,
            node_ports,
            self.get_policy_interface_link_level_fc(),
            'l1RsQosLlfcIfPolCons',
            policy_name=link_level_fc_policy_name
        )
