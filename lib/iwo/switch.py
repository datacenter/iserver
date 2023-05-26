import json


class IwoSwitch():
    def __init__(self):
        self.mo_switch = None

    def initialize_switch(self):
        body = {}
        body['className'] = 'Switch'

        self.mo_switch = self.search(body)
        if self.mo_switch is None:
            return False

        self.log.iwo_mo(
            'Switch.attributes',
            self.mo_switch
        )

        return True

    def get_switch_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        for key in managed_object:
            info[key] = managed_object[key]

        return info

    def get_switchs(self):
        if self.mo_switch is None:
            if not self.initialize_switch():
                self.log.error(
                    'get_switchs',
                    'Managed objects must be initialized first'
                )
                return None

        switchs = []

        for managed_object in self.mo_switch:
            switch_info = self.get_switch_info(
                managed_object
            )
            if switch_info is not None:
                switchs.append(
                    switch_info
                )

        self.log.iwo_mo(
            'Switch.info',
            self.mo_switch
        )

        return switchs

    def print_switchs(self, info):
        self.my_output.default(
            json.dumps(
                info,
                indent=4
            )
        )
