class K8sSandboxPolicyWait():
    def __init__(self):
        pass

    def wait_sandbox_policy(self, name, match_properties={}, break_properties={}, my_output=None, prompt='SandboxPolicy', max_time=60):
        return self.wait_managed_object(
            'sandbox_policy',
            name,
            match_properties=match_properties,
            break_properties=break_properties,
            my_output=my_output,
            prompt='Wait for %s %s [timeout:%ss]' % (prompt, name, max_time),
            max_time=max_time
        )

    def wait_no_sandbox_policy(self, name, my_output=None, prompt='SandboxPolicy', max_time=60):
        return self.wait_no_managed_object(
            'sandbox_policy',
            name,
            my_output=my_output,
            prompt='Wait for no %s %s [timeout:%ss]' % (prompt, name, max_time),
            max_time=max_time
        )