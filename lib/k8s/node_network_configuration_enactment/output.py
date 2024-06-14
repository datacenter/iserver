class K8sNodeNetworkConfigurationEnactmentOutput():
    def __init__(self):
        pass

    def print_node_network_configuration_enactment(self, info, title=False):
        if title:
            self.my_output.default(
                'Node Network Configuration Enactment [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )
