class BridgeDomainVrfInfo():
    def __init__(self):
        pass

    def get_bridge_domain_vrf_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        if managed_object['state'] == 'formed':
            info['dn'] = managed_object['tDn']
            info['state'] = managed_object['state']
            info['tenant'] = managed_object['tDn'].split('/')[1].split('tn-')[1]
            info['name'] = managed_object['tnFvCtxName']
            info['nameTenant'] = '%s/%s' % (
                info['tenant'],
                info['name']
            )

        if managed_object['state'] != 'formed':
            info['dn'] = managed_object['tDn']
            info['state'] = managed_object['state']
            info['tenant'] = None
            info['name'] = managed_object['tnFvCtxName']
            info['nameTenant'] = info['name']
            info['__Output']['nameTenant'] = 'Red'

        return info
