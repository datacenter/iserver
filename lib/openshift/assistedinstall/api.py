class AssistedInstallApi():
    def __init__(self):
        self.assisted_install_url = 'assisted-install'

    def get_assisted_install_mo(self, url_suffix, extra_headers=None, params=None):
        url = '%s/%s' % (
            self.assisted_install_url,
            url_suffix
        )
        if self.api_handler is None:
            return None

        response = self.api_handler.get_query(url, extra_headers=extra_headers, params=params)
        return response

    def patch_assisted_install_mo(self, url_suffix, extra_headers=None, data=None, content_type='application/json'):
        url = '%s/%s' % (
            self.assisted_install_url,
            url_suffix
        )
        if self.api_handler is None:
            return None

        response = self.api_handler.patch_query(url, extra_headers=extra_headers, data=data, content_type=content_type)
        return response

    def post_assisted_install_mo(self, url_suffix, extra_headers=None, data=None):
        url = '%s/%s' % (
            self.assisted_install_url,
            url_suffix
        )
        if self.api_handler is None:
            return None

        response = self.api_handler.post_query(url, extra_headers=extra_headers, data=data)
        return response

    def delete_assisted_install_mo(self, url_suffix, extra_headers=None):
        url = '%s/%s' % (
            self.assisted_install_url,
            url_suffix
        )
        if self.api_handler is None:
            return None

        response = self.api_handler.delete_query(url, extra_headers=extra_headers)
        return response
