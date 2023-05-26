import json


class IwoNetwork():
    def __init__(self):
        self.mo_network = None

    def initialize_network(self):
        body = {}
        body['className'] = 'Network'

        self.mo_network = self.search(body)
        if self.mo_network is None:
            return False

        self.log.iwo_mo(
            'Network.attributes',
            self.mo_network
        )

        return True

    def get_network_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        for key in managed_object:
            info[key] = managed_object[key]

        return info

    def get_networks(self):
        if self.mo_network is None:
            if not self.initialize_network():
                self.log.error(
                    'get_networks',
                    'Managed objects must be initialized first'
                )
                return None

        networks = []

        for managed_object in self.mo_network:
            network_info = self.get_network_info(
                managed_object
            )
            if network_info is not None:
                networks.append(
                    network_info
                )

        self.log.iwo_mo(
            'Network.info',
            self.mo_network
        )

        return networks

    def print_networks(self, info):
        self.my_output.default(
            json.dumps(
                info,
                indent=4
            )
        )
