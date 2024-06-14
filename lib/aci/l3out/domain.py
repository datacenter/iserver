class L3OutDomain():
    def __init__(self):
        pass

    def get_l3out_domain_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        info['dn'] = managed_object['tDn']
        info['name'] = managed_object['tDn'].split('/')[1][6:]

        return info
