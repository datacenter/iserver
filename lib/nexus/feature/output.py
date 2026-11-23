class FeatureOutput():
    def __init__(self):
        pass

    def print_features(self, info, title=False):
        if title:
            self.my_output.default(
                'Feature [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'nexus_name',
            'name',
            'instance',
            'status'
        ]

        headers = [
            'Device',
            'Feature',
            'Instance',
            'Status'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )
