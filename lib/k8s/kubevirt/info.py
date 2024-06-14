from lib import filter_helper


class K8sKubevirtInfo():
    def __init__(self):
        self.kubevirt = None

    def get_kubevirt_info(self, kubevirt_mo):
        if kubevirt_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        return info

    def get_kubevirts_info(self, cache_enabled=True):
        if cache_enabled:
            if self.kubevirt is not None:
                return self.kubevirt

        managed_objects = self.get_kubevirt_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.kubevirt = []
        for managed_object in managed_objects:
            kubevirt_info = {}
            kubevirt_info['info'] = self.get_kubevirt_info(
                managed_object
            )
            kubevirt_info['mo'] = managed_object
            self.kubevirt.append(
                kubevirt_info
            )

        return self.kubevirt

    def match_kubevirt(self, kubevirt_info, kubevirt_filter):
        if kubevirt_filter is None or len(kubevirt_filter) == 0:
            return True

        for ap_rule in kubevirt_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if not key_found:
                self.log.error(
                    'match_kubevirt',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_kubevirts(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_kubevirts = self.get_kubevirts_info(cache_enabled=cache_enabled)
        if all_kubevirts is None:
            return None

        kubevirts = []

        for kubevirt_info in all_kubevirts:
            if not self.match_kubevirt(kubevirt_info['info'], object_filter):
                continue

            if return_mo:
                kubevirts.append(
                    kubevirt_info['mo']
                )
                continue

            kubevirts.append(
                kubevirt_info['info']
            )

        return kubevirts
