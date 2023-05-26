import json


class IwoSpec():
    def __init__(self):
        self.mo_spec = None

    def initialize_spec(self):
        body = {}
        body['className'] = 'ContainerSpec'

        self.mo_spec = self.search(body)
        if self.mo_spec is None:
            return False

        self.log.iwo_mo(
            'ContainerSpec.attributes',
            self.mo_spec
        )

        return True

    def get_spec_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        for key in managed_object:
            info[key] = managed_object[key]

        return info

    def get_specs(self):
        if self.mo_spec is None:
            if not self.initialize_spec():
                self.log.error(
                    'get_specs',
                    'Managed objects must be initialized first'
                )
                return None

        specs = []

        for managed_object in self.mo_spec:
            spec_info = self.get_spec_info(
                managed_object
            )
            if spec_info is not None:
                specs.append(
                    spec_info
                )

        self.log.iwo_mo(
            'ContainerSpec.info',
            self.mo_spec
        )

        return specs

    def print_specs(self, info):
        self.my_output.default(
            json.dumps(
                info,
                indent=4
            )
        )
