import json
import time
import traceback
import requests

from lib.redfish.common import RedfishEndpointCommon

# mypy: ignore-errors
requests.packages.urllib3.disable_warnings()


class RedfishEndpointStandard(RedfishEndpointCommon):
    def __init__(
            self,
            endpoint_handler,
            endpoint_ip,
            endpoint_port,
            redfish_username,
            redfish_password,
            system_id=None,
            cache_filename=None,
            auto_connect=True,
            get_timeout=10,
            ssl_verify=False,
            deep_search_exlusions=True,
            log_id=None
            ):
        RedfishEndpointCommon.__init__(
            self,
            endpoint_handler,
            endpoint_ip,
            endpoint_port,
            redfish_username,
            redfish_password,
            system_id=system_id,
            cache_filename=cache_filename,
            auto_connect=auto_connect,
            get_timeout=get_timeout,
            ssl_verify=ssl_verify,
            deep_search_exlusions=deep_search_exlusions,
            log_id=log_id
        )

        self.endpoint_type = 'standard'
        if auto_connect:
            self.connect()

    def __del__(self):
        self.disconnect()

    def extract_session_id(self, authentication_response):
        if 'Location' in authentication_response.headers:
            return authentication_response.headers['Location'].split('/')[-1]

        # {\n  "@odata.id":"/redfish/v1/SessionService/Sessions/5819",\n  "Description":"Session of user: admin",\n  "Name":"User Session #5819",\n  "Id":5819\n}
        try:
            content = json.loads(authentication_response.content.decode('utf-8'))
            return content['@odata.id'].split('/')[-1]
        except BaseException:
            pass

        return None

    def connect(self):
        if self.is_cache_enabled():
            return True

        if self.session_handler is not None:
            return True

        start_time = int(time.time() * 1000)
        self.session_handler = requests.Session()

        url = 'https://%s:%s/redfish/v1/SessionService/Sessions' % (self.endpoint_ip, self.endpoint_port)
        data = {}
        data['UserName'] = self.redfish_username
        data['Password'] = self.redfish_password

        try:
            response = self.session_handler.post(
                url,
                data=json.dumps(data),
                verify=self.ssl_verify
            )

        except BaseException:
            self.log.error(
                'connect',
                'Redfish authentication exception: %s' % (self.endpoint_ip)
            )

            self.log.error(
                'connect',
                traceback.format_exc()
            )

            end_time = int(time.time() * 1000)
            duration_ms = end_time - start_time
            self.log.redfish(
                'connect %s' % (self.endpoint_ip),
                False,
                duration_ms
            )

            return False

        if response.status_code >= 300:
            self.log.error(
                'connect',
                'Redfish authentication failed: %s %s %s' % (
                    self.endpoint_ip,
                    response.status_code,
                    str(response.content)
                )
            )

            end_time = int(time.time() * 1000)
            duration_ms = end_time - start_time
            self.log.redfish(
                'connect %s' % (self.endpoint_ip),
                False,
                duration_ms
            )

            return False

        self.session_id = self.extract_session_id(response)
        if self.session_id is None:
            self.log.error(
                'connect',
                'Failed to get session_id from authentication response'
            )
            self.log.debug(
                'connect',
                'Response headers: %s' % (str(response.headers))
            )
            self.log.debug(
                'connect',
                'Response content: %s' % (str(response.content))
            )
            return False

        self.session_token = response.headers['X-Auth-Token']

        end_time = int(time.time() * 1000)
        duration_ms = end_time - start_time
        self.log.debug(
            'connect',
            'Redfish connected to %s in %s ms' % (self.endpoint_ip, duration_ms)
        )
        self.log.redfish(
            'connect %s' % (self.endpoint_ip),
            True,
            duration_ms
        )

        return True

    def disconnect(self):
        if self.is_cache_enabled():
            return True

        if self.session_handler is None:
            return True

        start_time = int(time.time() * 1000)
        url = 'https://%s:%s/redfish/v1/SessionService/Sessions/%s' % (
            self.endpoint_ip,
            self.endpoint_port,
            self.session_id
        )
        headers = {}
        headers['X-Auth-Token'] = self.session_token

        success = True
        try:
            response = self.session_handler.delete(
                url,
                headers=headers,
                verify=self.ssl_verify
            )
        except BaseException:
            success = False

        if not success:
            try:
                self.session_handler = requests.Session()
                response = self.session_handler.delete(
                    url,
                    headers=headers,
                    verify=self.ssl_verify
                )
            except BaseException:
                self.log.error(
                    'disconnect',
                    'Redfish session close exception: %s' % (self.endpoint_ip)
                )

                self.log.error(
                    'disconnect',
                    traceback.format_exc()
                )

                end_time = int(time.time() * 1000)
                duration_ms = end_time - start_time
                self.log.redfish(
                    'disconnect %s' % (self.endpoint_ip),
                    False,
                    duration_ms
                )

                return False

        if response.status_code >= 300:
            self.log.error(
                'disconnect',
                'Redfish session close failed: %s %s %s' % (
                    self.endpoint_ip,
                    response.status_code,
                    str(response.content)
                )
            )

            end_time = int(time.time() * 1000)
            duration_ms = end_time - start_time
            self.log.redfish(
                'disconnect %s' % (self.endpoint_ip),
                False,
                duration_ms
            )

            return False

        self.session_handler = None
        self.session_id = None
        self.session_token = None

        end_time = int(time.time() * 1000)
        duration_ms = end_time - start_time
        self.log.debug(
            'disconnect',
            'Redfish disconnected from %s in %s ms' % (self.endpoint_ip, duration_ms)
        )
        self.log.redfish(
            'disconnect %s' % (self.endpoint_ip),
            True,
            duration_ms
        )

        return True

    def patch(self, url, data=None):
        if self.session_handler is None:
            return False

        start_time = int(time.time() * 1000)

        headers = {}
        headers['X-Auth-Token'] = self.session_token

        try:
            if data is None:
                response = self.session_handler.patch(
                    url,
                    headers=headers,
                    verify=self.ssl_verify
                )
            else:
                response = self.session_handler.patch(
                    url,
                    headers=headers,
                    data=json.dumps(data),
                    verify=self.ssl_verify
                )

        except BaseException:
            self.log.error(
                'patch',
                'Redfish exception: %s' % (self.endpoint_ip)
            )

            self.log.error(
                'patch',
                traceback.format_exc()
            )

            end_time = int(time.time() * 1000)
            duration_ms = end_time - start_time
            self.log.redfish(
                'patch %s' % (self.endpoint_ip),
                False,
                duration_ms
            )

            return False

        if response.status_code >= 300:
            self.log.error(
                'patch',
                'Redfish failed: %s %s %s' % (
                    self.endpoint_ip,
                    response.status_code,
                    str(response.content)
                )
            )

            end_time = int(time.time() * 1000)
            duration_ms = end_time - start_time
            self.log.redfish(
                'patch %s' % (self.endpoint_ip),
                False,
                duration_ms
            )

            return False

        end_time = int(time.time() * 1000)
        duration_ms = end_time - start_time
        self.log.debug(
            'patch',
            'Redfish patch successful to %s in %s ms' % (self.endpoint_ip, duration_ms)
        )
        self.log.debug(
            'patch',
            '%s %s %s' % (
                url,
                response.status_code,
                str(response.content)
            )
        )
        self.log.redfish(
            'patch %s' % (self.endpoint_ip),
            True,
            duration_ms
        )

        return True

    def post(self, url, data=None):
        if self.session_handler is None:
            return False

        start_time = int(time.time() * 1000)

        headers = {}
        headers['X-Auth-Token'] = self.session_token

        try:
            if data is None:
                response = self.session_handler.post(
                    url,
                    headers=headers,
                    verify=self.ssl_verify
                )
            else:
                response = self.session_handler.post(
                    url,
                    headers=headers,
                    data=json.dumps(data),
                    verify=self.ssl_verify
                )

        except BaseException:
            self.log.error(
                'post',
                'Redfish exception: %s' % (self.endpoint_ip)
            )

            self.log.error(
                'post',
                traceback.format_exc()
            )

            end_time = int(time.time() * 1000)
            duration_ms = end_time - start_time
            self.log.redfish(
                'post %s' % (self.endpoint_ip),
                False,
                duration_ms
            )

            return False

        if response.status_code >= 300:
            self.log.error(
                'post',
                'Redfish failed: %s %s %s' % (
                    self.endpoint_ip,
                    response.status_code,
                    str(response.content)
                )
            )

            end_time = int(time.time() * 1000)
            duration_ms = end_time - start_time
            self.log.redfish(
                'post %s' % (self.endpoint_ip),
                False,
                duration_ms
            )

            return False

        end_time = int(time.time() * 1000)
        duration_ms = end_time - start_time
        self.log.debug(
            'post',
            'Redfish post successful to %s in %s ms' % (self.endpoint_ip, duration_ms)
        )
        self.log.redfish(
            'post %s' % (self.endpoint_ip),
            True,
            duration_ms
        )

        return True
