import json


class IwoChassis():
    def __init__(self):
        self.mo_chassis = None

    def initialize_chassis(self):
        body = {}
        body['className'] = 'Chassis'

        self.mo_chassis = self.search(body)
        if self.mo_chassis is None:
            return False

        self.log.iwo_mo(
            'Chassis.attributes',
            self.mo_chassis
        )

        return True

    def get_chassis_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        for key in managed_object:
            info[key] = managed_object[key]

        return info

    def get_chassiss(self):
        if self.mo_chassis is None:
            if not self.initialize_chassis():
                self.log.error(
                    'get_chassiss',
                    'Managed objects must be initialized first'
                )
                return None

        chassiss = []

        for managed_object in self.mo_chassis:
            chassis_info = self.get_chassis_info(
                managed_object
            )
            if chassis_info is not None:
                chassiss.append(
                    chassis_info
                )

        self.log.iwo_mo(
            'Chassis.info',
            self.mo_chassis
        )

        return chassiss

    def print_chassiss(self, info):
        self.my_output.default(
            json.dumps(
                info,
                indent=4
            )
        )
