import time


class OcpVmCreateDeployment():
    def __init__(self):
        pass

    def create_vm_deployment(self, user_input, report=False):
        self.set_user_input(user_input)

        namespace = self.user_input['deployment']['namespace']
        name = self.user_input['deployment']['name']

        self.my_output.default(
            'Check virtual machine state: %s/%s' % (
                namespace,
                name
            )
        )

        if self.k8s_handler.is_virtual_machine_instance(namespace, name, cache_enabled=False):
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

            if not self.create_multus_network():
                return False

            if not self.create_vm():
                return False

        if not self.create_deployment_services(self.user_input):
            return False

        if self.user_input['ready']['enabled']:
            if not self.wait_ocp_vm_ready(self.user_input):
                return False

        if report:
            if not self.user_input['running']['wait']:
                self.my_output.error('Report required running wait enabled')
                return True

            if not self.user_input['ready']['enabled']:
                self.my_output.error('Report required ready enabled')
                return True

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
