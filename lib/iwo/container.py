class IwoContainer():
    def __init__(self):
        self.mo_container = None
        self.container = None

    def initialize_container(self):
        body = {}
        body['className'] = 'Container'

        self.mo_container = self.search(body)
        if self.mo_container is None:
            return False

        self.log.iwo_mo(
            'Container.attributes',
            self.mo_container
        )

        return True

    def get_container_info(self, managed_object, resolve_dependencies=False):
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

        info['pod'] = []
        if 'providers' in managed_object:
            for provider in managed_object['providers']:
                if provider['className'] == 'ContainerPod':
                    info['pod'].append(
                        provider
                    )

                if provider['className'] not in ['ContainerPod']:
                    self.log.error(
                        'iwo.get_container_info',
                        'Unrecognized provider class name: %s' % (
                            provider['className']
                        )
                    )

            del info['providers']

        info['pod'] = sorted(
            info['pod'],
            key=lambda i: i['displayName']
        )

        # Consumers

        info['application'] = []
        if 'consumers' in managed_object:
            for consumer in managed_object['consumers']:
                if consumer['className'] == 'ApplicationComponent':
                    info['application'].append(
                        consumer
                    )

                if consumer['className'] not in ['ApplicationComponent']:
                    self.log.error(
                        'iwo.get_container_info',
                        'Unrecognized provider class name: %s' % (
                            consumer['className']
                        )
                    )

            del info['consumers']

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
            pod_match_rules = []
            for pod in info['pod']:
                pod['__Output'] = {}
                pod['severity'] = self.get_pod_severity(
                    pod['uuid']
                )
                pod['__Output']['displayName'] = self.map_severity_color(
                    pod['severity']
                )
                pod_match_rules.append(
                    'uuid:%s' % (pod['uuid'])
                )

            info['podSummary'] = self.get_severity_summary(
                info['pod']
            )
            info['__Output']['podSummary.severity'] = info['podSummary']['__Output']['severity']

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

    def match_container(self, container_info, match_rules):
        if match_rules is None or len(match_rules) == 0:
            return True

        rules = {}
        for match_rule in match_rules:
            rules[match_rule] = False

            if match_rule.startswith('uuid:'):
                if container_info['uuid'] == match_rule[5:]:
                    rules[match_rule] = True

            if match_rule.startswith('name:'):
                if match_rule[5:].lower() in container_info['displayName'].lower():
                    rules[match_rule] = True

            if match_rule.startswith('cluster:'):
                if match_rule[8:].lower() in container_info['discoveredBy']['displayName'].lower():
                    rules[match_rule] = True

            if match_rule.startswith('application:'):
                for app_info in container_info['application']:
                    if match_rule[12:].lower() in app_info['displayName'].lower():
                        rules[match_rule] = True

            if match_rule.startswith('pod:'):
                for pod_info in container_info['pod']:
                    if match_rule[4:].lower() in pod_info['displayName'].lower():
                        rules[match_rule] = True

            if match_rule == 'stale':
                if container_info['isStale']:
                    rules[match_rule] = True

            if match_rule == 'inactive':
                if not container_info['isActive']:
                    rules[match_rule] = True

            if match_rule == 'critical':
                if container_info['severity'].lower() in ['critical']:
                    rules[match_rule] = True

            if match_rule == 'major':
                if container_info['severity'].lower() in ['critical', 'major']:
                    rules[match_rule] = True

            if match_rule == 'minor':
                if container_info['severity'].lower() in ['critical', 'major', 'minor']:
                    rules[match_rule] = True

        match = True
        for rule in rules:
            match = match and rules[rule]

        return match

    def get_containers(self, resolve_dependencies=False, match_rules=None):
        if self.mo_container is None:
            if not self.initialize_container():
                self.log.error(
                    'get_containers',
                    'Managed objects must be initialized first'
                )
                return None

        containers = []

        for managed_object in self.mo_container:
            container_info = self.get_container_info(
                managed_object,
                resolve_dependencies=resolve_dependencies
            )
            if container_info is not None:
                if not self.match_container(container_info, match_rules):
                    continue

                containers.append(
                    container_info
                )

        self.log.iwo_mo(
            'Container.info',
            self.mo_container
        )

        return containers

    def get_container(self, container_uuid, resolve_dependencies=False):
        if self.container is None:
            self.container = self.get_containers(resolve_dependencies=resolve_dependencies)

        if self.container is not None:
            for container in self.container:
                if container['uuid'] == container_uuid:
                    return container

        return None

    def get_container_severity(self, container_uuid, resolve_dependencies=False):
        container = self.get_container(
            container_uuid,
            resolve_dependencies=resolve_dependencies
        )
        if container is not None:
            return container['severity']
        return None

    def get_containers_summary(self, match_rules=None):
        containers = self.get_containers(
            resolve_dependencies=False,
            match_rules=match_rules
        )

        summary = None
        if containers is not None:
            summary = self.get_summary(containers)

        return summary

    def print_containers_base(self, containers):
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
            'Container Name'
        ]

        self.my_output.my_table(
            containers,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            table=True
        )

    def print_containers_actions(self, containers):
        order = [
            'state',
            'severityFlag',
            'staleness',
            'discoveredBy.displayName',
            'displayName',
            'environmentType',
            'application.severity',
            'pod.severity'
        ]

        headers = [
            'State',
            'Severity',
            'Staleness',
            'Kubernetes',
            'Container Name',
            'Location',
            'Application',
            'Pod'
        ]

        for container in containers:
            if len(container['actionsList']) == 0:
                continue

            self.my_output.my_table(
                [container],
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
                container['actionsList'],
                order=action_order,
                headers=action_headers,
                allow_order_subkeys=True,
                table=True
            )

    def print_containers_pods(self, containers):
        order = [
            'state',
            'severityFlag',
            'staleness',
            'actionsSeverity',
            'discoveredBy.displayName',
            'displayName',
            'podSummary.severity',
            'pod.displayName'
        ]

        headers = [
            'State',
            'Severity',
            'Staleness',
            'Actions',
            'Cluster',
            'Container Name',
            'Pod Severity',
            'Pod'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                containers,
                order,
                ['pod']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            row_separator=True,
            table=True
        )

    def print_containers_apps(self, containers):
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
            'Container Name',
            'Application Severity',
            'Application'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                containers,
                order,
                ['application']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            row_separator=True,
            table=True
        )

    def print_containers(self, containers, show_actions=False, show_app=False, show_pod=False, summary=True):
        if summary:
            self.print_summary(containers)

        if not show_actions and not show_app and not show_pod:
            self.print_containers_base(containers)
            return

        if show_pod:
            self.print_containers_pods(containers)
            return

        if show_app:
            self.print_containers_apps(containers)
            return

        if show_actions:
            self.print_containers_actions(containers)
            return
