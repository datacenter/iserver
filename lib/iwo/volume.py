import json


class IwoVolume():
    def __init__(self):
        self.mo_volume = None

    def initialize_volume(self):
        body = {}
        body['className'] = 'VirtualVolume'

        self.mo_volume = self.search(body)
        if self.mo_volume is None:
            return False

        self.log.iwo_mo(
            'VirtualVolume.attributes',
            self.mo_volume
        )

        return True

    def get_volume_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        for key in managed_object:
            info[key] = managed_object[key]

        return info

    def get_volumes(self):
        if self.mo_volume is None:
            if not self.initialize_volume():
                self.log.error(
                    'get_volumes',
                    'Managed objects must be initialized first'
                )
                return None

        volumes = []

        for managed_object in self.mo_volume:
            volume_info = self.get_volume_info(
                managed_object
            )
            if volume_info is not None:
                volumes.append(
                    volume_info
                )

        self.log.iwo_mo(
            'VirtualVolume.info',
            self.mo_volume
        )

        return volumes

    def print_volumes(self, info):
        self.my_output.default(
            json.dumps(
                info,
                indent=4
            )
        )
