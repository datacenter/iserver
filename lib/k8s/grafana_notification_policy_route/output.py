class K8sGrafanaNotificationPolicyRouteOutput():
    def __init__(self):
        pass

    def print_grafana_notification_policy_routes(self, info, title=False):
        if title:
            self.my_output.default(
                'Grafana NotificationPolicyRoute - State [#%s]' % (len(info)),
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
            'Grafana Notification Policy Route'
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
