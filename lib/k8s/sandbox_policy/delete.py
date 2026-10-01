class K8sSandboxPolicyDelete():
    def __init__(self):
        pass

    def delete_sandbox_policy(self, name, my_output=None, wait=True):
        success = self.delete_resource_and_wait(
            'SandboxPolicy', 
            'cilium.io/v1alpha1',
            name, 
            'sandbox_policy',
            wait=wait, 
            max_time=60, 
            my_output=my_output
        )
        return success
    
    def delete_sandbox_policys(self, my_output=None, wait=True):
        items = self.get_sandbox_policys(
            cache_enabled=False
        )
        if items is None:
            if my_output is not None:
                my_output.error('Failed to get sandbox policy')
            return False
        
        for item in items:
            success = self.delete_sandbox_policy(
                item['name'],
                my_output=my_output,
                wait=wait
            )
            if not success:
                return False

        return True