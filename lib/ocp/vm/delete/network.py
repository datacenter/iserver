import yaml


class OcpVmDeleteNetwork():
    def __init__(self):
        pass

    def delete_sriov_network(self):
        if self.user_input['deployment']['sriov']['enabled']:
            if self.user_input['deployment']['sriov']['network'] is not None:
                for network_filename in self.user_input['deployment']['sriov']['network']:
                    yaml_content = self.user_input['files'][network_filename]
                    content = yaml.safe_load(yaml_content)

                    namespace = content['metadata']['namespace']
                    name = content['metadata']['name']
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
