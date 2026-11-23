class PolicySnoopOutput():
    def __init__(self):
        pass

    def print_policy_snoop_igmp(self, info):
        order = [
            'tenant',
            'name',
            'adminSt',
            'lastMbrIntvl',
            'queryIntvl',
            'rspIntvl',
            'startQueryCnt',
            'startQueryIntvl'
        ]

        headers = [
            'Tenant',
            'Name',
            'Admin state',
            'Last Member Query Interval',
            'Query Interval',
            'Query Response interval',
            'Start Query Count',
            'Start Query interval'
        ]

        self.my_output.dictionary(
            info,
            title='IGMP Snoop Policy',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

    def print_policy_snoop_mld(self, info):
        order = [
            'tenant',
            'name',
            'adminSt',
            'ver',
            'lastMbrIntvl',
            'queryIntvl',
            'rspIntvl',
            'startQueryCnt',
            'startQueryIntvl'
        ]

        headers = [
            'Tenant',
            'Name',
            'Admin state',
            'Version',
            'Last Member Query Interval',
            'Query Interval',
            'Query Response interval',
            'Start Query Count',
            'Start Query interval'
        ]

        self.my_output.dictionary(
            info,
            title='MLD Snoop Policy',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )
