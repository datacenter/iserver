import copy


class IwoStorage():
    def __init__(self):
        self.mo_storage = None
        self.storage = None

    def initialize_storage(self):
        body = {}
        body['className'] = 'Storage'

        self.mo_storage = self.search(body)
        if self.mo_storage is None:
            return False

        self.log.iwo_mo(
            'Storage.attributes',
            self.mo_storage
        )

        return True

    def get_storage_info(self, managed_object, resolve_dependencies=False):
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

        info['diskArray'] = []
        if 'providers' in managed_object:
            for provider in managed_object['providers']:
                if provider['className'] == 'DiskArray':
                    info['diskArray'].append(
                        provider
                    )

                if provider['className'] not in ['DiskArray']:
                    self.log.error(
                        'iwo.get_storage_info',
                        'Unrecognized provider class name: %s' % (
                            provider['className']
                        )
                    )

            del info['providers']

        info['diskArrayCount'] = len(
            info['diskArray']
        )

        # Consumers

        info['virtualMachine'] = []
        info['physicalMachine'] = []
        if 'consumers' in managed_object:
            for consumer in managed_object['consumers']:
                if consumer['className'] == 'VirtualMachine':
                    info['virtualMachine'].append(consumer)

                if consumer['className'] == 'PhysicalMachine':
                    info['physicalMachine'].append(consumer)

                if consumer['className'] not in ['VirtualMachine', 'PhysicalMachine']:
                    self.log.error(
                        'iwo.get_storage_info',
                        'Unrecognized consumer class name: %s' % (
                            consumer['className']
                        )
                    )

            del info['consumers']

        info['virtualMachine'] = sorted(
            info['virtualMachine'],
            key=lambda i: i['displayName']
        )

        info['physicalMachine'] = sorted(
            info['physicalMachine'],
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

    def match_storage(self, storage_info, match_rules):
        if match_rules is None or len(match_rules) == 0:
            return True

        match = False
        for match_rule in match_rules:
            if match_rule.startswith('uuid:'):
                if storage_info['uuid'] == match_rule[5:]:
                    match = True
                    break

            if match_rule.startswith('name:'):
                if match_rule[5:].lower() in storage_info['displayName'].lower():
                    match = True
                    break

            if match_rule.startswith('vm:'):
                for vm_info in storage_info['virtualMachine']:
                    if match_rule[3:].lower() in vm_info['displayName'].lower():
                        match = True
                        break

                if match:
                    break

            if match_rule.startswith('phy:'):
                for phy_info in storage_info['physicalMachine']:
                    if match_rule[4:].lower() in phy_info['displayName'].lower():
                        match = True
                        break

                if match:
                    break

            if match_rule == 'stale':
                if storage_info['isStale']:
                    match = True
                    break

            if match_rule == 'inactive':
                if not storage_info['isActive']:
                    match = True
                    break

            if match_rule == 'critical':
                if storage_info['severity'].lower() in ['critical']:
                    match = True
                    break

            if match_rule == 'major':
                if storage_info['severity'].lower() in ['critical', 'major']:
                    match = True
                    break

            if match_rule == 'minor':
                if storage_info['severity'].lower() in ['critical', 'major', 'minor']:
                    match = True
                    break

        return match

    def get_storages(self, resolve_dependencies=False, match_rules=None):
        if self.mo_storage is None:
            if not self.initialize_storage():
                self.log.error(
                    'get_storages',
                    'Managed objects must be initialized first'
                )
                return None

        storages = []

        for managed_object in self.mo_storage:
            storage_info = self.get_storage_info(
                managed_object,
                resolve_dependencies=resolve_dependencies
            )
            if storage_info is not None:
                if not self.match_storage(storage_info, match_rules):
                    continue

                storages.append(
                    storage_info
                )

        self.log.iwo_mo(
            'Storage.info',
            storages
        )

        return storages

    def get_storage(self, storage_uuid, resolve_dependencies=False):
        if self.storage is None:
            self.storage = self.get_storages(resolve_dependencies=resolve_dependencies)

        if self.storage is not None:
            for storage in self.storage:
                if storage['uuid'] == storage_uuid:
                    return storage

        return None

    def get_storage_severity(self, storage_uuid, resolve_dependencies=False):
        storage = self.get_storage(
            storage_uuid,
            resolve_dependencies=resolve_dependencies
        )
        if storage is not None:
            return storage['severity']
        return None

    def get_storages_summary(self, match_rules=None):
        storages = self.get_storages(
            resolve_dependencies=False,
            match_rules=match_rules
        )

        summary = None
        if storages is not None:
            summary = self.get_summary(storages)

        return summary

    def print_storages_no_dep(self, storages):
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
            storages,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            table=True
        )

    def print_storages_actions(self, storages):
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

        for storage in storages:
            if len(storage['actionsList']) == 0:
                continue

            self.my_output.my_table(
                [storage],
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
                storage['actionsList'],
                order=action_order,
                headers=action_headers,
                allow_order_subkeys=True,
                table=True
            )

    def print_storages(self, storages, show_dep=False, show_actions=False, show_vm=False, show_phy=False, summary=True):
        if summary:
            self.print_summary(storages)

        if not show_dep:
            self.print_storages_no_dep(storages)
            return

        if show_actions:
            self.print_storages_actions(storages)
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
                storages,
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
                    storages,
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
                    storages,
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
                    storages,
                    order,
                    ['physicalMachine', 'virtualMachine']
                ),
                order=order,
                headers=headers,
                allow_order_subkeys=True,
                row_separator=True,
                table=True
            )
