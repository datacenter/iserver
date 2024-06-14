import copy

from lib import filter_helper


class PolicyInterfaceDppInfo():
    def __init__(self):
        self.policy_interface_dpp = None

    def get_policy_interface_dpp_reln_info(self, managed_object):
        info = {}
        info['class'] = 'dppIfPol'
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

    def get_policy_interface_dpp_info(self, managed_object):
        # "adminSt": "disabled",
        # "annotation": "",
        # "be": "unspecified",
        # "beUnit": "unspecified",
        # "burst": "unspecified",
        # "burstUnit": "unspecified",
        # "childAction": "",
        # "conformAction": "transmit",
        # "conformMarkCos": "unspecified",
        # "conformMarkDscp": "unspecified",
        # "descr": "",
        # "dn": "uni/infra/qosdpppol-default",
        # "exceedAction": "drop",
        # "exceedMarkCos": "unspecified",
        # "exceedMarkDscp": "unspecified",
        # "extMngdBy": "",
        # "lcOwn": "local",
        # "modTs": "2020-12-09T19:07:28.202+01:00",
        # "mode": "bit",
        # "monPolDn": "",
        # "name": "default",
        # "nameAlias": "",
        # "ownerKey": "",
        # "ownerTag": "",
        # "pir": "0",
        # "pirUnit": "unspecified",
        # "rate": "0",
        # "rateUnit": "unspecified",
        # "sharingMode": "dedicated",
        # "status": "",
        # "type": "1R2C",
        # "uid": "0",
        # "userdom": "",
        # "violateAction": "drop",
        # "violateMarkCos": "unspecified",
        # "violateMarkDscp": "unspecified"
        keys = [
            'adminSt',
            'annotation',
            'be',
            'beUnit',
            'burst',
            'burstUnit',
            'conformAction',
            'conformMarkCos',
            'conformMarkDscp',
            'dn',
            'exceedAction',
            'exceedMarkCos',
            'exceedMarkDscp',
            'mode',
            'name',
            'pir',
            'pirUnit',
            'rate',
            'rateUnit',
            'sharingMode',
            'type',
            'violateAction',
            'violateMarkCos',
            'violateMarkDscp',
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

        if info['burst'] == 'unspecified':
            info['burstT'] = 'unspecified'
        else:
            info['burstT'] = '%s %s' % (
                info['burst'],
                info['burstUnit']
            )

        if info['be'] == 'unspecified':
            info['beT'] = 'unspecified'
        else:
            info['beT'] = '%s %s' % (
                info['be'],
                info['beUnit']
            )

        if info['rate'] == 'unspecified':
            info['rateT'] = 'unspecified'
        else:
            if info['rateUnit'] == 'unspecified':
                info['rateT'] = '%s pps' % (
                    info['rate']
                )
            else:
                info['rateT'] = '%s %s' % (
                    info['rate'],
                    info['rateUnit']
                )

        if info['pir'] == 'unspecified':
            info['pirT'] = 'unspecified'
        else:
            if info['pirUnit'] == 'unspecified':
                info['pirT'] = '%s pps' % (
                    info['pir']
                )
            else:
                info['pirT'] = '%s %s' % (
                    info['pir'],
                    info['pirUnit']
                )

        if info['annotation'] == 'orchestrator:terraform':
            info['tf'] = True
            info['tfTick'] = '\u2713'
        else:
            info['tf'] = False
            info['tfTick'] = ''

        info['references'] = len(
            info['relnFrom']
        )
        return info

    def get_policies_interface_dpp_info(self):
        if self.policy_interface_dpp is not None:
            return self.policy_interface_dpp

        managed_objects = self.get_policy_interface_dpp_mo()
        if managed_objects is not None:
            self.policy_interface_dpp = []
            for managed_object in managed_objects:
                self.policy_interface_dpp.append(
                    self.get_policy_interface_dpp_info(
                        managed_object
                    )
                )

        self.log.apic_mo(
            'dppIfPol.info',
            self.policy_interface_dpp
        )

        return self.policy_interface_dpp

    def match_policy_interface_dpp(self, policy_info, policy_filter):
        if policy_filter is None or len(policy_filter) == 0:
            return True

        for ap_rule in policy_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            if key == 'name':
                if not filter_helper.match_string(value, policy_info['name']):
                    return False

            if key == 'node':
                if 'l1RsQosEgressDppIfPolCons' in policy_info:
                    if len(policy_info['l1RsQosEgressDppIfPolCons']) == 0:
                        return False

            if key == 'ref_policy_name':
                if len(policy_info['relnFrom']) == 0:
                    return False

            if key == 'used':
                if value == 'true':
                    if len(policy_info['relnFrom']) == 0:
                        return False

                    if 'l1RsQosEgressDppIfPolCons' in policy_info:
                        if len(policy_info['l1RsQosEgressDppIfPolCons']) == 0:
                            return False

                if value == 'false':
                    if len(policy_info['relnFrom']) > 0:
                        return False

                    if 'l1RsQosEgressDppIfPolCons' in policy_info:
                        if len(policy_info['l1RsQosEgressDppIfPolCons']) > 0:
                            return False

        return True

    def match_policy_interface_dpp_reln(self, policy_reln_info, policy_filter):
        if policy_filter is None or len(policy_filter) == 0:
            return True

        for ap_rule in policy_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            if key == 'ref_policy_name':
                if not filter_helper.match_string(value, policy_reln_info['policyName']):
                    return False

        return True

    def get_policy_interface_dpp(self, policy_filter=None, attachment_info=False):
        all_policies = self.get_policies_interface_dpp_info()
        if all_policies is None:
            return None

        policy = []

        for policy_info in all_policies:
            if not self.match_policy_interface_dpp(policy_info, policy_filter):
                continue

            reln_from = []
            for policy_reln_info in policy_info['relnFrom']:
                if not self.match_policy_interface_dpp_reln(policy_reln_info, policy_filter):
                    continue

                reln_from.append(
                    policy_reln_info
                )

            policy_info['relnFrom'] = copy.deepcopy(reln_from)
            policy_info['references'] = len(
                policy_info['relnFrom']
            )

            if not self.match_policy_interface_dpp(policy_info, policy_filter):
                continue

            if attachment_info:
                attachment_filter = ['policy_dn:%s' % (policy_info['dn'])]
                if policy_filter is not None:
                    attachment_filter = attachment_filter + policy_filter

                policy_info['l1RsQosEgressDppIfPolCons'] = self.get_policy_interface_dpp_attachments(
                    attachment_filter=attachment_filter
                )

                policy_info['interfaces'] = 0
                if policy_info['l1RsQosEgressDppIfPolCons'] is not None:
                    policy_info['interfaces'] = len(
                        policy_info['l1RsQosEgressDppIfPolCons']
                    )

                policy_info['nodeInterfaces'] = self.get_policy_interface_dpp_attachments_node_summary(
                    policy_info['l1RsQosEgressDppIfPolCons']
                )

                if not self.match_policy_interface_dpp(policy_info, policy_filter):
                    continue

            policy.append(
                policy_info
            )

        policy = sorted(
            policy,
            key=lambda i: i['name'].lower()
        )

        return policy
