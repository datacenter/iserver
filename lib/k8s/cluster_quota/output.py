class K8sClusterQuotaOutput():
    def __init__(self):
        pass

    def print_cluster_quotas(self, info, title=False):
        if title:
            self.my_output.default(
                'Cluster Quota [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'tbd'
        ]

        headers = [
            'tbd'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=False,
            table=True
        )