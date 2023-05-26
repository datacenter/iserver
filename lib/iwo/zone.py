import json


class IwoZone():
    def __init__(self):
        self.mo_zone = None

    def initialize_zone(self):
        body = {}
        body['className'] = 'AvailabilityZone'

        self.mo_zone = self.search(body)
        if self.mo_zone is None:
            return False

        self.log.iwo_mo(
            'AvailabilityZone.attributes',
            self.mo_zone
        )

        return True

    def get_zone_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        for key in managed_object:
            info[key] = managed_object[key]

        return info

    def get_zones(self):
        if self.mo_zone is None:
            if not self.initialize_zone():
                self.log.error(
                    'get_zones',
                    'Managed objects must be initialized first'
                )
                return None

        zones = []

        for managed_object in self.mo_zone:
            zone_info = self.get_zone_info(
                managed_object
            )
            if zone_info is not None:
                zones.append(
                    zone_info
                )

        self.log.iwo_mo(
            'AvailabilityZone.info',
            self.mo_zone
        )

        return zones

    def print_zones(self, info):
        self.my_output.default(
            json.dumps(
                info,
                indent=4
            )
        )
