import json
import time
import traceback
import requests

from lib.redfish.common import RedfishEndpointCommon
from lib.redfish.fi.inventory import RedfishEndpointFabricInterconnectInventory
from lib.redfish.fi.templates import RedfishEndpointFabricInterconnectTemplates

# mypy: ignore-errors
requests.packages.urllib3.disable_warnings()


class RedfishEndpointFabricInterconnect(
        RedfishEndpointCommon, 
        RedfishEndpointFabricInterconnectInventory, 
        RedfishEndpointFabricInterconnectTemplates
    ):
    def __init__(
            self,
            endpoint_handler,
            endpoint_ip,
            endpoint_port,
            redfish_username,
            redfish_password,
            auto_connect=True,
            get_timeout=10,
            ssl_verify=False,
            deep_search_exlusions=True,
            log_id=None
            ):
        self.session_connected = False

        RedfishEndpointCommon.__init__(
            self,
            endpoint_handler,
            endpoint_ip,
            endpoint_port,
            redfish_username,
            redfish_password,
            auto_connect=auto_connect,
            get_timeout=get_timeout,
            ssl_verify=ssl_verify,
            deep_search_exlusions=deep_search_exlusions,
            log_id=log_id
        )
        RedfishEndpointFabricInterconnectInventory.__init__(
            self
        )
        RedfishEndpointFabricInterconnectTemplates.__init__(
            self
        )

        self.endpoint_type = 'fi'
        self.session_id = None
        self.session_token = None
        if auto_connect:
            self.connect()

    def __del__(self):
        self.disconnect()

    def get_chassis_type(self):
        uri = '/redfish/v1/Chassis'
        children = self.endpoint_handler.get_odata_ids(uri)
        if children is None:
            self.log.error(
                'get_chassis_type',
                'Failed to discover Chassis: %s' % (uri)
            )
            return None

        for child in children:
            if child == uri:
                continue

            properties = self.get_properties(child)
            if properties is not None:
                if 'ChassisType' in properties:
                    if properties['ChassisType'] in ['Blade', 'Enclosure']:
                        return 'Blade'

        return 'Rack'
    
    def get_excluded_tree_uri(self):
        if not self.deep_search_exclusions:
            return []

        uri = [
            '/api-explorer/resources/redfish/v1/JsonSchemas',
            '/api-explorer/resources/redfish/v1/TaskService'
        ]

        return uri

    def path_fixup(self, path):
        if path.startswith('/redfish/v1/'):
            path = path.lstrip('/redfish/v1/')

        if not path.startswith('/api-explorer/resources/redfish/v1'):
            path = '/api-explorer/resources/redfish/v1/%s' % (
                path.lstrip('/')
            )

        if 'SYSTEM_ID' in path:
            system_id = self.get_system_id()
            if system_id is None:
                self.log.error('get_properties', 'System ID not found')
                return None

            path = path.replace(
                'SYSTEM_ID',
                system_id
            )

        return path

    def get_properties(self, path, properties=[], fixup=True, inventory_type=None, inventory_id=None):
        if not self.is_connected():
            return None

        if fixup:
            path = self.path_fixup(path)

        start_time = int(time.time() * 1000)
        try:
            url = 'https://%s/%s' % (
                self.endpoint_ip,
                path
            )

            headers = {}
            if len(self.inventory_type) > 0 and len(self.inventory_id) > 0:
                headers['Inventory-Type'] = self.inventory_type
                headers['Inventory-Id'] = self.inventory_id

            if inventory_type is not None:
                headers['Inventory-Type'] = inventory_type

            if inventory_id is not None:
                headers['Inventory-Id'] = inventory_id

            response = self.session_handler.get(
                url,
                headers=headers,
                verify=self.ssl_verify,
                timeout=self.get_timeout
            )

        except BaseException:
            self.log.error(
                'get_properties',
                'Redfish get object exception: %s %s' % (self.endpoint_ip, path)
            )

            self.log.error(
                'get_properties',
                traceback.format_exc()
            )

            end_time = int(time.time() * 1000)
            duration_ms = end_time - start_time
            self.log.redfish(
                '%s:%s' % (self.endpoint_ip, path),
                False,
                duration_ms
            )

            return None

        if response.status_code > 299:
            self.log.error(
                'get_properties',
                'Redfish get object failed: %s %s %s %s' % (
                    self.endpoint_ip,
                    path,
                    response.status_code,
                    str(response.content)
                )
            )

            end_time = int(time.time() * 1000)
            duration_ms = end_time - start_time
            self.log.redfish(
                '%s:%s' % (self.endpoint_ip, path),
                False,
                duration_ms
            )

            return None

        try:
            all_properties = response.json()
        except BaseException:
            self.log.error(
                'get_properties',
                'Redfish get object json exception: %s %s' % (self.endpoint_ip, path)
            )

        end_time = int(time.time() * 1000)
        duration_ms = end_time - start_time
        self.log.redfish(
            '%s:%s' % (self.endpoint_ip, path),
            True,
            duration_ms
        )

        if properties is None or len(properties) == 0:
            self.log.debug(
                'get_properties',
                'Redfish get %s in %s ms' % (path, duration_ms)
            )
            self.log.odata(
                path,
                all_properties
            )
            return all_properties

        selected_properties = {}
        for key in properties:
            if key in all_properties:
                selected_properties[key] = all_properties[key]

        self.log.debug(
            'get_properties',
            'Redfish get %s in %s ms' % (path, duration_ms)
        )
        self.log.odata(
            path,
            selected_properties
        )

        return selected_properties

    def is_connected(self):
        return self.session_connected

    def connect(self):
        if self.session_handler is not None:
            return True

        start_time = int(time.time() * 1000)
        self.session_handler = requests.Session()

        url = 'https://%s/Login' % (self.endpoint_ip)
        data = {}
        data['User'] = self.redfish_username
        data['Password'] = self.redfish_password

        try:
            response = self.session_handler.post(
                url,
                data=json.dumps(data),
                verify=self.ssl_verify
            )
            
            self.session_id = response.json()['SessionId']
            self.session_token = response.headers['X-Csrf-Token']
            
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

        self.session_connected = True

        end_time = int(time.time() * 1000)
        duration_ms = end_time - start_time
        self.log.debug(
            'get_properties',
            'Redfish connected to %s in %s ms' % (self.endpoint_ip, duration_ms)
        )
        self.log.redfish(
            'connect %s' % (self.endpoint_ip),
            True,
            duration_ms
        )

        return True

    def disconnect(self):
        if self.session_handler is None:
            return True

        start_time = int(time.time() * 1000)
        url = 'https://%s/Logout' % (
            self.endpoint_ip
        )
        headers = {}
        headers['X-Csrf-Token'] = self.session_token

        success = True
        try:
            response = self.session_handler.post(
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
            success = False

        if not success:
            self.session_handler = requests.Session()
            try:
                response = self.session_handler.post(
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

        self.session_connected = False
        self.session_handler = None

        end_time = int(time.time() * 1000)
        duration_ms = end_time - start_time
        self.log.debug(
            'get_properties',
            'Redfish disconnected from %s in %s ms' % (self.endpoint_ip, duration_ms)
        )
        self.log.redfish(
            'disconnect %s' % (self.endpoint_ip),
            True,
            duration_ms
        )

        return True

    def get_virtual_media(self, virtual_media_id=0):
        path = 'Managers/CIMC/VirtualMedia/%s' % (virtual_media_id)
        response = self.get_properties(path)
        return response

    def is_virtual_media_defined(self, virtual_media_id=0):
        response = self.get_virtual_media(virtual_media_id=virtual_media_id)
        if response is None:
            return False

        if response['ConnectedVia'] == 'NotConnected':
            return False

        return True

    def is_virtual_media_inserted(self, virtual_media_id=0):
        response = self.get_virtual_media(virtual_media_id=virtual_media_id)
        if response is None:
            return False
        return response['Inserted']

    def wait_virtual_media_inserted(self, virtual_media_id=0, timeout=30):
        start_time = int(time.time())
        while True:
            if self.is_virtual_media_inserted(virtual_media_id=virtual_media_id):
                return True

            time.sleep(5)

            if int(time.time()) - start_time > timeout:
                return False

    def insert_media_http(self, iso_url, virtual_media_id=0, protocol='HTTP', safe=True, fixup=True):
        if safe:
            if self.is_virtual_media_defined(virtual_media_id=virtual_media_id):
                if not self.eject_media(virtual_media_id=virtual_media_id):
                    return False

        path = '/redfish/v1/Managers/CIMC/VirtualMedia/%s/Actions/VirtualMedia.InsertMedia' % (virtual_media_id)
        if fixup:
            path = self.path_fixup(path)

        url = 'https://%s:%s%s' % (self.endpoint_ip, self.endpoint_port, path)

        data = {}
        data['Image'] = iso_url
        data['WriteProtected'] = True
        data['TransferProtocolType'] = protocol
        data['TransferMethod'] = 'Stream'
        data['Inserted'] = True

        return self.post(url, data=data)

    def eject_media(self, virtual_media_id=0, fixup=True):
        path = '/redfish/v1/Managers/CIMC/VirtualMedia/%s/Actions/VirtualMedia.EjectMedia' % (virtual_media_id)
        if fixup:
            path = self.path_fixup(path)

        url = 'https://%s:%s%s' % (self.endpoint_ip, self.endpoint_port, path)
        data = {}
        return self.post(url, data=data)

    def get_boot_properties(self):
        system_id = self.get_system_id()
        path = 'Systems/%s' % (system_id)
        response = self.get_properties(path)
        if response is None or 'Boot' not in response:
            return None
        return response['Boot']

    def set_one_time_boot_source(self, target, enabled='Once', fixup=True):
        system_id = self.get_system_id()
        path = '/redfish/v1/Systems/%s' % (system_id)
        if fixup:
            path = self.path_fixup(path)
        url = 'https://%s:%s%s' % (self.endpoint_ip, self.endpoint_port, path)

        data = {}
        data['Boot'] = {}
        data['Boot']['BootSourceOverrideTarget'] = target
        data['Boot']['BootSourceOverrideEnabled'] = enabled

        return self.patch(url, data=data)

    def get_power_state(self):
        path = 'Systems/%s' % (self.get_system_id())
        response = self.get_properties(path)
        if response is None or 'PowerState' not in response:
            return None

        return response['PowerState']

    def is_power_on(self):
        power_state = self.get_power_state()
        if power_state is None or power_state != "On":
            return False
        return True

    def power_cycle(self, fixup=True):
        system_id = self.get_system_id()
        path = '/redfish/v1/Systems/%s/Actions/ComputerSystem.Reset' % (system_id)
        if fixup:
            path = self.path_fixup(path)
        
        url = 'https://%s:%s%s' % (self.endpoint_ip, self.endpoint_port, path)

        data = {}
        data['ResetType'] = 'PowerCycle'

        return self.post(url, data=data)

    def get_system_actions(self):
        system_id = self.get_system_id()
        path = 'Systems/%s' % (system_id)
        response = self.get_properties(path)
        if response is None or 'Actions' not in response:
            return None
        return response['Actions']

    def power_restart(self, graceful=False, fixup=True):
        system_id = self.get_system_id()
        path = '/redfish/v1/Systems/%s/Actions/ComputerSystem.Reset' % (system_id)
        if fixup:
            path = self.path_fixup(path)
        
        url = 'https://%s:%s%s' % (self.endpoint_ip, self.endpoint_port, path)

        data = {}
        if graceful:
            data['ResetType'] = 'GracefulRestart'
        else:
            data['ResetType'] = 'ForceRestart'

        return self.post(url, data=data)

    def power_on(self, fixup=True):
        system_id = self.get_system_id()
        path = '/redfish/v1/Systems/%s/Actions/ComputerSystem.Reset' % (system_id)
        if fixup:
            path = self.path_fixup(path)
        
        url = 'https://%s:%s%s' % (self.endpoint_ip, self.endpoint_port, path)

        data = {}
        data['ResetType'] = 'On'

        return self.post(url, data=data)

    def power_off(self, gracefull=False, fixup=True):
        system_id = self.get_system_id()
        path = '/redfish/v1/Systems/%s/Actions/ComputerSystem.Reset' % (system_id)
        if fixup:
            path = self.path_fixup(path)
        
        url = 'https://%s:%s%s' % (self.endpoint_ip, self.endpoint_port, path)

        data = {}

        if gracefull:
            data['ResetType'] = 'GracefulShutdown'
        else:
            data['ResetType'] = 'ForceOff'

        return self.post(url, data=data)

    def post(self, url, data=None):
        if self.session_handler is None:
            return False

        start_time = int(time.time() * 1000)

        headers = {}
        headers['X-Csrf-Token'] = self.session_token
        if len(self.inventory_type) > 0 and len(self.inventory_id) > 0:
            headers['Inventory-Type'] = self.inventory_type
            headers['Inventory-Id'] = self.inventory_id

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

    def patch(self, url, data=None):
        if self.session_handler is None:
            return False

        start_time = int(time.time() * 1000)

        headers = {}
        headers['X-Csrf-Token'] = self.session_token
        if len(self.inventory_type) > 0 and len(self.inventory_id) > 0:
            headers['Inventory-Type'] = self.inventory_type
            headers['Inventory-Id'] = self.inventory_id

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

    def delete(self, url):
        if self.session_handler is None:
            return False

        start_time = int(time.time() * 1000)

        headers = {}
        headers['X-Csrf-Token'] = self.session_token
        if len(self.inventory_type) > 0 and len(self.inventory_id) > 0:
            headers['Inventory-Type'] = self.inventory_type
            headers['Inventory-Id'] = self.inventory_id

        try:
            response = self.session_handler.delete(
                url,
                headers=headers,
                verify=self.ssl_verify
            )

        except BaseException:
            self.log.error(
                'patch',
                'Redfish exception: %s' % (self.endpoint_ip)
            )

            self.log.error(
                'delete',
                traceback.format_exc()
            )

            end_time = int(time.time() * 1000)
            duration_ms = end_time - start_time
            self.log.redfish(
                'delete %s' % (self.endpoint_ip),
                False,
                duration_ms
            )

            return False

        if response.status_code >= 300:
            self.log.error(
                'delete',
                'Redfish failed: %s %s %s' % (
                    self.endpoint_ip,
                    response.status_code,
                    str(response.content)
                )
            )

            end_time = int(time.time() * 1000)
            duration_ms = end_time - start_time
            self.log.redfish(
                'delete %s' % (self.endpoint_ip),
                False,
                duration_ms
            )

            return False

        end_time = int(time.time() * 1000)
        duration_ms = end_time - start_time
        self.log.debug(
            'delete',
            'Redfish delete successful to %s in %s ms' % (self.endpoint_ip, duration_ms)
        )
        self.log.debug(
            'delete',
            '%s %s %s' % (
                url,
                response.status_code,
                str(response.content)
            )
        )
        self.log.redfish(
            'delete %s' % (self.endpoint_ip),
            True,
            duration_ms
        )

        return True

