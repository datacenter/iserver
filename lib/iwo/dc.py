class IwoDataCenter():
    def __init__(self):
        self.mo_data_center = None

    def initialize_data_center(self):
        body = {}
        body['className'] = 'DataCenter'

        self.mo_data_center = self.search(body)
        if self.mo_data_center is None:
            return False

        self.log.iwo_mo(
            'DataCenter.attributes',
            self.mo_data_center
        )

        return True

    def get_data_center_info(self, managed_object):
        # {
        #     "uuid": "74691878199569",
        #     "displayName": "Berlin Lab",
        #     "className": "DataCenter",
        #     "environmentType": "ONPREM",
        #     "discoveredBy": {
        #         "uuid": "74175664340512",
        #         "displayName": "6149828e6f72612d301327e8",
        #         "category": "Hypervisor",
        #         "type": "vCenter",
        #         "readonly": false
        #     },
        #     "vendorIds": {
        #         "6149828e6f72612d301327e8": "datacenter-2"
        #     },
        #     "state": "ACTIVE",
        #     "severity": "Normal",
        #     "severityBreakdown": {
        #         "NORMAL": 1
        #     },
        #     "consumers": [
        #         {
        #             "uuid": "74691878199586",
        #             "displayName": "<ip>",
        #             "className": "PhysicalMachine"
        #         }
        #     ],
        #     "staleness": "CURRENT"
        # }
        info = {}
        info['__Output'] = {}

        for key in managed_object:
            info[key] = managed_object[key]

        info['physicalMachineCount'] = 0
        for consumer in managed_object['consumers']:
            if consumer['className'] == 'PhysicalMachine':
                info['physicalMachineCount'] = info['physicalMachineCount'] + 1

        if info['state'] == 'ACTIVE':
            info['__Output']['state'] = 'Green'
        else:
            info['__Output']['state'] = 'Red'

        return info

    def get_data_centers(self):
        if self.mo_data_center is None:
            if not self.initialize_data_center():
                self.log.error(
                    'get_data_centers',
                    'Managed objects must be initialized first'
                )
                return None

        data_centers = []

        for managed_object in self.mo_data_center:
            data_center_info = self.get_data_center_info(
                managed_object
            )
            if data_center_info is not None:
                data_centers.append(
                    data_center_info
                )

        return data_centers

    def print_data_centers(self, data_centers):
        order = [
            'state',
            'displayName',
            'environmentType',
            'discoveredBy.type',
            'physicalMachineCount'
        ]

        headers = [
            'State',
            'Name',
            'Location',
            'Type',
            'Physical Machines'
        ]

        self.my_output.my_table(
            data_centers,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            table=True
        )
