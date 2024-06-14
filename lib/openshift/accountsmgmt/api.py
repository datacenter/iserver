class AccountsMgmtApi():
    def __init__(self):
        self.accounts_mgmt_url = 'accounts_mgmt'

    def get_accounts_mgmt_mo(self, url_suffix, extra_headers=None, params=None):
        url = '%s/%s' % (
            self.accounts_mgmt_url,
            url_suffix
        )
        if self.api_handler is None:
            return None

        response = self.api_handler.get_query(url, extra_headers=extra_headers, params=params)
        return response

    def post_accounts_mgmt_mo(self, url_suffix, extra_headers=None, data=None):
        url = '%s/%s' % (
            self.accounts_mgmt_url,
            url_suffix
        )
        if self.api_handler is None:
            return None

        response = self.api_handler.post_query(url, extra_headers=extra_headers, data=data)
        return response

    def delete_accounts_mgmt_mo(self, url_suffix, extra_headers=None):
        url = '%s/%s' % (
            self.accounts_mgmt_url,
            url_suffix
        )
        if self.api_handler is None:
            return None

        response = self.api_handler.delete_query(url, extra_headers=extra_headers)
        return response
