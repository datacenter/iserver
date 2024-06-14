import copy


class IwoVirtualDataCenter():
    def __init__(self):
        self.mo_virtual_data_center = None
        self.virtual_data_center = None

    def initialize_virtual_data_center(self):
        body = {}
        body['className'] = 'VirtualDataCenter'

        self.mo_virtual_data_center = self.search(body)
        if self.mo_virtual_data_center is None:
            return False

        self.log.iwo_mo(
            'VirtualDataCenter.attributes',
            self.mo_virtual_data_center
        )

        return True

    def get_virtual_data_center_info(self, managed_object, resolve_dependencies=False):
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

        info['__Output']['state'] = self.map_state_color(
            info['state']
        )

        info['__Output']['severity'] = self.map_severity_color(
            info['severity']
        )

        info['__Output']['staleness'] = self.map_staleness_color(
            info['staleness']
        )

        info['isStale'] = False
        if info['staleness'] == 'STALE':
            info['isStale'] = True

        info['isActive'] = False
        if info['state'] == 'ACTIVE':
            info['isActive'] = True

        # Providers

        info['physicalMachine'] = []
        if 'providers' in managed_object:
            for provider in managed_object['providers']:
                if provider['className'] == 'PhysicalMachine':
                    info['physicalMachine'].append(provider)

                if provider['className'] not in ['PhysicalMachine', 'VirtualDataCenter']:
                    self.log.error(
                        'iwo.get_virtual_data_center_info',
                        'Unrecognized provider class name: %s' % (
                            provider['className']
                        )
                    )

            del info['providers']

        info['physicalMachine'] = sorted(
            info['physicalMachine'],
            key=lambda i: i['displayName']
        )

        # Consumers

        info['virtualMachine'] = []
        if 'consumers' in managed_object:
            for consumer in managed_object['consumers']:
                if consumer['className'] == 'VirtualMachine':
                    info['virtualMachine'].append(consumer)

                if consumer['className'] not in ['VirtualMachine', 'VirtualDataCenter']:
                    self.log.error(
                        'iwo.get_vdc_info',
                        'Unrecognized consumer class name: %s' % (
                            consumer['className']
                        )
                    )

            del info['consumers']

        info['virtualMachine'] = sorted(
            info['virtualMachine'],
            key=lambda i: i['displayName']
        )

        # Actions

        action_rules = []
        action_rules.append(
            'target_id:%s' % (info['uuid'])
        )
        info['actions'] = self.get_actions(
            related_class='Storage',
            match_rules=action_rules
        )
        info['actionsList'] = self.get_actions_list(
            info['actions']
        )
        (info['severityFlag'], info['__Output']['severityFlag']) = self.get_actions_severity_flag(
            info['actions']
        )

        if resolve_dependencies:
            physical_machine_match_rules = []
            for physical_machine in info['physicalMachine']:
                physical_machine['__Output'] = {}
                physical_machine['severity'] = self.get_physical_machine_severity(
                    physical_machine['uuid']
                )
                physical_machine['__Output']['displayName'] = self.map_severity_color(
                    physical_machine['severity']
                )
                physical_machine_match_rules.append(
                    'uuid:%s' % (physical_machine['uuid'])
                )

            info['physicalMachineSummary'] = self.get_empty_summary()
            if len(physical_machine_match_rules) > 0:
                summary = self.get_physical_machines_summary(
                    match_rules=physical_machine_match_rules
                )

                info['physicalMachineSummary'] = copy.deepcopy(summary)
                info['__Output']['physicalMachineSummary.severity'] = summary['__Output']['severity']

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

        return info

    def match_virtual_data_center(self, vdc_info, match_rules):
        if match_rules is None or len(match_rules) == 0:
            return True

        match = False
        for match_rule in match_rules:
            if match_rule.startswith('uuid:'):
                if vdc_info['uuid'] == match_rule[5:]:
                    match = True
                    break

            if match_rule.startswith('name:'):
                if match_rule[5:].lower() in vdc_info['displayName'].lower():
                    match = True
                    break

            if match_rule.startswith('vm:'):
                for vm_info in vdc_info['virtualMachine']:
                    if match_rule[3:].lower() in vm_info['displayName'].lower():
                        match = True
                        break

                if match:
                    break

            if match_rule.startswith('phy:'):
                for phy_info in vdc_info['physicalMachine']:
                    if match_rule[4:].lower() in phy_info['displayName'].lower():
                        match = True
                        break

                if match:
                    break

            if match_rule == 'stale':
                if vdc_info['isStale']:
                    match = True
                    break

            if match_rule == 'inactive':
                if not vdc_info['isActive']:
                    match = True
                    break

            if match_rule == 'critical':
                if vdc_info['severity'].lower() in ['critical']:
                    match = True
                    break

            if match_rule == 'major':
                if vdc_info['severity'].lower() in ['critical', 'major']:
                    match = True
                    break

            if match_rule == 'minor':
                if vdc_info['severity'].lower() in ['critical', 'major', 'minor']:
                    match = True
                    break

        return match

    def get_virtual_data_centers(self, resolve_dependencies=False, match_rules=None):
        if self.mo_virtual_data_center is None:
            if not self.initialize_virtual_data_center():
                self.log.error(
                    'get_virtual_data_centers',
                    'Managed objects must be initialized first'
                )
                return None

        virtual_data_centers = []

        for managed_object in self.mo_virtual_data_center:
            virtual_data_center_info = self.get_virtual_data_center_info(
                managed_object,
                resolve_dependencies=resolve_dependencies
            )
            if virtual_data_center_info is not None:
                if not self.match_virtual_data_center(virtual_data_center_info, match_rules):
                    continue

                virtual_data_centers.append(
                    virtual_data_center_info
                )

        self.log.iwo_mo(
            'VirtualDataCenter.info',
            virtual_data_centers
        )

        return virtual_data_centers

    def get_virtual_data_center(self, virtual_data_center_uuid, resolve_dependencies=False):
        if self.virtual_data_center is None:
            self.virtual_data_center = self.get_virtual_data_centers(resolve_dependencies=resolve_dependencies)

        if self.virtual_data_center is not None:
            for virtual_data_center in self.virtual_data_center:
                if virtual_data_center['uuid'] == virtual_data_center_uuid:
                    return virtual_data_center

        return None

    def get_virtual_data_center_severity(self, virtual_data_center_uuid, resolve_dependencies=False):
        virtual_data_center = self.get_virtual_data_center(
            virtual_data_center_uuid,
            resolve_dependencies=resolve_dependencies
        )
        if virtual_data_center is not None:
            return virtual_data_center['severity']
        return None

    def get_virtual_data_centers_summary(self, match_rules=None):
        virtual_data_centers = self.get_virtual_data_centers(
            resolve_dependencies=False,
            match_rules=match_rules
        )

        summary = None
        if virtual_data_centers is not None:
            summary = self.get_summary(virtual_data_centers)

        return summary

    def print_virtual_data_centers_no_dep(self, vdcs):
        order = [
            'state',
            'severityFlag',
            'staleness',
            'displayName',
            'environmentType',
            'discoveredBy.type'
        ]

        headers = [
            'State',
            'Severity',
            'Staleness',
            'Storage Device Name',
            'Location',
            'Type'
        ]

        self.my_output.my_table(
            vdcs,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            table=True
        )

    def print_virtual_data_centers_actions(self, vdcs):
        order = [
            'state',
            'severityFlag',
            'staleness',
            'displayName',
            'environmentType',
            'discoveredBy.type',
            'diskArrayCount',
            'virtualMachineSummary.severity',
            'physicalMachineSummary.severity'
        ]

        headers = [
            'State',
            'Severity',
            'Staleness',
            'Storage Device Name',
            'Location',
            'Type',
            'Disk Array',
            'Virtual Machine',
            'Physical Machine'
        ]

        for vdc in vdcs:
            if len(vdc['actionsList']) == 0:
                continue

            self.my_output.my_table(
                [vdc],
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
                vdc['actionsList'],
                order=action_order,
                headers=action_headers,
                allow_order_subkeys=True,
                table=True
            )

    def print_virtual_data_centers(self, vdcs, show_dep=False, show_actions=False, show_vm=False, show_phy=False, summary=True):
        if summary:
            self.print_summary(vdcs)

        if not show_dep:
            self.print_virtual_data_centers_no_dep(vdcs)
            return

        if show_actions:
            self.print_virtual_data_centers_actions(vdcs)
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

        if not show_vm and not show_phy:
            order = order + [
                'environmentType',
                'discoveredBy.type',
                'diskArrayCount',
                'virtualMachineSummary.severity',
                'physicalMachineSummary.severity'
            ]

            headers = headers + [
                'Location',
                'Type',
                'Disk Array',
                'Virtual Machine',
                'Physical Machine'
            ]

            self.my_output.my_table(
                vdcs,
                order=order,
                headers=headers,
                allow_order_subkeys=True,
                table=True
            )

        if show_vm and not show_phy:
            order = order + [
                'virtualMachineSummary.severity',
                'virtualMachine.displayName'
            ]

            headers = headers + [
                'Virtual Machine Severity',
                'Virtual Machine'
            ]

            self.my_output.my_table(
                self.my_output.expand_lists(
                    vdcs,
                    order,
                    ['virtualMachine']
                ),
                order=order,
                headers=headers,
                allow_order_subkeys=True,
                row_separator=True,
                table=True
            )

        if not show_vm and show_phy:
            order = order + [
                'physicalMachineSummary.severity',
                'physicalMachine.displayName'
            ]

            headers = headers + [
                'Physical Machine Severity',
                'Physical Machine'
            ]

            self.my_output.my_table(
                self.my_output.expand_lists(
                    vdcs,
                    order,
                    ['physicalMachine']
                ),
                order=order,
                headers=headers,
                allow_order_subkeys=True,
                row_separator=True,
                table=True
            )

        if show_vm and show_phy:
            order = order + [
                'physicalMachineSummary.severity',
                'physicalMachine.displayName',
                'virtualMachineSummary.severity',
                'virtualMachine.displayName'
            ]

            headers = headers + [
                'Physical Machine Severity',
                'Physical Machine',
                'Virtual Machine Severity',
                'Virtual Machine'
            ]

            self.my_output.my_table(
                self.my_output.expand_lists(
                    vdcs,
                    order,
                    ['physicalMachine', 'virtualMachine']
                ),
                order=order,
                headers=headers,
                allow_order_subkeys=True,
                row_separator=True,
                table=True
            )
