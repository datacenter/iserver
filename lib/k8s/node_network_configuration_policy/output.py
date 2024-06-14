class K8sNodeNetworkConfigurationPolicyOutput():
    def __init__(self):
        pass

    def print_node_network_configuration_policy(self, info, title=False):
        if title:
            self.my_output.default(
                'Node Network Configuration Policy [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )
