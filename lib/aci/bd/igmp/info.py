class BridgeDomainIgmpInfo():
    def __init__(self):
        pass

    def get_bridge_domain_igmp_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        if managed_object['state'] == 'formed':
            info['state'] = managed_object['state']
            info['tenant'] = managed_object['tDn'].split('/')[1][3:]
            info['configuredPolicyName'] = managed_object['tnIgmpSnoopPolName']
            info['actualPolicyName'] = managed_object['tDn'].split('/')[2].split('snPol-')[1]
            info['name'] = info['actualPolicyName']
            info['nameTenant'] = '%s/%s' % (
                info['tenant'],
                info['name']
            )

        if managed_object['state'] != 'formed':
            info['state'] = managed_object['state']
            info['tenant'] = None
            info['configuredPolicyName'] = managed_object['tnIgmpSnoopPolName']
            info['actualPolicyName'] = managed_object['tRn'].split('snPol-')[1]
            info['name'] = info['actualPolicyName']
            info['nameTenant'] = info['name']
            info['__Output']['nameTenant'] = 'Red'

        return info
