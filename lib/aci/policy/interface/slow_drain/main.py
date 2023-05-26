from lib import log_helper
from lib.aci.policy.interface.slow_drain.attachment import PolicyInterfaceSlowDrainAttachment


class PolicyInterfaceSlowDrain(PolicyInterfaceSlowDrainAttachment):
    def __init__(self, log_id=None):
        PolicyInterfaceSlowDrainAttachment.__init__(self)
        self.log = log_helper.Log(log_id=log_id)
        self.mo_policy_interface_slow_drain = None

    def initialize_policy_interface_slow_drain(self):
        if not self.initialize_policy_interface_slow_drain_attachment():
            return False

        if self.mo_policy_interface_slow_drain is not None:
            return True

        self.mo_policy_interface_slow_drain = self.get_policy_interface_attributes('qosSdIfPol')
        if self.mo_policy_interface_slow_drain is None:
            return False

        return True

    def get_policy_interface_slow_drain_info(self, managed_object):
        # "annotation": "",
        # "childAction": "",
        # "congClearAction": "off",
        # "congDetectMult": "10",
        # "descr": "",
        # "dn": "uni/infra/qossdpol-default",
        # "extMngdBy": "",
        # "flushAdminSt": "disabled",
        # "flushIntvl": "500",
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
            'congClearAction',
            'congDetectMult',
            'dn',
            'flushAdminSt',
            'flushIntvl',
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

        if info['flushAdminSt'] == 'enabled':
            info['__Output']['flushAdminSt'] = 'Green'
        else:
            info['__Output']['flushAdminSt'] = 'Red'

        info['references'] = len(
            info['relnFrom']
        )
        info['l1RsQosSdIfPolCons'] = self.get_policy_interface_slow_drain_attachments(managed_object)
        info['interfaces'] = len(
            info['l1RsQosSdIfPolCons']
        )

        info['nodeInterfaces'] = self.get_policy_interface_node_interfaces(
            info['l1RsQosSdIfPolCons']
        )

        return info

    def get_policy_interface_slow_drain(self, slow_drain_policy_name=None):
        if self.mo_policy_interface_slow_drain is None:
            if not self.initialize_policy_interface_slow_drain():
                self.log.error(
                    'get_policy_interface_slow_drain',
                    'Managed objects must be initialized first'
                )
                return None

        policy = []

        for managed_object in self.mo_policy_interface_slow_drain:
            policy_info = self.get_policy_interface_slow_drain_info(managed_object)
            policy.append(policy_info)

        policy = sorted(
            policy,
            key=lambda i: i['name'].lower()
        )

        if slow_drain_policy_name is not None:
            for slow_drain_policy in policy:
                if slow_drain_policy['name'] == slow_drain_policy_name:
                    self.log.apic_mo(
                        'qosSdIfPol.info',
                        slow_drain_policy
                    )
                    return slow_drain_policy
            return None

        self.log.apic_mo(
            'qosSdIfPol.info',
            policy
        )

        return policy

    def get_policy_interface_slow_drain_node(self, node_id, node_ports, slow_drain_policy_name=None):
        return self.get_policy_interface_node(
            node_id,
            node_ports,
            self.get_policy_interface_slow_drain(),
            'l1RsQosSdIfPolCons',
            policy_name=slow_drain_policy_name
        )
