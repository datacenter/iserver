class InterfaceLacpOutput():
    def __init__(self):
        pass

    def print_lacp_instance(self, settings):
        order = [
            'adminSt',
            'adminPrio',
            'operPrio',
            'sysMac'
        ]

        headers = [
            'Admin State',
            'Admin Priority',
            'Oper Priority',
            'Sys MAC'
        ]

        self.my_output.dictionary(
            settings,
            title='LACP Settings',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )
