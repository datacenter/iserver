class K8sTridentOrchestratorCreate():
    def __init__(self):
        pass

    def create_trident_orchestrator(self, body, my_output=None, confirmation=False, wait=True):
        success, _ = self.create_resource(body, object_name='trident_orchestrator', my_output=my_output, confirmation=confirmation)
        if not success:
            return False
        
        if not wait:
            return True
        
        success = self.wait_trident_orchestrator(
            body['metadata']['name'],
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False

        success = self.wait_subscription_trident(my_output=my_output, with_instance=True)
        if not success:
            return False

        return True    