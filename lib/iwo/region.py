import json


class IwoRegion():
    def __init__(self):
        self.mo_region = None

    def initialize_region(self):
        body = {}
        body['className'] = 'Region'

        self.mo_region = self.search(body)
        if self.mo_region is None:
            return False

        self.log.iwo_mo(
            'Region.attributes',
            self.mo_region
        )

        return True

    def get_region_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        for key in managed_object:
            info[key] = managed_object[key]

        return info

    def get_regions(self):
        if self.mo_region is None:
            if not self.initialize_region():
                self.log.error(
                    'get_regions',
                    'Managed objects must be initialized first'
                )
                return None

        regions = []

        for managed_object in self.mo_region:
            region_info = self.get_region_info(
                managed_object
            )
            if region_info is not None:
                regions.append(
                    region_info
                )

        self.log.iwo_mo(
            'Region.info',
            self.mo_region
        )

        return regions

    def print_regions(self, info):
        self.my_output.default(
            json.dumps(
                info,
                indent=4
            )
        )
