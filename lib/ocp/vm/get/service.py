import yaml


class OcpVmGetService():
    def __init__(self):
        pass

    def is_ocp_vm_services(self, label_special):
        services_mo = self.get_ocp_vm_services(
            label_special
        )
        if services_mo is None or len(services_mo) == 0:
            return False
        return True

    def get_ocp_vm_services(self, label_special):
        services_mo = self.k8s_handler.get_services_with_selector(
            'special',
            label_special
        )
        return services_mo

    def get_ocp_vm_service_ip_port(self, service_namespace, service_name, cache=True):
        service_mo = self.k8s_handler.get_service(
            service_namespace,
            service_name,
            cache=cache
        )
        if service_mo is None:
            self.my_output.error(
                'Service %s/%s not found' % (
                    service_namespace,
                    service_name
                )
            )
            return None, None

        try:
            node_port = service_mo['spec']['ports'][0]['node_port']
        except BaseException:
            self.my_output.error(
                'Service %s/%s expected to be node port type' % (
                    service_namespace,
                    service_name,
                )
            )
            return None, None

        nodes_ip = self.k8s_handler.get_worker_nodes_ip()
        if nodes_ip is None or len(nodes_ip) == 0:
            self.my_output.error(
                'No ready worker node found'
            )
            return None, None

        return nodes_ip[0], node_port

    def get_deployment_service_auth_info(self, deployment, namespace, name):
        info = ''
        for key in deployment['deployment']['service']:
            filename = deployment['deployment']['service'][key]
            if filename is not None:
                service_yaml = yaml.safe_load(
                    deployment['files'][filename]
                )

                if service_yaml['metadata']['namespace'] == namespace and service_yaml['metadata']['name'] == name:
                    if key == 'ssh':
                        try:
                            info = 'SSH with (%s, %s) credentials' % (
                                deployment['ssh']['username'],
                                deployment['ssh']['password']
                            )
                        except BaseException:
                            pass

                    if key == 'snmp':
                        try:
                            info = 'SNMP with community %s' % (
                                deployment['snmp']['community']
                            )
                        except BaseException:
                            pass

                    if key == 'netconf':
                        try:
                            info = 'Netconf with (%s, %s) credentials' % (
                                deployment['netconf']['username'],
                                deployment['netconf']['password']
                            )
                        except BaseException:
                            pass

        return info

    def get_ocp_vm_services_info(self, label_special, deployment=None):
        services = []

        if label_special is None:
            return services

        nodes_ip = self.k8s_handler.get_worker_nodes_ip()
        node_ip = None
        if nodes_ip is not None and len(nodes_ip) > 0:
            node_ip = nodes_ip[0]

        services_mo = self.get_ocp_vm_services(label_special)
        if services_mo is not None:
            for service_mo in services_mo:
                service_info = {}
                service_info['namespace'] = service_mo['metadata']['namespace']
                service_info['name'] = service_mo['metadata']['name']
                service_info['namespace_name'] = '%s/%s' % (
                    service_info['namespace'],
                    service_info['name']
                )
                service_info['cluster_ip'] = service_mo['spec']['cluster_ip']
                service_info['external_traffic_policy'] = service_mo['spec']['external_traffic_policy']
                service_info['type'] = service_mo['spec']['type']
                service_info['selector'] = service_mo['spec']['selector']['special']

                service_info['ports'] = []
                for port_mo in service_mo['spec']['ports']:
                    if 'node_port' not in port_mo:
                        self.log.error(
                            'get_ocp_vm_services_info',
                            'Unsupported service port: %s' % (service_mo)
                        )
                        continue

                    port_info = {}
                    port_info['ip'] = node_ip
                    port_info['port'] = port_mo['node_port']
                    port_info['ip_port'] = '%s:%s' % (
                        port_info['ip'],
                        port_info['port']
                    )
                    port_info['target_protocol'] = port_mo['protocol']
                    port_info['target_port'] = port_mo['port']
                    port_info['protocol_port'] = '%s/%s' % (
                        port_info['target_protocol'],
                        port_info['target_port']
                    )
                    service_info['ports'].append(
                        port_info
                    )

                if deployment is not None:
                    service_info['auth'] = self.get_deployment_service_auth_info(
                        deployment,
                        service_mo['metadata']['namespace'],
                        service_mo['metadata']['name']
                    )

                services.append(
                    service_info
                )

        return services
