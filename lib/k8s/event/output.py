from lib import filter_helper


class K8sEventOutput():
    def __init__(self):
        pass

    def print_events(self, info, title=False):
        if title:
            self.my_output.default(
                'Event [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        for item in info:
            item['ageT'] = []
            item['ageT'].append('First: %s' % (item['first_timestamp_age']))
            item['ageT'].append('Last: %s' % (item['last_timestamp_age']))

        order = [
            'objT',
            'ageT',
            'count',
            'messageT',
            'type',
            'reason',
            'action'
        ]

        headers = [
            'Object',
            'When',
            'Count',
            'Message',
            'Type',
            'Reason',
            'Action'
        ]

        chunk = {}
        chunk['message'] = 40
        empty = ['type', 'reason', 'action']
        collapse = {}
        collapse['objT'] = ['obj_kind', 'obj_namespace', 'obj_name', 'obj_uid']

        self.my_output.my_table(
            self.my_output.expand_lists(
                self.my_output.prepare_list(
                    info,
                    chunk=chunk,
                    empty=empty,
                    collapse=collapse
                ),
                order,
                ['objT', 'ageT', 'messageT']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )
