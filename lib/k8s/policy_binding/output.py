class K8sPolicyBindingOutput():
    def __init__(self):
        pass

    def print_policy_bindings(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Policy Binding', 'namespace_nameT']
            ]
        )