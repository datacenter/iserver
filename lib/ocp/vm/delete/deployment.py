import yaml


class OcpVmDeleteDeployment():
    def __init__(self):
        self.user_input = None

    def delete_vm_deployment(self, user_input, include_sriov_policy=False, include_image=False):
        self.user_input = user_input

        if not self.delete_service():
            return False

        if not self.delete_vm():
            return False

        if not self.delete_multus_network():
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
                        yaml_content = self.user_input['files'][policy_filename]
                        content = yaml.safe_load(yaml_content)

                        namespace = content['metadata']['namespace']
                        name = content['metadata']['name']
                        if self.k8s_handler.is_sriov_network_node_policy(name, cache_enabled=False):
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
                    yaml_content = self.user_input['files'][image_dv_filename]
                    content = yaml.safe_load(yaml_content)

                    namespace = content['metadata']['namespace']
                    name = content['metadata']['name']

                    if self.k8s_handler.is_data_volume(namespace, name, cache_enabled=False) or self.k8s_handler.is_pvc(namespace, name, cache_enabled=False):
                        self.my_output.default(
                            'Image remains: %s/%s' % (
                                namespace,
                                name
                            )
                        )

        return True
