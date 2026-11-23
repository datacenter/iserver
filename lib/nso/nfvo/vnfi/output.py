class NfvoVnfiOutput():
    def __init__(self):
        pass

    def print_vnfi_plan(self, plan):
        for component in plan['plan']['component']:
            order = [
                'type',
                'name',
                'back-track'
            ]

            headers = [
                'Type',
                'Name',
                'Back Track'
            ]

            self.my_output.dictionary(
                component,
                title='Component',
                underline=True,
                prefix="- ",
                justify=True,
                keys=order,
                title_keys=headers
            )

            order = [
                'name',
                'status',
                'when'
            ]

            headers = [
                'Name',
                'Status',
                'When'
            ]

            self.my_output.my_table(
                component['state'],
                order=order,
                headers=headers,
                underline=True,
                table=True
            )

        if 'error-info' in plan['plan']:
            self.my_output.error(
                plan['plan']['error-info']['message']
            )

    def print_vnfis(self, info):
        order = [
            'name',
            'vnfd',
            'vnfd-flavour',
            'instantiation-level',
            'vnfm',
            'vnfm-type',
            'vim-type',
            'vim-ids',
            'readyTick'
        ]

        headers = [
            'VNF-INFO Name',
            'VNFD ID',
            'Flavor',
            'Level',
            'VNFM',
            'VNFM Type',
            'VIM Type',
            'VIM ID',
            'Ready'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )
