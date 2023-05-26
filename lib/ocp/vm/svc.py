import yaml


class OcpVmSvc():
    def __init__(self):
        self.vms = None

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

    def create_deployment_services(self, deployment):
        if deployment['deployment']['service'] is not None:
            for key in deployment['deployment']['service']:
                service_filename = deployment['deployment']['service'][key]
                if service_filename is not None:
                    service_yaml = yaml.safe_load(
                        self.user_input['files'][service_filename]
                    )

                    namespace = service_yaml['metadata']['namespace']
                    name = service_yaml['metadata']['name']
                    self.my_output.default(
                        'Preparing %s service: %s/%s...' % (
                            key,
                            namespace,
                            name
                        )
                    )

                    service_mo = self.k8s_handler.get_service(
                        namespace,
                        name,
                        cache=False
                    )
                    if service_mo is not None:
                        self.my_output.default('Service already exists')
                        continue

                    if not self.k8s_handler.create_namespaced_service(service_yaml):
                        self.my_output.error('Service create failed')
                        return False

        return True

    def get_ocp_vm_service_ip_port(self, service_namespace, service_name):
        service_mo = self.k8s_handler.get_service(
            service_namespace,
            service_name,
            cache=False
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

    def get_ocp_vm_services_ip_port(self, label_special, deployment=None):
        services = []

        svcs = self.get_ocp_vm_services(label_special)
        if svcs is not None:
            for svc in svcs:
                service_ip, service_port = self.get_ocp_vm_service_ip_port(
                    svc['metadata']['namespace'],
                    svc['metadata']['name']
                )
                if service_ip is not None and service_port is not None:
                    info = {}
                    info['namespace'] = svc['metadata']['namespace']
                    info['name'] = svc['metadata']['name']
                    info['ip'] = service_ip
                    info['port'] = service_port
                    if deployment is not None:
                        info['auth'] = self.get_deployment_service_auth_info(
                            deployment,
                            svc['metadata']['namespace'],
                            svc['metadata']['name']
                        )

                    services.append(
                        info
                    )

        return services

    def delete_ocp_vm_services(self, label_special):
        services_mo = self.get_ocp_vm_services(
            label_special
        )

        if services_mo is not None and len(services_mo) > 0:
            for service_mo in services_mo:
                service_namespace = service_mo['metadata']['namespace']
                service_name = service_mo['metadata']['name']
                if not self.k8s_handler.delete_namespaced_service(service_namespace, service_name):
                    self.log.error(
                        'delete_ocp_vm_service',
                        'Service delete failed: %s/%s' % (service_namespace, service_name)
                    )
                    return False

                self.log.debug(
                    'delete_ocp_vm_service',
                    'Service deleted: %s/%s' % (service_namespace, service_name)
                )

                self.my_output.default(
                    'Service %s/%s deleted' % (service_namespace, service_name)
                )

        return True

    def print_deployment_service_access_info(self, info):
        order = [
            'namespace',
            'name',
            'ip',
            'port',
            'auth'
        ]

        headers = [
            'Service Namespace',
            'Service Name',
            'Node IP',
            'Node Port',
            'Authentication Info'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            table=True
        )
