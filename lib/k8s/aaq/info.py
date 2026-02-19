from lib import filter_helper


class K8sAaqInfo():
    def __init__(self):
        self.aaq = None

    def get_aaq_info(self, aaq_mo):
        if aaq_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            aaq_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(aaq_mo, 'spec')
        info['status'] = self.get(aaq_mo, 'status')
        return info

    def get_aaqs_info(self, cache_enabled=True):
        if cache_enabled:
            if self.aaq is not None:
                return self.aaq

        managed_objects = self.get_aaq_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.aaq = []
        for managed_object in managed_objects:
            aaq_info = {}
            aaq_info['info'] = self.get_aaq_info(
                managed_object
            )
            aaq_info['mo'] = managed_object
            self.aaq.append(
                aaq_info
            )

        return self.aaq

    def match_aaq(self, aaq_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, aaq_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_aaq',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_aaqs(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_aaqs = self.get_aaqs_info(cache_enabled=cache_enabled)
        if all_aaqs is None:
            return None

        aaqs = []

        for aaq_info in all_aaqs:
            if not self.match_aaq(aaq_info['info'], object_filter):
                continue

            if return_mo:
                aaqs.append(
                    aaq_info['mo']
                )
                continue

            aaqs.append(
                aaq_info['info']
            )

        return aaqs

    def is_aaq(self, name, cache_enabled=True):
        if self.get_aaq(name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_aaq(self, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'name:%s' % (name)
        )
        aaqs = self.get_aaqs(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if aaqs is None:
            return None

        if len(aaqs) == 1:
            return aaqs[0]

        return None
