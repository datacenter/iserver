class K8sReplicaSetOutput():
    def __init__(self):
        pass

    def print_replica_sets(self, info, title=False):
        if title:
            self.my_output.default(
                'Replica Set [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'namespace',
            'name',
            'replicas',
            'availableReplicas',
            'readyReplicas',
            'age'
        ]

        headers = [
            'Namespace',
            'Name',
            'Desired',
            'Current',
            'Ready',
            'Age'
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

    def print_replica_sets_metadata(self, info, title=False):
        if title:
            self.my_output.default(
                'Replica Set - Metadata [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        for item in info:
            item['namespace_nameT'] = []
            item['namespace_nameT'].append(
                item['namespace']
            )
            item['namespace_nameT'].append(
                item['name']
            )

            if item['owner'] is None:
                item['ownerT'] = ['--']
            else:
                item['ownerT'] = item['owner'].split('/')

        order = [
            'namespace_nameT',
            'ownerT',
            'labelT',
            'annotationT'
        ]

        headers = [
            'Replica Set',
            'Owner',
            'Label',
            'Annotation'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['namespace_nameT', 'labelT', 'annotationT', 'ownerT']
            ),
            order=order,
            headers=headers,
            row_separator=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
