class OcpClusterCnvOutput():
    def __init__(self):
        pass

    def print_ocp_cnv_state(self, info):
        order = [
            'namespace.name',
            'operator.name',
            'subscription.name',
            'subscription.state',
            'csv.name',
            'csv.phase'
        ]

        headers = [
            'Namespace',
            'Operator Group',
            'Subscription',
            'Subscription State',
            'Cluster Service Version (CSV)',
            'CSV Phase'
        ]

        self.my_output.dictionary(
            info,
            title='Container Virtualization (CNV) State',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )
