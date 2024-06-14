class AccountsMgmtSubscriptionApi():
    def __init__(self):
        self.accounts_mgmt_subscription_mo = None

        self.accounts_mgmt_subscription_api_version = 'v1'
        self.accounts_mgmt_subscription_url = '%s/subscriptions' % (
            self.accounts_mgmt_subscription_api_version
        )

    def get_accounts_mgmt_subscription_mo(self, cache_enabled=True):
        if cache_enabled and self.accounts_mgmt_subscription_mo is not None:
            return self.accounts_mgmt_subscription_mo

        params = {}
        params['search'] = 'status NOT IN (\'Deprovisioned\', \'Archived\')'

        response = self.get_accounts_mgmt_mo(
            self.accounts_mgmt_subscription_url,
            params=params
        )

        if response is None:
            return None

        return response['items']
