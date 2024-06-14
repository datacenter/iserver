import time
import json

from lib import filter_helper


class K8sPodInfo():
    def __init__(self):
        self.pod = None

    def get_pod_networks_info(self, pod_mo):
        networks = []

        annotations = self.get(pod_mo, 'metadata:annotations', on_error={}, on_none={})
        if 'k8s.v1.cni.cncf.io/networks-status' in annotations:
            networks_mo = json.loads(
                annotations['k8s.v1.cni.cncf.io/networks-status']
            )
            for network_mo in networks_mo:
                network_info = {}
                network_info['name'] = network_mo['name']
                network_info['interface'] = network_mo['interface']
                network_info['mac'] = self.get(network_mo, 'mac')
                network_info['ips'] = self.get(network_mo, 'ips', on_error=[], on_none=[])
                network_info['default'] = self.get(network_mo, 'default', on_error=False, on_none=False)
                network_info['device-info'] = self.get(network_mo, 'device-info', on_error={}, on_none={})
                network_info['pci'] = self.get(network_mo, 'device-info:pci:pci-address')
                network_info['dns'] = self.get(network_mo, 'dns', on_error={}, on_none={})
                networks.append(
                    network_info
                )

        return networks

    def get_pod_container_res_info(self, res_mo):
        info = {}

        keys = ['cpu', 'memory', 'hugepages-2Mi', 'hugepages-1Gi']
        for key in keys:
            info[key] = None
            if key in res_mo:
                info[key] = res_mo[key]

            if info[key] is not None:
                info['%sT' % (key)] = info[key]
            if info[key] is None:
                info['%sT' % (key)] = '--'

        info['hpT'] = '--'
        if info['hugepages-2Mi'] is not None:
            info['hpT'] = '%s (2Mi)' % (
                info['hugepages-2Mi']
            )
        if info['hugepages-1Gi'] is not None:
            info['hpT'] = '%s (1Gi)' % (
                info['hugepages-1Gi']
            )

        info['custom'] = {}
        info['customT'] = []
        for key in res_mo:
            if key not in keys:
                info['custom'][key] = res_mo[key]
                info['customT'].append(
                    '%s: %s' % (key, res_mo[key])
                )

        if len(info['customT']) == 0:
            info['customT'].append('--')

        return info

    def get_pod_container_port_info(self, ports_mo):
        info = []

        for port_mo in ports_mo:
            port_info = {}
            for key in ['container_port', 'host_ip', 'host_port', 'name', 'protocol']:
                port_info[key] = None
                if key in port_mo:
                    port_info[key] = port_mo[key]

            port_info['portT'] = '%s/%s' % (
                port_info['container_port'],
                port_info['protocol']
            )
            if port_info['name'] is not None:
                port_info['portT'] = '%s [%s]' % (
                    port_info['portT'],
                    port_info['name']
                )

            if port_info['host_ip'] is None and port_info['host_port'] is None:
                port_info['hostT'] = '--'

            if port_info['host_ip'] is None and port_info['host_port'] is not None:
                port_info['hostT'] = port_info['host_port']

            if port_info['host_ip'] is not None and port_info['host_port'] is not None:
                port_info['hostT'] = '%s:%s' % (
                    port_info['host_ip'],
                    port_info['host_port']
                )

            info.append(
                port_info
            )

        return info

    def get_pod_container_info(self, pod_namespace, container_spec_mo, container_status_mo, volumes_info):
        info = {}
        info['__Output'] = {}
        now = int(time.time())

        info['name'] = self.get(container_spec_mo, 'name')
        info['image'] = self.get(container_spec_mo, 'image')
        info['image_id'] = self.get(container_status_mo, 'image_id')
        info['container_id'] = self.get(container_status_mo, 'container_id')
        info['command'] = self.get(container_spec_mo, 'command', on_error=[], on_none=[])

        info['volume_mount'] = []
        mounts_mo = self.get(container_spec_mo, 'volume_mounts', on_error=[], on_none=[])
        for mount_mo in mounts_mo:
            mount_info = {}
            mount_info['name'] = self.get(mount_mo, 'name')
            mount_info['path'] = self.get(mount_mo, 'mount_path')
            mount_info['sub_path'] = self.get(mount_mo, 'sub_path')
            mount_info['read_only'] = self.get(mount_mo, 'read_only')
            for volume_info in volumes_info:
                if volume_info['name'] == mount_info['name']:
                    mount_info['type'] = volume_info['type']
                    mount_info['mo'] = volume_info['mo']

            info['volume_mount'].append(
                mount_info
            )

        info['volume_mount'] = sorted(
            info['volume_mount'],
            key=lambda i: i['name']
        )

        envs_mo = self.get(container_spec_mo, 'env', on_error=[], on_none=[])
        info['env'] = []
        for env_mo in envs_mo:
            env_info = {}
            env_info['name'] = self.get(env_mo, 'name')
            env_info['value'] = self.get(env_mo, 'value')
            env_info['config_map_key_ref'] = self.get(env_mo, 'value_from:config_map_key_ref')
            env_info['field_ref'] = self.get(env_mo, 'value_from:field_ref')
            env_info['resource_field_ref'] = self.get(env_mo, 'value_from:resource_field_ref')
            env_info['secret_key_ref'] = self.get(env_mo, 'value_from:secret_key_ref')

            env_info['source_type'] = '--'
            env_info['source_value'] = '--'

            if env_info['value'] is not None:
                env_info['source_type'] = 'value'
                env_info['source_value'] = env_info['value']

            if env_info['config_map_key_ref'] is not None:
                env_info['source_type'] = 'cm'
                cm_name = self.get(env_mo, 'value_from:config_map_key_ref:name')
                cm_key = self.get(env_mo, 'value_from:config_map_key_ref:key')
                if cm_name is not None and cm_key is not None:
                    env_info['source_value'] = '%s:%s' % (
                        cm_name,
                        cm_key
                    )

            if env_info['resource_field_ref'] is not None:
                env_info['source_type'] = 'res'

            if env_info['field_ref'] is not None:
                env_info['source_type'] = 'field'
                field_path = self.get(env_mo, 'value_from:field_ref:field_path')
                if field_path is not None:
                    env_info['source_value'] = field_path

            if env_info['secret_key_ref'] is not None:
                env_info['source_type'] = 'secret'
                secret_name = self.get(env_mo, 'value_from:secret_key_ref:name')
                secret_key = self.get(env_mo, 'value_from:secret_key_ref:key')
                if secret_name is not None and secret_key is not None:
                    env_info['source_value'] = '%s:%s' % (
                        secret_name,
                        secret_key
                    )

            info['env'].append(
                env_info
            )

        info['cm'] = []
        for env_info in info['env']:
            if env_info['config_map_key_ref'] is not None:
                cm_info = {}
                cm_info['namespace'] = pod_namespace
                cm_info['name'] = env_info['config_map_key_ref']['name']
                info['cm'].append(
                    cm_info
                )

        info['requests'] = self.get_pod_container_res_info(
            self.get(container_spec_mo, 'resources:requests', on_error={}, on_none={})
        )
        info['limits'] = self.get_pod_container_res_info(
            self.get(container_spec_mo, 'resources:limits', on_error={}, on_none={})
        )

        info['port'] = self.get_pod_container_port_info(
            self.get(container_spec_mo, 'ports', on_error=[], on_none=[])
        )

        info['started_at'] = None
        info['finished_at'] = None
        info['age'] = '--'

        info['started'] = self.get(container_status_mo, 'started', on_error=False, on_none=False)
        info['ready'] = self.get(container_status_mo, 'ready', on_error=False, on_none=False)
        info['restart_count'] = self.get(container_status_mo, 'restart_count', on_error=0)
        info['restart_countT'] = info['restart_count']

        container_state_mo = self.get(container_status_mo, 'state', on_error={})
        container_state_running_mo = self.get(container_state_mo, 'running')
        container_state_terminated_mo = self.get(container_state_mo, 'terminated')
        container_state_waiting_mo = self.get(container_state_mo, 'waiting')

        # ContainerState holds a possible state of container. Only one of its members may be specified. If none of them is specified, the default one is ContainerStateWaiting.
        info['stateT'] = 'Waiting'
        info['__Output']['stateT'] = 'Yellow'
        info['state_waiting'] = True
        info['state_running'] = False
        info['state_terminated'] = False

        if container_state_running_mo is not None:
            info['stateT'] = 'Running'
            info['__Output']['stateT'] = 'Green'
            info['state_waiting'] = False
            info['state_running'] = True
            info['state_terminated'] = False
            info['started_at'] = self.get(container_state_running_mo, 'started_at')
            info['started_at_epoch'] = self.convert_timestamp(
                info['started_at']
            )
            info['age'] = self.convert_timestamp_to_age(
                info['started_at'],
                on_error='--'
            )

            if info['restart_count'] > 0:
                info['restart_countT'] = '%s (%s ago)' % (
                    info['restart_countT'],
                    self.convert_age(now - info['started_at_epoch'])
                )

        if container_state_terminated_mo is not None:
            info['stateT'] = 'Terminated'
            info['state_waiting'] = False
            info['state_running'] = False
            info['state_terminated'] = True
            info['started_at'] = self.get(container_state_terminated_mo, 'started_at')
            info['finished_at'] = self.get(container_state_terminated_mo, 'finished_at')
            info['terminated_exit_code'] = self.get(container_state_terminated_mo, 'exit_code')
            if info['terminated_exit_code'] is None:
                info['__Output']['stateT'] = 'Red'
                info['stateT'] = 'Terminated (code: --)'
            else:
                info['stateT'] = 'Terminated (code: %s)' % (
                    info['terminated_exit_code']
                )
                if info['terminated_exit_code'] > 0:
                    info['__Output']['stateT'] = 'Red'
                else:
                    info['__Output']['stateT'] = 'Green'

            info['terminate_message'] = self.get(container_state_terminated_mo, 'message')
            info['terminate_reason'] = self.get(container_state_terminated_mo, 'reason')
            info['terminate_signal'] = self.get(container_state_terminated_mo, 'signal')

        if container_state_waiting_mo is not None:
            info['waiting_message'] = self.get(container_state_waiting_mo, 'message')
            info['waiting_reason'] = self.get(container_state_waiting_mo, 'reason')

        return info

    def get_pod_volume_info(self, volume_mo):
        info = {}
        info['name'] = volume_mo['name']
        info['type'] = None
        info['mo'] = None

        unsupported = [
            'aws_elastic_block_store',
            'azure_disk',
            'azure_file',
            'cephfs',
            'cinder',
            'csi',
            'flex_volume',
            'flocker',
            'gce_persistent_disk',
            'git_repo',
            'glusterfs',
            'iscsi',
            'photon_persistent_disk',
            'quobyte',
            'rbd',
            'scale_io',
            'storageos',
            'vsphere_volume'
        ]
        for key in unsupported:
            if self.get(volume_mo, key) is not None:
                info['type'] = 'Unsupported'
                self.log.error(
                    'get_pod_volume_info',
                    'Unsupported volume defined: %s' % (key)
                )

        config_map = self.get(volume_mo, 'config_map')
        if config_map is not None:
            info['type'] = 'config_map'
            info['mo'] = config_map

        downward_api = self.get(volume_mo, 'downward_api')
        if downward_api is not None:
            info['type'] = 'downward_api'
            info['mo'] = downward_api

        empty_dir = self.get(volume_mo, 'empty_dir')
        if empty_dir is not None:
            info['type'] = 'empty_dir'
            info['mo'] = empty_dir

        ephemeral = self.get(volume_mo, 'ephemeral')
        if ephemeral is not None:
            info['type'] = 'ephemeral'
            info['mo'] = ephemeral

        fc_mo = self.get(volume_mo, 'fc')
        if fc_mo is not None:
            info['type'] = 'fc'
            info['mo'] = fc_mo

        host_path = self.get(volume_mo, 'host_path')
        if host_path is not None:
            info['type'] = 'host_path'
            info['mo'] = host_path

        nfs = self.get(volume_mo, 'nfs')
        if nfs is not None:
            info['type'] = 'nfs'
            info['mo'] = nfs

        pvc = self.get(volume_mo, 'persistent_volume_claim')
        if pvc is not None:
            info['type'] = 'persistent_volume_claim'
            info['mo'] = pvc

        portworx_volume = self.get(volume_mo, 'portworx_volume')
        if portworx_volume is not None:
            info['type'] = 'portworx_volume'
            info['mo'] = portworx_volume

        secret = self.get(volume_mo, 'secret')
        if secret is not None:
            info['type'] = 'secret'
            info['mo'] = secret

        projected = self.get(volume_mo, 'projected')
        if projected is not None:
            info['type'] = 'projected'
            info['mo'] = []
            for item_mo in self.get(volume_mo, 'projected:sources', on_error=[], on_none=[]):
                config_map = self.get(item_mo, 'config_map')
                if config_map is not None:
                    projected_info = {}
                    projected_info['name'] = info['name']
                    projected_info['type'] = 'config_map'
                    projected_info['mo'] = config_map
                    info['mo'].append(
                        projected_info
                    )

                secret = self.get(item_mo, 'secret')
                if secret is not None:
                    projected_info = {}
                    projected_info['name'] = info['name']
                    projected_info['type'] = 'secret'
                    projected_info['mo'] = secret
                    info['mo'].append(
                        projected_info
                    )

                downward_api = self.get(item_mo, 'downward_api')
                if downward_api is not None:
                    projected_info = {}
                    projected_info['name'] = info['name']
                    projected_info['type'] = 'downward_api'
                    projected_info['mo'] = downward_api
                    info['mo'].append(
                        projected_info
                    )

                service_account_token = self.get(item_mo, 'service_account_token')
                if service_account_token is not None:
                    projected_info = {}
                    projected_info['name'] = info['name']
                    projected_info['type'] = 'service_account_token'
                    projected_info['mo'] = service_account_token
                    info['mo'].append(
                        projected_info
                    )
        return info

    def get_pod_info(self, pod_mo):
        if pod_mo is None:
            return None

        now = int(time.time())

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            pod_mo
        )
        info.update(metadata_info)

        info['volume'] = []
        for volume_mo in self.get(pod_mo, 'spec:volumes'):
            info['volume'].append(
                self.get_pod_volume_info(
                    volume_mo
                )
            )

        info['volume'] = sorted(
            info['volume'],
            key=lambda i: i['name']
        )

        info['container'] = []
        info['container_count'] = 0
        info['container_ready'] = 0
        info['container_restart_count'] = 0
        last_container_started_at_epoch = None

        container_specs = self.get(pod_mo, 'spec:containers', on_error=[], on_none=[])
        container_statuses = self.get(pod_mo, 'status:container_statuses', on_error=[], on_none=[])
        for container_spec in container_specs:
            container_spec_name = self.get(container_spec, 'name')
            if container_spec_name is None:
                self.log.error(
                    'k8s.get_pod_info',
                    'Unexpected container spec: %s' % (container_spec)
                )
                continue

            container_info = None
            for container_status in container_statuses:
                container_status_name = self.get(container_status, 'name')
                if container_status_name is None:
                    self.log.error(
                        'k8s.get_pod_info',
                        'Unexpected container status: %s' % (container_status)
                    )
                    continue

                if container_spec_name == container_status_name:
                    container_info = self.get_pod_container_info(
                        info['namespace'],
                        container_spec,
                        container_status,
                        info['volume']
                    )
                    break

            if container_info is None:
                self.log.error(
                    'k8s.get_pod_info',
                    'Unexpected lack of container status: %s' % (container_spec)
                )
                container_info = self.get_pod_container_info(
                    info['namespace'],
                    container_spec,
                    None,
                    info['volume']
                )

            info['container_count'] = info['container_count'] + 1
            info['container_restart_count'] = info['container_restart_count'] + container_info['restart_count']
            if container_info['ready']:
                info['container_ready'] = info['container_ready'] + 1

            if container_info['state_running']:
                if container_info['started_at_epoch'] is not None:
                    if last_container_started_at_epoch is None:
                        last_container_started_at_epoch = container_info['started_at_epoch']

                    if last_container_started_at_epoch < container_info['started_at_epoch']:
                        last_container_started_at_epoch = container_info['started_at_epoch']

            info['container'].append(
                container_info
            )

        info['container'] = sorted(
            info['container'],
            key=lambda i: i['name']
        )

        info['container_restart_countT'] = info['container_restart_count']
        if info['container_restart_count'] > 0:
            if last_container_started_at_epoch is not None:
                info['container_restart_countT'] = '%s (%s ago)' % (
                    info['container_restart_count'],
                    self.convert_age(now - last_container_started_at_epoch)
                )

        info['container_state_summary'] = '%s/%s' % (
            info['container_ready'],
            info['container_count']
        )

        # Condition: Initialized, PodScheduled, ContainersReady, Ready
        info['condition'] = []
        for condition_type in ['Initialized', 'PodScheduled', 'ContainersReady', 'Ready']:
            condition_info = {}
            condition_info['__Output'] = {}
            condition_info['type'] = condition_type
            condition_info['status'] = 'Unknown'
            for condition_mo in self.get(pod_mo, 'status:conditions', on_error=[], on_none=[]):
                condition_mo_type = self.get(condition_mo, 'type')
                if condition_mo_type is not None and condition_mo_type == condition_type:
                    condition_info['status'] = self.get(condition_mo, 'status', on_error='Unknown', on_none='Unknown')

            if condition_info['status'] == 'True':
                condition_info['typeT'] = '%s: \u2713' % (
                    condition_info['type']
                )

            if condition_info['status'] in ['False', 'Unknown']:
                condition_info['typeT'] = '%s: \u2717' % (
                    condition_info['type']
                )

            info['condition'].append(
                condition_info
            )

        # Phase: Pending, Running, Succeeded (Completed), Failed, Unknown
        info['phase'] = self.get(pod_mo, 'status:phase', on_error='Unknown', on_none='Unknown')
        info['phaseT'] = info['phase']
        if info['phaseT'] == 'Succeeded':
            info['phaseT'] = 'Completed'

        if info['phaseT'] in ['Running', 'Completed']:
            info['__Output']['phaseT'] = 'Green'

        if info['phaseT'] in ['Failed', 'Unknown']:
            info['__Output']['phaseT'] = 'Red'

        if info['phaseT'] in ['Pending']:
            info['__Output']['phaseT'] = 'Yellow'

        info['running'] = False
        if info['phase'] == 'Running':
            info['running'] = True

        info['pod_ip'] = self.get(pod_mo, 'status:pod_ip', on_error='--', on_none='--')
        info['host_ip'] = self.get(pod_mo, 'status:host_ip', on_error='--', on_none='--')

        info['host_name'] = info['host_ip']
        node_info = self.get_node_with_ip(
            info['host_ip']
        )
        if node_info is not None:
            info['host_name'] = node_info['name']

        info['host_network'] = self.get(pod_mo, 'spec:host_network', on_error=False, on_none=False)
        info['network'] = self.get_pod_networks_info(
            pod_mo
        )

        return info

    def get_pods_info(self, cache_enabled=True):
        if cache_enabled:
            if self.pod is not None:
                return self.pod

        managed_objects = self.get_pod_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.pod = []
        for managed_object in managed_objects:
            pod_info = {}
            pod_info['info'] = self.get_pod_info(
                managed_object
            )
            pod_info['mo'] = managed_object
            self.pod.append(
                pod_info
            )

        return self.pod

    def match_pod(self, pod_info, pod_filter):
        if pod_filter is None or len(pod_filter) == 0:
            return True

        for ap_rule in pod_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, pod_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_namespace_name(value, '%s/%s' % (pod_info['namespace'], pod_info['name'])):
                    return False

            if key == 'owner':
                key_found = True
                if not filter_helper.match_namespace_name(value, pod_info['owner']):
                    return False

            if key == 'label':
                key_found = True
                found = False
                for label_name in pod_info['label']:
                    if filter_helper.match_string(value.split(':', maxsplit=1)[0], label_name):
                        if filter_helper.match_string(value.split(':')[1], pod_info['label'][label_name]):
                            found = True

                if not found:
                    return False

            if key == 'cm':
                key_found = True
                found = False

                if len(value.split(':')) > 2:
                    self.log.error(
                        'match_pod',
                        'Unsupported cm-name value: %s' % (value)
                    )
                    return False

                if len(value.split(':')) == 1:
                    cm_namespace = None
                    cm_name = value

                if len(value.split(':')) == 2:
                    (cm_namespace, cm_name) = value.split(':')

                for container_info in pod_info['container']:
                    for cm_info in container_info['cm']:
                        if cm_namespace is None:
                            if filter_helper.match_string(cm_name, cm_info['name']):
                                found = True
                                break

                        if cm_namespace is not None:
                            if filter_helper.match_string(cm_namespace, cm_info['namespace']):
                                if filter_helper.match_string(cm_name, cm_info['name']):
                                    found = True
                                    break

                if not found:
                    return False

            if key == 'pvc':
                key_found = True
                found = False
                for volume_info in pod_info['volume']:
                    if volume_info['type'] == 'persistent_volume_claim':
                        if filter_helper.match_namespace_name(value, '%s/%s' % (pod_info['namespace'], volume_info['mo']['claim_name'])):
                            found = True
                            break

                if not found:
                    return False

            # if key == 'mac':
            #     key_found = True
            #     found = False
            #     for network in pod_info['networks']:
            #         if 'mac' in network:
            #             if filter_helper.match_string(value, network['mac']):
            #                 found = True

            #     if not found:
            #         return False

            # if key == 'network':
            #     key_found = True
            #     found = False
            #     for network in pod_info['networks']:
            #         if 'mac' in network:
            #             if filter_helper.match_string(value, network['name']):
            #                 found = True

            #     if not found:
            #         return False

            if not key_found:
                self.log.error(
                    'match_pod',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_pods(self, object_filter=None, service_info=False, log_info=False, return_mo=False, cache_enabled=True):
        all_pods = self.get_pods_info(cache_enabled=cache_enabled)
        if all_pods is None:
            return None

        pods = []

        for pod_info in all_pods:
            if not self.match_pod(pod_info['info'], object_filter):
                continue

            if return_mo:
                pods.append(
                    pod_info['mo']
                )
                continue

            if service_info:
                pod_info['info']['service'] = []
                pod_services = []
                for label_key in pod_info['info']['label']:
                    service_filter = [
                        'selector:%s:%s' % (
                            label_key,
                            pod_info['info']['label'][label_key]
                        )
                    ]
                    services = self.get_services(
                        object_filter=service_filter
                    )
                    if services is not None:
                        for pod_service_info in services:
                            service_match = True
                            for key in pod_service_info['selector']:
                                if key not in pod_info['info']['label']:
                                    service_match = False
                                    break

                                if pod_info['info']['label'][key] != pod_service_info['selector'][key]:
                                    service_match = False
                                    break

                            if service_match:
                                if pod_service_info['namespace_name'] not in pod_services:
                                    pod_info['info']['service'].append(
                                        pod_service_info
                                    )
                                    pod_services.append(
                                        pod_service_info['namespace_name']
                                    )

            if log_info:
                pod_info['info']['log'] = self.get_pod_log_mo(
                    pod_info['info']['namespace'],
                    pod_info['info']['name']
                )

            pods.append(
                pod_info['info']
            )

        return pods

    # def get_pod_replicaset_info(self, pod_id):
    #     try:
    #         data = dict()

    #         pod = self.get_pod_summary(self.get_pod(pod_id))
    #         if pod is None:
    #             return None

    #         replicaset_name = pod['replicaset_name']
    #         data['name'] = replicaset_name
    #         if data['name'] is not None:
    #             data['data'] = self.get_replica_set(
    #                 replicaset_name,
    #                 pod['namespace'],
    #                 summary = True
    #             )
    #             data['pods'] = self.get_pods_with_replica_set(
    #                 replicaset_name,
    #                 exclude_pod_id = pod_id
    #             )

    #     except:
    #         self.log.error('k8s_pods.get_pod_replicaset_info', traceback.format_exc())

    #     return data

    # def get_pod_replicaset_name(self, pod):
    #     try:
    #         for owner_reference in pod['metadata']['owner_references']:
    #             if owner_reference['kind'] == 'ReplicaSet':
    #                 return owner_reference['name']
    #     except:
    #         self.log.error('k8s_pods.get_pod_replicaset_name', traceback.format_exc())
    #     return None

    # def is_pod_ready(self, pod):
    #     try:
    #         ready = True

    #         if pod['status']['conditions'] is None:
    #             return False

    #         for c in pod['status']['conditions']:
    #             if c['type'] == 'Ready':
    #                 if c['status'] != 'True':
    #                     ready = False

    #     except:
    #         self.log.error('k8s_pods.is_pod_ready', traceback.format_exc())
    #         self.log.error('k8s_pods.is_pod_ready', pod)
    #         return False

    #     return ready

    # def get_pod_job(self, pod):
    #     try:
    #         for owner_reference in pod['metadata']['owner_references']:
    #             if owner_reference['kind'] == 'Job':
    #                 return owner_reference['name']

    #     except:
    #         self.log.error('k8s_pods.get_pod_job', traceback.format_exc())
    #         self.log.error('k8s_pods.get_pod_job', pod)

    #     return None

    # def is_pod_scheduled(self, pod):
    #     try:
    #         scheduled = True

    #         if pod['status']['conditions'] is None:
    #             return False

    #         for c in pod['status']['conditions']:
    #             if c['type'] == 'PodScheduled':
    #                 if c['status'] != 'True':
    #                     scheduled = False

    #     except:
    #         self.log.error('k8s_pods.is_pod_scheduled', traceback.format_exc())
    #         self.log.error('k8s_pods.is_pod_scheduled', pod)
    #         return False

    #     return scheduled

    # def get_pod_scheduling_problem(self, node_labels, node_selector):
    #     try:
    #         scheduling_problem = None
    #         if node_selector is not None:
    #             for s in node_selector:
    #                 if s['match_expressions'] is not None:
    #                     for m in s['match_expressions']:
    #                         if m['operator'] == 'In':
    #                             k = m['key']
    #                             for v in m['values']:
    #                                 node_exists = False
    #                                 for label in node_labels:
    #                                     if label['key'] == k and label['value'] == v:
    #                                         node_exists = True

    #                                 if not node_exists:
    #                                     scheduling_problem = 'No node with label %s:%s' % (k, v)

    #     except:
    #         self.log.error('k8s_pods.get_pod_scheduling_problem', traceback.format_exc())
    #         return None

    #     return scheduling_problem

    # def are_pods_scheduled(self, pods):
    #     try:
    #         scheduled = True
    #         for p in pods:
    #             scheduled = scheduled and p['scheduled']
    #             if not scheduled:
    #                 break

    #     except:
    #         self.log.error('k8s_pods.are_pods_scheduled', traceback.format_exc())
    #         return False

    #     return scheduled

    # def get_pods_ready_count(self):
    #     count = 0
    #     try:
    #         for p in self.pods:
    #             if p['ready']:
    #                 count = count + 1

    #     except:
    #         self.log.error('k8s_pods.get_pods_ready_count', traceback.format_exc())

    #     return count

    # def get_pods_status_summary(self, pods):
    #     try:
    #         status = dict()
    #         for p in pods:
    #             if p['job_name'] is None:
    #                 if p['ready']:
    #                     if 'Ready' in status:
    #                         status['Ready'] = status['Ready'] + 1
    #                     else:
    #                         status['Ready'] = 1

    #                 if not p['ready']:
    #                     if 'Not Ready' in status:
    #                         status['Not Ready'] = status['Not Ready'] + 1
    #                     else:
    #                         status['Not Ready'] = 1

    #             if p['job_name'] is not None:
    #                 if p['job_succeeded']:
    #                     if 'Succeeded' in status:
    #                         status['Succeeded'] = status['Succeeded'] + 1
    #                     else:
    #                         status['Succeeded'] = 1
    #                 else:
    #                     if 'Not Succeeded' in status:
    #                         status['Not Succeeded'] = status['Not Succeeded'] + 1
    #                     else:
    #                         status['Not Succeeded'] = 1

    #         summary = []
    #         for s in status:
    #             summary.append(dict(status=s, count=status[s]))

    #         summary = sorted(summary, key = lambda i: i['status'])

    #     except:
    #         self.log.error('k8s_pods.get_pods_status_summary', traceback.format_exc())
    #         return None

    #     return summary

    # def get_pod_container_summary(self, pod, job_name):
    #     '''
    #         {
    #             "ready": 1,
    #             "completed": 0,
    #             "count": 1,
    #             "restarts": 0,
    #             "reasons": []
    #         }
    #     '''
    #     summary = dict()
    #     summary['ready'] = 0
    #     summary['completed'] = 0
    #     summary['count'] = 0
    #     summary['restarts'] = 0
    #     summary['reasons'] = []

    #     if pod['status']['container_statuses'] is not None:
    #         for c in pod['status']['container_statuses']:
    #             summary['count'] = summary['count'] + 1
    #             summary['restarts'] = summary['restarts'] + c['restart_count']
    #             if c['ready']:
    #                 summary['ready'] = summary['ready'] + 1
    #             else:
    #                 try:
    #                     reason = c['state']['waiting']['reason']
    #                     if reason is not None and reason not in summary['reasons']:
    #                         summary['reasons'].append(reason)
    #                 except:
    #                     pass

    #             if job_name is not None:
    #                 try:
    #                     if c['state']['terminated']['reason'] == 'Completed':
    #                         summary['completed'] = summary['completed'] + 1
    #                 except:
    #                     pass

    #     return summary

    # def get_pod_summary(self, pod):
    #     '''
    #     {
    #         "namespace": "iks",
    #         "labels": {
    #             "app.kubernetes.io/component": "controller",
    #             "app.kubernetes.io/instance": "essential-nginx-ingress",
    #             "app.kubernetes.io/name": "ingress-nginx",
    #             "controller-revision-hash": "794954b8c6",
    #             "pod-template-generation": "1"
    #         },
    #         "name": "essential-nginx-ingress-ingress-nginx-controller-2nk8m",
    #         "uid": "8b2bcc15-da82-4092-9381-71ffca698158",
    #         "age": 249258,
    #         "node": "milan-kali-worker-4078840427",
    #         "replicaset_name": null,
    #         "scheduled": true,
    #         "status": "Running",
    #         "ready": true,
    #         "pod_ip": "<ip>",
    #         "cni": {
    #             "ip": "<ip>",
    #             "ports": [
    #                 {
    #                     "container_port": 80,
    #                     "host_ip": null,
    #                     "host_port": null,
    #                     "name": "http",
    #                     "protocol": "TCP"
    #                 },
    #                 {
    #                     "container_port": 443,
    #                     "host_ip": null,
    #                     "host_port": null,
    #                     "name": "https",
    #                     "protocol": "TCP"
    #                 }
    #             ]
    #         },
    #         "job_name": null,
    #         "job_succeeded": false,
    #         "healthy": true,
    #         "containers": {
    #             "ready": 1,
    #             "completed": 0,
    #             "count": 1,
    #             "restarts": 0,
    #             "reasons": []
    #         },
    #         "node_selector": [
    #             {
    #                 "match_expressions": null,
    #                 "match_fields": [
    #                     {
    #                         "key": "metadata.name",
    #                         "operator": "In",
    #                         "values": [
    #                             "milan-kali-worker-4078840427"
    #                         ]
    #                     }
    #                 ]
    #             }
    #         ],
    #         "scheduling_problem": null
    #     }
    #     '''
    #     try:
    #         summary = dict()

    #         summary['namespace'] = pod['metadata']['namespace']
    #         summary['labels'] = pod['metadata']['labels']
    #         summary['name'] = pod['metadata']['name']
    #         summary['uid'] = pod['metadata']['uid']
    #         summary['age'] = int(time.time()) - pod['metadata']['creation_timestamp']
    #         summary['node'] = pod['spec']['node_name']
    #         summary['replicaset_name'] = self.get_pod_replicaset_name(pod)

    #         summary['scheduled'] = self.is_pod_scheduled(pod)
    #         summary['status'] = pod['status']['phase']
    #         summary['ready'] = self.is_pod_ready(pod)

    #         summary['pod_ip'] = pod['status']['pod_ip']
    #         summary['cni'] = None
    #         cni = self.get_pod_calico_ip(pod['metadata']['uid'], pod=pod)
    #         if cni is not None:
    #             summary['cni'] = dict()
    #             summary['cni']['ip'] = cni['ip']
    #             summary['cni']['ports'] = cni['ports']

    #         summary['job_name'] = self.get_pod_job(pod)
    #         summary['job_succeeded'] = False
    #         summary['healthy'] = False
    #         if summary['ready']:
    #             summary['healthy'] = True
    #         if not summary['ready'] and summary['job_name'] is not None and summary['status'] == 'Succeeded':
    #             summary['job_succeeded'] = True
    #             summary['healthy'] = True

    #         summary['containers'] = self.get_pod_container_summary(pod, summary['job_name'])

    #         try:
    #             summary['node_selector'] = pod['spec']['affinity']['node_affinity']['required_during_scheduling_ignored_during_execution']['node_selector_terms']
    #         except:
    #             summary['node_selector'] = None

    #         summary['scheduling_problem'] = None
    #         if summary['node_selector'] is not None:
    #             labels = self.get_nodes_labels()
    #             summary['scheduling_problem'] = self.get_pod_scheduling_problem(labels, summary['node_selector'])

    #     except:
    #         self.log.error('k8s_pods.get_pod_summary', traceback.format_exc())
    #         self.log.error('k8s_pods.get_pod_summary', pod)
    #         return None

    #     return summary

    # def get_pods_namespaces(self):
    #     namespaces = dict()
    #     try:
    #         for p in self.pods:
    #             namespace = p['namespace']
    #             if namespace not in namespaces:
    #                 namespaces[namespace] = dict()

    #     except:
    #         self.log.error('k8s_pods.get_pods_namespaces', traceback.format_exc())

    #     return namespaces

    # def get_pods_in_namespace(self, namespace):
    #     pods = []
    #     try:
    #         for p in self.pods:
    #             if p['namespace'] == namespace:
    #                 pods.append(p)

    #     except:
    #         self.log.error('k8s_pods.get_pods_in_namespace', traceback.format_exc())

    #     return pods

    # def get_pod_nodes(self, pods=None):
    #     nodes = []
    #     try:
    #         for p in self.pods:
    #             if p['node'] not in nodes:
    #                 nodes.append(p['node'])

    #     except:
    #         self.log.error('k8s_pods.get_pod_nodes', traceback.format_exc())

    #     return nodes

    # def get_pod_id(self, namespace, name, cache=True):
    #     try:
    #         for p in self.pods:
    #             if p['metadata']['name'] == name and p['metadata']['namespace'] == namespace:
    #                 return p['metadata']['uid']
    #     except:
    #         self.log.error('k8s_pods.get_pod_id', traceback.format_exc())
    #     return None

    # def get_pod(self, pod_id, cache=True, nice=True, events=False):
    #     try:
    #         for p in self.pods:
    #             if p['metadata']['uid'] == pod_id:
    #                 if not nice:
    #                     return p

    #                 info = dict()
    #                 info['pod'] = p
    #                 info['summary'] = self.get_pod_summary(p)
    #                 info['timestamp'] = self.get_pods_cache_timestamp()
    #                 info['age'] = int(time.time()*1000) - info['timestamp']

    #                 if events:
    #                     field_selector = 'involvedObject.uid=%s' % (
    #                         info['summary']['uid']
    #                     )
    #                     info['events'] = self.get_namespace_events(
    #                         info['summary']['namespace'],
    #                         field_selector = field_selector
    #                     )

    #                 return info

    #     except:
    #         self.log.error('k8s_pods.get_pod', traceback.format_exc())

    #     return None

    # def get_pods_state(self, summary_only=False):
    #     try:
    #         pods = self.get_pods_summary()
    #         if pods is None:
    #             return None

    #         state = dict()
    #         state['summary'] = dict()
    #         state['summary']['count'] = pods['count']
    #         state['summary']['ready'] = pods['ready']
    #         state['summary']['job_succeeded'] = pods['job_succeeded']
    #         state['summary']['healthy'] = pods['healthy']
    #         state['summary']['scheduled'] = pods['scheduled']
    #         state['summary']['functional'] = False
    #         if state['summary']['count'] > 0:
    #             if state['summary']['count'] == state['summary']['healthy']:
    #                 if state['summary']['count'] == state['summary']['scheduled']:
    #                     state['summary']['functional'] = True

    #         state['summary']['status'] = pods['status']

    #         if summary_only:
    #             return state['summary']

    #         state['pods'] = pods['pods']

    #         state['namespaces'] = self.get_pods_namespaces()
    #         for n in state['namespaces']:
    #             npods = self.get_pods_in_namespace(n)
    #             state['namespaces'][n]['pods'] = npods
    #             state['namespaces'][n]['summary'] = dict()
    #             state['namespaces'][n]['summary']['count'] = len(npods)
    #             state['namespaces'][n]['summary']['status'] = self.get_pods_status_summary(npods)
    #             state['namespaces'][n]['summary']['scheduled'] = self.are_pods_scheduled(npods)
    #             state['namespaces'][n]['nodes'] = self.get_pod_nodes(pods=npods)

    #     except:
    #         self.log.error('k8s_pods.get_pods_state', traceback.format_exc())
    #         return None

    #     return state

    # def get_pods_calico_ip(self, cache=True):
    #     try:
    #         pods = self.get_pods(cache=cache)
    #         if pods is None:
    #             return None

    #         ip = []
    #         for p in pods:
    #             try:
    #                 i = dict()
    #                 i['pod'] = p['metadata']['name']
    #                 i['pod_id'] = p['metadata']['uid']
    #                 i['node'] = p['spec']['node_name']
    #                 i['ip'] = p['metadata']['annotations']['cni.projectcalico.org/podIP'].split('/')[0]
    #                 i['ports'] = []
    #                 for c in p['spec']['containers']:
    #                     if c['ports'] is not None:
    #                         i['ports'] = i['ports'] + c['ports']

    #                 ip.append(i)

    #             except:
    #                 pass

    #     except:
    #         self.log.error('k8s_pods.get_pods_calico_ip', traceback.format_exc())
    #         return None

    #     return ip

    # def get_pod_calico_ip(self, pod_id, pod=None, cache=True):
    #     try:
    #         if pod is None:
    #             pods = self.get_pods(cache=cache)
    #             if pods is None:
    #                 return None

    #             for p in pods:
    #                 if p['metadata']['uid'] == pod_id:
    #                     pod = p

    #         if pod is None:
    #             self.log.error('k8s_pods.get_pod_calico_ip', 'POD not found: %s' % (pod_id))
    #             return None

    #         cni = dict()
    #         cni['pod'] = pod['metadata']['name']
    #         cni['pod_id'] = pod['metadata']['uid']
    #         cni['node'] = pod['spec']['node_name']
    #         try:
    #             cni['ip'] = pod['metadata']['annotations']['cni.projectcalico.org/podIP'].split('/')[0]
    #         except:
    #             return None

    #         cni['ports'] = []
    #         for c in pod['spec']['containers']:
    #             if c['ports'] is not None:
    #                 cni['ports'] = cni['ports'] + c['ports']

    #     except:
    #         self.log.error('k8s_pods.get_pod_calico_ip', traceback.format_exc())
    #         return None

    #     return cni

    # def get_pods_summary(self, namespaces=None):
    #     try:
    #         my_pods = []
    #         for p in self.pods:
    #             pod = self.get_pod_summary(p)
    #             if pod is not None:
    #                 if namespaces is None or pod['namespace'] in namespaces:
    #                     my_pods.append(pod)

    #         summary = dict()
    #         summary['count'] = len(my_pods)
    #         summary['scheduled'] = 0
    #         summary['ready'] = 0
    #         summary['job_succeeded'] = 0
    #         summary['healthy'] = 0
    #         summary['status'] = self.get_pods_status_summary(my_pods)

    #         for pod in my_pods:
    #             if pod['ready']:
    #                 summary['ready'] = summary['ready'] + 1
    #             if pod['job_name'] is not None and pod['job_succeeded']:
    #                 summary['job_succeeded'] = summary['job_succeeded'] + 1
    #             if pod['scheduled']:
    #                 summary['scheduled'] = summary['scheduled'] + 1
    #             if pod['healthy']:
    #                 summary['healthy'] = summary['healthy'] + 1

    #         summary['functional'] = False
    #         if summary['count'] > 0 and summary['count'] == summary['healthy']:
    #             summary['functional'] = True

    #     except:
    #         self.log.error('k8s_pods.get_pods_summary', traceback.format_exc())
    #         return None

    #     return summary

    # def get_pods_health_summary(self, namespaces=None):
    #     try:
    #         my_pods = []
    #         for p in self.pods:
    #             pod = self.get_pod_summary(p)
    #             if pod is not None:
    #                 if namespaces is None or pod['namespace'] in namespaces:
    #                     my_pods.append(pod)

    #         return self.get_selected_pods_health_summary(my_pods)
    #     except:
    #         self.log.error('k8s_pods.get_pods_summary', traceback.format_exc())
    #         return None

    # def get_selected_pods_health_summary(self, my_pods, no_pods_unhealthy = True):
    #     '''
    #         {
    #             "pods_count": 63,
    #             "pods_scheduled": 63,
    #             "pods_ready": 46,
    #             "pods_job_succeeded": 13,
    #             "pods_all_good": 59,
    #             "pods_healthy": false,
    #             "pods_status": [
    #                 {
    #                     "status": "Not Ready",
    #                     "count": 4
    #                 },
    #                 {
    #                     "status": "Ready",
    #                     "count": 46
    #                 },
    #                 {
    #                     "status": "Succeeded",
    #                     "count": 13
    #                 }
    #             ]
    #         }
    #     '''
    #     try:
    #         summary = dict()
    #         summary['pods_count'] = len(my_pods)
    #         summary['pods_scheduled'] = 0
    #         summary['pods_ready'] = 0
    #         summary['pods_job_succeeded'] = 0
    #         summary['pods_all_good'] = 0
    #         summary['pods_status'] = self.get_pods_status_summary(my_pods)

    #         for pod in my_pods:
    #             if pod['ready']:
    #                 summary['pods_ready'] = summary['pods_ready'] + 1
    #             if pod['job_name'] is not None and pod['job_succeeded']:
    #                 summary['pods_job_succeeded'] = summary['pods_job_succeeded'] + 1
    #             if pod['scheduled']:
    #                 summary['pods_scheduled'] = summary['pods_scheduled'] + 1
    #             if pod['healthy']:
    #                 summary['pods_all_good'] = summary['pods_all_good'] + 1

    #         summary['pods_healthy'] = True
    #         if summary['pods_count'] == 0 and no_pods_unhealthy:
    #             summary['pods_healthy'] = False
    #         if summary['pods_all_good'] < summary['pods_count']:
    #             summary['pods_healthy'] = False

    #         summary['pods_state_summary'] = '%s/%s' % (
    #             summary['pods_count'],
    #             summary['pods_all_good']
    #         )

    #     except:
    #         self.log.error('k8s_pods.get_pods_summary', traceback.format_exc())
    #         return None

    #     return summary

    # def get_pod_logs(self, name, namespace):
    #     # https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/CoreV1Api.md#list_secret_for_all_namespaces
    #     try:
    #         start_time = int(time.time()*1000)
    #         response = self.api.read_namespaced_pod_log(name=name, namespace=namespace)
    #         self.api_statistics(
    #             'read_namespaced_pod_log:%s:%s' % (namespace, name),
    #             int(time.time()*1000) - start_time
    #         )

    #     except:
    #         self.log.error('k8s_pods.get_pod_logs', traceback.format_exc())
    #         return None

    #     return response
