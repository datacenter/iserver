class K8sGrafanaMuteTimingOutput():
    def __init__(self):
        pass

    def print_grafana_mute_timings(self, info, title=False):
        if title:
            self.my_output.default(
                'Grafana MuteTiming - State [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'namespace_name'
        ]

        headers = [
            'Grafana Mute Timing'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            row_separator=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
