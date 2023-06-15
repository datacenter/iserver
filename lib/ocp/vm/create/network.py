import yaml


class OcpVmCreateNetwork():
    def __init__(self):
        pass

    def create_sriov_network(self):
        if self.user_input['deployment']['sriov']['enabled']:
            if self.user_input['deployment']['sriov']['network'] is not None:
                for network_filename in self.user_input['deployment']['sriov']['network']:
                    yaml_content = self.user_input['files'][network_filename]
                    content = yaml.safe_load(yaml_content)

                    namespace = content['metadata']['namespace']
                    name = content['metadata']['name']
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
                        content
                    )
                    if not success:
                        return False

        return True
