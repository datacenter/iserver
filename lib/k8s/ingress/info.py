from lib import filter_helper


class K8sIngressInfo():
    def __init__(self):
        self.ingress = None

    def get_ingress_info(self, ingress_mo):
        if ingress_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            ingress_mo
        )
        info.update(metadata_info)

        return info

    def get_ingresses_info(self, cache_enabled=True):
        if cache_enabled:
            if self.ingress is not None:
                return self.ingress

        managed_objects = self.get_ingress_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.ingress = []
        for managed_object in managed_objects:
            ingress_info = {}
            ingress_info['info'] = self.get_ingress_info(
                managed_object
            )
            ingress_info['mo'] = managed_object
            self.ingress.append(
                ingress_info
            )

        return self.ingress

    def match_ingress(self, ingress_info, ingress_filter):
        if ingress_filter is None or len(ingress_filter) == 0:
            return True

        for ap_rule in ingress_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if not key_found:
                self.log.error(
                    'match_ingress',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_ingresses(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_ingresses = self.get_ingresses_info(cache_enabled=cache_enabled)
        if all_ingresses is None:
            return None

        ingresses = []

        for ingress_info in all_ingresses:
            if not self.match_ingress(ingress_info['info'], object_filter):
                continue

            if return_mo:
                ingresses.append(
                    ingress_info['mo']
                )
                continue

            ingresses.append(
                ingress_info['info']
            )

        return ingresses
