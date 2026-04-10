class K8sOperatorGroupOutput():
    def __init__(self):
        pass

    def print_operator_groups_state(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Operator Group', 'namespace_nameT'],
                ['Target Namespaces', 'ns.name'],
                ['Age', 'age']
            ]
        )