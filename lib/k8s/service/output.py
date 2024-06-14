class K8sServiceOutput():
    def __init__(self):
        pass

    def print_services(self, info, title=False):
        if title:
            self.my_output.default(
                'Service [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        for item in info:
            if len(item['cluster_ipT']) == 0:
                item['cluster_ipT'].append('--')

            if len(item['external_ipT']) == 0:
                item['external_ipT'].append('--')

            if len(item['port']) == 0:
                item['port'].append(dict(descr='--'))

        order = [
            'namespace',
            'name',
            'type',
            'cluster_ipT',
            'external_ipT',
            'port.descr',
            'age'
        ]

        headers = [
            'Namespace',
            'Name',
            'Type',
            'Cluster IP',
            'External IP',
            'Port',
            'Age'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['cluster_ipT', 'external_ipT', 'port']
            ),
            order=order,
            headers=headers,
            row_separator=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_services_metadata(self, info, title=False):
        if title:
            self.my_output.default(
                'Service Metadata [#%s]' % (len(info)),
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

            if len(item['cluster_ipT']) == 0:
                item['cluster_ipT'].append('--')

            if len(item['external_ipT']) == 0:
                item['external_ipT'].append('--')

            if len(item['port']) == 0:
                item['port'].append(dict(descr='--'))

            if item['owner'] is None:
                item['ownerT'] = ['--']
            else:
                item['ownerT'] = item['owner'].split('/')

        order = [
            'namespace_nameT',
            'ownerT',
            'labelT',
            'selectorT',
            'specialT'
        ]

        headers = [
            'Service',
            'Owner',
            'Label',
            'Selector',
            'Special'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['namespace_nameT', 'labelT', 'selectorT', 'ownerT']
            ),
            order=order,
            headers=headers,
            row_separator=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_services_pod(self, info, title=False):
        if title:
            self.my_output.default(
                'Service - Selector and Pods [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'namespace_nameT',
            'selectorT',
            'pod.namespace_name',
            'pod.phaseT'
        ]

        headers = [
            'Service',
            'Selector',
            'POD',
            'POD State'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['namespace_nameT', 'selectorT', 'pod']
            ),
            order=order,
            headers=headers,
            row_separator=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
