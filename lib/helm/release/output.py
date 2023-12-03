import json
from lib import filter_helper


class HelmReleaseOutput():
    def __init__(self):
        pass

    def print_releases(self, info, title=False):
        if title:
            self.my_output.default(
                'Helm Release [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'namespace',
            'name',
            'revision',
            'updated',
            'status',
            'chart',
            'app_version'
        ]

        headers = [
            'Namespace',
            'Name',
            'Revision',
            'Updated',
            'Status',
            'Chart - Version',
            'App Version'
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

    def print_releases_day0(self, info, title=False):
        if title:
            self.my_output.default(
                'Helm Release - Generated Day0 [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'namespace',
            'name',
            'day0.dv.metadata.namespace',
            'day0.dv.metadata.name'
        ]

        headers = [
            'Namespace',
            'Name',
            'Day0 PVC Namespace',
            'Day0 PVC Name'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['day0']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=False,
            table=True
        )

    def print_release_values(self, info, title=False):
        if title:
            self.my_output.default(
                'Helm Release Values [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        for item in info:
            item['valuesT'] = json.dumps(item['values'], indent=4).split('\n')

        order = [
            'namespace',
            'name',
            'chart',
            'valuesT'
        ]

        headers = [
            'Namespace',
            'Name',
            'Chart - Version',
            'Values'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['valuesT']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=False,
            table=True
        )
