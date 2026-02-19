import json
import time
import traceback
import requests


class Api():
    def __init__(self, cnc_ip, cnc_port, username, password, timeout=2000):
        self.cnc_ip = cnc_ip
        self.cnc_port = cnc_port
        self.cnc_username = username
        self.cnc_password = password
        self.timeout = timeout

        self.session_connected = False
        self.ticket = None
        self.token = None
        self.request_info = {}

    def __del__(self):
        self.disconnect()

    def get_cnc_ip(self):
        return self.cnc_ip

    def get_request_info(self):
        return self.request_info

    def get_token(self, generate_if_none=False):
        if generate_if_none and self.token is None:
            self.generate_token()
        return self.token

    def generate_token(self):
        url = "https://%s:%s/crosswork/sso/v1/tickets" % (
            self.cnc_ip,
            self.cnc_port
        )

        payload = {
            "username": self.cnc_username,
            "password": self.cnc_password
        }

        headers = {
            "Accept": "text/plain"
        }

        requests.packages.urllib3.disable_warnings()
        start_time = int(time.time() * 1000)
        try:
            response = requests.post(
                url,
                data=payload,
                headers=headers,
                verify=False,
                timeout=self.timeout
            )
            if response.status_code == 201:
                self.ticket = response.text

                url = "https://%s:%s/crosswork/sso/v1/tickets/%s" % (
                    self.cnc_ip,
                    self.cnc_port,
                    self.ticket
                )
                payload = {
                    "service": "https://%s:%s/app-dashboard" % (
                        self.cnc_ip,
                        self.cnc_port
                    )
                }

                response = requests.post(
                    url,
                    data=payload,
                    headers=headers,
                    verify=False,
                    timeout=self.timeout
                )
                if response.status_code == 200:
                    self.token = "Bearer %s" % (response.text)
                    self.session_connected = True
                else:
                    self.log.error(
                        'cnc.connect',
                        'Failed to get token [%s]: %s' % (
                            response.status_code,
                            response.text
                        )
                    )
                    self.session_connected = False

            else:
                self.log.error(
                    'cnc.connect',
                    'Failed to get ticket url [%s] username [%s] password [%s] code [%s]: %s' % (
                        url,
                        self.cnc_username,
                        self.cnc_password,
                        response.status_code,
                        response.text
                    )
                )
                self.session_connected = False

        except BaseException:
            self.log.error(
                'cnc.connect',
                traceback.format_exc()
            )
            self.session_connected = False

        end_time = int(time.time() * 1000)
        duration_ms = end_time - start_time
        self.log.cnc(
            'connect %s:%s' % (
                self.cnc_ip,
                self.cnc_port
            ),
            self.session_connected,
            duration_ms
        )

    def is_connected(self):
        if self.token is None:
            self.generate_token()
            if self.token is None:
                return False

        return True

    def disconnect(self):
        if self.ticket is None:
            return

        requests.packages.urllib3.disable_warnings()
        start_time = int(time.time() * 1000)

        url = "https://%s:%s/crosswork/sso/v1/tickets/%s" % (
            self.cnc_ip,
            self.cnc_port,
            self.ticket
        )
        headers = {
            "Authorization": self.token
        }

        try:
            response = requests.delete(
                url,
                headers=headers,
                verify=False,
                timeout=self.timeout
            )
            self.session_connected = False

            if response.status_code >= 300:
                self.log.error(
                    'cnc.disconnect',
                    'Failed to disconnect url [%s] code [%s]: %s' % (
                        url,
                        response.status_code,
                        response.text
                    )
                )

        except BaseException:
            self.log.error(
                'cnc.disconnect',
                traceback.format_exc()
            )
            self.session_connected = False
            self.my_output.error(
                'Failed to disconnect: %s:%s' % (
                    self.cnc_ip,
                    self.cnc_port
                )
            )

        end_time = int(time.time() * 1000)
        duration_ms = end_time - start_time
        self.log.cnc(
            'disconnect %s:%s' % (
                self.cnc_ip,
                self.cnc_port
            ),
            self.session_connected,
            duration_ms
        )

    def get_resource(self, location):
        self.request_info = {}
        self.request_info['url'] = '--'
        self.request_info['status_code'] = '--'
        self.request_info['duration'] = '--'
        self.request_info['error'] = None
        self.request_info['connected'] = True

        if not self.is_connected():
            self.request_info['connected'] = False
            self.log.error(
                'cnc.get_resource',
                'Connection to CNC failed'
            )
            return None

        url = "https://%s:%s%s" % (
            self.cnc_ip,
            self.cnc_port,
            location
        )
        headers = {
            "Authorization": self.token,
            "Accept": "application/json"
        }

        requests.packages.urllib3.disable_warnings()
        start_time = int(time.time() * 1000)
        success = True
        try:
            self.request_info['url'] = url
            response = requests.get(
                url,
                headers=headers,
                verify=False,
                timeout=self.timeout
            )
            self.request_info['status_code'] = response.status_code
            if response.status_code >= 300:
                self.log.error(
                    'cnc.get_resource',
                    'Url %s response code %s' % (
                        url,
                        response.status_code
                    )
                )

                self.log.error(
                    'cnc.get_resource',
                    'Url %s response %s' % (
                        url,
                        response.content
                    )
                )

                self.request_info['error'] = response.content.decode('utf-8')
                success = False
                response = None

            if response is not None:
                response = response.json()

        except BaseException:
            self.log.error(
                'cnc.get_resource',
                traceback.format_exc()
            )
            response = None
            success = False

        end_time = int(time.time() * 1000)
        duration_ms = end_time - start_time
        self.request_info['duration'] = duration_ms

        log_info = '%s:%s resource %s' % (
            self.cnc_ip,
            self.cnc_port,
            location
        )

        self.log.cnc(
            log_info,
            success,
            duration_ms
        )

        return response

    def get_value(self, managed_object, key, default):
        if key not in managed_object:
            return default

        return managed_object[key]
