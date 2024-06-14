import copy

from lib import filter_helper


class PolicyInterfacePfcInfo():
    def __init__(self):
        self.policy_interface_pfc = None

    def get_policy_interface_pfc_reln_info(self, managed_object):
        info = {}
        info['class'] = 'qosPfcIfPol'
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

    def get_policy_interface_pfc_info(self, managed_object):
        # "adminSt": "auto",
        # "annotation": "",
        # "childAction": "",
        # "descr": "",
        # "dn": "uni/infra/pfc-default",
        # "extMngdBy": "",
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
            'name',
            'relnFrom'
        ]
        info = {}
        info['__Output'] = {}

        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        if info['adminSt'] in ['auto', 'on']:
            info['__Output']['adminSt'] = 'Green'
        else:
            info['__Output']['adminSt'] = 'Red'

        if info['annotation'] == 'orchestrator:terraform':
            info['tf'] = True
            info['tfTick'] = '\u2713'
        else:
            info['tf'] = False
            info['tfTick'] = ''

        info['relnFrom'] = []
        for reln_mo in managed_object['relnFrom']:
            info['relnFrom'].append(
                self.get_policy_interface_pfc_reln_info(
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

    def get_policies_interface_pfc_info(self):
        if self.policy_interface_pfc is not None:
            return self.policy_interface_pfc

        managed_objects = self.get_policy_interface_pfc_mo()
        if managed_objects is not None:
            self.policy_interface_pfc = []
            for managed_object in managed_objects:
                self.policy_interface_pfc.append(
                    self.get_policy_interface_pfc_info(
                        managed_object
                    )
                )

        self.log.apic_mo(
            'qosPfcIfPol.info',
            self.policy_interface_pfc
        )

        return self.policy_interface_pfc

    def match_policy_interface_pfc(self, policy_info, policy_filter):
        if policy_filter is None or len(policy_filter) == 0:
            return True

        for ap_rule in policy_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            if key == 'name':
                if not filter_helper.match_string(value, policy_info['name']):
                    return False

            if key == 'node':
                if 'l1RsQosPfcIfPolCons' in policy_info:
                    if len(policy_info['l1RsQosPfcIfPolCons']) == 0:
                        return False

            if key == 'ref_policy_name':
                if len(policy_info['relnFrom']) == 0:
                    return False

            if key == 'used':
                if value == 'true':
                    if len(policy_info['relnFrom']) == 0:
                        return False

                    if 'l1RsQosPfcIfPolCons' in policy_info:
                        if len(policy_info['l1RsQosPfcIfPolCons']) == 0:
                            return False

                if value == 'false':
                    if len(policy_info['relnFrom']) > 0:
                        return False

                    if 'l1RsQosPfcIfPolCons' in policy_info:
                        if len(policy_info['l1RsQosPfcIfPolCons']) > 0:
                            return False

        return True

    def match_policy_interface_pfc_reln(self, policy_reln_info, policy_filter):
        if policy_filter is None or len(policy_filter) == 0:
            return True

        for ap_rule in policy_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            if key == 'ref_policy_name':
                if not filter_helper.match_string(value, policy_reln_info['policyName']):
                    return False

        return True

    def get_policy_interface_pfc(self, policy_filter=None, reln_info=True, attachment_info=False):
        all_policies = self.get_policies_interface_pfc_info()
        if all_policies is None:
            return None

        policy = []

        for policy_info in all_policies:
            if not self.match_policy_interface_pfc(policy_info, policy_filter):
                continue

            reln_from = []
            for policy_reln_info in policy_info['relnFrom']:
                if not self.match_policy_interface_pfc_reln(policy_reln_info, policy_filter):
                    continue

                reln_from.append(
                    policy_reln_info
                )

            policy_info['relnFrom'] = copy.deepcopy(reln_from)
            policy_info['references'] = len(
                policy_info['relnFrom']
            )

            if not self.match_policy_interface_pfc(policy_info, policy_filter):
                continue

            if attachment_info:
                attachment_filter = ['policy_dn:%s' % (policy_info['dn'])]
                if policy_filter is not None:
                    attachment_filter = attachment_filter + policy_filter

                policy_info['l1RsQosPfcIfPolCons'] = self.get_policy_interface_pfc_attachments(
                    attachment_filter=attachment_filter
                )

                policy_info['interfaces'] = 0
                if policy_info['l1RsQosPfcIfPolCons'] is not None:
                    policy_info['interfaces'] = len(
                        policy_info['l1RsQosPfcIfPolCons']
                    )

                policy_info['nodeInterfaces'] = self.get_policy_interface_pfc_attachments_node_summary(
                    policy_info['l1RsQosPfcIfPolCons']
                )

                if not self.match_policy_interface_pfc(policy_info, policy_filter):
                    continue

            policy.append(
                policy_info
            )

        policy = sorted(
            policy,
            key=lambda i: i['name'].lower()
        )

        return policy
