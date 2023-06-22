# https://www.cisco.com/c/en/us/td/docs/switches/datacenter/aci/apic/sw/4-x/L3-configuration/Cisco-APIC-Layer-3-Networking-Configuration-Guide-411/Cisco-APIC-Layer-3-Networking-Configuration-Guide-411_chapter_010100.html


class BridgeDomainMldInfo():
    def __init__(self):
        pass

    def get_bridge_domain_mld_info(self, managed_object):
        # "annotation": "",
        # "childAction": "",
        # "extMngdBy": "",
        # "forceResolve": "yes",
        # "lcOwn": "local",
        # "modTs": "2021-10-27T15:21:50.404+01:00",
        # "monPolDn": "uni/tn-common/monepg-default",
        # "rType": "mo",
        # "rn": "rsmldsn",
        # "state": "formed",
        # "stateQual": "default-target",
        # "status": "",
        # "tCl": "mldSnoopPol",
        # "tContextDn": "",
        # "tDn": "uni/tn-common/mldsnoopPol-default",
        # "tRn": "mldsnoopPol-default",
        # "tType": "name",
        # "tnMldSnoopPolName": "",
        # "uid": "0",
        # "userdom": "all"
        info = {}
        info['__Output'] = {}

        info['tenant'] = managed_object['tDn'].split('/')[1][3:]
        info['configuredPolicyName'] = managed_object['tnMldSnoopPolName']
        info['actualPolicyName'] = managed_object['tDn'].split('/')[2].split('mldsnoopPol-')[1]
        info['name'] = info['actualPolicyName']
        info['nameTenant'] = '%s/%s' % (
            info['tenant'],
            info['name']
        )

        return info
