class IwoService():
    def __init__(self):
        self.mo_service = None
        self.service = None

    def initialize_service(self):
        body = {}
        body['className'] = 'Service'

        self.mo_service = self.search(body)
        if self.mo_service is None:
            return False

        self.log.iwo_mo(
            'Service.attributes',
            self.mo_service
        )

        return True

    def get_service_info(self, managed_object, resolve_dependencies=False):
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

        info['__Output']['severityFlag'] = self.map_severity_color(
            info['severity']
        )

        info['severityFlag'] = info['severity']

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

        info['application'] = []
        if 'providers' in managed_object:
            for provider in managed_object['providers']:
                if provider['className'] == 'ApplicationComponent':
                    info['application'].append(
                        provider
                    )

                if provider['className'] not in ['ApplicationComponent']:
                    self.log.error(
                        'iwo.get_service_info',
                        'Unrecognized provider class name: %s' % (
                            provider['className']
                        )
                    )

            del info['providers']

        info['application'] = sorted(
            info['application'],
            key=lambda i: i['displayName']
        )

        # Actions

        action_rules = []
        action_rules.append(
            'target_id:%s' % (info['uuid'])
        )
        info['actions'] = self.get_actions(
            related_class='Service',
            match_rules=action_rules
        )
        info['actionsList'] = self.get_actions_list(
            info['actions']
        )
        (info['actionsSeverity'], info['__Output']['actionsSeverity']) = self.get_action_severity_summary(
            info['actions']
        )

        if resolve_dependencies:
            application_match_rules = []
            for application in info['application']:
                application['__Output'] = {}
                application['severity'] = self.get_application_severity(
                    application['uuid']
                )
                application['__Output']['displayName'] = self.map_severity_color(
                    application['severity']
                )
                application_match_rules.append(
                    'uuid:%s' % (application['uuid'])
                )

            info['applicationSummary'] = self.get_severity_summary(
                info['application']
            )
            info['__Output']['applicationSummary.severity'] = info['applicationSummary']['__Output']['severity']

        return info

    def match_service(self, service_info, match_rules):
        if match_rules is None or len(match_rules) == 0:
            return True

        rules = {}
        for match_rule in match_rules:
            rules[match_rule] = False

            if match_rule.startswith('uuid:'):
                if service_info['uuid'] == match_rule[5:]:
                    rules[match_rule] = True

            if match_rule.startswith('name:'):
                if match_rule[5:].lower() in service_info['displayName'].lower():
                    rules[match_rule] = True

            if match_rule.startswith('cluster:'):
                if match_rule[8:].lower() in service_info['discoveredBy']['displayName'].lower():
                    rules[match_rule] = True

            if match_rule.startswith('app:'):
                for app_info in service_info['application']:
                    if match_rule[4:].lower() in app_info['displayName'].lower():
                        rules[match_rule] = True

            if match_rule == 'stale':
                if service_info['isStale']:
                    rules[match_rule] = True

            if match_rule == 'inactive':
                if not service_info['isActive']:
                    rules[match_rule] = True

            if match_rule == 'critical':
                if service_info['severity'].lower() in ['critical']:
                    rules[match_rule] = True

            if match_rule == 'major':
                if service_info['severity'].lower() in ['critical', 'major']:
                    rules[match_rule] = True

            if match_rule == 'minor':
                if service_info['severity'].lower() in ['critical', 'major', 'minor']:
                    rules[match_rule] = True

        match = True
        for rule in rules:
            match = match and rules[rule]

        return match

    def get_services(self, resolve_dependencies=False, match_rules=None):
        if self.mo_service is None:
            if not self.initialize_service():
                self.log.error(
                    'get_services',
                    'Managed objects must be initialized first'
                )
                return None

        services = []

        for managed_object in self.mo_service:
            service_info = self.get_service_info(
                managed_object,
                resolve_dependencies=resolve_dependencies
            )
            if service_info is not None:
                if not self.match_service(service_info, match_rules):
                    continue

                services.append(
                    service_info
                )

        self.log.iwo_mo(
            'Service.info',
            services
        )

        return services

    def get_service(self, service_uuid, resolve_dependencies=False):
        if self.service is None:
            self.service = self.get_services(resolve_dependencies=resolve_dependencies)

        if self.service is not None:
            for service in self.service:
                if service['uuid'] == service_uuid:
                    return service

        return None

    def get_service_severity(self, service_uuid, resolve_dependencies=False):
        service = self.get_service(
            service_uuid,
            resolve_dependencies=resolve_dependencies
        )
        if service is not None:
            return service['severity']
        return None

    def get_services_summary(self, match_rules=None):
        services = self.get_services(
            resolve_dependencies=False,
            match_rules=match_rules
        )

        summary = None
        if services is not None:
            summary = self.get_summary(services)

        return summary

    def print_services_base(self, services):
        order = [
            'state',
            'severityFlag',
            'staleness',
            'actionsSeverity',
            'discoveredBy.displayName',
            'displayName'
        ]

        headers = [
            'State',
            'Severity',
            'Staleness',
            'Actions',
            'Cluster',
            'Service Name'
        ]

        self.my_output.my_table(
            services,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            table=True
        )

    def print_services_actions(self, services):
        order = [
            'state',
            'severityFlag',
            'staleness',
            'displayName',
            'environmentType',
            'discoveredBy.displayName',
            'applicationSummary.severity'
        ]

        headers = [
            'State',
            'Severity',
            'Staleness',
            'Service Name',
            'Location',
            'Kubernetes',
            'Application'
        ]

        for service in services:
            if len(service['actionsList']) == 0:
                continue

            self.my_output.my_table(
                [service],
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
                service['actionsList'],
                order=action_order,
                headers=action_headers,
                allow_order_subkeys=True,
                table=True
            )

    def print_services_apps(self, services):
        order = [
            'state',
            'severityFlag',
            'staleness',
            'actionsSeverity',
            'discoveredBy.displayName',
            'displayName',
            'applicationSummary.severity',
            'application.displayName'
        ]

        headers = [
            'State',
            'Severity',
            'Staleness',
            'Actions',
            'Cluster',
            'Service Name',
            'Application Severity',
            'Application'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                services,
                order,
                ['application']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            row_separator=True,
            table=True
        )

    def print_services(self, services, show_actions=False, show_app=False, summary=True):
        if summary:
            self.print_summary(services)

        if not show_actions and not show_app:
            self.print_services_base(services)
            return

        if show_actions:
            self.print_services_actions(services)
            return

        if show_app:
            self.print_services_apps(services)
            return
