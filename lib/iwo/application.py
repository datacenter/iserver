class IwoApplication():
    def __init__(self):
        self.mo_application = None
        self.application = None

    def initialize_application(self):
        body = {}
        body['className'] = 'ApplicationComponent'

        self.mo_application = self.search(body)
        if self.mo_application is None:
            return False

        self.log.iwo_mo(
            'ApplicationComponent.attributes',
            self.mo_application
        )

        return True

    def get_application_info(self, managed_object, resolve_dependencies=False):
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

        info['container'] = []
        if 'providers' in managed_object:
            for provider in managed_object['providers']:
                if provider['className'] == 'Container':
                    info['container'].append(
                        provider
                    )

                if provider['className'] not in ['Container']:
                    self.log.error(
                        'iwo.get_application_info',
                        'Unrecognized provider class name: %s' % (
                            provider['className']
                        )
                    )

            del info['providers']

        info['container'] = sorted(
            info['container'],
            key=lambda i: i['displayName']
        )

        # Consumers

        info['service'] = []
        if 'consumers' in managed_object:
            for consumer in managed_object['consumers']:
                if consumer['className'] == 'Service':
                    info['service'].append(
                        consumer
                    )

                if consumer['className'] not in ['Service']:
                    self.log.error(
                        'iwo.get_application_info',
                        'Unrecognized provider class name: %s' % (
                            consumer['className']
                        )
                    )

            del info['consumers']

        info['service'] = sorted(
            info['service'],
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
            container_match_rules = []
            for container in info['container']:
                container['__Output'] = {}
                container['severity'] = self.get_container_severity(
                    container['uuid']
                )
                container['__Output']['displayName'] = self.map_severity_color(
                    container['severity']
                )
                container_match_rules.append(
                    'uuid:%s' % (container['uuid'])
                )

            info['containerSummary'] = self.get_severity_summary(
                info['container']
            )
            info['__Output']['containerSummary.severity'] = info['containerSummary']['__Output']['severity']

            service_match_rules = []
            for service in info['service']:
                service['__Output'] = {}
                service['severity'] = self.get_service_severity(
                    service['uuid']
                )
                service['__Output']['displayName'] = self.map_severity_color(
                    service['severity']
                )
                service_match_rules.append(
                    'uuid:%s' % (service['uuid'])
                )

            info['serviceSummary'] = self.get_severity_summary(
                info['service']
            )
            info['__Output']['serviceSummary.severity'] = info['serviceSummary']['__Output']['severity']

        return info

    def match_application(self, application_info, match_rules):
        if match_rules is None or len(match_rules) == 0:
            return True

        rules = {}
        for match_rule in match_rules:
            rules[match_rule] = False

            if match_rule.startswith('uuid:'):
                if application_info['uuid'] == match_rule[5:]:
                    rules[match_rule] = True

            if match_rule.startswith('name:'):
                if match_rule[5:].lower() in application_info['displayName'].lower():
                    rules[match_rule] = True

            if match_rule.startswith('cluster:'):
                if match_rule[8:].lower() in application_info['discoveredBy']['displayName'].lower():
                    rules[match_rule] = True

            if match_rule.startswith('service:'):
                for service_info in application_info['service']:
                    if match_rule[8:].lower() in service_info['displayName'].lower():
                        rules[match_rule] = True

            if match_rule.startswith('container:'):
                for container_info in application_info['container']:
                    if match_rule[10:].lower() in container_info['displayName'].lower():
                        rules[match_rule] = True

            if match_rule == 'stale':
                if application_info['isStale']:
                    rules[match_rule] = True

            if match_rule == 'inactive':
                if not application_info['isActive']:
                    rules[match_rule] = True

            if match_rule == 'critical':
                if application_info['severity'].lower() in ['critical']:
                    rules[match_rule] = True

            if match_rule == 'major':
                if application_info['severity'].lower() in ['critical', 'major']:
                    rules[match_rule] = True

            if match_rule == 'minor':
                if application_info['severity'].lower() in ['critical', 'major', 'minor']:
                    rules[match_rule] = True

        match = True
        for rule in rules:
            match = match and rules[rule]

        return match

    def get_applications(self, resolve_dependencies=False, match_rules=None):
        if self.mo_application is None:
            if not self.initialize_application():
                self.log.error(
                    'get_applications',
                    'Managed objects must be initialized first'
                )
                return None

        applications = []

        for managed_object in self.mo_application:
            application_info = self.get_application_info(
                managed_object,
                resolve_dependencies=resolve_dependencies
            )
            if application_info is not None:
                if not self.match_application(application_info, match_rules):
                    continue

                applications.append(
                    application_info
                )

        self.log.iwo_mo(
            'ApplicationComponent.info',
            self.mo_application
        )

        return applications

    def get_application(self, application_uuid, resolve_dependencies=False):
        if self.application is None:
            self.application = self.get_applications(resolve_dependencies=resolve_dependencies)

        if self.application is not None:
            for application in self.application:
                if application['uuid'] == application_uuid:
                    return application

        return None

    def get_application_severity(self, application_uuid, resolve_dependencies=False):
        application = self.get_application(
            application_uuid,
            resolve_dependencies=resolve_dependencies
        )
        if application is not None:
            return application['severity']
        return None

    def get_applications_summary(self, match_rules=None):
        applications = self.get_applications(
            resolve_dependencies=False,
            match_rules=match_rules
        )

        summary = None
        if applications is not None:
            summary = self.get_summary(applications)

        return summary

    def print_applications_base(self, applications):
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
            'Application Name'
        ]

        self.my_output.my_table(
            applications,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            table=True
        )

    def print_applications_actions(self, applications):
        order = [
            'state',
            'severityFlag',
            'staleness',
            'discoveredBy.displayName',
            'displayName',
            'environmentType',
            'serviceSummary.severity',
            'containerSummary.severity'
        ]

        headers = [
            'State',
            'Severity',
            'Staleness',
            'Kubernetes',
            'Application Name',
            'Location',
            'Service',
            'Container'
        ]

        for application in applications:
            if len(application['actionsList']) == 0:
                continue

            self.my_output.my_table(
                [application],
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
                application['actionsList'],
                order=action_order,
                headers=action_headers,
                allow_order_subkeys=True,
                table=True
            )

    def print_applications_services(self, applications):
        order = [
            'state',
            'severityFlag',
            'staleness',
            'actionsSeverity',
            'discoveredBy.displayName',
            'displayName',
            'serviceSummary.severity',
            'service.displayName'
        ]

        headers = [
            'State',
            'Severity',
            'Staleness',
            'Actions',
            'Cluster',
            'Application Name',
            'Service Severity',
            'Service'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                applications,
                order,
                ['service']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            row_separator=True,
            table=True
        )

    def print_applications_containers(self, applications):
        order = [
            'state',
            'severityFlag',
            'staleness',
            'actionsSeverity',
            'discoveredBy.displayName',
            'displayName',
            'containerSummary.severity',
            'container.displayName'
        ]

        headers = [
            'State',
            'Severity',
            'Staleness',
            'Actions',
            'Cluster',
            'Application Name',
            'Container Severity',
            'Container'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                applications,
                order,
                ['container']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            row_separator=True,
            table=True
        )

    def print_applications(self, applications, show_actions=False, show_container=False, show_service=False, summary=True):
        if summary:
            self.print_summary(applications)

        if not show_actions and not show_container and not show_service:
            self.print_applications_base(applications)
            return

        if show_actions:
            self.print_applications_actions(applications)
            return

        if show_service:
            self.print_applications_services(applications)
            return

        if show_container:
            self.print_applications_containers(applications)
            return
