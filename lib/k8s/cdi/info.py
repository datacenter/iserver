from lib import filter_helper


class K8sCdiInfo():
    def __init__(self):
        self.cdi = None

    def get_cdi_info(self, cdi_mo):
        if cdi_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            cdi_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(cdi_mo, 'spec')
        info['status'] = self.get(cdi_mo, 'status')

        info['phase'] = self.get(cdi_mo, 'status:phase')
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

    def get_cdis_info(self, cache_enabled=True):
        if cache_enabled:
            if self.cdi is not None:
                return self.cdi

        managed_objects = self.get_cdi_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.cdi = []
        for managed_object in managed_objects:
            cdi_info = {}
            cdi_info['info'] = self.get_cdi_info(
                managed_object
            )
            cdi_info['mo'] = managed_object
            self.cdi.append(
                cdi_info
            )

        return self.cdi

    def match_cdi(self, cdi_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, cdi_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_cdi',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_cdis(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_cdis = self.get_cdis_info(cache_enabled=cache_enabled)
        if all_cdis is None:
            return None

        cdis = []

        for cdi_info in all_cdis:
            if not self.match_cdi(cdi_info['info'], object_filter):
                continue

            if return_mo:
                cdis.append(
                    cdi_info['mo']
                )
                continue

            cdis.append(
                cdi_info['info']
            )

        return cdis

    def is_cdi(self, name, cache_enabled=True):
        if self.get_cdi(name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_cdi(self, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'name:%s' % (name)
        )
        cdis = self.get_cdis(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if cdis is None:
            return None

        if len(cdis) == 1:
            return cdis[0]

        return None
