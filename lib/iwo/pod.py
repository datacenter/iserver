import json


class IwoPod():
    def __init__(self):
        self.mo_pod = None
        self.pod = None

    def initialize_pod(self):
        body = {}
        body['className'] = 'ContainerPod'

        self.mo_pod = self.search(body)
        if self.mo_pod is None:
            return False

        self.log.iwo_mo(
            'ContainerPod.attributes',
            self.mo_pod
        )

        return True

    def get_pod_info(self, managed_object, resolve_dependencies=False):
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

        info['workload'] = []
        info['vm'] = []
        info['namespace'] = []
        info['volume'] = []
        if 'providers' in managed_object:
            for provider in managed_object['providers']:
                if provider['className'] == 'Namespace':
                    info['namespace'].append(
                        provider
                    )

                if provider['className'] == 'WorkloadController':
                    info['workload'].append(
                        provider
                    )

                if provider['className'] == 'VirtualMachine':
                    info['vm'].append(
                        provider
                    )

                if provider['className'] == 'VirtualVolume':
                    info['volume'].append(
                        provider
                    )

                if provider['className'] not in ['WorkloadController', 'VirtualMachine', 'Namespace', 'VirtualVolume']:
                    self.log.error(
                        'iwo.get_pod_info',
                        'Unrecognized provider class name: %s' % (
                            provider['className']
                        )
                    )

            del info['providers']

        # Consumers

        info['container'] = []
        if 'consumers' in managed_object:
            for consumer in managed_object['consumers']:
                if consumer['className'] == 'Container':
                    info['container'].append(
                        consumer
                    )

                if consumer['className'] == 'WorkloadController':
                    found = False
                    for workload in info['workload']:
                        if workload['uuid'] == consumer['uuid']:
                            found = True

                    if not found:
                        info['workload'].append(
                            consumer
                        )

                if consumer['className'] == 'VirtualMachine':
                    found = False
                    for vm_info in info['vm']:
                        if vm_info['uuid'] == consumer['uuid']:
                            found = True

                    if not found:
                        info['vm'].append(
                            consumer
                        )

                if consumer['className'] not in ['WorkloadController', 'VirtualMachine', 'Container']:
                    self.log.error(
                        'iwo.get_pod_info',
                        'Unrecognized consumer class name: %s' % (
                            consumer['className']
                        )
                    )

            del info['consumers']

        info['container'] = sorted(
            info['container'],
            key=lambda i: i['displayName']
        )

        info['namespace'] = sorted(
            info['namespace'],
            key=lambda i: i['displayName']
        )

        info['volume'] = sorted(
            info['volume'],
            key=lambda i: i['displayName']
        )

        info['workload'] = sorted(
            info['workload'],
            key=lambda i: i['displayName']
        )

        info['vm'] = sorted(
            info['vm'],
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
            workload_match_rules = []
            for workload in info['workload']:
                workload['__Output'] = {}
                workload['severity'] = self.get_workload_severity(
                    workload['uuid']
                )
                workload['__Output']['displayName'] = self.map_severity_color(
                    workload['severity']
                )
                workload_match_rules.append(
                    'uuid:%s' % (workload['uuid'])
                )

            info['workloadSummary'] = self.get_severity_summary(
                info['workload']
            )
            info['__Output']['workloadSummary.severity'] = info['workloadSummary']['__Output']['severity']

            vm_match_rules = []
            for vm_info in info['vm']:
                vm_info['__Output'] = {}
                vm_info['severity'] = self.get_virtual_machine_severity(
                    vm_info['uuid']
                )
                vm_info['__Output']['displayName'] = self.map_severity_color(
                    vm_info['severity']
                )
                vm_match_rules.append(
                    'uuid:%s' % (vm_info['uuid'])
                )

            info['vmSummary'] = self.get_severity_summary(
                info['vm']
            )
            info['__Output']['vmSummary.severity'] = info['vmSummary']['__Output']['severity']

        return info

    def match_pod(self, pod_info, match_rules):
        if match_rules is None or len(match_rules) == 0:
            return True

        rules = {}
        for match_rule in match_rules:
            rules[match_rule] = False

            if match_rule.startswith('uuid:'):
                if pod_info['uuid'] == match_rule[5:]:
                    rules[match_rule] = True

            if match_rule.startswith('name:'):
                if match_rule[5:].lower() in pod_info['displayName'].lower():
                    rules[match_rule] = True

            if match_rule.startswith('cluster:'):
                if match_rule[8:].lower() in pod_info['discoveredBy']['displayName'].lower():
                    rules[match_rule] = True

            if match_rule == 'stale':
                if pod_info['isStale']:
                    rules[match_rule] = True

            if match_rule == 'inactive':
                if not pod_info['isActive']:
                    rules[match_rule] = True

            if match_rule == 'critical':
                if pod_info['severity'].lower() in ['critical']:
                    rules[match_rule] = True

            if match_rule == 'major':
                if pod_info['severity'].lower() in ['critical', 'major']:
                    rules[match_rule] = True

            if match_rule == 'minor':
                if pod_info['severity'].lower() in ['critical', 'major', 'minor']:
                    rules[match_rule] = True

        match = True
        for rule in rules:
            match = match and rules[rule]

        return match

    def get_pods(self, resolve_dependencies=False, match_rules=None):
        if self.mo_pod is None:
            if not self.initialize_pod():
                self.log.error(
                    'get_pods',
                    'Managed objects must be initialized first'
                )
                return None

        pods = []

        for managed_object in self.mo_pod:
            pod_info = self.get_pod_info(
                managed_object,
                resolve_dependencies=resolve_dependencies
            )
            if pod_info is not None:
                if not self.match_pod(pod_info, match_rules):
                    continue

                pods.append(
                    pod_info
                )

        self.log.iwo_mo(
            'ContainerPod.info',
            self.mo_pod
        )

        return pods

    def get_pod(self, pod_uuid, resolve_dependencies=False):
        if self.pod is None:
            self.pod = self.get_pods(resolve_dependencies=resolve_dependencies)

        if self.pod is not None:
            for pod in self.pod:
                if pod['uuid'] == pod_uuid:
                    return pod

        return None

    def get_pod_severity(self, pod_uuid, resolve_dependencies=False):
        pod = self.get_pod(
            pod_uuid,
            resolve_dependencies=resolve_dependencies
        )
        if pod is not None:
            return pod['severity']
        return None

    def get_pods_summary(self, match_rules=None):
        pods = self.get_pods(
            resolve_dependencies=False,
            match_rules=match_rules
        )

        summary = None
        if pods is not None:
            summary = self.get_summary(pods)

        return summary

    def print_pods(self, info):
        self.my_output.default(
            json.dumps(
                info,
                indent=4
            )
        )
