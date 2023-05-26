from lib import log_helper
from lib.aci.policy.interface.synce.attachment import PolicyInterfaceSyncEAttachment


class PolicyInterfaceSyncE(PolicyInterfaceSyncEAttachment):
    def __init__(self, log_id=None):
        PolicyInterfaceSyncEAttachment.__init__(self)
        self.log = log_helper.Log(log_id=log_id)
        self.mo_policy_interface_synce = None

    def initialize_policy_interface_synce(self):
        if not self.initialize_policy_interface_synce_attachment():
            return False

        if self.mo_policy_interface_synce is not None:
            return True

        self.mo_policy_interface_synce = self.get_policy_interface_attributes('synceEthIfPol')
        if self.mo_policy_interface_synce is None:
            return False

        return True

    def get_policy_interface_synce_info(self, managed_object):
        # "adminSt": "disabled",
        # "annotation": "",
        # "childAction": "",
        # "descr": "",
        # "dn": "uni/infra/synceEthIfP-default",
        # "extMngdBy": "",
        # "lcOwn": "local",
        # "modTs": "2021-09-01T11:35:59.198+01:00",
        # "monPolDn": "uni/fabric/monfab-default",
        # "name": "default",
        # "nameAlias": "",
        # "ownerKey": "",
        # "ownerTag": "",
        # "qloptype": "none",
        # "qlrcvexactval": "fsync-ql-common-none",
        # "qlrcvhval": "fsync-ql-common-none",
        # "qlrcvlval": "fsync-ql-common-none",
        # "qltxexactval": "fsync-ql-common-none",
        # "qltxhval": "fsync-ql-common-none",
        # "qltxlval": "fsync-ql-common-none",
        # "selinput": "no",
        # "srcpriority": "100",
        # "ssm": "yes",
        # "status": "",
        # "uid": "0",
        # "userdom": "all",
        # "wtr": "5"
        keys = [
            'adminSt',
            'annotation',
            'dn',
            'name',
            'qloptype',
            'qlrcvexactval',
            'qlrcvhval',
            'qlrcvlval',
            'qltxexactval',
            'qltxhval',
            'qltxlval',
            'selinput',
            'srcpriority',
            'ssm',
            'wtr',
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

        info['qlrcv'] = []
        info['qlrcv'].append('%s (min)' % (info['qlrcvlval']))
        info['qlrcv'].append('%s (eq)' % (info['qlrcvexactval']))
        info['qlrcv'].append('%s (max)' % (info['qlrcvhval']))

        info['qltx'] = []
        info['qltx'].append('%s (min)' % (info['qltxlval']))
        info['qltx'].append('%s (eq)' % (info['qltxexactval']))
        info['qltx'].append('%s (max)' % (info['qltxhval']))

        if info['adminSt'] == 'enabled':
            info['__Output']['adminSt'] = 'Green'
        else:
            info['__Output']['adminSt'] = 'Red'

        info['references'] = len(
            info['relnFrom']
        )
        info['l1RsSynceEthIfPolCons'] = self.get_policy_interface_synce_attachments(managed_object)
        info['interfaces'] = len(
            info['l1RsSynceEthIfPolCons']
        )

        info['nodeInterfaces'] = self.get_policy_interface_node_interfaces(
            info['l1RsSynceEthIfPolCons']
        )

        return info

    def get_policy_interface_synce(self, synce_policy_name=None):
        if self.mo_policy_interface_synce is None:
            if not self.initialize_policy_interface_synce():
                self.log.error(
                    'get_policy_interface_synce',
                    'Managed objects must be initialized first'
                )
                return None

        policy = []

        for managed_object in self.mo_policy_interface_synce:
            policy_info = self.get_policy_interface_synce_info(managed_object)
            policy.append(policy_info)

        policy = sorted(
            policy,
            key=lambda i: i['name'].lower()
        )

        if synce_policy_name is not None:
            for synce_policy in policy:
                if synce_policy['name'] == synce_policy_name:
                    self.log.apic_mo(
                        'synceEthIfPol.info',
                        synce_policy
                    )
                    return synce_policy
            return None

        self.log.apic_mo(
            'synceEthIfPol.info',
            policy
        )

        return policy

    def get_policy_interface_synce_node(self, node_id, node_ports, synce_policy_name=None):
        return self.get_policy_interface_node(
            node_id,
            node_ports,
            self.get_policy_interface_synce(),
            'l1RsSynceEthIfPolCons',
            policy_name=synce_policy_name
        )
