import json


class K8sNetworkAttachmentDefinitionOutput():
    def __init__(self):
        pass

    def print_nads(self, info, title=False):
        if title:
            self.my_output.default(
                'Network Attachment Definition [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        for item in info:
            if item['resource_name'] is None:
                item['resource_name'] = '--'

            item['configT'] = json.dumps(
                item['config'],
                indent=2
            ).split('\n')

        order = [
            'namespace',
            'name',
            'config.type',
            'resource_name',
            'configT',
            'age'
        ]

        headers = [
            'Namespace',
            'Name',
            'Type',
            'SR-IOV Resource',
            'Config',
            'Age'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['configT']
            ),
            order=order,
            headers=headers,
            row_separator=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
