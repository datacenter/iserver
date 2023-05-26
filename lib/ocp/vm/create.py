import time
import yaml


class OcpVmCreate():
    def __init__(self):
        self.user_input = None

    def create_image(self):
        if self.user_input['deployment']['image']['enabled']:
            image_dv_filename = self.user_input['deployment']['image']['dv']
            if image_dv_filename is not None:
                image_dv_yaml = yaml.safe_load(
                    self.user_input['files'][image_dv_filename]
                )

                success = self.create_ocp_vm_image(
                    self.user_input['deployment']['image']['ip'],
                    self.user_input['deployment']['image']['username'],
                    self.user_input['deployment']['image']['password'],
                    self.user_input['deployment']['image']['key_filename'],
                    self.user_input['deployment']['image']['path'],
                    image_dv_yaml
                )
                if not success:
                    return False

        return True

    def create_day0(self):
        if self.user_input['deployment']['day0']['enabled']:
            day0_dv_filename = self.user_input['deployment']['day0']['dv']
            if day0_dv_filename is not None:
                day0_dv_yaml = yaml.safe_load(
                    self.user_input['files'][day0_dv_filename]
                )

                source_filename = self.user_input['deployment']['day0']['source']
                source_content = self.user_input['files'][source_filename]
                success = self.create_ocp_vm_day0(
                    self.user_input['deployment']['day0']['filename'],
                    source_content,
                    self.user_input['deployment']['day0']['destination'],
                    day0_dv_yaml,
                    tools=self.user_input['tools']
                )
                if not success:
                    return False

        return True

    def create_sriov_policy(self):
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
                            'SRIOV network node policy already exists: %s/%s' % (
                                namespace,
                                name
                            )
                        )
                        continue

                    self.my_output.default(
                        'SRIOV network node policy will be created: %s/%s' % (
                            namespace,
                            name
                        )
                    )

                    success = self.create_ocp_sriov_network_node_policy(
                        policy_yaml
                    )
                    if not success:
                        return False

        return True

    def create_sriov_network(self):
        if self.user_input['deployment']['sriov']['enabled']:
            if self.user_input['deployment']['sriov']['network'] is not None:
                for network_filename in self.user_input['deployment']['sriov']['network']:
                    network_yaml = yaml.safe_load(
                        self.user_input['files'][network_filename]
                    )

                    namespace = network_yaml['metadata']['namespace']
                    name = network_yaml['metadata']['name']
                    if self.is_ocp_sriov_network(namespace, name):
                        self.my_output.default(
                            'SRIOV network already exists: %s/%s' % (
                                namespace,
                                name
                            )
                        )
                        continue

                    self.my_output.default(
                        'SRIOV network will be created: %s/%s' % (
                            namespace,
                            name
                        )
                    )

                    success = self.create_ocp_sriov_network(
                        network_yaml
                    )
                    if not success:
                        return False

        return True

    def create_vm(self):
        vm_filename = self.user_input['deployment']['vm']

        vm_yaml = yaml.safe_load(
            self.user_input['files'][vm_filename]
        )
        if vm_yaml is None:
            self.my_output.error(
                'Create virtual machine deployment file failed to be loaded: %s' % (vm_filename)
            )
            return False

        namespace = vm_yaml['metadata']['namespace']
        name = vm_yaml['metadata']['name']

        if not self.create_ocp_vm(vm_yaml):
            self.my_output.error(
                'Create virtual machine request failed'
            )
            return False

        self.my_output.default(
            'Virtual machine %s/%s created' % (
                namespace,
                name
            )
        )

        if vm_yaml['spec']['running']:
            self.my_output.default('Wait for virtual machine running...')
            if not self.wait_ocp_vm_running(namespace, name):
                self.my_output.error('Timed out')
                return False

        if not vm_yaml['spec']['running']:
            self.my_output.default('Wait for virtual machine stopped...')
            if not self.wait_ocp_vm_stopped(namespace, name):
                self.my_output.error('Timed out')
                return False

        return True

    def create_vm_deployment(self, user_input, report=False):
        self.user_input = user_input

        namespace = self.user_input['deployment']['namespace']
        name = self.user_input['deployment']['name']

        self.my_output.default(
            'Check virtual machine state: %s/%s' % (
                namespace,
                name
            )
        )
        if self.is_ocp_vmi(namespace, name):
            self.my_output.default(
                'Virtual machine already exists'
            )
            created = False
        else:
            self.my_output.default(
                'Virtual machine does not exist yet'
            )

            created = True

            if not self.create_image():
                return False

            if not self.create_day0():
                return False

            if not self.create_sriov_policy():
                return False

            if not self.create_sriov_network():
                return False

            if not self.create_vm():
                return False

        if not self.create_deployment_services(self.user_input):
            return False

        if self.user_input['ready']['enabled']:
            if not self.wait_ocp_vm_ready(self.user_input):
                return False

        if report:
            if user_input['report']['enabled']:
                if created:
                    if 'sleep' in user_input['ready']:
                        self.my_output.default(
                            'Wait for %s seconds before collecting report...' % (
                                user_input['ready']['sleep']
                            )
                        )
                        time.sleep(user_input['ready']['sleep'])

                if not self.create_vm_state_report(self.user_input):
                    return False

        return True
