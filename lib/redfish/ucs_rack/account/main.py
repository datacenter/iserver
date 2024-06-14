class RedfishEndpointUcsRackAccount():
    def __init__(self):
        self.accounts = None

    def get_accounts(self, include_disabled=False, cache_enabled=True):
        if cache_enabled and self.accounts is not None:
            return self.accounts

        self.accounts = self.get_template_account_properties(
            role_info=True,
            include_disabled=include_disabled,
            cache_enabled=False
        )
        return self.accounts

    def get_account_by_username(self, username, cache_enabled=True):
        accounts = self.get_accounts(cache_enabled=cache_enabled)
        if accounts is None:
            return None

        for account in accounts:
            if account['username'] == username:
                return account

        return None

    def is_account_username(self, username, cache_enabled=True):
        if self.get_account_by_username(username, cache_enabled=cache_enabled):
            return True
        return False

    def get_account_empty_ids(self, cache_enabled=False):
        accounts = self.get_accounts(cache_enabled=cache_enabled)
        if accounts is None:
            return None

        account_ids = []
        for account in accounts:
            account_ids.append(
                account['id']
            )

        empty_ids = []
        for account_id in range(1, 15):
            if str(account_id) not in account_ids:
                empty_ids.append(
                    str(account_id)
                )

        return empty_ids

    def get_account_empty_id(self, cache_enabled=False):
        accounts = self.get_accounts(cache_enabled=cache_enabled)
        if accounts is None:
            return None

        account_ids = []
        for account in accounts:
            account_ids.append(
                account['id']
            )

        for account_id in range(1, 15):
            if str(account_id) not in account_ids:
                return str(account_id)

        return None

    def get_non_admin_role_usernames(self, allowed_usernames=[]):
        accounts = self.get_accounts(cache_enabled=False)
        if accounts is None:
            return None

        usernames = []
        for account in accounts:
            if account['username'] in allowed_usernames:
                usernames.append(
                    account['username']
                )
                continue

            if account['role_id'] != 'admin':
                usernames.append(
                    account['username']
                )

        return usernames
