import json


class K8sSandboxPolicyNamespacedOutput():
    def __init__(self):
        pass

    def print_sandbox_policy_namespaceds_state(self, info):
        for item in info:
            item['specT'] = json.dumps(item['spec'], indent=2).split('\n')

        self.my_output.my_table_ng(
            info,
            [
                ['Sandbox Policy', 'namespace_nameT'],
                ['Spec', 'specT']
            ]
        )