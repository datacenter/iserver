class K8sClusterOperatorOutput():
    def __init__(self):
        pass

    def print_cluster_operators(self, info, title=False):
        if title:
            self.my_output.default(
                'Cluster Operator [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        for item in info:
            if item['version'] is None:
                item['version'] = '--'

            if item['owner'] is None:
                item['ownerT'] = ['--']
            else:
                item['ownerT'] = item['owner'].split('/')

        order = [
            'name',
            'version',
            'ownerT',
            'availableTick',
            'progressingTick',
            'degradedTick',
            'upgradeableTick',
            'availableSince',
            'age'
        ]

        headers = [
            'Name',
            'Version',
            'Owner',
            'Available',
            'Progressing',
            'Degraded',
            'Upgradeable',
            'Since',
            'Age'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['ownerT']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_cluster_operators_deployment(self, info, title=False):
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
