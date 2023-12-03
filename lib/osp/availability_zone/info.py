from lib import filter_helper


class OspAvailabilityZoneInfo():
    def __init__(self):
        self.availability_zone = None

    def get_availability_zones_properties(self, managed_objects):
        properties = []
        for managed_object in managed_objects:
            properties.append(
                managed_object.to_dict()
            )
        return properties

    def get_availability_zone_info(self, availability_zone_mo):
        if availability_zone_mo is None:
            return None

        properties = availability_zone_mo.to_dict()

        info = {}
        info['__Output'] = {}
        info['name'] = properties['zoneName']
        info['available'] = properties['zoneState']['available']
        if info['available']:
            info['availableTick'] = '\u2713'
            info['__Output']['availableTick'] = 'Green'
        else:
            info['availableTick'] = '\u2717'
            info['__Output']['availableTick'] = 'Red'

        info['host'] = []
        for host_name in properties['hosts']:
            host_info = {}
            host_info['name'] = host_name
            host_info['service'] = []
            service_names = []
            service_namesT = []
            for service_name in properties['hosts'][host_name]:
                service_info = {}
                service_info['__Output'] = {}
                service_info['name'] = service_name
                service_names.append(
                    service_name
                )
                service_info['available'] = properties['hosts'][host_name][service_name]['available']
                if service_info['available']:
                    service_info['availableTick'] = '\u2713'
                    service_info['__Output']['availableTick'] = 'Green'
                else:
                    service_info['availableTick'] = '\u2717'
                    service_info['__Output']['availableTick'] = 'Red'

                service_info['active'] = properties['hosts'][host_name][service_name]['active']
                if service_info['active']:
                    service_info['activeTick'] = '\u2713'
                    service_info['__Output']['activeTick'] = 'Green'
                    service_namesT.append(
                        '%s [\u2713]' % (service_name)
                    )
                else:
                    service_info['activeTick'] = '\u2717'
                    service_info['__Output']['activeTick'] = 'Red'
                    service_namesT.append(
                        '%s [\u2717]' % (service_name)
                    )

                service_info['updated_at'] = properties['hosts'][host_name][service_name]['updated_at']
                service_info['updated_age'] = self.convert_timestamp_to_age(
                    service_info['updated_at'],
                    on_error='--'
                )

                host_info['service'].append(
                    service_info
                )

            host_info['service_names'] = ', '.join(service_names)
            host_info['service_namesT'] = ', '.join(service_namesT)
            info['host'].append(
                host_info
            )

        info['host'] = sorted(
            info['host'],
            key=lambda i: i['name']
        )

        return info

    def get_availability_zones_info(self, cache_enabled=True):
        if cache_enabled:
            if self.availability_zone is not None:
                return self.availability_zone

        managed_objects = self.get_availability_zone_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.log.osp_mo(
            'availability_zones',
            self.get_availability_zones_properties(managed_objects)
        )

        self.availability_zone = []
        for managed_object in managed_objects:
            availability_zone_info = self.get_availability_zone_info(
                managed_object
            )
            self.availability_zone.append(
                availability_zone_info
            )

        self.log.osp_mo(
            'availability_zones.info',
            self.availability_zone
        )

        return self.availability_zone

    def match_availability_zone(self, availability_zone_info, availability_zone_filter):
        if availability_zone_filter is None or len(availability_zone_filter) == 0:
            return True

        for ap_rule in availability_zone_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, availability_zone_info['name']):
                    return False

            if key == 'hv':
                key_found = True
                found = False
                for host_info in availability_zone_info['host']:
                    if filter_helper.match_string(value, host_info['name']):
                        found = True
                        break

                if not found:
                    return False

            if not key_found:
                self.log.error(
                    'match_availability_zone',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_availability_zones(self, object_filter=None, hv_info=False, cache_enabled=True):
        all_availability_zones = self.get_availability_zones_info(cache_enabled=cache_enabled)
        if all_availability_zones is None:
            return None

        availability_zones = []

        for availability_zone_info in all_availability_zones:
            if not self.match_availability_zone(availability_zone_info, object_filter):
                continue

            if hv_info:
                for host in availability_zone_info['host']:
                    hypervisor_info = self.get_hypervisor(host['name'])
                    if hypervisor_info is not None:
                        host['running_vms'] = hypervisor_info['running_vms']
                        host['cpu_summary'] = hypervisor_info['cpu_summary']
                        host['memory_summary'] = hypervisor_info['memory_summary']
                        host['disk_summary'] = hypervisor_info['disk_summary']

            availability_zones.append(
                availability_zone_info
            )

        availability_zones = sorted(
            availability_zones,
            key=lambda i: i['name']
        )

        return availability_zones
