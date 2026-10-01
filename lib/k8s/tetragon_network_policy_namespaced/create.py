class K8sTetragonNetworkPolicyNamespacedCreate():
    def __init__(self):
        pass

    def create_tetragon_network_policy_namespaced(self, body, my_output=None, confirmation=False, wait=True):
        success = self.create_resource_and_wait(
            body, 
            'tetragon_network_policy_namespaced', 
            wait=wait,
            my_output=my_output, 
            confirmation=confirmation
        )
        if not success:
            return False

        return True    