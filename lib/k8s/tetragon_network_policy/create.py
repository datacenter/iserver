class K8sTetragonNetworkPolicyCreate():
    def __init__(self):
        pass

    def create_tetragon_network_policy(self, body, confirmation=False, my_output=None, wait=True):
        success = self.create_resource_and_wait(
            body, 
            'tetragon_network_policy', 
            wait=wait,
            my_output=my_output, 
            confirmation=confirmation
        )
        return success