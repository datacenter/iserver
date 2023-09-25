from lib import filter_helper


class K8sProfileOutput():
    def __init__(self):
        pass

    def print_profiles(self, info, title=False):
        if title:
            self.my_output.default(
                'Tuned Profile [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'namespace',
            'name',
            'profile',
            'owner',
            'appliedTick',
            'degradedTick',
            'bootcmdlineTick',
            'errorTick',
            'age'
        ]

        headers = [
            'Namespace',
            'Name',
            'Profile',
            'Owner',
            'Applied',
            'Degraded',
            'BootCmd',
            'Error',
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

    def print_profiles_boot(self, info, title=False):
        if title:
            self.my_output.default(
                'Tuned Profile Boot Command [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        for item in info:
            item['bootcmdlineT'] = []
            if len(item['bootcmdline']) > 0:
                item['bootcmdlineT'] = item['bootcmdline'].split(' ')

            if len(item['bootcmdlineT']) == 0:
                item['bootcmdlineT'] = ['--']

        order = [
            'namespace',
            'name',
            'profile',
            'bootcmdlineT'
        ]

        headers = [
            'Namespace',
            'Name',
            'Profile',
            'Boot Command'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['bootcmdlineT']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=False,
            table=True
        )

    def print_profiles_error(self, info, title=False):
        if title:
            self.my_output.default(
                'Tuned Profile Error [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        for item in info:
            item['errorT'] = []
            if len(item['error']) > 0:
                item['errorT'] = filter_helper.get_string_chunks(
                    item['error'],
                    80
                )

            if len(item['errorT']) == 0:
                item['errorT'] = ['--']

        order = [
            'namespace',
            'name',
            'profile',
            'errorT'
        ]

        headers = [
            'Namespace',
            'Name',
            'Profile',
            'Error'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['errorT']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=False,
            table=True
        )
