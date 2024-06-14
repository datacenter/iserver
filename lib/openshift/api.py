import time
import traceback
import requests

from lib import log_helper


class Api():
    def __init__(self, token, log_id=None):
        self.authentication_token = token
        self.access_token = None
        self.access_token_timestamp = None
        self.access_token_ttl = 240

        self.authentication_request_timeout = 5
        self.get_request_timeout = 5
        self.patch_request_timeout = 5
        self.post_request_timeout = 5
        self.delete_request_timeout = 5

        self.log = log_helper.Log(log_id=log_id)

    def generate_access_token(self):
        url = 'https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token'
        headers = {}
        headers['Content-Type'] = 'application/x-www-form-urlencoded'

        data = {}
        data['grant_type'] = 'refresh_token'
        data['client_id'] = 'cloud-services'
        data['refresh_token'] = self.authentication_token

        requests.packages.urllib3.disable_warnings()
        start_time = int(time.time() * 1000)
        try:
            response = requests.post(
                url,
                data=data,
                headers=headers,
                verify=False,
                timeout=self.authentication_request_timeout
            )
            if response.status_code < 300:
                self.access_token = response.json()['access_token']
                self.access_token_timestamp = start_time
                authenticated = True

            if response.status_code >= 300:
                self.log.error(
                    'generate_access_token',
                    'Response code %s body %s' % (
                        response.status_code,
                        response.content.decode('utf-8')
                    )
                )
                authenticated = False
                self.access_token = None
                self.access_token_timestamp = None

        except BaseException:
            self.log.error(
                'generate_access_token',
                traceback.format_exc()
            )
            authenticated = False
            self.access_token = None
            self.access_token_timestamp = None

        end_time = int(time.time() * 1000)
        duration_ms = end_time - start_time
        self.log.openshift(
            'authenticate',
            authenticated,
            duration_ms
        )

    def is_access_token_valid(self):
        if self.access_token is None:
            return False

        if int(time.time() * 1000) - self.access_token_timestamp > self.access_token_ttl * 1000:
            return False

        return True

    def get_access_token(self):
        if self.is_access_token_valid():
            return self.access_token

        self.generate_access_token()
        return self.access_token

    def get_query(self, url_suffix, extra_headers=None, params=None):
        token = self.get_access_token()
        if token is None:
            self.log.error(
                'get_query',
                'Failed to get access token'
            )
            return None

        url = 'https://api.openshift.com/api/%s' % (url_suffix)

        headers = {}
        headers['Content-Type'] = 'application/json'
        headers['Authorization'] = 'Bearer %s' % (token)

        if extra_headers is not None:
            for key in extra_headers:
                headers[key] = extra_headers[key]

        requests.packages.urllib3.disable_warnings()
        start_time = int(time.time() * 1000)
        try:
            if params is not None:
                self.log.debug(
                    'get_query',
                    'URL [%s] Headers [%s] Params [%s]' % (
                        url,
                        headers,
                        params
                    )
                )
                response = requests.get(
                    url,
                    headers=headers,
                    params=params,
                    verify=False,
                    timeout=self.get_request_timeout
                )
            else:
                self.log.debug(
                    'get_query',
                    'URL [%s] Headers [%s]' % (
                        url,
                        headers
                    )
                )
                response = requests.get(
                    url,
                    headers=headers,
                    verify=False,
                    timeout=self.get_request_timeout
                )

            if response.status_code < 300:
                get_response = response.json()
                success = True

            if response.status_code >= 300:
                self.log.error(
                    'get_query',
                    'Response code %s body %s' % (
                        response.status_code,
                        response.content.decode('utf-8')
                    )
                )
                get_response = None
                success = False

        except BaseException:
            self.log.error(
                'get_query',
                traceback.format_exc()
            )
            get_response = None
            success = False

        end_time = int(time.time() * 1000)
        duration_ms = end_time - start_time
        self.log.openshift(
            url,
            success,
            duration_ms
        )

        return get_response

    def patch_query(self, url_suffix, extra_headers=None, data=None, content_type='application/json'):
        token = self.get_access_token()
        if token is None:
            self.log.error(
                'patch_query',
                'Failed to get access token'
            )
            return None

        url = 'https://api.openshift.com/api/%s' % (url_suffix)

        headers = {}
        headers['Content-Type'] = content_type
        headers['Authorization'] = 'Bearer %s' % (token)

        if extra_headers is not None:
            for key in extra_headers:
                headers[key] = extra_headers[key]

        requests.packages.urllib3.disable_warnings()
        start_time = int(time.time() * 1000)
        try:
            if data is not None:
                self.log.debug(
                    'patch_query',
                    'URL [%s]' % (
                        url
                    )
                )
                self.log.debug(
                    'patch_query',
                    'Headers [%s]' % (
                        headers
                    )
                )
                self.log.debug(
                    'patch_query',
                    'Payload [%s]' % (
                        data
                    )
                )
                response = requests.patch(
                    url,
                    headers=headers,
                    data=data,
                    verify=False,
                    timeout=self.patch_request_timeout
                )
            else:
                self.log.debug(
                    'patch_query',
                    'URL [%s]' % (
                        url
                    )
                )
                self.log.debug(
                    'patch_query',
                    'Headers [%s]' % (
                        headers
                    )
                )
                response = requests.post(
                    url,
                    headers=headers,
                    verify=False,
                    timeout=self.patch_request_timeout
                )

            if response.status_code < 300:
                try:
                    patch_response = response.json()
                except BaseException:
                    patch_response = 'non json response'
                success = True

            if response.status_code >= 300:
                self.log.error(
                    'patch_query',
                    'Response code %s body %s' % (
                        response.status_code,
                        response.content.decode('utf-8')
                    )
                )
                patch_response = None
                success = False

        except BaseException:
            self.log.error(
                'patch_query',
                traceback.format_exc()
            )
            patch_response = None
            success = False

        end_time = int(time.time() * 1000)
        duration_ms = end_time - start_time
        self.log.openshift(
            url,
            success,
            duration_ms
        )

        return patch_response

    def post_query(self, url_suffix, extra_headers=None, data=None):
        token = self.get_access_token()
        if token is None:
            self.log.error(
                'post_query',
                'Failed to get access token'
            )
            return None

        url = 'https://api.openshift.com/api/%s' % (url_suffix)

        headers = {}
        headers['Content-Type'] = 'application/json'
        headers['Authorization'] = 'Bearer %s' % (token)

        if extra_headers is not None:
            for key in extra_headers:
                headers[key] = extra_headers[key]

        requests.packages.urllib3.disable_warnings()
        start_time = int(time.time() * 1000)
        try:
            if data is not None:
                self.log.debug(
                    'post_query',
                    'URL [%s] Headers [%s] Payload [%s]' % (
                        url,
                        headers,
                        data
                    )
                )
                response = requests.post(
                    url,
                    headers=headers,
                    data=data,
                    verify=False,
                    timeout=self.post_request_timeout
                )
            else:
                self.log.debug(
                    'post_query',
                    'URL [%s] Headers [%s]' % (
                        url,
                        headers
                    )
                )
                response = requests.post(
                    url,
                    headers=headers,
                    verify=False,
                    timeout=self.post_request_timeout
                )

            if response.status_code < 300:
                post_response = response.json()
                success = True

            if response.status_code >= 300:
                self.log.error(
                    'post_query',
                    'Response code %s body %s' % (
                        response.status_code,
                        response.content.decode('utf-8')
                    )
                )
                post_response = None
                success = False

        except BaseException:
            self.log.error(
                'post_query',
                traceback.format_exc()
            )
            post_response = None
            success = False

        end_time = int(time.time() * 1000)
        duration_ms = end_time - start_time
        self.log.openshift(
            url,
            success,
            duration_ms
        )

        return post_response

    def delete_query(self, url_suffix, extra_headers=None):
        token = self.get_access_token()
        if token is None:
            self.log.error(
                'delete_query',
                'Failed to get access token'
            )
            return None

        url = 'https://api.openshift.com/api/%s' % (url_suffix)

        headers = {}
        headers['Content-Type'] = 'application/json'
        headers['Authorization'] = 'Bearer %s' % (token)

        if extra_headers is not None:
            for key in extra_headers:
                headers[key] = extra_headers[key]

        requests.packages.urllib3.disable_warnings()
        start_time = int(time.time() * 1000)
        try:
            self.log.debug(
                'delete_query',
                'URL [%s] Headers [%s]' % (
                    url,
                    headers
                )
            )
            response = requests.delete(
                url,
                headers=headers,
                verify=False,
                timeout=self.delete_request_timeout
            )

            if response.status_code < 300:
                success = True

            if response.status_code >= 300:
                self.log.error(
                    'delete_query',
                    'Response code %s body %s' % (
                        response.status_code,
                        response.content.decode('utf-8')
                    )
                )
                success = False

        except BaseException:
            self.log.error(
                'post_query',
                traceback.format_exc()
            )
            success = False

        end_time = int(time.time() * 1000)
        duration_ms = end_time - start_time
        self.log.openshift(
            url,
            success,
            duration_ms
        )

        return success
