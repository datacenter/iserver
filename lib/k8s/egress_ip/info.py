from lib import filter_helper


class K8sEgressIpInfo():
    def __init__(self):
        self.egress_ip = None

    def get_egress_ip_info(self, egress_ip_mo):
        if egress_ip_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            egress_ip_mo
        )
        info.update(metadata_info)

        return info

    def get_egress_ips_info(self, cache_enabled=True):
        if cache_enabled:
            if self.egress_ip is not None:
                return self.egress_ip

        managed_objects = self.get_egress_ip_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.egress_ip = []
        for managed_object in managed_objects:
            egress_ip_info = {}
            egress_ip_info['info'] = self.get_egress_ip_info(
                managed_object
            )
            egress_ip_info['mo'] = managed_object
            self.egress_ip.append(
                egress_ip_info
            )

        return self.egress_ip

    def match_egress_ip(self, egress_ip_info, egress_ip_filter):
        if egress_ip_filter is None or len(egress_ip_filter) == 0:
            return True

        for ap_rule in egress_ip_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if not key_found:
                self.log.error(
                    'match_egress_ip',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_egress_ips(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_egress_ips = self.get_egress_ips_info(cache_enabled=cache_enabled)
        if all_egress_ips is None:
            return None

        egress_ips = []

        for egress_ip_info in all_egress_ips:
            if not self.match_egress_ip(egress_ip_info['info'], object_filter):
                continue

            if return_mo:
                egress_ips.append(
                    egress_ip_info['mo']
                )
                continue

            egress_ips.append(
                egress_ip_info['info']
            )

        return egress_ips
