class RedfishEndpointUcsRackTemplateAccount():
    def __init__(self):
        self.account_uri = '/redfish/v1/AccountService/Accounts'
        self.account = None

    def get_account_uri(self):
        return self.defult_account_uri

    def get_account_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.account is not None:
                return self.account

        account_uris = self.endpoint_handler.get_odata_ids(self.account_uri)
        if account_uris is None:
            return None

        self.account = []
        for account_uri in account_uris:
            if account_uri == self.account_uri:
                continue

            account_info = self.get_account_info(
                account_uri
            )

            self.account.append(
                account_info
            )

        return self.account

    def get_account_info(self, uri):
        info = {}
        info['__Output'] = {}
        info['Uri'] = uri

        data = self.get_properties(uri)

        info['id'] = self.get_property_value(
            data,
            'Id'
        )

        info['role_id'] = self.get_property_value(
            data,
            'RoleId'
        )

        info['name'] = self.get_property_value(
            data,
            'Name'
        )

        info['description'] = self.get_property_value(
            data,
            'Description'
        )

        info['username'] = self.get_property_value(
            data,
            'UserName'
        )

        info['enabled'] = self.get_property_value(
            data,
            'Enabled'
        )

        if info['enabled']:
            info['enabledTick'] = '\u2713'
            info['__Output']['enabledTick'] = 'Green'
        else:
            info['enabledTick'] = '\u2717'
            info['__Output']['enabledTick'] = 'Red'

        info['change_required'] = self.get_property_value(
            data,
            'PasswordChangeRequired'
        )

        if info['change_required']:
            info['changeTick'] = '\u2713'
            info['__Output']['changeTick'] = 'Red'
        else:
            info['changeTick'] = '\u2717'
            info['__Output']['changeTick'] = 'Green'

        info['type'] = self.get_property_value(
            data,
            'AccountTypes'
        )

        return info

    def get_template_account_properties(self, role_info=False, include_disabled=False, cache_enabled=True):
        all_accounts = self.get_account_mo(cache_enabled=cache_enabled)
        if all_accounts is None:
            return None

        accounts = []
        for account in all_accounts:
            if not account['enabled'] and not include_disabled:
                continue

            if role_info:
                account_role_info = self.get_role_by_id(
                    account['role_id']
                )
                if account_role_info is None:
                    account['privileges'] = []
                    account['oem'] = []
                else:
                    account['privileges'] = account_role_info['privileges']
                    account['oem'] = account_role_info['oem']

            accounts.append(
                account
            )

        return accounts

    def get_accounts_with_role_id(self, role_id):
        accounts = self.get_template_account_properties()
        role_accounts = []
        for account in accounts:
            if account['role_id'] == role_id:
                role_accounts.append(
                    account
                )
        return role_accounts
