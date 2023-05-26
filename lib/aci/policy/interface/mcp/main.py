from lib import log_helper
from lib.aci.policy.interface.mcp.attachment import PolicyInterfaceMcpAttachment


class PolicyInterfaceMcp(PolicyInterfaceMcpAttachment):
    def __init__(self, log_id=None):
        PolicyInterfaceMcpAttachment.__init__(self)
        self.log = log_helper.Log(log_id=log_id)
        self.mo_policy_interface_mcp = None

    def initialize_policy_interface_mcp(self):
        if not self.initialize_policy_interface_mcp_attachment():
            return False

        if self.mo_policy_interface_mcp is not None:
            return True

        self.mo_policy_interface_mcp = self.get_policy_interface_attributes('mcpIfPol')
        if self.mo_policy_interface_mcp is None:
            return False

        return True

    def get_policy_interface_mcp_info(self, managed_object):
        # "adminSt": "enabled",
        # "annotation": "",
        # "childAction": "",
        # "descr": "",
        # "dn": "uni/infra/mcpIfP-default",
        # "extMngdBy": "",
        # "gracePeriod": "3",
        # "gracePeriodMsec": "0",
        # "lcOwn": "local",
        # "mcpMode": "off",
        # "modTs": "2020-12-09T19:07:28.202+01:00",
        # "name": "default",
        # "nameAlias": "",
        # "ownerKey": "",
        # "ownerTag": "",
        # "status": "",
        # "strictInitDelayTime": "0",
        # "strictTxFreq": "0",
        # "strictTxFreqMsec": "500",
        # "uid": "0",
        # "userdom": ""
        keys = [
            'adminSt',
            'annotation',
            'dn',
            'gracePeriod',
            'gracePeriodMsec',
            'mcpMode',
            'name',
            'strictInitDelayTime',
            'strictTxFreq',
            'strictTxFreqMsec',
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

        if info['mcpMode'] == 'off':
            info['mcpModeT'] = 'Non strict'
            info['strictInitDelayTime'] = ''
            info['strictTxFreq'] = ''
            info['strictTxFreqMsec'] = ''
            info['gracePeriod'] = ''
            info['gracePeriodMsec'] = ''
        else:
            info['mcpModeT'] = 'Strict'

        info['references'] = len(
            info['relnFrom']
        )
        info['l1RsMcpIfPolCons'] = self.get_policy_interface_mcp_attachments(managed_object)
        info['interfaces'] = len(
            info['l1RsMcpIfPolCons']
        )

        info['nodeInterfaces'] = self.get_policy_interface_node_interfaces(
            info['l1RsMcpIfPolCons']
        )

        return info

    def get_policy_interface_mcp(self, mcp_policy_name=None):
        if self.mo_policy_interface_mcp is None:
            if not self.initialize_policy_interface_mcp():
                self.log.error(
                    'get_policy_interface_mcp',
                    'Managed objects must be initialized first'
                )
                return None

        policy = []

        for managed_object in self.mo_policy_interface_mcp:
            policy_info = self.get_policy_interface_mcp_info(managed_object)
            policy.append(policy_info)

        policy = sorted(
            policy,
            key=lambda i: i['name'].lower()
        )

        if mcp_policy_name is not None:
            for mcp_policy in policy:
                if mcp_policy['name'] == mcp_policy_name:
                    self.log.apic_mo(
                        'mcpIfPol.info',
                        mcp_policy
                    )
                    return mcp_policy
            return None

        self.log.apic_mo(
            'mcpIfPol.info',
            policy
        )

        return policy

    def get_policy_interface_mcp_node(self, node_id, node_ports, mcp_policy_name=None):
        return self.get_policy_interface_node(
            node_id,
            node_ports,
            self.get_policy_interface_mcp(),
            'l1RsMcpIfPolCons',
            policy_name=mcp_policy_name
        )
