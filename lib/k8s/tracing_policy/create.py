class K8sTracingPolicyCreate():
    def __init__(self):
        pass

    def create_tracing_policy(self, body, confirmation=False, my_output=None, wait=True):
        success = self.create_resource_and_wait(
            body, 
            'tracing_policy', 
            wait=wait,
            my_output=my_output, 
            confirmation=confirmation
        )
        return success