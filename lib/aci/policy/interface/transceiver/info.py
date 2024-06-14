import copy

from lib import filter_helper


class PolicyInterfaceTransceiverInfo():
    def __init__(self):
        self.policy_interface_transceiver = None

    def get_policy_interface_transceiver_reln_info(self, managed_object):
        info = {}
        info['class'] = 'xcvrOpticsIfPol'
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

    def get_policy_interface_transceiver_info(self, managed_object):
        # "adminSt": "disabled",
        # "annotation": "",
        # "cdMax": "2400",
        # "cdMin": "-2400",
        # "childAction": "",
        # "dacRate": "1x1",
        # "descr": "",
        # "dn": "uni/infra/zr-default",
        # "dwdmCarrier": "100MHzFrequency",
        # "extMngdBy": "",
        # "fecMode": "cFEC",
        # "frequency100MHz": "1931000",
        # "frequency50GHz": "19310",
        # "ituChannel50GHz": "61",
        # "lcOwn": "local",
        # "modTs": "2022-09-14T19:08:11.182+01:00",
        # "modulation": "16QAM",
        # "muxponder": "1x400",
        # "name": "default",
        # "nameAlias": "",
        # "ownerKey": "",
        # "ownerTag": "",
        # "status": "",
        # "transmitPower": "-190",
        # "uid": "0",
        # "userdom": "all",
        # "wavelength50GHz": "1552524"
        keys = [
            'adminSt',
            'annotation',
            'cdMax',
            'cdMin',
            'dacRate',
            'dn',
            'dwdmCarrier',
            'fecMode',
            'frequency100MHz',
            'frequency50GHz',
            'ituChannel50GHz',
            'modulation',
            'muxponder',
            'name',
            'type',
            'transmitPower',
            'wavelength50GHz'
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

        if info['adminSt'] == 'enabled':
            info['__Output']['adminSt'] = 'Green'
        else:
            info['__Output']['adminSt'] = 'Red'

        if info['type'] == 'xcvrZRIfPol':
            info['typeT'] = 'ZR'

        if info['type'] == 'xcvrZRPIfPol':
            info['typeT'] = 'ZRP'

        return info

    def get_policies_interface_transceiver_info(self):
        if self.policy_interface_transceiver is not None:
            return self.policy_interface_transceiver

        managed_objects = self.get_policy_interface_transceiver_mo()
        if managed_objects is not None:
            self.policy_interface_transceiver = []
            for managed_object in managed_objects:
                self.policy_interface_transceiver.append(
                    self.get_policy_interface_transceiver_info(
                        managed_object
                    )
                )

        self.log.apic_mo(
            'transceiverIfPol.info',
            self.policy_interface_transceiver
        )

        return self.policy_interface_transceiver

    def match_policy_interface_transceiver(self, policy_info, policy_filter):
        if policy_filter is None or len(policy_filter) == 0:
            return True

        for ap_rule in policy_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            if key == 'name':
                if not filter_helper.match_string(value, policy_info['name']):
                    return False

            if key == 'node':
                if 'l1RsSynceEthIfPolCons' in policy_info:
                    if len(policy_info['l1RsSynceEthIfPolCons']) == 0:
                        return False

            if key == 'used':
                if value == 'true':
                    if 'l1RsSynceEthIfPolCons' in policy_info:
                        if len(policy_info['l1RsSynceEthIfPolCons']) == 0:
                            return False

                if value == 'false':
                    if 'l1RsSynceEthIfPolCons' in policy_info:
                        if len(policy_info['l1RsSynceEthIfPolCons']) > 0:
                            return False

        return True

    def match_policy_interface_transceiver_reln(self, policy_reln_info, policy_filter):
        if policy_filter is None or len(policy_filter) == 0:
            return True

        for ap_rule in policy_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            if key == 'ref_policy_name':
                if not filter_helper.match_string(value, policy_reln_info['policyName']):
                    return False

        return True

    def get_policy_interface_transceiver(self, policy_filter=None, reln_info=True, attachment_info=False):
        all_policies = self.get_policies_interface_transceiver_info()
        if all_policies is None:
            return None

        policy = []

        for policy_info in all_policies:
            if not self.match_policy_interface_transceiver(policy_info, policy_filter):
                continue

            if attachment_info:
                attachment_filter = ['policy_dn:%s' % (policy_info['dn'])]
                if policy_filter is not None:
                    attachment_filter = attachment_filter + policy_filter

                policy_info['l1RsSynceEthIfPolCons'] = self.get_policy_interface_transceiver_attachments(
                    attachment_filter=attachment_filter
                )

                policy_info['interfaces'] = 0
                if policy_info['l1RsSynceEthIfPolCons'] is not None:
                    policy_info['interfaces'] = len(
                        policy_info['l1RsSynceEthIfPolCons']
                    )

                policy_info['nodeInterfaces'] = self.get_policy_interface_transceiver_attachments_node_summary(
                    policy_info['l1RsSynceEthIfPolCons']
                )

                if not self.match_policy_interface_transceiver(policy_info, policy_filter):
                    continue

            policy.append(
                policy_info
            )

        policy = sorted(
            policy,
            key=lambda i: i['name'].lower()
        )

        return policy
