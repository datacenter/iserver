from lib import filter_helper


class K8sIsovalentBGPAdvertisementInfo():
    def __init__(self):
        self.isovalent_bgp_advertisement = None

    def get_isovalent_bgp_advertisement_info(self, isovalent_bgp_advertisement_mo):
        if isovalent_bgp_advertisement_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            isovalent_bgp_advertisement_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(isovalent_bgp_advertisement_mo, 'spec')
        return info

    def get_isovalent_bgp_advertisements_info(self, cache_enabled=True):
        if cache_enabled:
            if self.isovalent_bgp_advertisement is not None:
                return self.isovalent_bgp_advertisement

        managed_objects = self.get_isovalent_bgp_advertisement_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.isovalent_bgp_advertisement = []
        for managed_object in managed_objects:
            isovalent_bgp_advertisement_info = {}
            isovalent_bgp_advertisement_info['info'] = self.get_isovalent_bgp_advertisement_info(
                managed_object
            )
            isovalent_bgp_advertisement_info['mo'] = managed_object
            self.isovalent_bgp_advertisement.append(
                isovalent_bgp_advertisement_info
            )

        return self.isovalent_bgp_advertisement

    def match_isovalent_bgp_advertisement(self, isovalent_bgp_advertisement_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, isovalent_bgp_advertisement_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_isovalent_bgp_advertisement',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_isovalent_bgp_advertisements(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_isovalent_bgp_advertisements = self.get_isovalent_bgp_advertisements_info(cache_enabled=cache_enabled)
        if all_isovalent_bgp_advertisements is None:
            return None

        isovalent_bgp_advertisements = []

        for isovalent_bgp_advertisement_info in all_isovalent_bgp_advertisements:
            if not self.match_isovalent_bgp_advertisement(isovalent_bgp_advertisement_info['info'], object_filter):
                continue

            if return_mo:
                isovalent_bgp_advertisements.append(
                    isovalent_bgp_advertisement_info['mo']
                )
                continue

            isovalent_bgp_advertisements.append(
                isovalent_bgp_advertisement_info['info']
            )

        return isovalent_bgp_advertisements

    def is_isovalent_bgp_advertisement(self, name, cache_enabled=True):
        if self.get_isovalent_bgp_advertisement(name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_isovalent_bgp_advertisement(self, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'name:%s' % (name)
        )
        isovalent_bgp_advertisements = self.get_isovalent_bgp_advertisements(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if isovalent_bgp_advertisements is None:
            return None

        if len(isovalent_bgp_advertisements) == 1:
            return isovalent_bgp_advertisements[0]

        return None
