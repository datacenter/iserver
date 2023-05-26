import time
import traceback


class K8sNodeInfo():
    def __init__(self):
        pass

    def get_node_pods(self, node_name):
        try:
            node_pods = []
            for pod in self.pods:
                if pod['node'] == node_name:
                    node_pods.append(pod)

        except BaseException:
            self.log.error('k8s_nodes.get_node_pods', traceback.format_exc())
            return None

        return node_pods

    def get_node_pods_ip(self, node_name):
        try:
            ips = {}
            for pod in self.pods:
                try:
                    pod_ip = pod['status']['pod_ip']
                    ips[pod_ip] = {}
                    ips[pod_ip]['uid'] = pod['metadata']['uid']
                    ips[pod_ip]['name'] = pod['metadata']['name']
                except BaseException:
                    pass

        except BaseException:
            self.log.error('k8s_nodes.get_node_pods_ip', traceback.format_exc())
            return None

        return ips

    def get_node_status(self, node_mo):
        status = []
        for condition in node_mo['status']['conditions']:
            if condition['status'] == 'True':
                status.append(
                    condition['type']
                )
        return ','.join(status)

    def get_node_ready_status(self, node_mo):
        for condition in node_mo['status']['conditions']:
            if condition['type'] == 'Ready':
                if condition['status'] == 'True':
                    return 'Ready'
        return 'NotReady'

    def is_node_ready(self, node_mo):
        for condition in node_mo['status']['conditions']:
            if condition['type'] == 'Ready':
                if condition['status'] == 'True':
                    return True
        return False

    def is_node_memory_pressure(self, node):
        for condition in node['status']['conditions']:
            if condition['type'] == 'MemoryPressure':
                if condition['status'] == 'True':
                    return True
        return False

    def is_node_disk_pressure(self, node):
        for condition in node['status']['conditions']:
            if condition['type'] == 'DiskPressure':
                if condition['status'] == 'True':
                    return True
        return False

    def is_node_pid_pressure(self, node):
        for condition in node['status']['conditions']:
            if condition['type'] == 'PIDPressure':
                if condition['status'] == 'True':
                    return True
        return False

    def get_nodes_ready_count(self):
        count = 0
        for node in self.nodes:
            if self.is_node_ready(node):
                count = count + 1
        return count

    def get_nodes_status_summary(self):
        status = {}
        status['Ready'] = 0
        status['Memory Pressure'] = 0
        status['Disk Pressure'] = 0
        status['PID Pressure'] = 0

        for node in self.nodes:
            if self.is_node_ready(node):
                status['Ready'] = status['Ready'] + 1
            if self.is_node_memory_pressure(node):
                status['Memory Pressure'] = status['Memory Pressure'] + 1
            if self.is_node_disk_pressure(node):
                status['Disk Pressure'] = status['Disk Pressure'] + 1
            if self.is_node_pid_pressure(node):
                status['PID Pressure'] = status['PID Pressure'] + 1

        summary = []
        for field in status:
            summary.append(dict(status=field, count=status[field]))

        return summary

    def get_node_name(self, node_mo):
        return node_mo['metadata']['name']

    def get_node_ip(self, node, address_type):
        addresses = node['status']['addresses']
        if addresses is not None:
            for address in addresses:
                if address['type'] == address_type:
                    return address['address']
        return None

    def get_node_machine_id(self, node):
        try:
            return node['status']['node_info']['machine_id']
        except BaseException:
            self.log.error('k8s_nodes.get_node_machine_id', traceback.format_exc())
        return None

    def get_node_roles(self, node):
        roles = []
        for label in node['metadata']['labels']:
            if label == 'node-role.kubernetes.io/master':
                roles.append('Master')
            if label == 'node-role.kubernetes.io/worker':
                roles.append('Worker')

        return ','.join(roles)

    def is_node_master(self, node):
        for label in node['metadata']['labels']:
            if label == 'node-role.kubernetes.io/master':
                return True
        return False

    def is_node_worker(self, node_mo):
        for label in node_mo['metadata']['labels']:
            if label == 'node-role.kubernetes.io/worker':
                return True
        return False

    def get_node_vm_name(self, node_mo):
        for annotation in node_mo['metadata']['annotations']:
            if annotation == 'csi.volume.kubernetes.io/nodeid':
                for csi in node_mo['metadata']['annotations'][annotation]:
                    if csi == 'csi.vsphere.vmware.com':
                        return node_mo['metadata']['annotations'][annotation][csi]
        return None

    def is_node_vm(self, node_mo):
        if self.get_node_vm_name(node_mo) is None:
            return False
        return True

    def is_node_bm(self, node):
        return False

    def is_node(self, node_name):
        if self.get_node_mo(node_name) is None:
            return False
        return True

    def get_worker_nodes_ip(self, ready=True):
        if not self.get_nodes():
            return None

        node_ips = []
        for node_mo in self.nodes:
            if self.is_node_worker(node_mo):
                if ready:
                    if self.get_node_ready_status(node_mo) != 'Ready':
                        continue
                node_ip = self.get_node_ip(node_mo, 'ExternalIP')
                if node_ip is not None:
                    node_ips.append(
                        node_ip
                    )
                    continue

                node_ip = self.get_node_ip(node_mo, 'InternalIP')
                if node_ip is not None:
                    node_ips.append(
                        node_ip
                    )
                    continue

        return node_ips

    def get_worker_nodes_name(self):
        if not self.get_nodes():
            return None

        names = []
        for node_mo in self.nodes:
            if self.is_node_worker(node_mo):
                names.append(
                    node_mo['metadata']['name']
                )

        return names

    def get_nodes_name(self):
        if not self.get_nodes():
            return None

        names = []
        for node_mo in self.nodes:
            names.append(
                node_mo['metadata']['name']
            )

        return names

    def get_node_info(self, node_mo):
        info = {}
        info['__Output'] = {}

        info['uid'] = node_mo['metadata']['uid']
        info['name'] = node_mo['metadata']['name']
        info['namespace'] = node_mo['metadata']['namespace']
        info['age'] = self.convert_age(
            int(time.time()) - node_mo['metadata']['creation_timestamp']
        )
        info['node_info'] = node_mo['status']['node_info']
        info['internal_ip'] = self.get_node_ip(node_mo, 'InternalIP')
        info['external_ip'] = self.get_node_ip(node_mo, 'ExternalIP')
        info['labels'] = node_mo['metadata']['labels']
        info['roles'] = self.get_node_roles(node_mo)
        info['master'] = self.is_node_master(node_mo)
        info['worker'] = self.is_node_worker(node_mo)
        info['ready'] = self.get_node_ready_status(node_mo)
        if info['ready'] == 'Ready':
            info['__Output']['ready'] = 'Green'
        else:
            info['__Output']['ready'] = 'Red'

        info['conditions'] = {}
        info['conditions']['Memory Pressure'] = self.is_node_memory_pressure(node_mo)
        info['conditions']['Disk Pressure'] = self.is_node_disk_pressure(node_mo)
        info['conditions']['PID Pressure'] = self.is_node_pid_pressure(node_mo)

        info['is_vm'] = self.is_node_vm(node_mo)
        info['is_bm'] = self.is_node_bm(node_mo)
        info['type'] = ''
        if info['is_vm']:
            info['type'] = 'VM'
        if info['is_bm']:
            info['type'] = 'BM'

        return info

    def get_nodes_info(self):
        if not self.get_nodes():
            return None

        info = []
        for node_mo in self.nodes:
            node_info = self.get_node_info(node_mo)
            if node_info is not None:
                info.append(node_info)

        info = sorted(
            info,
            key=lambda i: i['name']
        )

        return info

    def get_nodes_state(self, summary_only=False):
        try:
            state = {}
            state['summary'] = {}
            state['summary']['count'] = len(self.nodes)
            state['summary']['ready'] = self.get_nodes_ready_count()
            state['summary']['functional'] = False
            if state['summary']['count'] > 0 and state['summary']['count'] == state['summary']['ready']:
                state['summary']['functional'] = True
            state['summary']['status'] = self.get_nodes_status_summary()

            if summary_only:
                return state['summary']

            state['nodes'] = self.get_nodes_info()

        except BaseException:
            self.log.error('k8s_nodes.get_nodes_state', traceback.format_exc())
            return None

        return state

    def get_nodes_health_summary(self):
        '''
            {
                "nodes_count": 5,
                "nodes_ready": 5,
                "nodes_healthy": true,
                "nodes_status": [
                    {
                        "status": "Ready",
                        "count": 5
                    },
                    {
                        "status": "Memory Pressure",
                        "count": 0
                    },
                    {
                        "status": "Disk Pressure",
                        "count": 0
                    },
                    {
                        "status": "PID Pressure",
                        "count": 0
                    }
                ]
            }
        '''
        summary = {}
        summary['nodes_count'] = len(self.nodes)
        summary['nodes_ready'] = self.get_nodes_ready_count()
        summary['nodes_healthy'] = False
        if summary['nodes_count'] > 0 and summary['nodes_count'] == summary['nodes_ready']:
            summary['nodes_healthy'] = True
            summary['nodes_status'] = self.get_nodes_status_summary()
        return summary

    def get_nodes_labels(self):
        try:
            labels = []
            for node in self.nodes:
                try:
                    node_labels = node['metadata']['labels']
                    if node_labels is not None:
                        for key in node_labels:
                            labels.append(
                                dict(
                                    key=key,
                                    value=node_labels[key]
                                )
                            )

                except BaseException:
                    self.log.error('k8s_nodes.get_nodes_labels', traceback.format_exc())

        except BaseException:
            self.log.error('k8s_nodes.get_nodes_labels', traceback.format_exc())
            return None

        return labels

    def get_node_mo(self, node_name, cache=True):
        if not self.get_nodes(cache=cache):
            return False

        for node in self.nodes:
            if node['metadata']['name'] == node_name:
                return node

        return None

    def get_node(self, name):
        try:
            for node_mo in self.nodes:
                if node_mo['metadata']['name'] == name:
                    info = {}
                    info['node'] = node_mo
                    info['summary'] = self.get_node_info(node_mo)
                    info['pods'] = self.get_node_pods(name)
                    info['age'] = int(time.time() * 1000) - info['timestamp']
                    return info

        except BaseException:
            self.log.error(
                'k8s_nodes.get_node',
                traceback.format_exc()
            )

        return None
