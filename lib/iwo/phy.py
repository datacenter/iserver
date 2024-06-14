import copy


class IwoPhysicalMachine():
    def __init__(self):
        self.mo_physical_machine = None
        self.physical_machine = None

    def initialize_physical_machine(self):
        body = {}
        body['className'] = 'PhysicalMachine'

        self.mo_physical_machine = self.search(body)
        if self.mo_physical_machine is None:
            return False

        self.log.iwo_mo(
            'PhysicalMachine.attributes',
            self.mo_physical_machine
        )

        return True

    def get_physical_machine_info(self, managed_object, resolve_dependencies=True):
        # {
        #     "uuid": "74691878199586",
        #     "displayName": "<ip>",
        #     "className": "PhysicalMachine",
        #     "environmentType": "ONPREM",
        #     "discoveredBy": {
        #         "uuid": "74175664340512",
        #         "displayName": "6149828e6f72612d301327e8",
        #         "category": "Hypervisor",
        #         "type": "vCenter",
        #         "readonly": false
        #     },
        #     "vendorIds": {
        #         "6149828e6f72612d301327e8": "host-32744"
        #     },
        #     "state": "ACTIVE",
        #     "severity": "Normal",
        #     "severityBreakdown": {
        #         "NORMAL": 1
        #     },
        #     "providers": [
        #         {
        #             "uuid": "74691878199569",
        #             "displayName": "Berlin Lab",
        #             "className": "DataCenter"
        #         },
        #         {
        #             "uuid": "74691878199581",
        #             "displayName": "disk (berlin-esxi-242)",
        #             "className": "Storage"
        #         }
        #     ],
        #     "consumers": [
        #         {
        #             "uuid": "74691878199590",
        #             "displayName": "Resources-berlin-esxi-cluster",
        #             "className": "VirtualDataCenter"
        #         },
        #         {
        #             "uuid": "74872469331928",
        #             "displayName": "vCLS-c054ea9e-77b0-4630-be60-759f7606649c",
        #             "className": "VirtualMachine"
        #         }
        #     ],
        #     "staleness": "STALE"
        # },
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

        # Actions

        action_rules = []
        action_rules.append(
            'target_id:%s' % (info['uuid'])
        )
        info['actions'] = self.get_actions(
            related_class='PhysicalMachine',
            match_rules=action_rules
        )
        info['actionsList'] = self.get_actions_list(
            info['actions']
        )
        (info['severityFlag'], info['__Output']['severityFlag']) = self.get_actions_severity_flag(
            info['actions']
        )

        info['dataCenterName'] = ''
        info['dataCenterId'] = None
        info['storage'] = []
        info['switch'] = []
        info['chassis'] = []

        # Providers

        if 'providers' in managed_object:
            for provider in managed_object['providers']:
                if provider['className'] == 'DataCenter':
                    info['dataCenterName'] = provider['displayName']
                    info['dataCenterId'] = provider['uuid']

                if provider['className'] == 'Storage':
                    info['storage'].append(provider)

                if provider['className'] == 'Switch':
                    info['switch'].append(provider)

                if provider['className'] == 'Chassis':
                    info['chassis'].append(provider)

                if provider['className'] not in ['DataCenter', 'Storage', 'Switch', 'Chassis']:
                    self.log.error(
                        'iwo.phy.get_physical_machine_info',
                        'Unrecognized provider class name: %s' % (
                            provider['className']
                        )
                    )

            del info['providers']

        info['storage'] = sorted(
            info['storage'],
            key=lambda i: i['displayName']
        )

        # Consumers

        info['virtualMachine'] = []
        info['virtualDataCenter'] = []

        if 'consumers' in managed_object:
            for consumer in managed_object['consumers']:
                if consumer['className'] == 'VirtualMachine':
                    info['virtualMachine'].append(consumer)

                if consumer['className'] == 'VirtualDataCenter':
                    info['virtualDataCenter'].append(consumer)

                if consumer['className'] not in ['VirtualMachine', 'VirtualDataCenter']:
                    self.log.error(
                        'iwo.phy.get_physical_machine_info',
                        'Unrecognized consumer class name: %s' % (
                            consumer['className']
                        )
                    )

            del info['consumers']

        info['virtualMachine'] = sorted(
            info['virtualMachine'],
            key=lambda i: i['displayName']
        )

        info['virtualDataCenter'] = sorted(
            info['virtualDataCenter'],
            key=lambda i: i['displayName']
        )

        if resolve_dependencies:
            virtual_machine_match_rules = []
            for virtual_machine in info['virtualMachine']:
                virtual_machine['__Output'] = {}
                virtual_machine['severity'] = self.get_virtual_machine_severity(
                    virtual_machine['uuid']
                )
                virtual_machine['__Output']['displayName'] = self.map_severity_color(
                    virtual_machine['severity']
                )
                virtual_machine_match_rules.append(
                    'uuid:%s' % (virtual_machine['uuid'])
                )

            info['virtualMachineSummary'] = self.get_empty_summary()
            if len(virtual_machine_match_rules) > 0:
                summary = self.get_virtual_machines_summary(
                    match_rules=virtual_machine_match_rules
                )

                info['virtualMachineSummary'] = copy.deepcopy(summary)
                info['__Output']['virtualMachineSummary.severity'] = summary['__Output']['severity']

            virtual_data_center_rules = []
            for virtual_data_center in info['virtualDataCenter']:
                virtual_data_center['__Output'] = {}
                virtual_data_center['severity'] = self.get_virtual_data_center_severity(
                    virtual_data_center['uuid']
                )
                virtual_data_center['__Output']['displayName'] = self.map_severity_color(
                    virtual_data_center['severity']
                )
                virtual_data_center_rules.append(
                    'uuid:%s' % (virtual_data_center['uuid'])
                )

            info['virtualDataCenterSummary'] = self.get_empty_summary()
            if len(virtual_data_center_rules) > 0:
                summary = self.get_virtual_data_centers_summary(
                    match_rules=virtual_data_center_rules
                )

                info['virtualDataCenterSummary'] = copy.deepcopy(summary)
                info['__Output']['virtualDataCenterSummary.severity'] = summary['__Output']['severity']

            storage_rules = []
            for storage in info['storage']:
                storage['__Output'] = {}
                storage['severity'] = self.get_storage_severity(
                    storage['uuid']
                )
                storage['__Output']['displayName'] = self.map_severity_color(
                    storage['severity']
                )
                storage_rules.append(
                    'uuid:%s' % (storage['uuid'])
                )

            info['storageSummary'] = self.get_empty_summary()
            if len(storage_rules) > 0:
                summary = self.get_storages_summary(
                    match_rules=storage_rules
                )

                info['storageSummary'] = copy.deepcopy(summary)
                info['__Output']['storageSummary.severity'] = summary['__Output']['severity']

        return info

    def match_physical_machine(self, physical_machine_info, match_rules):
        if match_rules is None or len(match_rules) == 0:
            return True

        match = False
        for match_rule in match_rules:
            if match_rule.startswith('uuid:'):
                if physical_machine_info['uuid'] == match_rule[5:]:
                    match = True
                    break

            if match_rule.startswith('name:'):
                if match_rule[5:].lower() in physical_machine_info['displayName'].lower():
                    match = True
                    break

            if match_rule.startswith('vm:'):
                for vm_info in physical_machine_info['virtualMachine']:
                    if match_rule[3:].lower() in vm_info['displayName'].lower():
                        match = True
                        break

                if match:
                    break

            if match_rule.startswith('vdc:'):
                for vdc_info in physical_machine_info['virtualDataCenter']:
                    if match_rule[4:].lower() in vdc_info['displayName'].lower():
                        match = True
                        break

                if match:
                    break

            if match_rule.startswith('storage:'):
                for storage_info in physical_machine_info['storage']:
                    if match_rule[8:].lower() in storage_info['displayName'].lower():
                        match = True
                        break

                if match:
                    break

            if match_rule == 'stale':
                if physical_machine_info['isStale']:
                    match = True
                    break

            if match_rule == 'inactive':
                if not physical_machine_info['isActive']:
                    match = True
                    break

            if match_rule == 'critical':
                if physical_machine_info['severity'].lower() in ['critical']:
                    match = True
                    break

            if match_rule == 'major':
                if physical_machine_info['severity'].lower() in ['critical', 'major']:
                    match = True
                    break

            if match_rule == 'minor':
                if physical_machine_info['severity'].lower() in ['critical', 'major', 'minor']:
                    match = True
                    break

        return match

    def get_physical_machine(self, physical_machine_uuid, resolve_dependencies=False):
        if self.physical_machine is None:
            self.physical_machine = self.get_physical_machines(resolve_dependencies=resolve_dependencies)

        if self.physical_machine is not None:
            for physical_machine in self.physical_machine:
                if physical_machine['uuid'] == physical_machine_uuid:
                    return physical_machine

        return None

    def get_physical_machine_severity(self, physical_machine_uuid, resolve_dependencies=False):
        physical_machine = self.get_physical_machine(
            physical_machine_uuid,
            resolve_dependencies=resolve_dependencies
        )
        if physical_machine is not None:
            return physical_machine['severity']
        return None

    def get_physical_machines(self, resolve_dependencies=False, match_rules=None):
        if self.mo_physical_machine is None:
            if not self.initialize_physical_machine():
                self.log.error(
                    'get_physical_machines',
                    'Managed objects must be initialized first'
                )
                return None

        physical_machines = []

        for managed_object in self.mo_physical_machine:
            physical_machine_info = self.get_physical_machine_info(
                managed_object,
                resolve_dependencies=resolve_dependencies
            )
            if physical_machine_info is not None:
                if not self.match_physical_machine(physical_machine_info, match_rules):
                    continue

                physical_machines.append(
                    physical_machine_info
                )

        self.log.iwo_mo(
            'PhysicalMachine.info',
            physical_machines
        )

        return physical_machines

    def get_physical_machines_summary(self, match_rules=None):
        physical_machines = self.get_physical_machines(
            resolve_dependencies=False,
            match_rules=match_rules
        )

        summary = None
        if physical_machines is not None:
            summary = self.get_summary(physical_machines)

        return summary

    def print_physical_machines_actions(self, phys):
        order = [
            'state',
            'severityFlag',
            'staleness',
            'displayName',
            'environmentType',
            'discoveredBy.type',
            'dataCenterName'
        ]

        headers = [
            'State',
            'Severity',
            'Staleness',
            'Physical Machine Name',
            'Location',
            'Type',
            'Data Center'
        ]

        for phy in phys:
            if len(phy['actionsList']) == 0:
                continue

            self.my_output.my_table(
                [phy],
                order=order,
                headers=headers,
                allow_order_subkeys=True,
                table=True
            )

            action_order = [
                'severity',
                'description',
                'subCategory',
                'details'
            ]

            action_headers = [
                'Severity',
                'Description',
                'Category',
                'Details'
            ]

            self.my_output.my_table(
                phy['actionsList'],
                order=action_order,
                headers=action_headers,
                allow_order_subkeys=True,
                table=True
            )

    def print_physical_machines_no_dep(self, phys):
        order = [
            'state',
            'severityFlag',
            'staleness',
            'displayName',
            'environmentType',
            'discoveredBy.type',
            'dataCenterName'
        ]

        headers = [
            'State',
            'Severity',
            'Staleness',
            'Physical Machine Name',
            'Location',
            'Type',
            'Data Center'
        ]

        self.my_output.my_table(
            phys,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            table=True
        )

    def print_physical_machines(self, info, show_dep=False, show_actions=False, show_vm=False, show_vdc=False, show_storage=False, summary=True):
        if summary:
            self.print_summary(info)

        if not show_dep:
            self.print_physical_machines_no_dep(info)
            return

        if show_actions:
            self.print_physical_machines_actions(info)
            return

        order = [
            'state',
            'severityFlag',
            'staleness',
            'displayName'
        ]

        headers = [
            'State',
            'Severity',
            'Staleness',
            'Name'
        ]

        if not show_vm and not show_vdc and not show_storage:
            order = order + [
                'environmentType',
                'discoveredBy.type',
                'dataCenterName',
                'storageSummary.severity',
                'virtualMachineSummary.severity',
                'virtualDataCenterSummary.severity'
            ]

            headers = headers + [
                'Location',
                'Type',
                'Data Center',
                'Storage',
                'Virtual Machine',
                'Virtual Data Center'
            ]

            self.my_output.my_table(
                info,
                order=order,
                headers=headers,
                allow_order_subkeys=True,
                table=True
            )

            return

        expand_list = []

        if show_vm:
            order = order + [
                'virtualMachineSummary.severity',
                'virtualMachine.displayName'
            ]

            headers = headers + [
                'Virtual Machine Severity',
                'Virtual Machine'
            ]

            expand_list.append('virtualMachine')

        if show_vdc:
            order = order + [
                'virtualDataCenterSummary.severity',
                'virtualDataCenter.displayName'
            ]

            headers = headers + [
                'VDC Severity',
                'VDC'
            ]

            expand_list.append('virtualDataCenter')

        if show_storage:
            order = order + [
                'storageSummary.severity',
                'storage.displayName'
            ]

            headers = headers + [
                'Storage Severity',
                'Storage'
            ]

            expand_list.append('storage')

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                expand_list
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            row_separator=True,
            table=True
        )
