class TenantOutput():
    def __init__(self):
        pass

    def print_tenants(self, info):
        order = [
            'name',
            'apCount',
            'aEpgCount',
            'bdCount',
            'vrfCount',
            'l2OutCount',
            'l3OutCount',
            'mplsL3OutCount',
            'contractCount',
            'endpointCount'
        ]

        headers = [
            'Name',
            'App Profile',
            'EPG',
            'Bridge Domain',
            'VRF',
            'L2Out',
            'L3Out',
            'MPLS-SR L3Out',
            'Contract',
            'Endpoint'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            underline=True,
            remove_empty_columns=True,
            table=True
        )
