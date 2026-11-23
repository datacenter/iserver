from lib import filter_helper


class K8sProbeInfo():
    def __init__(self):
        self.probe = None

    def get_probe_info(self, probe_mo):
        if probe_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        return info

    def get_probes_info(self, cache_enabled=True):
        if cache_enabled:
            if self.probe is not None:
                return self.probe

        managed_objects = self.get_probe_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.probe = []
        for managed_object in managed_objects:
            probe_info = {}
            probe_info['info'] = self.get_probe_info(
                managed_object
            )
            probe_info['mo'] = managed_object
            self.probe.append(
                probe_info
            )

        return self.probe

    def match_probe(self, probe_info, probe_filter):
        if probe_filter is None or len(probe_filter) == 0:
            return True

        for ap_rule in probe_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if not key_found:
                self.log.error(
                    'match_probe',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_probes(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_probes = self.get_probes_info(cache_enabled=cache_enabled)
        if all_probes is None:
            return None

        probes = []

        for probe_info in all_probes:
            if not self.match_probe(probe_info['info'], object_filter):
                continue

            if return_mo:
                probes.append(
                    probe_info['mo']
                )
                continue

            probes.append(
                probe_info['info']
            )

        return probes
