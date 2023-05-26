import json
import time
import traceback
import requests


class Api():
    def __init__(self, apic_name, username, password):
        self.apic_name = apic_name
        self.apic_username = username
        self.apic_password = password

        self.session_connected = False
        self.token = None
        self.get_token()

    def get_apic_name(self):
        return self.apic_name

    def get_token(self):
        if self.token is not None:
            return

        url = "https://%s/api/aaaLogin.json" % (self.apic_name)

        payload = {
            "aaaUser": {
                "attributes": {
                    "name": self.apic_username,
                    "pwd": self.apic_password
                }
            }
        }

        headers = {
            "Content-Type": "application/json"
        }

        requests.packages.urllib3.disable_warnings()
        start_time = int(time.time() * 1000)
        try:
            response = requests.post(
                url,
                data=json.dumps(
                    payload
                ),
                headers=headers,
                verify=False
            ).json()
            self.token = response['imdata'][0]['aaaLogin']['attributes']['token']
            self.session_connected = True
        except BaseException:
            self.log.error(
                'apic.connect',
                traceback.format_exc()
            )
            self.session_connected = False
            self.my_output.error(
                'Failed to connect: %s' % (self.apic_name)
            )

        end_time = int(time.time() * 1000)
        duration_ms = end_time - start_time
        self.log.apic(
            'connect %s' % (self.apic_name),
            self.session_connected,
            duration_ms
        )

    def is_connected(self):
        if self.token is None:
            return False
        return True

    def get_mo_children_attributes(self, mo_name, managed_object, child_name):
        attributes = []
        if 'children' in managed_object[mo_name]:
            for child in managed_object[mo_name]['children']:
                for key in child:
                    if key == child_name:
                        attributes.append(
                            child[child_name]['attributes']
                        )
        return attributes

    def get_mo_child_attributes(self, mo_name, managed_object, child_name):
        if 'children' in managed_object[mo_name]:
            for child in managed_object[mo_name]['children']:
                for key in child:
                    if key == child_name:
                        return child[child_name]['attributes']
        return None

    def get_class(self, class_name, response_format='json', query_target_filter=None, query=None, node_class=False):
        if not self.is_connected():
            return None

        if node_class:
            url = "https://%s/api/node/class/%s.%s" % (
                self.apic_name,
                class_name,
                response_format
            )
        else:
            url = "https://%s/api/class/%s.%s" % (
                self.apic_name,
                class_name,
                response_format
            )

        if query is not None:
            url = '%s?%s' % (
                url,
                query
            )

        if query_target_filter is not None:
            url = '%s?query-target-filter=%s' % (
                url,
                query_target_filter
            )

        headers = {
            "Cookie": "APIC-Cookie=%s" % (self.token),
        }

        requests.packages.urllib3.disable_warnings()
        start_time = int(time.time() * 1000)
        success = True
        item_count = '-'
        try:
            response = requests.get(
                url,
                headers=headers,
                verify=False
            )
            if response.status_code >= 300:
                self.log.error(
                    'apic.get_class',
                    'Url %s response code %s' % (
                        url,
                        response.status_code
                    )
                )

                self.log.error(
                    'apic.get_class',
                    'Url %s response %s' % (
                        url,
                        response.content
                    )
                )

                success = False
                response = None

            if response is not None:
                if response_format == 'json':
                    response = response.json()
                    item_count = len(response['imdata'])
                else:
                    response = response.content

        except BaseException:
            self.log.error(
                'apic.get_class',
                traceback.format_exc()
            )
            response = None
            success = False

        end_time = int(time.time() * 1000)
        duration_ms = end_time - start_time

        log_info = '%s class %s' % (
            self.apic_name,
            class_name
        )
        if query_target_filter is not None:
            log_info = '%s filter %s' % (
                log_info,
                query_target_filter
            )
        if query is not None:
            log_info = '%s query %s' % (
                log_info,
                query
            )

        self.log.apic(
            log_info,
            success,
            duration_ms,
            item_count=item_count
        )

        return response

    def get_managed_object(self, distinguished_name, response_format='json', query_target_filter=None, query=None, node_mo=False):
        if not self.is_connected():
            return None

        if node_mo:
            url = "https://%s/api/node/mo/%s.%s" % (
                self.apic_name,
                distinguished_name,
                response_format
            )
        else:
            url = "https://%s/api/mo/%s.%s" % (
                self.apic_name,
                distinguished_name,
                response_format
            )

        if query is not None:
            url = '%s?%s' % (
                url,
                query
            )

        if query_target_filter is not None:
            url = '%s?query-target=%s' % (
                url,
                query_target_filter
            )

        headers = {
            "Cookie": "APIC-Cookie=%s" % (self.token),
        }

        start_time = int(time.time() * 1000)
        requests.packages.urllib3.disable_warnings()
        success = True
        item_count = None
        try:
            response = requests.get(
                url,
                headers=headers,
                verify=False
            )
            if response.status_code >= 300:
                self.log.error(
                    'apic.get_managed_object',
                    'Url %s response code %s' % (
                        url,
                        response.status_code
                    )
                )

                self.log.error(
                    'apic.get_managed_object',
                    'Url %s response %s' % (
                        url,
                        response.content
                    )
                )

                success = False
                response = None

            if response is not None:
                if response_format == 'json':
                    response = response.json()
                    item_count = len(response['imdata'])
                else:
                    response = response.content

        except BaseException:
            self.log.error(
                'apic.get_managed_object',
                traceback.format_exc()
            )
            response = None
            success = False

        end_time = int(time.time() * 1000)
        duration_ms = end_time - start_time

        log_info = '%s mo %s' % (
            self.apic_name,
            distinguished_name
        )
        if query_target_filter is not None:
            log_info = '%s filter %s' % (
                log_info,
                query_target_filter
            )
        if query is not None:
            log_info = '%s query %s' % (
                log_info,
                query
            )

        self.log.apic(
            log_info,
            success,
            duration_ms,
            item_count=item_count
        )

        return response
