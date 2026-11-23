class L3OutVrf():
    def __init__(self):
        pass

    def get_l3out_vrf_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        if managed_object is None:
            info['enabled'] = False
            info['enabledTick'] = '\u2717'
            info['__Output']['enabledTick'] = 'Red'
            return info

        info['enabled'] = True
        info['enabledTick'] = '\u2713'
        info['__Output']['enabledTick'] = 'Green'

        info['dn'] = managed_object['tDn']
        info['tenant'] = managed_object['tDn'].split('/')[1][3:]
        info['name'] = managed_object['tDn'].split('/')[2][4:]
        info['nameTenant'] = '%s/%s' % (
            info['tenant'],
            info['name']
        )

        return info
