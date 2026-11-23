from lib import filter_helper


class K8sCniInfo():
    def __init__(self):
        self.cni = None

    def get_cni_info(self, cni_mo):
        if cni_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        info['cni'] = self.get(cni_mo, 'status:networkType', on_error='--', on_none='--')
        info['cluster'] = self.get(cni_mo, 'status:clusterNetwork', on_error=[], on_none=[])
        info['service'] = self.get(cni_mo, 'status:serviceNetwork', on_error=[], on_none=[])

        return info

    def get_cnis_info(self, cache_enabled=True):
        if cache_enabled:
            if self.cni is not None:
                return self.cni

        managed_objects = self.get_cni_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.cni = []
        for managed_object in managed_objects:
            cni_info = {}
            cni_info['info'] = self.get_cni_info(
                managed_object
            )
            cni_info['mo'] = managed_object
            self.cni.append(
                cni_info
            )

        return self.cni

    def match_cni(self, cni_info, cni_filter):
        if cni_filter is None or len(cni_filter) == 0:
            return True

        for ap_rule in cni_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if not key_found:
                self.log.error(
                    'match_cni',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_cnis(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_cnis = self.get_cnis_info(cache_enabled=cache_enabled)
        if all_cnis is None:
            return None

        cnis = []

        for cni_info in all_cnis:
            if not self.match_cni(cni_info['info'], object_filter):
                continue

            if return_mo:
                cnis.append(
                    cni_info['mo']
                )
                continue

            cnis.append(
                cni_info['info']
            )

        return cnis

    def get_cni(self):
        cnis = self.get_cnis()
        if cnis is None or len(cnis) != 1:
            return None
        return cnis[0]
