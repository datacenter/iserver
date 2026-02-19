class K8sMutatingWebhookOutput():
    def __init__(self):
        pass

    def print_mutating_webhooks(self, info, title=False):
        if title:
            self.my_output.default(
                'Mutating Webhook [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'name'
        ]

        headers = [
            'MutatingWebhook'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            row_separator=False,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
