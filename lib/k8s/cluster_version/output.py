class K8sClusterVersionOutput():
    def __init__(self):
        pass

    def print_cluster_versions(self, info, title=False):
        if title:
            self.my_output.default(
                'Cluster Version [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'name'
        ]

        headers = [
            'Cluster Version'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_cluster_versions_deployment(self, info, title=False):
        if title:
            self.my_output.default(
                'Cluster Operator - Deployment [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        for item in info:
            item['deploymentT'] = []
            if item['co_deployment'] is not None:
                item['deploymentT'].append(
                    item['co_deployment']['namespace']
                )
                item['deploymentT'].append(
                    item['co_deployment']['name']
                )

            item['relatedT'] = []
            if item['related_deployment'] is not None:
                for related in item['related_deployment']:
                    item['relatedT'].append(
                        '%s/%s' % (
                            related['namespace'],
                            related['name']
                        )
                    )

            if len(item['relatedT']) == 0:
                item['relatedT'].append('--')

        order = [
            'name',
            'deploymentT',
            'relatedT'
        ]

        headers = [
            'Name',
            'Operator Deployment',
            'Managed Deployments'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['deploymentT', 'relatedT']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )
