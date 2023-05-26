class L3OutPim():
    def __init__(self):
        pass

    def get_l3out_pim_info(self, managed_object):
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

        return info
