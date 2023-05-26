from lib import log_helper


# https://www.cisco.com/c/en/us/td/docs/switches/datacenter/aci/apic/sw/2-x/KB/b_KB_Cisco_APIC_IGMP_Multicast.html


class BridgeDomainIgmp():
    def __init__(self, log_id=None):
        self.log = log_helper.Log(log_id=log_id)

    def get_bridge_domain_igmp_info(self, managed_object):
        # "annotation": "",
        # "childAction": "",
        # "extMngdBy": "",
        # "forceResolve": "yes",
        # "lcOwn": "local",
        # "modTs": "2021-10-27T15:21:50.404+01:00",
        # "monPolDn": "uni/tn-common/monepg-default",
        # "rType": "mo",
        # "rn": "rsigmpsn",
        # "state": "formed",
        # "stateQual": "default-target",
        # "status": "",
        # "tCl": "igmpSnoopPol",
        # "tContextDn": "",
        # "tDn": "uni/tn-common/snPol-default",
        # "tRn": "snPol-default",
        # "tType": "name",
        # "tnIgmpSnoopPolName": "",
        # "uid": "0",
        # "userdom": "all"
        info = {}
        info['__Output'] = {}

        info['tenant'] = managed_object['tDn'].split('/')[1][3:]
        info['configuredPolicyName'] = managed_object['tnIgmpSnoopPolName']
        info['actualPolicyName'] = managed_object['tDn'].split('/')[2].split('snPol-')[1]
        info['name'] = info['actualPolicyName']
        info['nameTenant'] = '%s/%s' % (
            info['tenant'],
            info['name']
        )

        return info
