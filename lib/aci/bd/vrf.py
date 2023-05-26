class BridgeDomainVrf():
    def __init__(self):
        pass

    def get_bridge_domain_vrf_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        info['dn'] = managed_object['tDn']
        info['tenant'] = managed_object['tDn'].split('/')[1].split('tn-')[1]
        info['name'] = managed_object['tnFvCtxName']
        info['nameTenant'] = '%s/%s' % (
            info['tenant'],
            info['name']
        )

        return info
