class L3OutOspf():
    def __init__(self):
        pass

    def get_l3out_ospf_info(self, managed_object):
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

        keys = [
            'areaCost',
            'areaCtrl',
            'areaId',
            'areaType',
            'multipodInternal'
        ]
        for key in keys:
            info[key] = managed_object[key]

        if 'redistribute' in info['areaCtrl'].split(','):
            info['redistribute'] = True
            info['redistributeTick'] = '\u2713'
            info['__Output']['redistributeTick'] = 'Green'
        else:
            info['redistribute'] = False
            info['redistributeTick'] = '\u2717'
            info['__Output']['redistributeTick'] = 'Red'

        if 'summary' in info['areaCtrl'].split(','):
            info['summary'] = True
            info['summaryTick'] = '\u2713'
            info['__Output']['summaryTick'] = 'Green'
        else:
            info['summary'] = False
            info['summaryTick'] = '\u2717'
            info['__Output']['summaryTick'] = 'Red'

        if 'suppress' in info['areaCtrl'].split(','):
            info['suppress'] = True
            info['suppressTick'] = '\u2713'
            info['__Output']['suppressTick'] = 'Green'
        else:
            info['suppress'] = False
            info['suppressTick'] = '\u2717'
            info['__Output']['suppressTick'] = 'Red'

        return info
