from lib import filter_helper
from lib import ip_helper


class K8sNodeInfo():
    def __init__(self):
        self.node = None

    def get_node_info(self, node_mo):
        if node_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        info['name'] = self.get(node_mo, 'metadata:name')
        info['node_info'] = self.get(node_mo, 'status:node_info')

        conditions = self.get(node_mo, 'status:conditions', on_error=[], on_none=[])

        info['ready'] = False
        for condition in conditions:
            if condition['type'] == 'Ready':
                if condition['status'] == 'True':
                    info['ready'] = True

        if info['ready']:
            info['readyTick'] = '\u2713'
            info['__Output']['readyTick'] = 'Green'
        else:
            info['readyTick'] = '\u2717'
            info['__Output']['readyTick'] = 'Red'

        info['memory_pressure'] = False
        for condition in conditions:
            if condition['type'] == 'MemoryPressure':
                if condition['status'] == 'True':
                    info['memory_pressure'] = True

        if info['memory_pressure']:
            info['memoryTick'] = '\u2717'
            info['__Output']['memoryTick'] = 'Red'
        else:
            info['memoryTick'] = '\u2713'
            info['__Output']['memoryTick'] = 'Green'

        info['disk_pressure'] = False
        for condition in conditions:
            if condition['type'] == 'MemoryPressure':
                if condition['status'] == 'True':
                    info['disk_pressure'] = True

        if info['disk_pressure']:
            info['diskTick'] = '\u2717'
            info['__Output']['diskTick'] = 'Red'
        else:
            info['diskTick'] = '\u2713'
            info['__Output']['diskTick'] = 'Green'

        info['pid_pressure'] = False
        for condition in conditions:
            if condition['type'] == 'PIDPressure':
                if condition['status'] == 'True':
                    info['pid_pressure'] = True

        if info['pid_pressure']:
            info['pidTick'] = '\u2717'
            info['__Output']['pidTick'] = 'Red'
        else:
            info['pidTick'] = '\u2713'
            info['__Output']['pidTick'] = 'Green'

        info['label'] = self.get(node_mo, 'metadata:labels', on_error={}, on_none={})

        info['role'] = []
        info['master'] = False
        for label in info['label']:
            if label == 'node-role.kubernetes.io/master':
                info['master'] = True
                info['role'].append('Master')

        info['worker'] = False
        for label in info['label']:
            if label == 'node-role.kubernetes.io/worker':
                info['worker'] = True
                info['role'].append('Worker')

        info['cnv'] = False
        info['cnvTick'] = '\u2717'
        info['__Output']['cnvTick'] = 'Red'
        for label in info['label']:
            if label == 'kubevirt.io/schedulable' and info['label'][label] == 'true':
                info['cnv'] = True
                info['cnvTick'] = '\u2713'
                info['__Output']['cnvTick'] = 'Green'

        annotations_mo = self.get(node_mo, 'metadata:annotations', on_error={}, on_none={})
        info['mcp_current_config'] = None
        info['mcp_desired_config'] = None
        info['mcpTick'] = '--'
        if 'machineconfiguration.openshift.io/currentConfig' in annotations_mo:
            info['mcp_current_config'] = annotations_mo['machineconfiguration.openshift.io/currentConfig']
        if 'machineconfiguration.openshift.io/desiredConfig' in annotations_mo:
            info['mcp_desired_config'] = annotations_mo['machineconfiguration.openshift.io/desiredConfig']
        if info['mcp_current_config'] is not None and info['mcp_desired_config'] is not None:
            if info['mcp_current_config'] == info['mcp_desired_config']:
                info['mcpTick'] = '\u2713'
                info['__Output']['mcpTick'] = 'Green'
            else:
                info['mcpTick'] = '\u2717'
                info['__Output']['mcpTick'] = 'Red'

        info['capacity'] = self.get(node_mo, 'status:capacity', on_error={}, on_none={})
        info['capacityT'] = []
        for key in info['capacity']:
            info['capacityT'].append(
                '%s:%s' % (
                    key,
                    info['capacity'][key]
                )
            )

        info['capacity_cpu'] = self.get(node_mo, 'status:capacity:cpu')
        info['capacity_pod'] = self.get(node_mo, 'status:capacity:pods')
        info['capacity_memory'] = self.get(node_mo, 'status:capacity:memory')
        info['capacity_storage'] = self.get(node_mo, 'status:capacity:ephemeral-storage')
        info['capacity_hp2m'] = self.get(node_mo, 'status:capacity:hugepages-2Mi')
        info['capacity_hp1g'] = self.get(node_mo, 'status:capacity:hugepages-1Gi')
        info['capacity_kubevirt'] = []
        info['capacity_vendor'] = []

        for key in info['capacity']:
            if key not in ['cpu', 'pods', 'memory', 'ephemeral-storage', 'hugepages-2Mi', 'hugepages-1Gi']:
                if key.startswith('devices.kubevirt.io'):
                    info['capacity_kubevirt'].append(
                        '%s: %s' % (
                            key,
                            info['capacity'][key]
                        )
                    )
                else:
                    info['capacity_vendor'].append(
                        '%s: %s' % (
                            key,
                            info['capacity'][key]
                        )
                    )

        info['capacity_vendor'] = sorted(info['capacity_vendor'])
        info['capacity_kubevirt'] = sorted(info['capacity_kubevirt'])

        info['internal_ip'] = None
        info['external_ip'] = None
        info['ip'] = []
        info['ipT'] = []

        addresses = self.get(node_mo, 'status:addresses', on_error=[], on_none=[])
        for address in addresses:
            if address['type'] == 'InternalIP':
                info['internal_ip'] = address['address']
                info['ip'].append(
                    address['address']
                )
                info['ipT'].append(
                    '%s (int)' % (
                        address['address']
                    )
                )

            if address['type'] == 'ExternalIP':
                info['external_ip'] = address['address']
                info['ip'].append(
                    address['address']
                )
                info['ipT'].append(
                    '%s (int)' % (
                        address['address']
                    )
                )

        info['ssh_ip'] = info['external_ip']
        if info['external_ip'] is None:
            info['ssh_ip'] = info['internal_ip']

        info['age'] = self.convert_timestamp_to_age(
            self.get(node_mo, 'metadata:creation_timestamp'),
            on_error='--'
        )

        return info

    def get_nodes_info(self, cache_enabled=True):
        if cache_enabled:
            if self.node is not None:
                return self.node

        managed_objects = self.get_node_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.node = []
        for managed_object in managed_objects:
            node_info = {}
            node_info['info'] = self.get_node_info(
                managed_object
            )
            node_info['mo'] = managed_object
            self.node.append(
                node_info
            )

        return self.node

    def filter_node_label(self, labels, label_filter):
        new_labels = {}

        if len(label_filter.split(':')) > 2:
            return new_labels

        if len(label_filter.split(':')) == 1:
            label_filter_key = label_filter
            label_filter_value = None

        if len(label_filter.split(':')) == 2:
            (label_filter_key, label_filter_value) = label_filter.split(':')

        for lkey in labels:
            if filter_helper.match_string(label_filter_key, lkey):
                if label_filter_value is None:
                    new_labels[lkey] = labels[lkey]
                    continue

                if filter_helper.match_string(label_filter_value, labels[lkey]):
                    new_labels[lkey] = labels[lkey]
                    continue

        return new_labels

    def get_node_filter_value(self, node_filter, filter_key):
        if node_filter is not None:
            for ap_rule in node_filter:
                key = ap_rule.split(':')[0]
                value = ':'.join(ap_rule.split(':')[1:])

                if key == filter_key:
                    return value

        return None

    def match_node(self, node_info, node_filter):
        if node_filter is None or len(node_filter) == 0:
            return True

        for ap_rule in node_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, node_info['name']):
                    return False

            if key == 'ip':
                key_found = True
                found = False
                for address in node_info['ip']:
                    if address == value:
                        found = True
                        break

                if not found:
                    return False

            if key == 'worker':
                key_found = True
                if value == 'true' and not node_info['worker']:
                    return False
                if value == 'false' and node_info['worker']:
                    return False

            if key == 'master':
                key_found = True
                if value == 'true' and not node_info['master']:
                    return False
                if value == 'false' and node_info['master']:
                    return False

            if key == 'label':
                key_found = True
                filtered_labels = self.filter_node_label(
                    node_info['label'],
                    value
                )
                if len(filtered_labels) == 0:
                    return False

            if not key_found:
                self.log.error(
                    'match_node',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_nodes(self, object_filter=None, sriov_phy_info=False, sriov_policy_info=False, sriov_network_info=False, sriov_vf_info=False, return_mo=False, cache_enabled=True):
        all_nodes = self.get_nodes_info(cache_enabled=cache_enabled)
        if all_nodes is None:
            return None

        nodes = []

        for node_info in all_nodes:
            if not self.match_node(node_info['info'], object_filter):
                continue

            if return_mo:
                nodes.append(
                    node_info['mo']
                )
                continue

            label_filter = self.get_node_filter_value(object_filter, 'label')
            if label_filter is not None:
                node_info['info']['label'] = self.filter_node_label(
                    node_info['info']['label'],
                    label_filter
                )

            if sriov_policy_info:
                node_info['info']['sriov_policy'] = self.get_ocp_node_sriov_policy(
                    node_info['info']['name']
                )

            nodes.append(
                node_info['info']
            )

        if not return_mo:
            nodes = sorted(
                nodes,
                key=lambda i: i['name']
            )

        return nodes

    def get_node(self, node_name):
        node_filter = ['name:%s' % (node_name)]
        nodes = self.get_nodes(
            object_filter=node_filter
        )

        if nodes is None or len(nodes) != 1:
            return None

        return nodes[0]

    def get_node_name(self, ip_address):
        node_info = self.get_node_with_ip(ip_address)
        if node_info is None:
            return None
        return node_info['name']

    def get_node_with_ip(self, ip_address):
        node_filter = ['ip:%s' % (ip_address)]
        nodes = self.get_nodes(
            object_filter=node_filter
        )

        if nodes is None or len(nodes) != 1:
            return None

        return nodes[0]

    def get_node_internal_ip(self, node_name, address_type='ipv4'):
        node_info = self.get_node(node_name)
        if node_info is None:
            return None

        if len(node_info['internal_ip']) == 0:
            return None

        for internal_ip in node_info['internal_ip']:
            if address_type == 'ipv4':
                if ip_helper.is_valid_ipv4_address(internal_ip):
                    return internal_ip
            if address_type == 'ipv6':
                if ip_helper.is_valid_ipv6_address(internal_ip):
                    return internal_ip

        return None

    def get_node_external_ip(self, node_name, address_type='ipv4'):
        node_info = self.get_node(node_name)
        if node_info is None:
            return None

        if len(node_info['external_ip']) == 0:
            return None

        for external_ip in node_info['external_ip']:
            if address_type == 'ipv4':
                if ip_helper.is_valid_ipv4_address(external_ip):
                    return external_ip
            if address_type == 'ipv6':
                if ip_helper.is_valid_ipv6_address(external_ip):
                    return external_ip

        return None

    def get_node_ip(self, node_name, address_type='ipv4'):
        node_info = self.get_node(node_name)
        if node_info is None:
            return None

        if len(node_info['ip']) == 0:
            return None

        for ip_address in node_info['ip']:
            if address_type == 'ipv4':
                if ip_helper.is_valid_ipv4_address(ip_address):
                    return ip_address
            if address_type == 'ipv6':
                if ip_helper.is_valid_ipv6_address(ip_address):
                    return ip_address

        return None

    def get_master_nodes(self):
        node_filter = ['master:true']
        return self.get_nodes(object_filter=node_filter)

    def get_worker_nodes(self):
        node_filter = ['worker:true']
        return self.get_nodes(object_filter=node_filter)

    def get_worker_nodes_name(self):
        names = []
        for node_info in self.get_worker_nodes():
            names.append(
                node_info['name']
            )
        return names

    def get_worker_nodes_ip(self, ready=True):
        node_ips = []
        for node_info in self.get_worker_nodes():
            if ready and not node_info['ready']:
                continue
            node_ips = node_ips + node_info['ip']

        return node_ips

    def get_any_worker_node_ip(self):
        node_ips = self.get_worker_nodes_ip()
        if len(node_ips) == 0:
            return None
        return node_ips[0]

    def get_master_nodes_name(self):
        names = []
        for node_info in self.get_master_nodes():
            names.append(
                node_info['name']
            )
        return names

    # def get_node_pods(self, node_name):
    #     try:
    #         node_pods = []
    #         for pod in self.pods:
    #             if pod['node'] == node_name:
    #                 node_pods.append(pod)

    #     except BaseException:
    #         self.log.error('k8s_nodes.get_node_pods', traceback.format_exc())
    #         return None

    #     return node_pods

    # def get_node_pods_ip(self, node_name):
    #     try:
    #         ips = {}
    #         for pod in self.pods:
    #             try:
    #                 pod_ip = pod['status']['pod_ip']
    #                 ips[pod_ip] = {}
    #                 ips[pod_ip]['uid'] = pod['metadata']['uid']
    #                 ips[pod_ip]['name'] = pod['metadata']['name']
    #             except BaseException:
    #                 pass

    #     except BaseException:
    #         self.log.error('k8s_nodes.get_node_pods_ip', traceback.format_exc())
    #         return None

    #     return ips

    # def get_node_status(self, node_mo):
    #     status = []
    #     for condition in node_mo['status']['conditions']:
    #         if condition['status'] == 'True':
    #             status.append(
    #                 condition['type']
    #             )
    #     return ','.join(status)

    # def get_node_ready_status(self, node_mo):
    #     for condition in node_mo['status']['conditions']:
    #         if condition['type'] == 'Ready':
    #             if condition['status'] == 'True':
    #                 return 'Ready'
    #     return 'NotReady'

    # def is_node_ready(self, node_mo):
    #     for condition in node_mo['status']['conditions']:
    #         if condition['type'] == 'Ready':
    #             if condition['status'] == 'True':
    #                 return True
    #     return False

    # def is_node_memory_pressure(self, node):
    #     for condition in node['status']['conditions']:
    #         if condition['type'] == 'MemoryPressure':
    #             if condition['status'] == 'True':
    #                 return True
    #     return False

    # def is_node_disk_pressure(self, node):
    #     for condition in node['status']['conditions']:
    #         if condition['type'] == 'DiskPressure':
    #             if condition['status'] == 'True':
    #                 return True
    #     return False

    # def is_node_pid_pressure(self, node):
    #     for condition in node['status']['conditions']:
    #         if condition['type'] == 'PIDPressure':
    #             if condition['status'] == 'True':
    #                 return True
    #     return False

    # def get_nodes_ready_count(self):
    #     count = 0
    #     for node in self.nodes:
    #         if self.is_node_ready(node):
    #             count = count + 1
    #     return count

    # def get_nodes_status_summary(self):
    #     status = {}
    #     status['Ready'] = 0
    #     status['Memory Pressure'] = 0
    #     status['Disk Pressure'] = 0
    #     status['PID Pressure'] = 0

    #     for node in self.nodes:
    #         if self.is_node_ready(node):
    #             status['Ready'] = status['Ready'] + 1
    #         if self.is_node_memory_pressure(node):
    #             status['Memory Pressure'] = status['Memory Pressure'] + 1
    #         if self.is_node_disk_pressure(node):
    #             status['Disk Pressure'] = status['Disk Pressure'] + 1
    #         if self.is_node_pid_pressure(node):
    #             status['PID Pressure'] = status['PID Pressure'] + 1

    #     summary = []
    #     for field in status:
    #         summary.append(dict(status=field, count=status[field]))

    #     return summary

    # def get_node_name(self, node_mo):
    #     return node_mo['metadata']['name']

    # def get_node_ip(self, node_mo, address_type):
    #     addresses = node_mo['status']['addresses']
    #     if addresses is not None:
    #         for address in addresses:
    #             if address['type'] == address_type:
    #                 return address['address']
    #     return None

    # def get_node_machine_id(self, node):
    #     try:
    #         return node['status']['node_info']['machine_id']
    #     except BaseException:
    #         self.log.error('k8s_nodes.get_node_machine_id', traceback.format_exc())
    #     return None

    # def get_node_roles(self, node):
    #     roles = []
    #     for label in node['metadata']['labels']:
    #         if label == 'node-role.kubernetes.io/master':
    #             roles.append('Master')
    #         if label == 'node-role.kubernetes.io/worker':
    #             roles.append('Worker')

    #     return ','.join(roles)

    # def get_node_vm_name(self, node_mo):
    #     for annotation in node_mo['metadata']['annotations']:
    #         if annotation == 'csi.volume.kubernetes.io/nodeid':
    #             for csi in node_mo['metadata']['annotations'][annotation]:
    #                 if csi == 'csi.vsphere.vmware.com':
    #                     return node_mo['metadata']['annotations'][annotation][csi]
    #     return None

    # def is_node_vm(self, node_mo):
    #     if self.get_node_vm_name(node_mo) is None:
    #         return False
    #     return True

    # def is_node_bm(self, node):
    #     return False

    # def is_node(self, node_name):
    #     if self.get_node_mo(node_name) is None:
    #         return False
    #     return True

    # def get_worker_nodes_name(self):
    #     if not self.get_nodes():
    #         return None

    #     names = []
    #     for node_mo in self.nodes:
    #         if self.is_node_worker(node_mo):
    #             names.append(
    #                 node_mo['metadata']['name']
    #             )

    #     return names

    # def get_nodes_name(self):
    #     if not self.get_nodes():
    #         return None

    #     names = []
    #     for node_mo in self.nodes:
    #         names.append(
    #             node_mo['metadata']['name']
    #         )

    #     return names

    # def get_node_info(self, node_mo):
    #     info = {}
    #     info['__Output'] = {}

    #     info['uid'] = node_mo['metadata']['uid']
    #     info['name'] = node_mo['metadata']['name']
    #     info['namespace'] = node_mo['metadata']['namespace']
    #     info['age'] = self.convert_age(
    #         int(time.time()) - node_mo['metadata']['creation_timestamp']
    #     )
    #     info['node_info'] = node_mo['status']['node_info']
    #     info['internal_ip'] = self.get_node_ip(node_mo, 'InternalIP')
    #     info['external_ip'] = self.get_node_ip(node_mo, 'ExternalIP')
    #     info['labels'] = node_mo['metadata']['labels']
    #     info['roles'] = self.get_node_roles(node_mo)
    #     info['master'] = self.is_node_master(node_mo)
    #     info['worker'] = self.is_node_worker(node_mo)
    #     info['ready'] = self.get_node_ready_status(node_mo)
    #     if info['ready'] == 'Ready':
    #         info['__Output']['ready'] = 'Green'
    #     else:
    #         info['__Output']['ready'] = 'Red'

    #     info['conditions'] = {}
    #     info['conditions']['Memory Pressure'] = self.is_node_memory_pressure(node_mo)
    #     info['conditions']['Disk Pressure'] = self.is_node_disk_pressure(node_mo)
    #     info['conditions']['PID Pressure'] = self.is_node_pid_pressure(node_mo)

    #     info['is_vm'] = self.is_node_vm(node_mo)
    #     info['is_bm'] = self.is_node_bm(node_mo)
    #     info['type'] = ''
    #     if info['is_vm']:
    #         info['type'] = 'VM'
    #     if info['is_bm']:
    #         info['type'] = 'BM'

    #     return info

    # def get_nodes_info(self):
    #     if not self.get_nodes():
    #         return None

    #     info = []
    #     for node_mo in self.nodes:
    #         node_info = self.get_node_info(node_mo)
    #         if node_info is not None:
    #             info.append(node_info)

    #     info = sorted(
    #         info,
    #         key=lambda i: i['name']
    #     )

    #     return info

    # def get_nodes_state(self, summary_only=False):
    #     try:
    #         state = {}
    #         state['summary'] = {}
    #         state['summary']['count'] = len(self.nodes)
    #         state['summary']['ready'] = self.get_nodes_ready_count()
    #         state['summary']['functional'] = False
    #         if state['summary']['count'] > 0 and state['summary']['count'] == state['summary']['ready']:
    #             state['summary']['functional'] = True
    #         state['summary']['status'] = self.get_nodes_status_summary()

    #         if summary_only:
    #             return state['summary']

    #         state['nodes'] = self.get_nodes_info()

    #     except BaseException:
    #         self.log.error('k8s_nodes.get_nodes_state', traceback.format_exc())
    #         return None

    #     return state

    # def get_nodes_health_summary(self):
    #     '''
    #         {
    #             "nodes_count": 5,
    #             "nodes_ready": 5,
    #             "nodes_healthy": true,
    #             "nodes_status": [
    #                 {
    #                     "status": "Ready",
    #                     "count": 5
    #                 },
    #                 {
    #                     "status": "Memory Pressure",
    #                     "count": 0
    #                 },
    #                 {
    #                     "status": "Disk Pressure",
    #                     "count": 0
    #                 },
    #                 {
    #                     "status": "PID Pressure",
    #                     "count": 0
    #                 }
    #             ]
    #         }
    #     '''
    #     summary = {}
    #     summary['nodes_count'] = len(self.nodes)
    #     summary['nodes_ready'] = self.get_nodes_ready_count()
    #     summary['nodes_healthy'] = False
    #     if summary['nodes_count'] > 0 and summary['nodes_count'] == summary['nodes_ready']:
    #         summary['nodes_healthy'] = True
    #         summary['nodes_status'] = self.get_nodes_status_summary()
    #     return summary

    # def get_nodes_labels(self):
    #     try:
    #         labels = []
    #         for node in self.nodes:
    #             try:
    #                 node_labels = node['metadata']['labels']
    #                 if node_labels is not None:
    #                     for key in node_labels:
    #                         labels.append(
    #                             dict(
    #                                 key=key,
    #                                 value=node_labels[key]
    #                             )
    #                         )

    #             except BaseException:
    #                 self.log.error('k8s_nodes.get_nodes_labels', traceback.format_exc())

    #     except BaseException:
    #         self.log.error('k8s_nodes.get_nodes_labels', traceback.format_exc())
    #         return None

    #     return labels

    # def get_node_mo(self, node_name, cache=True):
    #     if not self.get_nodes(cache=cache):
    #         return False

    #     for node in self.nodes:
    #         if node['metadata']['name'] == node_name:
    #             return node

    #     return None

    # def get_node(self, name):
    #     try:
    #         for node_mo in self.nodes:
    #             if node_mo['metadata']['name'] == name:
    #                 info = {}
    #                 info['node'] = node_mo
    #                 info['summary'] = self.get_node_info(node_mo)
    #                 info['pods'] = self.get_node_pods(name)
    #                 info['age'] = int(time.time() * 1000) - info['timestamp']
    #                 return info

    #     except BaseException:
    #         self.log.error(
    #             'k8s_nodes.get_node',
    #             traceback.format_exc()
    #         )

    #     return None
