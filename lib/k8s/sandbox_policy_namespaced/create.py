class K8sSandboxPolicyNamespacedCreate():
    def __init__(self):
        pass

    def create_sandbox_policy_namespaced(self, body, my_output=None, confirmation=False, wait=True):
        success = self.create_resource_and_wait(
            body, 
            'sandbox_policy_namespaced', 
            wait=wait,
            my_output=my_output, 
            confirmation=confirmation
        )
        if not success:
            return False

        return True    