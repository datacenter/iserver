class PolicyGroupAccessInterfaceBreakoutOutput():
    def __init__(self):
        pass

    def print_policy_groups_access_interface_breakout_policies(self, info):
        order = [
            'name',
            'brkoutMap'
        ]

        headers = [
            'Name',
            'Breakout Map'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
