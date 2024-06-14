import json


class IwoDisk():
    def __init__(self):
        self.mo_disk = None

    def initialize_disk(self):
        body = {}
        body['className'] = 'DiskArray'

        self.mo_disk = self.search(body)
        if self.mo_disk is None:
            return False

        self.log.iwo_mo(
            'DiskArray.attributes',
            self.mo_disk
        )

        return True

    def get_disk_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        for key in managed_object:
            info[key] = managed_object[key]

        return info

    def get_disks(self):
        if self.mo_disk is None:
            if not self.initialize_disk():
                self.log.error(
                    'get_disks',
                    'Managed objects must be initialized first'
                )
                return None

        disks = []

        for managed_object in self.mo_disk:
            disk_info = self.get_disk_info(
                managed_object
            )
            if disk_info is not None:
                disks.append(
                    disk_info
                )

        self.log.iwo_mo(
            'DiskArray.info',
            self.mo_disk
        )

        return disks

    def print_disks(self, info):
        self.my_output.default(
            json.dumps(
                info,
                indent=4
            )
        )
