import yaml


class OcpVmDelete():
    def __init__(self):
        self.user_input = None

    def delete_image(self):
        if self.user_input['deployment']['image']['enabled']:
            image_dv_filename = self.user_input['deployment']['image']['dv']
            if image_dv_filename is not None:
                image_dv_yaml = yaml.safe_load(
                    self.user_input['files'][image_dv_filename]
                )

                namespace = image_dv_yaml['metadata']['namespace']
                name = image_dv_yaml['metadata']['name']

                if self.is_ocp_dv(namespace, name, cache=False):
                    self.my_output.default(
                        'Image dv will be deleted: %s/%s' % (
                            namespace,
                            name
                        )
                    )
                    success = self.delete_ocp_dv(
                        namespace,
                        name
                    )
                    return success

                if self.k8s_handler.is_pvc(namespace, name, cache=False):
                    self.my_output.default(
                        'Image pvc will be deleted: %s/%s' % (
                            namespace,
                            name
                        )
                    )
                    success = self.k8s_handler.delete_namespaced_pvc(
                        namespace,
                        name
                    )
                    return success

                self.my_output.default(
                    'Image dv/pvc already deleted: %s/%s' % (
                        namespace,
                        name
                    )
                )

        return True

    def delete_day0(self):
        if self.user_input['deployment']['day0']['enabled']:
            day0_dv_filename = self.user_input['deployment']['day0']['dv']
            if day0_dv_filename is not None:
                day0_dv_yaml = yaml.safe_load(
                    self.user_input['files'][day0_dv_filename]
                )

                namespace = day0_dv_yaml['metadata']['namespace']
                name = day0_dv_yaml['metadata']['name']

                if self.is_ocp_dv(namespace, name, cache=False):
                    self.my_output.default(
                        'Day0 dv will be deleted: %s/%s' % (
                            namespace,
                            name
                        )
                    )
                    success = self.delete_ocp_dv(
                        namespace,
                        name
                    )
                    return success

                if self.k8s_handler.is_pvc(namespace, name, cache=False):
                    self.my_output.default(
                        'Day0 pvc will be deleted: %s/%s' % (
                            namespace,
                            name
                        )
                    )
                    success = self.k8s_handler.delete_namespaced_pvc(
                        namespace,
                        name
                    )
                    return success

                self.my_output.default(
                    'Day0 dv/pvc already deleted: %s/%s' % (
                        namespace,
                        name
                    )
                )

        return True

    def delete_sriov_policy(self):
        if self.user_input['deployment']['sriov']['enabled']:
            if self.user_input['deployment']['sriov']['policy'] is not None:
                for policy_filename in self.user_input['deployment']['sriov']['policy']:
                    policy_yaml = yaml.safe_load(
                        self.user_input['files'][policy_filename]
                    )

                    namespace = policy_yaml['metadata']['namespace']
                    name = policy_yaml['metadata']['name']
                    if not self.is_ocp_sriov_network_node_policy(namespace, name):
                        self.my_output.default(
                            'SRIOV network node policy already deleted: %s/%s' % (
                                namespace,
                                name
                            )
                        )
                        continue

                    self.my_output.default(
                        'SRIOV network node policy will be deleted: %s/%s' % (
                            namespace,
                            name
                        )
                    )

                    success = self.delete_ocp_sriov_network_node_policy(
                        namespace,
                        name
                    )
                    if not success:
                        return False

        return True

    def delete_sriov_network(self):
        if self.user_input['deployment']['sriov']['enabled']:
            if self.user_input['deployment']['sriov']['network'] is not None:
                for network_filename in self.user_input['deployment']['sriov']['network']:
                    network_yaml = yaml.safe_load(
                        self.user_input['files'][network_filename]
                    )

                    namespace = network_yaml['metadata']['namespace']
                    name = network_yaml['metadata']['name']
                    if not self.is_ocp_sriov_network(namespace, name):
                        self.my_output.default(
                            'SRIOV network already deleted: %s/%s' % (
                                namespace,
                                name
                            )
                        )
                        continue

                    self.my_output.default(
                        'SRIOV network will be deleted: %s/%s' % (
                            namespace,
                            name
                        )
                    )

                    success = self.delete_ocp_sriov_network(
                        namespace,
                        name
                    )
                    if not success:
                        return False

        return True

    def delete_vm(self):
        vm_filename = self.user_input['deployment']['vm']
        vm_yaml = yaml.safe_load(
            self.user_input['files'][vm_filename]
        )
        namespace = vm_yaml['metadata']['namespace']
        name = vm_yaml['metadata']['name']

        is_running = self.is_ocp_vmi(
            namespace,
            name
        )

        is_defined = self.is_ocp_vm(
            namespace,
            name
        )

        if not is_running:
            self.my_output.default(
                'Virtual machine instance %s/%s does not exist' % (
                    namespace,
                    name
                )
            )

        if is_running:
            self.my_output.default(
                'Stopping virtual machine %s/%s...' % (
                    namespace,
                    name
                )
            )
            if not self.stop_ocp_vm(namespace, name):
                self.my_output.error('Virtual machine stop failed')
                return False

            self.my_output.default('Wait for virtual machine stopped...')
            if not self.wait_ocp_vm_stopped(namespace, name):
                self.my_output.error('Timed out')
                return False

        if not is_defined:
            self.my_output.default(
                'Virtual machine not defined %s/%s' % (
                    namespace,
                    name
                )
            )

        if is_defined:
            self.my_output.default(
                'Deleting virtual machine %s/%s...' % (
                    namespace,
                    name
                )
            )
            success = self.delete_ocp_vm(
                namespace,
                name
            )
            if not success:
                self.my_output.error('Virtual machine delete failed')
                return False

            self.my_output.default('Virtual machine deleted')

        return True

    def delete_service(self):
        vm_filename = self.user_input['deployment']['vm']
        vm_yaml = yaml.safe_load(
            self.user_input['files'][vm_filename]
        )

        label_special = None
        if 'spec' in vm_yaml:
            if 'special' in vm_yaml['spec']['template']['metadata']['labels']:
                label_special = vm_yaml['spec']['template']['metadata']['labels']['special']
                is_service = self.is_ocp_vm_services(
                    label_special
                )

                if not is_service:
                    self.my_output.default('No virtual machine service found with label: %s' % (label_special))

                if is_service:
                    self.my_output.default('Deleting virtual machine services...')
                    success = self.delete_ocp_vm_services(label_special)

                    if not success:
                        self.my_output.error('Virtual machine services delete failed')
                        return False

                    self.my_output.default('Virtual machine services deleted')

        return True

    def delete_vm_deployment(self, user_input, include_sriov_policy=False, include_image=False):
        self.user_input = user_input

        if not self.delete_service():
            return False

        if not self.delete_vm():
            return False

        if not self.delete_sriov_network():
            return False

        if include_sriov_policy:
            if not self.delete_sriov_policy():
                return False
        else:
            if self.user_input['deployment']['sriov']['enabled']:
                if self.user_input['deployment']['sriov']['policy'] is not None:
                    for policy_filename in self.user_input['deployment']['sriov']['policy']:
                        policy_yaml = yaml.safe_load(
                            self.user_input['files'][policy_filename]
                        )

                        namespace = policy_yaml['metadata']['namespace']
                        name = policy_yaml['metadata']['name']
                        if self.is_ocp_sriov_network_node_policy(namespace, name):
                            self.my_output.default(
                                'SRIOV network node policy remains: %s/%s' % (
                                    namespace,
                                    name
                                )
                            )

        if not self.delete_day0():
            return False

        if include_image:
            if not self.delete_image():
                return False
        else:
            if self.user_input['deployment']['image']['enabled']:
                image_dv_filename = self.user_input['deployment']['image']['dv']
                if image_dv_filename is not None:
                    image_dv_yaml = yaml.safe_load(
                        self.user_input['files'][image_dv_filename]
                    )

                    namespace = image_dv_yaml['metadata']['namespace']
                    name = image_dv_yaml['metadata']['name']

                    if self.is_ocp_dv(namespace, name, cache=False) or self.k8s_handler.is_pvc(namespace, name, cache=False):
                        self.my_output.default(
                            'Image remains: %s/%s' % (
                                namespace,
                                name
                            )
                        )

        return True
