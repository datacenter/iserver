import time
import json
import traceback
import requests

from lib import log_helper


class Rest():
    def __init__(self, protocol, ip_address, port, username, password, restconf_enabled=True, log_id=None):
        self.log = log_helper.Log(log_id=log_id)

        self.session = requests.Session()
        if username is not None and password is not None:
            self.session.auth = (username, password)

        self.protocol = protocol
        self.ip_address = ip_address
        self.port = port
        self.restconf_enabled = restconf_enabled

        self.get_timeout = 15
        self.patch_timeout = 15
        self.post_timeout = 15
        self.put_timeout = 15
        self.delete_timeout = 15

    def format_url_rest(self, path, resource_type=None):
        if resource_type is None:
            if path is None:
                url = '%s://%s:%s/api' % (
                    self.protocol,
                    self.ip_address,
                    self.port
                )
            else:
                url = '%s://%s:%s/api/%s' % (
                    self.protocol,
                    self.ip_address,
                    self.port,
                    path
                )
        else:
            if path is None:
                url = '%s://%s:%s/api/%s' % (
                    self.protocol,
                    self.ip_address,
                    self.port,
                    resource_type
                )
            else:
                url = '%s://%s:%s/api/%s/%s' % (
                    self.protocol,
                    self.ip_address,
                    self.port,
                    resource_type,
                    path
                )

        return url

    def format_url_restconf(self, path, resource_type=None):
        if resource_type is None:
            if path is None:
                url = '%s://%s:%s/restconf' % (
                    self.protocol,
                    self.ip_address,
                    self.port
                )
            else:
                url = '%s://%s:%s/restconf/%s' % (
                    self.protocol,
                    self.ip_address,
                    self.port,
                    path
                )
        else:
            if path is None:
                url = '%s://%s:%s/restconf/data' % (
                    self.protocol,
                    self.ip_address,
                    self.port
                )
            else:
                url = '%s://%s:%s/restconf/data/%s' % (
                    self.protocol,
                    self.ip_address,
                    self.port,
                    path
                )

            if resource_type == 'operational':
                url = '%s?content=nonconfig' % (url)

        return url

    def format_url(self, path, resource_type=None):
        if self.restconf_enabled:
            return self.format_url_restconf(path, resource_type=resource_type)
        return self.format_url_rest(path, resource_type=resource_type)

    def get_headers_rest(self, header, media_type, output_format):
        if header == 'Accept':
            response = {}
            response['Accept'] = '%s+%s' % (media_type, output_format)
            return response

        if header == 'Content-Type':
            response = {}
            response['Content-Type'] = '%s+%s' % (media_type, output_format)
            return response

        self.log.error(
            'get_headers',
            'Unsupported header: %s' % (header)
        )
        return None

    def get_headers_restconf(self, header, media_type, output_format):
        if header == 'Accept':
            if media_type == 'application/vnd.yang.data':
                media_type = 'application/yang-data'

            response = {}
            response['Accept'] = '%s+%s' % (media_type, output_format)
            return response

        if header == 'Content-Type':
            if media_type == 'application/vnd.yang.data':
                media_type = 'application/yang-data'

            response = {}
            response['Content-Type'] = '%s+%s' % (media_type, output_format)
            return response

        self.log.error(
            'nso.get_headers',
            'Unsupported header: %s' % (header)
        )
        return None

    def get_headers(self, header, media_type, output_format):
        if self.restconf_enabled:
            return self.get_headers_restconf(header, media_type, output_format)
        return self.get_headers_rest(header, media_type, output_format)

    def format_error_message(self, response):
        try:
            message = response.json()['errors']['error'][0]['error-message']
        except KeyError:
            message = 'Failed to make request or error not returned as expected'
        except BaseException:
            message = 'Failed to make request or error not returned as expected'

        error_message = 'Error code %s: %s' % (response.status_code, message)
        return error_message

    def get_rest(self, output_format, resource_type, header, media_type, path=None, params=None, trace=None):
        url = self.format_url(path, resource_type=resource_type)
        headers = self.get_headers(header, media_type, output_format)

        success = True
        content = None
        try:
            self.log.debug(
                'nso.get_rest',
                url
            )
            self.log.debug(
                'nso.get_rest',
                headers
            )
            self.log.debug(
                'nso.get_rest',
                params
            )
            rest_response = self.session.get(
                url,
                headers=headers,
                params=params,
                timeout=self.get_timeout
            )

            self.log.debug(
                'nso.get_rest',
                'Response code: %s' % (rest_response.status_code)
            )

            if rest_response.status_code == 204:
                content = None
                self.log.debug(
                    'nso.get_rest',
                    'Content set to none based on status code'
                )
            else:
                if output_format == 'json':
                    content = rest_response.json()
                else:
                    content = rest_response.content.decode('utf-8')

            rest_response.raise_for_status()

        except requests.HTTPError as err:
            success = False
            self.log.error(
                'nso.get_rest',
                'HTTPError exception: %s' % (url)
            )
            self.log.error(
                'nso.get_rest',
                'Status code: %s' % (err.response.status_code)
            )
            self.log.error(
                'nso.get_rest',
                err.response.text
            )

        except BaseException:
            success = False
            self.log.error(
                'nso.get_rest',
                'HTTPError exception: %s' % (url)
            )
            self.log.error(
                'nso.get_rest',
                traceback.format_exc()
            )

        if success:
            self.trace_rest(
                trace,
                'GET',
                url,
                headers,
                None,
                params,
                rest_response.status_code,
                content
            )

        return success, content

    def post_rest(self, output_format, resource_type, header, media_type, data, path=None, params=None, timeout=None, trace=None):
        url = self.format_url(path, resource_type=resource_type)
        headers = self.get_headers(header, media_type, output_format)

        if timeout is None:
            timeout = self.post_timeout

        success = True
        content = None
        try:
            # curl
            #     -X POST
            #     --header "Content-Type:application/yang-data+xml"
            #     -u admin:admin
            #     -d @/tmp/ausf-vnfd.xml
            #     http://<ip>:8080/restconf/data/etsi-nfv-descriptors:nfv

            rest_response = self.session.post(
                url,
                headers=headers,
                data=data,
                params=params,
                timeout=timeout
            )

            if rest_response.status_code == 204:
                content = None
            else:
                if output_format == 'json':
                    content = rest_response.json()
                else:
                    content = rest_response.content.decode('utf-8')

            rest_response.raise_for_status()

        except requests.HTTPError as err:
            success = False
            self.log.error(
                'nso.post_rest',
                'HTTP Error exception: %s' % (url)
            )
            self.log.error(
                'nso.post_rest',
                'Status code: %s' % (err.response.status_code)
            )
            self.log.error(
                'nso.post_rest',
                err.response.text
            )

        except BaseException:
            success = False
            self.log.error(
                'nso.post_rest',
                traceback.format_exc()
            )

        self.trace_rest(
            trace,
            'POST',
            url,
            headers,
            data,
            params,
            rest_response.status_code,
            rest_response.text
        )

        return success, content

    def patch_rest(self, output_format, resource_type, header, media_type, data, path=None, params=None, timeout=None, trace=None):
        url = self.format_url(path, resource_type=resource_type)
        headers = self.get_headers(header, media_type, output_format)

        if timeout is None:
            timeout = self.patch_timeout

        success = True
        content = None
        try:
            rest_response = self.session.patch(
                url,
                headers=headers,
                data=data,
                params=params,
                timeout=timeout
            )

            if rest_response.status_code == 204:
                content = None
            else:
                if output_format == 'json':
                    content = rest_response.json()
                else:
                    content = rest_response.content.decode('utf-8')

            rest_response.raise_for_status()

        except requests.HTTPError as err:
            success = False
            self.log.error(
                'nso.patch_rest',
                'HTTPError exception: %s' % (url)
            )
            self.log.error(
                'nso.patch_rest',
                'Status code: %s' % (err.response.status_code)
            )
            self.log.error(
                'nso.patch_rest',
                err.response.text
            )

        except BaseException:
            success = False
            self.log.error(
                'nso.patch_rest',
                'Base exception: %s' % (url)
            )
            self.log.error(
                'nso._patch_rest',
                traceback.format_exc()
            )

        self.trace_rest(
            trace,
            'PATCH',
            url,
            headers,
            data,
            params,
            rest_response.status_code,
            rest_response.text
        )

        return success, content

    def put_rest(self, output_format, resource_type, header, media_type, data, path=None, params=None, timeout=None, trace=None):
        url = self.format_url(path, resource_type=resource_type)
        headers = self.get_headers(header, media_type, output_format)

        if timeout is None:
            timeout = self.put_timeout

        success = True
        content = None
        try:
            rest_response = self.session.put(
                url,
                headers=headers,
                data=data,
                params=params,
                timeout=timeout
            )

            if rest_response.status_code == 204:
                content = None
            else:
                if output_format == 'json':
                    content = rest_response.json()
                else:
                    content = rest_response.content.decode('utf-8')

            rest_response.raise_for_status()

        except requests.HTTPError as err:
            success = False
            self.log.error(
                'nso.put_rest',
                'HTTPError exception: %s' % (url)
            )
            self.log.error(
                'nso.put_rest',
                'Status code: %s' % (err.response.status_code)
            )
            self.log.error(
                'nso.put_rest',
                err.response.text
            )

        except BaseException:
            success = False
            content = None
            self.log.error(
                'nso.put_rest',
                'Base exception: %s' % (url)
            )
            self.log.error(
                'nso.put_rest',
                traceback.format_exc()
            )

        self.trace_rest(
            trace,
            'PUT',
            url,
            headers,
            data,
            params,
            rest_response.status_code,
            rest_response.text
        )

        return success, content

    def delete_rest(self, output_format, resource_type, header, media_type, path=None, params=None, trace=None):
        url = self.format_url(path, resource_type=resource_type)
        headers = self.get_headers(header, media_type, output_format)

        success = True
        content = None
        try:
            rest_response = self.session.delete(
                url,
                headers=headers,
                params=params,
                timeout=self.delete_timeout
            )

            if rest_response.status_code == 204:
                content = None
            else:
                if output_format == 'json':
                    content = rest_response.json()
                else:
                    content = rest_response.content.decode('utf-8')

            rest_response.raise_for_status()

        except requests.HTTPError as err:
            success = False
            self.log.error(
                'nso.delete_rest',
                'HTTPError exception: %s' % (url)
            )
            self.log.error(
                'nso.delete_rest',
                'Status code: %s' % (err.response.status_code)
            )
            self.log.error(
                'nso.delete_rest',
                err.response.text
            )

        except BaseException:
            success = False
            self.log.error(
                'nso.delete_rest',
                'HTTPError exception: %s' % (url)
            )
            self.log.error(
                'nso.delete_rest',
                traceback.format_exc()
            )

        self.trace_rest(
            trace,
            'DELETE',
            url,
            headers,
            None,
            params,
            rest_response.status_code,
            rest_response.text
        )

        return success, content

    def trace_rest(self, trace_filename, method, url, headers, data, params, response_code, response_data):
        if response_data is None:
            return

        if data is not None:
            try:
                data = data.decode('utf-8')
            except BaseException:
                data = str(data)

        timestamp = int(time.time() * 1000)
        message = {
            'timestamp': timestamp,
            'message': method,
            'url': url,
            'headers': headers,
            'data': data,
            'params': params,
            'response_code': response_code,
            'response_data': response_data
        }

        if trace_filename is not None:
            self.log.adhoc(
                trace_filename,
                json.dumps(message, indent=4)
            )

        else:
            self.log.adhoc(
                'nso.trace.%s' % (timestamp),
                json.dumps(
                    message,
                    indent=4
                )
            )
