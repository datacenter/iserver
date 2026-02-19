class BridgeDomainMldInfo():
    def __init__(self):
        pass

    def get_bridge_domain_mld_info(self, managed_object):
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
