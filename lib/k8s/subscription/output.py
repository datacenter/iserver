class K8sSubscriptionOutput():
    def __init__(self):
        pass

    def print_subscriptions(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Subscription', 'namespace_nameT'],
                ['Package', 'package'],
                ['Channel', 'channel'],
                ['Owner', 'owner_name'],
                ['Install Plan', 'install_plan_name'],
                ['CSV', 'installed_csv'],
                ['Latest', 'csvTick'],
                ['Age', 'age']
            ]
        )

    def print_subscription(self, item):
        self.my_output.dictionary_ng(
            'Subscription',
            item, 
            [
                ['Namespace', 'namespace'],
                ['Name', 'name'],
                ['Package', 'package'],
                ['Channel', 'channel'],
                ['Owner', 'owner_name'],
                ['Install Plan', 'install_plan_name'],
                ['CSV', 'installed_csv'],
                ['Latest', 'csvTick'],
                ['Age', 'age']
            ]
        )
        