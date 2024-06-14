import json


class IwoVirtualMachine():
    def __init__(self):
        self.mo_virtual_machine = None

    def initialize_virtual_machine(self):
        body = {}
        body['className'] = 'VirtualMachine'

        self.mo_virtual_machine = self.search(body)
        if self.mo_virtual_machine is None:
            return False

        self.log.iwo_mo(
            'VirtualMachine.attributes',
            self.mo_virtual_machine
        )

        return True

    def get_virtual_machine_info(self, managed_object, resolve_dependencies=True):
        # {
        #     "uuid": "74691878216315",
        #     "displayName": "client2",
        #     "className": "VirtualMachine",
        #     "environmentType": "ONPREM",
        #     "discoveredBy": {
        #         "uuid": "74869892680816",
        #         "displayName": "63fa369b6f72612d31e82971",
        #         "category": "Hypervisor",
        #         "type": "vCenter",
        #         "readonly": false
        #     },
        #     "vendorIds": {
        #         "63fa369b6f72612d31e82971": "vm-3456"
        #     },
        #     "state": "IDLE",
        #     "severity": "Normal",
        #     "severityBreakdown": {
        #         "NORMAL": 1
        #     },
        #     "providers": [
        #         {
        #             "uuid": "74857429819607",
        #             "displayName": "Resources-eu-spdc-dc-A-racks",
        #             "className": "VirtualDataCenter"
        #         },
        #         {
        #             "uuid": "74691878215438",
        #             "displayName": "EU-SPDC-Datastore-TNAS-DO-NOT-USE",
        #             "className": "Storage"
        #         },
        #         {
        #             "uuid": "74691878215486",
        #             "displayName": "esx8",
        #             "className": "PhysicalMachine"
        #         },
        #         {
        #             "uuid": "74691878215455",
        #             "displayName": "EU-SPDC-Datastore-WNAS",
        #             "className": "Storage"
        #         }
        #     ],
        #     "staleness": "CURRENT"
        # }

        info = {}
        info['__Output'] = {}

        for key in managed_object:
            info[key] = managed_object[key]

        info['__Output']['state'] = self.map_state_color(
            info['state']
        )

        info['__Output']['severity'] = self.map_severity_color(
            info['severity']
        )

        info['__Output']['staleness'] = self.map_staleness_color(
            info['staleness']
        )

        if resolve_dependencies:
            info['virtualDataCenterName'] = ''
            info['virtualDataCenterId'] = None
            info['storageCount'] = 0
            info['phyCount'] = 0

            if 'providers' in managed_object:
                for provider in managed_object['providers']:
                    if provider['className'] == 'VirtualDataCenter':
                        info['virtualDataCenterName'] = provider['displayName']
                        info['virtualDataCenterId'] = provider['uuid']

                    if provider['className'] == 'Storage':
                        info['storageCount'] = info['storageCount'] + 1

                    if provider['className'] == 'PhysicalMachine':
                        info['phyCount'] = info['phyCount'] + 1

                    if provider['className'] not in ['VirtualDataCenter', 'Storage', 'PhysicalMachine']:
                        self.log.error(
                            'iwo.get_virtual_machine_info',
                            'Unrecognized provider class name: %s' % (
                                provider['className']
                            )
                        )

        return info

    def match_virtual_machine(self, virtual_machine_info, match_rules):
        if match_rules is None or len(match_rules) == 0:
            return True

        match = False
        for match_rule in match_rules:
            if match_rule.startswith('uuid:'):
                if virtual_machine_info['uuid'] == match_rule[5:]:
                    match = True
                    break

        return match

    def get_virtual_machine(self, virtual_machine_uuid, resolve_dependencies=True):
        virtual_machines = self.get_virtual_machines(resolve_dependencies=resolve_dependencies)
        if virtual_machines is not None:
            for virtual_machine in self.mo_virtual_machine:
                if virtual_machine['uuid'] == virtual_machine_uuid:
                    return virtual_machine
        return None

    def get_virtual_machine_severity(self, virtual_machine_uuid, resolve_dependencies=False):
        virtual_machine = self.get_virtual_machine(
            virtual_machine_uuid,
            resolve_dependencies=resolve_dependencies
        )
        if virtual_machine is not None:
            return virtual_machine['severity']
        return None

    def get_virtual_machines(self, resolve_dependencies=True, match_rules=None):
        if self.mo_virtual_machine is None:
            if not self.initialize_virtual_machine():
                self.log.error(
                    'get_virtual_machines',
                    'Managed objects must be initialized first'
                )
                return None

        virtual_machines = []

        for managed_object in self.mo_virtual_machine:
            virtual_machine_info = self.get_virtual_machine_info(
                managed_object,
                resolve_dependencies=resolve_dependencies
            )
            if virtual_machine_info is not None:
                if not self.match_virtual_machine(virtual_machine_info, match_rules):
                    continue

                virtual_machines.append(
                    virtual_machine_info
                )

        return virtual_machines

    def get_virtual_machines_summary(self, match_rules=None):
        virtual_machines = self.get_virtual_machines(
            resolve_dependencies=False,
            match_rules=match_rules
        )

        summary = None
        if virtual_machines is not None:
            summary = self.get_summary(virtual_machines)

        return summary

    def print_virtual_machines(self, info, summary=True):
        if summary:
            self.print_summary(info)

        self.my_output.default(
            json.dumps(
                info,
                indent=4
            )
        )
