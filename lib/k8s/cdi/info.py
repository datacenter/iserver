from lib import filter_helper


class K8sCdiInfo():
    def __init__(self):
        self.cdi = None

    def get_cdi_info(self, managed_object):
        if managed_object is None:
            return None
        
        info = self.get_base_info(managed_object)

        info['phase'] = self.get(managed_object, 'status:phase')
        if info['phase'] is not None and info['phase'].lower() == 'deployed':
            info['ready'] = True
            info['readyTick'] = '\u2713'
            info['__Output']['phase'] = 'Green'
            info['__Output']['readyTick'] = 'Green'
        else:
            info['ready'] = False
            info['readyTick'] = '\u2717'
            info['__Output']['phase'] = 'Red'
            info['__Output']['readyTick'] = 'Red'

        return info

    def get_cdis(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'cdi', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_cdi(self, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'cdi', 
            name,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_cdi(self, name, cache_enabled=True, optimized=True):
        if self.get_cdi(name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def is_any_cdi(self, cache_enabled=True):
        infos = self.get_cdis(cache_enabled=cache_enabled)
        if infos is None or len(infos) == 0:
            return False
        return True