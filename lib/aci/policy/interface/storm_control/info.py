import copy

from lib import filter_helper


class PolicyInterfaceStormControlInfo():
    def __init__(self):
        self.policy_interface_storm_control = None

    def get_policy_interface_storm_control_reln_info(self, managed_object):
        info = {}
        info['class'] = 'stormctrlIfPol'
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

    def get_policy_interface_storm_control_info(self, managed_object):
        # "annotation": "",
        # "bcBurstPps": "unspecified",
        # "bcBurstRate": "100.000000",
        # "bcRate": "100.000000",
        # "bcRatePps": "unspecified",
        # "burstPps": "unspecified",
        # "burstRate": "100.000000",
        # "childAction": "",
        # "descr": "",
        # "dn": "uni/infra/stormctrlifp-default",
        # "extMngdBy": "",
        # "isUcMcBcStormPktCfgValid": "Invalid",
        # "lcOwn": "local",
        # "mcBurstPps": "unspecified",
        # "mcBurstRate": "100.000000",
        # "mcRate": "100.000000",
        # "mcRatePps": "unspecified",
        # "modTs": "2020-12-09T19:07:28.202+01:00",
        # "monPolDn": "uni/fabric/monfab-default",
        # "name": "default",
        # "nameAlias": "",
        # "ownerKey": "",
        # "ownerTag": "",
        # "rate": "100.000000",
        # "ratePps": "unspecified",
        # "status": "",
        # "stormCtrlAction": "drop",
        # "stormCtrlSoakInstCount": "3",
        # "type": "all",
        # "uid": "0",
        # "userdom": "",
        # "uucBurstPps": "unspecified",
        # "uucBurstRate": "100.000000",
        # "uucRate": "100.000000",
        # "uucRatePps": "unspecified"
        keys = [
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

        info['packetType'] = []

        if managed_object['isUcMcBcStormPktCfgValid'] == 'Valid':
            packet_type_info = {}
            packet_type_info['type'] = 'unicast'
            packet_type_info['burstPps'] = managed_object['uucBurstPps']
            packet_type_info['burstRate'] = managed_object['uucBurstRate']
            packet_type_info['rate'] = managed_object['uucRate']
            packet_type_info['ratePps'] = managed_object['uucRatePps']
            packet_type_info['stormCtrlAction'] = managed_object['stormCtrlAction']
            packet_type_info['stormCtrlSoakInstCount'] = managed_object['stormCtrlSoakInstCount']
            info['packetType'].append(packet_type_info)

            packet_type_info = {}
            packet_type_info['type'] = 'broadcast'
            packet_type_info['burstPps'] = managed_object['bcBurstPps']
            packet_type_info['burstRate'] = managed_object['bcBurstRate']
            packet_type_info['rate'] = managed_object['bcRate']
            packet_type_info['ratePps'] = managed_object['bcRatePps']
            packet_type_info['stormCtrlAction'] = managed_object['stormCtrlAction']
            packet_type_info['stormCtrlSoakInstCount'] = managed_object['stormCtrlSoakInstCount']
            info['packetType'].append(packet_type_info)

            packet_type_info = {}
            packet_type_info['type'] = 'multicast'
            packet_type_info['burstPps'] = managed_object['mcBurstPps']
            packet_type_info['burstRate'] = managed_object['mcBurstRate']
            packet_type_info['rate'] = managed_object['mcRate']
            packet_type_info['ratePps'] = managed_object['mcRatePps']
            packet_type_info['stormCtrlAction'] = managed_object['stormCtrlAction']
            packet_type_info['stormCtrlSoakInstCount'] = managed_object['stormCtrlSoakInstCount']
            info['packetType'].append(packet_type_info)

        if managed_object['isUcMcBcStormPktCfgValid'] == 'Invalid':
            packet_type_info = {}
            packet_type_info['type'] = 'all'
            packet_type_info['burstPps'] = managed_object['burstPps']
            packet_type_info['burstRate'] = managed_object['burstRate']
            packet_type_info['rate'] = managed_object['rate']
            packet_type_info['ratePps'] = managed_object['ratePps']
            packet_type_info['stormCtrlAction'] = managed_object['stormCtrlAction']
            packet_type_info['stormCtrlSoakInstCount'] = managed_object['stormCtrlSoakInstCount']
            info['packetType'].append(packet_type_info)

        if info['annotation'] == 'orchestrator:terraform':
            info['tf'] = True
            info['tfTick'] = '\u2713'
        else:
            info['tf'] = False
            info['tfTick'] = ''

        info['relnFrom'] = []
        for reln_mo in managed_object['relnFrom']:
            info['relnFrom'].append(
                self.get_policy_interface_storm_control_reln_info(
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

    def get_policies_interface_storm_control_info(self):
        if self.policy_interface_storm_control is not None:
            return self.policy_interface_storm_control

        managed_objects = self.get_policy_interface_storm_control_mo()
        if managed_objects is not None:
            self.policy_interface_storm_control = []
            for managed_object in managed_objects:
                self.policy_interface_storm_control.append(
                    self.get_policy_interface_storm_control_info(
                        managed_object
                    )
                )

        self.log.apic_mo(
            'stormctrlIfPol.info',
            self.policy_interface_storm_control
        )

        return self.policy_interface_storm_control

    def match_policy_interface_storm_control(self, policy_info, policy_filter):
        if policy_filter is None or len(policy_filter) == 0:
            return True

        for ap_rule in policy_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            if key == 'name':
                if not filter_helper.match_string(value, policy_info['name']):
                    return False

            if key == 'node':
                if 'l1RsStormctrlIfPolCons' in policy_info:
                    if len(policy_info['l1RsStormctrlIfPolCons']) == 0:
                        return False

            if key == 'ref_policy_name':
                if len(policy_info['relnFrom']) == 0:
                    return False

            if key == 'used':
                if value == 'true':
                    if len(policy_info['relnFrom']) == 0:
                        return False

                    if 'l1RsStormctrlIfPolCons' in policy_info:
                        if len(policy_info['l1RsStormctrlIfPolCons']) == 0:
                            return False

                if value == 'false':
                    if len(policy_info['relnFrom']) > 0:
                        return False

                    if 'l1RsStormctrlIfPolCons' in policy_info:
                        if len(policy_info['l1RsStormctrlIfPolCons']) > 0:
                            return False

        return True

    def match_policy_interface_storm_control_reln(self, policy_reln_info, policy_filter):
        if policy_filter is None or len(policy_filter) == 0:
            return True

        for ap_rule in policy_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            if key == 'ref_policy_name':
                if not filter_helper.match_string(value, policy_reln_info['policyName']):
                    return False

        return True

    def get_policy_interface_storm_control(self, policy_filter=None, reln_info=True, attachment_info=False):
        all_policies = self.get_policies_interface_storm_control_info()
        if all_policies is None:
            return None

        policy = []

        for policy_info in all_policies:
            if not self.match_policy_interface_storm_control(policy_info, policy_filter):
                continue

            reln_from = []
            for policy_reln_info in policy_info['relnFrom']:
                if not self.match_policy_interface_storm_control_reln(policy_reln_info, policy_filter):
                    continue

                reln_from.append(
                    policy_reln_info
                )

            policy_info['relnFrom'] = copy.deepcopy(reln_from)
            policy_info['references'] = len(
                policy_info['relnFrom']
            )

            if not self.match_policy_interface_storm_control(policy_info, policy_filter):
                continue

            if attachment_info:
                attachment_filter = ['policy_dn:%s' % (policy_info['dn'])]
                if policy_filter is not None:
                    attachment_filter = attachment_filter + policy_filter

                policy_info['l1RsStormctrlIfPolCons'] = self.get_policy_interface_storm_control_attachments(
                    attachment_filter=attachment_filter
                )

                policy_info['interfaces'] = 0
                if policy_info['l1RsStormctrlIfPolCons'] is not None:
                    policy_info['interfaces'] = len(
                        policy_info['l1RsStormctrlIfPolCons']
                    )

                policy_info['nodeInterfaces'] = self.get_policy_interface_storm_control_attachments_node_summary(
                    policy_info['l1RsStormctrlIfPolCons']
                )

                if not self.match_policy_interface_storm_control(policy_info, policy_filter):
                    continue

            policy.append(
                policy_info
            )

        policy = sorted(
            policy,
            key=lambda i: i['name'].lower()
        )

        return policy
