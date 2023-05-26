import json
import traceback


class K8sPodObject():
    def __init__(self):
        pass

    def convert_pod_output_json(self, output):
        try:
            output = str(output)
            output = output.replace('\'', '\"')
            output = output.replace(': None', ': null')
            output = output.replace(': True', ': true')
            output = output.replace(': False', ': false')
            return json.loads(output)
        except BaseException:
            self.log.debug('k8s_pods.convert_pod_output_json', output)
            self.log.debug('k8s_pods.convert_pod_output_json', traceback.format_exc())
            return None

    def convert_managed_field(self, managed_field):
        try:
            managed_object = {}
            for attribute in ['api_version', 'fields_type', 'manager', 'operation']:
                managed_object[attribute] = getattr(managed_field, attribute, None)

            managed_object['time'] = self.convert_timestamp(getattr(managed_field, 'time', None))

        except BaseException:
            self.log.error('k8s_pods.convert_managed_field', traceback.format_exc())
            return None

        return managed_object

    def convert_managed_fields(self, managed_fields):
        try:
            if managed_fields is None:
                return None

            managed_object = []
            for item in managed_fields:
                managed_field = self.convert_managed_field(item)
                if managed_field is not None:
                    managed_object.append(managed_field)

        except BaseException:
            self.log.error('k8s_pods.convert_managed_fields', traceback.format_exc())
            return None

        return managed_object

    def convert_owner_reference(self, owner_reference):
        try:
            managed_object = {}
            for attribute in ['api_version', 'block_owner_deletion', 'controller', 'kind', 'name', 'uid']:
                managed_object[attribute] = getattr(owner_reference, attribute, None)

        except BaseException:
            self.log.error('k8s_pods.convert_owner_reference', traceback.format_exc())
            return None

        return managed_object

    def convert_owner_references(self, owner_references):
        try:
            if owner_references is None:
                return None

            managed_object = []
            for item in owner_references:
                owner_reference = self.convert_owner_reference(item)
                if owner_reference is not None:
                    managed_object.append(owner_reference)

        except BaseException:
            self.log.error('k8s_pods.convert_owner_references', traceback.format_exc())
            return None

        return managed_object

    def convert_pod_metadata(self, metadata):
        try:
            managed_object = {}
            attributes = [
                'annotations',
                'cluster_name',
                'deletion_grace_period_seconds',
                'finalizers',
                'generate_name',
                'generation',
                'labels',
                'name',
                'namespace',
                'resource_version',
                'uid'
            ]
            for attribute in attributes:
                managed_object[attribute] = getattr(metadata, attribute, None)

            managed_object['creation_timestamp'] = self.convert_timestamp(getattr(metadata, 'creation_timestamp', None))
            managed_object['deletion_timestamp'] = self.convert_timestamp(getattr(metadata, 'deletion_timestamp', None))
            managed_object['managed_fields'] = self.convert_managed_fields(getattr(metadata, 'managed_fields', None))
            managed_object['owner_references'] = self.convert_owner_references(getattr(metadata, 'owner_references', None))

        except BaseException:
            self.log.error('k8s_pods.convert_pod_metadata', traceback.format_exc())
            return None

        return managed_object

    def convert_env_vars(self, env, fallback_to_string=True):
        try:
            if env is None:
                return None

            output = self.convert_pod_output_json(env)
            if output is None:
                if fallback_to_string:
                    return str(env)
                self.log.error('k8s_pods.convert_env_vars', 'JSON parse failed')

        except BaseException:
            self.log.error('k8s_pods.convert_env_vars', traceback.format_exc())
            return None

        return output

    def convert_env_source_vars(self, env):
        try:
            if env is None:
                return None

            env = self.convert_pod_output_json(env)
            if env is None:
                self.log.error('k8s_pods.convert_env_source_vars', 'JSON parse failed')

        except BaseException:
            self.log.error('k8s_pods.convert_env_source_vars', traceback.format_exc())
            return None

        return env

    def convert_lifecycle(self, lifecycle):
        try:
            if lifecycle is None:
                return None

            lifecycle = self.convert_pod_output_json(lifecycle)
            if lifecycle is None:
                self.log.error('k8s_pods.convert_lifecycle', 'JSON parse failed')

        except BaseException:
            self.log.error('k8s_pods.convert_lifecycle', traceback.format_exc())
            return None

        return lifecycle

    def convert_probe(self, probe, fallback_to_string=True):
        try:
            if probe is None:
                return None

            output = self.convert_pod_output_json(probe)
            if output is None:
                if fallback_to_string:
                    return str(probe)
                self.log.error('k8s_pods.convert_probe', 'JSON parse failed')

        except BaseException:
            self.log.error('k8s_pods.convert_probe', traceback.format_exc())
            return None

        return output

    def convert_container_ports(self, ports):
        try:
            if ports is None:
                return None

            ports = self.convert_pod_output_json(ports)
            if ports is None:
                self.log.error('k8s_pods.convert_container_ports', 'JSON parse failed')

        except BaseException:
            self.log.error('k8s_pods.convert_container_ports', traceback.format_exc())
            return None

        return ports

    def convert_resource_requirements(self, resources):
        try:
            if resources is None:
                return None

            resources = self.convert_pod_output_json(resources)
            if resources is None:
                self.log.error('k8s_pods.convert_resource_requirements', 'JSON parse failed')

        except BaseException:
            self.log.error('k8s_pods.convert_resource_requirements', traceback.format_exc())
            return None

        return resources

    def convert_security_context(self, security_context):
        try:
            if security_context is None:
                return None

            security_context = self.convert_pod_output_json(security_context)
            if security_context is None:
                self.log.error('k8s_pods.convert_security_context', 'JSON parse failed')

        except BaseException:
            self.log.error('k8s_pods.convert_security_context', traceback.format_exc())
            return None

        return security_context

    def convert_container(self, container, include_lifecycle=False):
        try:
            managed_object = {}
            attributes = [
                'args',
                'command',
                'image',
                'image_pull_policy',
                'name',
                'stdin',
                'stdin_once',
                'termination_message_path',
                'termination_message_policy'
            ]
            for attribute in attributes:
                managed_object[attribute] = getattr(container, attribute, None)

            managed_object['env'] = self.convert_env_vars(getattr(container, 'env', None))
            managed_object['env_from'] = self.convert_env_source_vars(getattr(container, 'env_from', None))
            if include_lifecycle:
                managed_object['lifecycle'] = self.convert_lifecycle(getattr(container, 'lifecycle', None))
            managed_object['liveness_probe'] = self.convert_probe(getattr(container, 'probe', None))
            managed_object['ports'] = self.convert_container_ports(getattr(container, 'ports', None))
            managed_object['readiness_probe'] = self.convert_probe(getattr(container, 'readiness_probe', None))
            managed_object['resources'] = self.convert_resource_requirements(getattr(container, 'resources', None))
            managed_object['security_context'] = self.convert_security_context(getattr(container, 'security_context', None))
            managed_object['startup_probe'] = self.convert_probe(getattr(container, 'startup_probe', None))

        except BaseException:
            self.log.error('k8s_pods.convert_container', traceback.format_exc())
            return None

        return managed_object

    def convert_containers(self, containers):
        try:
            if containers is None:
                return None

            managed_object = []
            for item in containers:
                container = self.convert_container(item)
                if container is not None:
                    managed_object.append(container)

        except BaseException:
            self.log.error('k8s_pods.convert_containers', traceback.format_exc())
            return None

        return managed_object

    def convert_node_affinity(self, affinity):
        try:
            if affinity is None:
                return None

            affinity = self.convert_pod_output_json(affinity)
            if affinity is None:
                self.log.error('k8s_pods.convert_node_affinity', 'JSON parse failed')

        except BaseException:
            self.log.error('k8s_pods.convert_node_affinity', traceback.format_exc())
            return None

        return affinity

    def convert_pod_affinity(self, affinity):
        try:
            if affinity is None:
                return None

            affinity = self.convert_pod_output_json(affinity)
            if affinity is None:
                self.log.error('k8s_pods.convert_pod_affinity', 'JSON parse failed')

        except BaseException:
            self.log.error('k8s_pods.convert_pod_affinity', traceback.format_exc())
            return None

        return affinity

    def convert_pod_anti_affinity(self, affinity):
        try:
            if affinity is None:
                return None

            affinity = self.convert_pod_output_json(affinity)
            if affinity is None:
                self.log.error('k8s_pods.convert_pod_anti_affinity', 'JSON parse failed')

        except BaseException:
            self.log.error('k8s_pods.convert_pod_anti_affinity', traceback.format_exc())
            return None

        return affinity

    def convert_affinity(self, affinity):
        try:
            if affinity is None:
                return None

            managed_object = {}
            managed_object['node_affinity'] = self.convert_node_affinity(getattr(affinity, 'node_affinity', None))
            managed_object['pod_affinity'] = self.convert_pod_affinity(getattr(affinity, 'pod_affinity', None))
            managed_object['pod_anti_affinity'] = self.convert_pod_anti_affinity(getattr(affinity, 'pod_anti_affinity', None))

        except BaseException:
            self.log.error('k8s_pods.convert_affinity', traceback.format_exc())
            return None

        return managed_object

    def convert_pod_dns_config(self, dns_config):
        try:
            if dns_config is None:
                return None

            dns_config = self.convert_pod_output_json(dns_config)
            if dns_config is None:
                self.log.error('k8s_pods.convert_pod_dns_config', 'JSON parse failed')

        except BaseException:
            self.log.error('k8s_pods.convert_pod_dns_config', traceback.format_exc())
            return None

        return dns_config

    def convert_host_aliases(self, host_aliases):
        try:
            if host_aliases is None:
                return None

            host_aliases = self.convert_pod_output_json(host_aliases)
            if host_aliases is None:
                self.log.error('k8s_pods.convert_pod_dns_config', 'JSON parse failed')

        except BaseException:
            self.log.error('k8s_pods.convert_pod_dns_config', traceback.format_exc())
            return None

        return host_aliases

    def convert_pod_readiness_gates(self, readiness_gates):
        try:
            if readiness_gates is None:
                return None

            readiness_gates = self.convert_pod_output_json(readiness_gates)
            if readiness_gates is None:
                self.log.error('k8s_pods.convert_pod_readiness_gates', 'JSON parse failed')

        except BaseException:
            self.log.error('k8s_pods.convert_pod_readiness_gates', traceback.format_exc())
            return None

        return readiness_gates

    def convert_pod_security_context(self, security_context):
        try:
            if security_context is None:
                return None

            security_context = self.convert_pod_output_json(security_context)
            if security_context is None:
                self.log.error('k8s_pods.convert_pod_security_context', 'JSON parse failed')

        except BaseException:
            self.log.error('k8s_pods.convert_pod_security_context', traceback.format_exc())
            return None

        return security_context

    def convert_tolerations(self, tolerations):
        try:
            if tolerations is None:
                return None

            tolerations = self.convert_pod_output_json(tolerations)
            if tolerations is None:
                self.log.error('k8s_pods.convert_tolerations', 'JSON parse failed')

        except BaseException:
            self.log.error('k8s_pods.convert_tolerations', traceback.format_exc())
            return None

        return tolerations

    def convert_topology_spread_constraints(self, topology_spread_constraints):
        try:
            if topology_spread_constraints is None:
                return None

            topology_spread_constraints = self.convert_pod_output_json(topology_spread_constraints)
            if topology_spread_constraints is None:
                self.log.error('k8s_pods.convert_topology_spread_constraints', 'JSON parse failed')

        except BaseException:
            self.log.error('k8s_pods.convert_topology_spread_constraints', traceback.format_exc())
            return None

        return topology_spread_constraints

    def convert_volumes(self, volumes):
        if volumes is None:
            return None

        return self.convert_pod_output_json(volumes)

    def convert_pod_spec(self, spec):
        try:
            managed_object = {}
            attributes = [
                'active_deadline_seconds',
                'automount_service_account_token',
                'dns_policy',
                'enable_service_links',
                'host_ipc',
                'host_network',
                'host_pid',
                'hostname',
                'node_name',
                'node_selector',
                'overhead',
                'preemption_policy',
                'priority',
                'priority_class_name',
                'restart_policy',
                'runtime_class_name',
                'scheduler_name',
                'service_account_name',
                'subdomain',
                'termination_grace_period_seconds'
            ]
            for attribute in attributes:
                managed_object[attribute] = getattr(spec, attribute, None)

            managed_object['affinity'] = self.convert_affinity(getattr(spec, 'affinity', None))
            managed_object['containers'] = self.convert_containers(getattr(spec, 'containers', None))
            managed_object['dns_config'] = self.convert_pod_dns_config(getattr(spec, 'dns_config', None))
            managed_object['host_aliases'] = self.convert_host_aliases(getattr(spec, 'host_aliases', None))
            managed_object['readiness_gates'] = self.convert_pod_readiness_gates(getattr(spec, 'readiness_gates', None))
            managed_object['security_context'] = self.convert_pod_security_context(getattr(spec, 'security_context', None))
            managed_object['tolerations'] = self.convert_tolerations(getattr(spec, 'tolerations', None))
            managed_object['topology_spread_constraints'] = self.convert_topology_spread_constraints(getattr(spec, 'topology_spread_constraints', None))
            managed_object['volumes'] = self.convert_volumes(getattr(spec, 'volumes', None))

        except BaseException:
            self.log.error('k8s_pods.convert_pod_spec', traceback.format_exc())
            return None

        return managed_object

    def convert_pod_condition(self, condition):
        try:
            managed_object = {}
            for attribute in ['message', 'reason', 'status', 'type']:
                managed_object[attribute] = getattr(condition, attribute, None)

            managed_object['last_probe_time'] = self.convert_timestamp(getattr(condition, 'last_probe_time', None))
            managed_object['last_transition_time'] = self.convert_timestamp(getattr(condition, 'last_transition_time', None))

        except BaseException:
            self.log.error('k8s_pods.convert_pod_condition', traceback.format_exc())
            return None

        return managed_object

    def convert_pod_conditions(self, conditions):
        try:
            if conditions is None:
                return None

            managed_object = []
            for condition in conditions:
                info = self.convert_pod_condition(condition)
                if info is not None:
                    managed_object.append(info)

        except BaseException:
            self.log.error('k8s_pods.convert_pod_conditions', traceback.format_exc())
            return None

        return managed_object

    def convert_container_state_running(self, state):
        try:
            if state is None:
                return None

            managed_object = {}
            managed_object['started_at'] = self.convert_timestamp(getattr(state, 'started_at', None))

        except BaseException:
            self.log.error('k8s_pods.convert_container_state_running', traceback.format_exc())
            return None

        return managed_object

    def convert_container_state_terminated(self, state):
        try:
            managed_object = {}
            for attribute in ['container_id', 'exit_code', 'reason', 'message', 'signal']:
                managed_object[attribute] = getattr(state, attribute, None)

            managed_object['started_at'] = self.convert_timestamp(getattr(state, 'started_at', None))
            managed_object['finished_at'] = self.convert_timestamp(getattr(state, 'finished_at', None))

        except BaseException:
            self.log.error('k8s_pods.convert_container_state_terminated', traceback.format_exc())
            return None

        return managed_object

    def convert_container_state_waiting(self, state):
        try:
            if state is None:
                return state

            managed_object = {}
            for attribute in ['reason', 'messsage']:
                managed_object[attribute] = getattr(state, attribute, None)

        except BaseException:
            self.log.error('k8s_pods.convert_container_state_waiting', traceback.format_exc())
            return None

        return managed_object

    def convert_container_state(self, state):
        try:
            managed_object = {}
            managed_object['running'] = self.convert_container_state_running(getattr(state, 'running', None))
            managed_object['terminated'] = self.convert_container_state_terminated(getattr(state, 'terminated', None))
            managed_object['waiting'] = self.convert_container_state_waiting(getattr(state, 'waiting', None))

        except BaseException:
            self.log.error('k8s_pods.convert_container_state', traceback.format_exc())
            return None

        return managed_object

    def convert_container_status(self, container_status):
        try:
            managed_object = {}
            for attribute in ['container_id', 'image', 'image_id', 'name', 'ready', 'restart_count', 'started']:
                managed_object[attribute] = getattr(container_status, attribute, None)

            managed_object['state'] = self.convert_container_state(getattr(container_status, 'state', None))
            managed_object['last_state'] = self.convert_container_state(getattr(container_status, 'last_state', None))

        except BaseException:
            self.log.error('k8s_pods.convert_container_status', traceback.format_exc())
            return None

        return managed_object

    def convert_container_statuses(self, container_statuses):
        try:
            if container_statuses is None:
                return None

            managed_object = []
            for container_status in container_statuses:
                info = self.convert_container_status(container_status)
                if info is not None:
                    managed_object.append(info)

        except BaseException:
            self.log.error('k8s_pods.convert_container_statuses', traceback.format_exc())
            return None

        return managed_object

    def convert_pod_ip(self, ip_address):
        try:
            return getattr(ip_address, 'ip', None)

        except BaseException:
            self.log.error('k8s_pods.convert_pod_ip', traceback.format_exc())
            return None

    def convert_pod_ips(self, ips):
        try:
            if ips is None:
                return None

            managed_object = []
            for ip_address in ips:
                info = self.convert_pod_ip(ip_address)
                if info is not None:
                    managed_object.append(info)

        except BaseException:
            self.log.error('k8s_pods.convert_pod_ips', traceback.format_exc())
            return None

        return managed_object

    def convert_pod_status(self, status):
        try:
            managed_object = {}
            for attribute in ['host_ip', 'message', 'nominated_node_name', 'phase', 'pod_ip', 'qos_class', 'reason']:
                managed_object[attribute] = getattr(status, attribute, None)

            managed_object['conditions'] = self.convert_pod_conditions(getattr(status, 'conditions', None))
            managed_object['container_statuses'] = self.convert_container_statuses(getattr(status, 'container_statuses', None))
            managed_object['init_container_statuses'] = self.convert_container_statuses(getattr(status, 'init_container_statuses', None))
            managed_object['pod_i_ps'] = self.convert_pod_ips(getattr(status, 'pod_i_ps', None))
            managed_object['start_time'] = self.convert_timestamp(getattr(status, 'start_time', None))

        except BaseException:
            self.log.error('k8s_pods.convert_pod_status', traceback.format_exc())
            return None

        return managed_object

    def convert_pod(self, pod):
        try:
            managed_object = {}
            managed_object['metadata'] = self.convert_pod_metadata(getattr(pod, 'metadata', None))
            managed_object['spec'] = self.convert_pod_spec(getattr(pod, 'spec', None))
            managed_object['status'] = self.convert_pod_status(getattr(pod, 'status', None))

        except BaseException:
            self.log.error('k8s_pods.convert_node', traceback.format_exc())
            return None

        return managed_object
