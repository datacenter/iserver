import json


class IwoWorkload():
    def __init__(self):
        self.mo_workload = None

    def initialize_workload(self):
        body = {}
        body['className'] = 'WorkloadController'

        self.mo_workload = self.search(body)
        if self.mo_workload is None:
            return False

        self.log.iwo_mo(
            'WorkloadController.attributes',
            self.mo_workload
        )

        return True

    def get_workload_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        for key in managed_object:
            info[key] = managed_object[key]

        return info

    def get_workloads(self):
        if self.mo_workload is None:
            if not self.initialize_workload():
                self.log.error(
                    'get_workloads',
                    'Managed objects must be initialized first'
                )
                return None

        workloads = []

        for managed_object in self.mo_workload:
            workload_info = self.get_workload_info(
                managed_object
            )
            if workload_info is not None:
                workloads.append(
                    workload_info
                )

        self.log.iwo_mo(
            'WorkloadController.info',
            self.mo_workload
        )

        return workloads

    def print_workloads(self, info):
        self.my_output.default(
            json.dumps(
                info,
                indent=4
            )
        )
