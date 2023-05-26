from lib import log_helper
from lib.aci.policy.interface.fc.attachment import PolicyInterfaceFcAttachment


class PolicyInterfaceFc(PolicyInterfaceFcAttachment):
    def __init__(self, log_id=None):
        PolicyInterfaceFcAttachment.__init__(self)
        self.log = log_helper.Log(log_id=log_id)
        self.mo_policy_interface_fc = None

    def initialize_policy_interface_fc(self):
        if not self.initialize_policy_interface_fc_attachment():
            return False

        if self.mo_policy_interface_fc is not None:
            return True

        self.mo_policy_interface_fc = self.get_policy_interface_attributes('fcIfPol')
        if self.mo_policy_interface_fc is None:
            return False

        return True

    def get_policy_interface_fc_info(self, managed_object):
        # "annotation": "",
        # "automaxspeed": "32G",
        # "childAction": "",
        # "descr": "",
        # "dn": "uni/infra/fcIfPol-default",
        # "extMngdBy": "",
        # "fillPattern": "IDLE",
        # "lcOwn": "local",
        # "modTs": "2020-12-09T19:07:28.202+01:00",
        # "name": "default",
        # "nameAlias": "",
        # "ownerKey": "",
        # "ownerTag": "",
        # "portMode": "f",
        # "rxBBCredit": "64",
        # "speed": "auto",
        # "status": "",
        # "trunkMode": "trunk-off",
        # "uid": "0",
        # "userdom": ""
        keys = [
            'annotation',
            'automaxspeed',
            'dn',
            'fillPattern',
            'name',
            'portMode',
            'rxBBCredit',
            'speed',
            'trunkMode',
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
        info['l1RsFcIfPolCons'] = self.get_policy_interface_fc_attachments(managed_object)
        info['interfaces'] = len(
            info['l1RsFcIfPolCons']
        )

        info['nodeInterfaces'] = self.get_policy_interface_node_interfaces(
            info['l1RsFcIfPolCons']
        )

        return info

    def get_policy_interface_fc(self, fc_policy_name=None):
        if self.mo_policy_interface_fc is None:
            if not self.initialize_policy_interface_fc():
                self.log.error(
                    'get_policy_interface_fc',
                    'Managed objects must be initialized first'
                )
                return None

        policy = []

        for managed_object in self.mo_policy_interface_fc:
            policy_info = self.get_policy_interface_fc_info(managed_object)
            policy.append(policy_info)

        policy = sorted(
            policy,
            key=lambda i: i['name'].lower()
        )

        if fc_policy_name is not None:
            for fc_policy in policy:
                if fc_policy['name'] == fc_policy_name:
                    self.log.apic_mo(
                        'fcIfPol.info',
                        fc_policy
                    )
                    return fc_policy
            return None

        self.log.apic_mo(
            'fcIfPol.info',
            policy
        )

        return policy

    def get_policy_interface_fc_node(self, node_id, node_ports, fc_policy_name=None):
        return self.get_policy_interface_node(
            node_id,
            node_ports,
            self.get_policy_interface_fc(),
            'l1RsFcIfPolCons',
            policy_name=fc_policy_name
        )
