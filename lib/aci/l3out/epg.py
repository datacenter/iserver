class L3OutEpg():
    def __init__(self):
        pass

    def get_l3out_epg_info(self, managed_object):
        keys = [
            'annotation',
            'configSt',
            'descr',
            'exceptionTag',
            'floodOnEncap',
            'isSharedSrvMsiteEPg',
            'matchT',
            'name',
            'nameAlias',
            'pcEnfPref',
            'pcTag',
            'prefGrMemb',
            'prio',
            'rn',
            'status',
            'targetDscp'
        ]

        info = {}
        info['__Output'] = {}

        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        if info['configSt'] == 'applied':
            info['__Output']['configSt'] = 'Green'
        else:
            info['__Output']['configSt'] = 'Red'

        return info
