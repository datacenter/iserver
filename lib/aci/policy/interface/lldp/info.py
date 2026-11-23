import copy

from lib import filter_helper


class PolicyInterfaceLldpInfo():
    def __init__(self):
        self.policy_interface_lldp = None

    def init_policy_interface_lldp(self):
        self.policy_interface_lldp = None

    def get_policy_interface_lldp_reln_info(self, managed_object):
        info = {}
        info['class'] = 'lldpIfPol'
        info['rn'] = managed_object['rn']
        info['tCl'] = managed_object['tCl']
        info['tDn'] = managed_object['tDn']
        info['policyType'] = self.get_policy_type_from_tcl(
            managed_object['tCl']
        )
        info['policyName'] = self.get_policy_name_from_tdn(
            managed_object['tDn']
        )
        return info

    def get_policy_interface_lldp_info(self, managed_object):
        keys = [
            'adminRxSt',
            'adminTxSt',
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

        if info['adminRxSt'] == 'enabled':
            info['__Output']['adminRxSt'] = 'Green'
        else:
            info['__Output']['adminRxSt'] = 'Red'

        if info['adminTxSt'] == 'enabled':
            info['__Output']['adminTxSt'] = 'Green'
        else:
            info['__Output']['adminTxSt'] = 'Red'

        info['relnFrom'] = []
        for reln_mo in managed_object['relnFrom']:
            info['relnFrom'].append(
                self.get_policy_interface_lldp_reln_info(
                    reln_mo
                )
            )

        info['relnFrom'] = sorted(
            info['relnFrom'],
            key=lambda i: (
                i['policyType'],
                i['policyName']
            )
        )

        info['references'] = len(
            info['relnFrom']
        )

        return info

    def get_policies_interface_lldp_info(self, cache_enabled=True):
        if self.policy_interface_lldp is not None:
            return self.policy_interface_lldp

        managed_objects = self.get_policy_interface_lldp_mo(cache_enabled=cache_enabled)
        if managed_objects is not None:
            self.policy_interface_lldp = []
            for managed_object in managed_objects:
                self.policy_interface_lldp.append(
                    self.get_policy_interface_lldp_info(
                        managed_object
                    )
                )

        self.log.apic_mo(
            'lldpIfPol.info',
            self.policy_interface_lldp
        )

        return self.policy_interface_lldp

    def match_policy_interface_lldp(self, policy_info, policy_filter):
        if policy_filter is None or len(policy_filter) == 0:
            return True

        for ap_rule in policy_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            if key == 'name':
                if not filter_helper.match_string(value, policy_info['name']):
                    return False

            if key == 'node':
                if 'l1RsLldpIfPolCons' in policy_info:
                    if len(policy_info['l1RsLldpIfPolCons']) == 0:
                        return False

            if key == 'ref_policy_name':
                if len(policy_info['relnFrom']) == 0:
                    return False

            if key == 'used':
                if value == 'true':
                    if len(policy_info['relnFrom']) == 0:
                        return False

                    if 'l1RsLldpIfPolCons' in policy_info:
                        if len(policy_info['l1RsLldpIfPolCons']) == 0:
                            return False

                if value == 'false':
                    if len(policy_info['relnFrom']) > 0:
                        return False

                    if 'l1RsLldpIfPolCons' in policy_info:
                        if len(policy_info['l1RsLldpIfPolCons']) > 0:
                            return False

        return True

    def match_policy_interface_lldp_reln(self, policy_reln_info, policy_filter):
        if policy_filter is None or len(policy_filter) == 0:
            return True

        for ap_rule in policy_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            if key == 'ref_policy_name':
                if not filter_helper.match_string(value, policy_reln_info['policyName']):
                    return False

        return True

    def get_policies_interface_lldp(self, policy_filter=None, reln_info=True, attachment_info=False, cache_enabled=True):
        if not cache_enabled:
            self.init_policy_interface_lldp()
            self.init_policy_interface_lldp_mo()

        all_policies = self.get_policies_interface_lldp_info(cache_enabled=cache_enabled)
        if all_policies is None:
            return None

        policy = []

        for policy_info in all_policies:
            if not self.match_policy_interface_lldp(policy_info, policy_filter):
                continue

            reln_from = []
            for policy_reln_info in policy_info['relnFrom']:
                if not self.match_policy_interface_lldp_reln(policy_reln_info, policy_filter):
                    continue

                reln_from.append(
                    policy_reln_info
                )

            policy_info['relnFrom'] = copy.deepcopy(reln_from)
            policy_info['references'] = len(
                policy_info['relnFrom']
            )

            if not self.match_policy_interface_lldp(policy_info, policy_filter):
                continue

            if attachment_info:
                attachment_filter = ['policy_dn:%s' % (policy_info['dn'])]
                if policy_filter is not None:
                    attachment_filter = attachment_filter + policy_filter

                policy_info['l1RsLldpIfPolCons'] = self.get_policy_interface_lldp_attachments(
                    attachment_filter=attachment_filter
                )

                policy_info['interfaces'] = 0
                if policy_info['l1RsLldpIfPolCons'] is not None:
                    policy_info['interfaces'] = len(
                        policy_info['l1RsLldpIfPolCons']
                    )

                policy_info['nodeInterfaces'] = self.get_policy_interface_lldp_attachments_node_summary(
                    policy_info['l1RsLldpIfPolCons']
                )

                if not self.match_policy_interface_lldp(policy_info, policy_filter):
                    continue

            policy.append(
                policy_info
            )

        policy = sorted(
            policy,
            key=lambda i: i['name'].lower()
        )

        return policy

    def get_policy_interface_lldp(self, policy_name, reln_info=True, attachment_info=False, cache_enabled=True):
        policy_filter = []
        policy_filter.append(
            'name:%s' % (policy_name)
        )
        policies = self.get_policies_interface_lldp(
            policy_filter=policy_filter,
            reln_info=reln_info,
            attachment_info=attachment_info,
            cache_enabled=cache_enabled
        )
        if policies is None:
            return None

        if len(policies) == 0:
            return None

        if len(policies) > 1:
            return None

        return policies[0]

    def is_policy_interface_lldp(self, policy_name, cache_enabled=True):
        if self.get_policy_interface_lldp(policy_name, cache_enabled=cache_enabled) is None:
            return False
        return True
