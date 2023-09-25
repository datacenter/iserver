import yaml


class OcpVmCreatePolicy():
    def __init__(self):
        pass

    def create_sriov_policy(self):
        if self.user_input['deployment']['sriov']['enabled']:
            if self.user_input['deployment']['sriov']['policy'] is not None:
                for policy_filename in self.user_input['deployment']['sriov']['policy']:
                    yaml_content = self.user_input['files'][policy_filename]
                    content = yaml.safe_load(yaml_content)

                    namespace = content['metadata']['namespace']
                    name = content['metadata']['name']
                    if self.k8s_handler.is_sriov_network_node_policy(name, cache_enabled=False):
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

                    success = self.k8s_handler.create_sriov_network_node_policy(
                        content
                    )
                    if not success:
                        return False

        return True
