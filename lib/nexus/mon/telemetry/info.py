from lib import filter_helper
from lib import ip_helper


class MonTelemetryInfo():
    def __init__(self):
        self.telemetry = None

    def get_telemetry_info(self, telemetry_mo):
        if telemetry_mo is None:
            return None

        info = {}
        info['__Output'] = {}
        info['nexus_name'] = self.nexus_name

        for key in telemetry_mo:
            info[key] = telemetry_mo[key]

        info['mac'] = info['remote_intf_mac']

        return info

    def get_telemetrys_info(self, local_cache_enabled=True, cache_enabled=True):
        if local_cache_enabled:
            if self.telemetry is not None:
                return self.telemetry

        managed_objects = self.get_telemetry_mo(
            local_cache_enabled=local_cache_enabled,
            cache_enabled=cache_enabled
        )
        if managed_objects is None:
            self.log.error(
                'get_telemetrys_info',
                'No telemetry neighbor managed objects: %s' % (self.nexus_name)
            )
            return None

        self.telemetry = []
        for managed_object in managed_objects['TABLE_telemetry_neighbor_detail_info']['ROW_telemetry_neighbor_detail_info']:
            telemetry_info = self.get_telemetry_info(
                managed_object
            )
            self.telemetry.append(
                telemetry_info
            )

        return self.telemetry

    def match_telemetry(self, telemetry_info, telemetry_filter):
        if telemetry_filter is None or len(telemetry_filter) == 0:
            return True

        for ap_rule in telemetry_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'mac':
                key_found = True

                if telemetry_info['mac'] is None:
                    return False

                found = False
                for mac_address in value.split(','):
                    if ip_helper.is_mac_match(mac_address, telemetry_info['mac']):
                        found = True
                        break

                if not found:
                    return False

            if not key_found:
                self.log.error(
                    'match_telemetry',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_telemetrys(self, object_filter=None, local_cache_enabled=True, cache_enabled=True):
        all_telemetrys = self.get_telemetrys_info(
            local_cache_enabled=local_cache_enabled,
            cache_enabled=cache_enabled
        )
        if all_telemetrys is None:
            self.log.error(
                'get_telemetrys',
                'Failed to get telemetry neighbors: %s' % (self.nexus_name)
            )
            return None

        telemetrys = []

        for telemetry_info in all_telemetrys:
            if not self.match_telemetry(telemetry_info, object_filter):
                continue

            telemetrys.append(
                telemetry_info
            )

        return telemetrys
