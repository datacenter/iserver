class NsoCnfmCnfdOutput():
    def __init__(self):
        pass

    def print_cnfm_cnfds(self, info, title=False):
        if title:
            self.my_output.default(
                'CNFM - CNFD [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'name',
            'chart',
            'localTick',
            'version.version',
            'version.cnfi_summary'
        ]

        headers = [
            'Name',
            'Chart',
            'Local',
            'Version',
            'CNF Instance'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['version']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=False,
            table=True
        )
