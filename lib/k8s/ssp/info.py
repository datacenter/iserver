from lib import filter_helper


class K8sSspInfo():
    def __init__(self):
        self.ssp = None

    def get_ssp_info(self, ssp_mo):
        if ssp_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            ssp_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(ssp_mo, 'spec')
        info['status'] = self.get(ssp_mo, 'status')
        return info

    def get_ssps_info(self, cache_enabled=True):
        if cache_enabled:
            if self.ssp is not None:
                return self.ssp

        managed_objects = self.get_ssp_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.ssp = []
        for managed_object in managed_objects:
            ssp_info = {}
            ssp_info['info'] = self.get_ssp_info(
                managed_object
            )
            ssp_info['mo'] = managed_object
            self.ssp.append(
                ssp_info
            )

        return self.ssp

    def match_ssp(self, ssp_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, ssp_info['name']):
                    return False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, ssp_info['namespace']):
                    return False
                
            if not key_found:
                self.log.error(
                    'match_ssp',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_ssps(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_ssps = self.get_ssps_info(cache_enabled=cache_enabled)
        if all_ssps is None:
            return None

        ssps = []

        for ssp_info in all_ssps:
            if not self.match_ssp(ssp_info['info'], object_filter):
                continue

            if return_mo:
                ssps.append(
                    ssp_info['mo']
                )
                continue

            ssps.append(
                ssp_info['info']
            )

        return ssps

    def is_ssp(self, namespace, name, cache_enabled=True):
        if self.get_ssp(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_ssp(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        ssps = self.get_ssps(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if ssps is None:
            return None

        if len(ssps) == 1:
            return ssps[0]

        return None
