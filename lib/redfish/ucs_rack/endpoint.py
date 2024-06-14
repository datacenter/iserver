import time

from lib.redfish.standard.endpoint import RedfishEndpointStandard
from lib.redfish.ucs_rack.account.main import RedfishEndpointUcsRackAccount
from lib.redfish.ucs_rack.template.main import RedfishEndpointUcsRackTemplate


class RedfishEndpointUcsRack(
        RedfishEndpointStandard,
        RedfishEndpointUcsRackAccount,
        RedfishEndpointUcsRackTemplate
        ):
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
        RedfishEndpointStandard.__init__(
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
        RedfishEndpointUcsRackAccount.__init__(self)
        RedfishEndpointUcsRackTemplate.__init__(
            self,
            endpoint_handler
        )

        self.endpoint_type = 'ucsc'
        self.default_chassis_uri = '/redfish/v1/Chassis/1'
        self.chassis_uri = None

    def __del__(self):
        self.disconnect()

    def get_chassis_uri(self):
        if self.chassis_uri is not None:
            return self.chassis_uri

        uri = '/redfish/v1/Chassis'
        children = self.endpoint_handler.get_odata_ids(uri)
        if children is None:
            self.log.error(
                'get_chassis_uri',
                'Failed to discover Chassis: %s' % (uri)
            )
            return self.default_chassis_uri

        chassis_uri = None
        for child in children:
            if child == uri:
                continue

            leaf = child.split('/')[-1]
            if leaf == 'CMC':
                continue

            chassis_uri = child
            break

        if chassis_uri is None:
            self.log.error(
                'get_chassis_uri',
                'Failed to find Chassis: %s' % (uri)
            )
            return self.default_chassis_uri

        self.chassis_uri = chassis_uri
        return chassis_uri

    def get_excluded_tree_uri(self):
        if not self.deep_search_exclusions:
            return []

        system_id = self.get_system_id()

        uri = [
            '/redfish/v1/JsonSchemas',
            '%s/LogServices' % (self.get_chassis_uri()),
            '/redfish/v1/Chassis/CMC/LogServices',
            '/redfish/v1/SessionService',
            '/redfish/v1/Managers/CIMC/LogServices',
            '/redfish/v1/Systems/%s/LogServices' % (system_id)
        ]

        return uri

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

    def insert_media_http(self, iso_url, virtual_media_id=0, protocol='HTTP', safe=True):
        if safe:
            if self.is_virtual_media_defined(virtual_media_id=virtual_media_id):
                if not self.eject_media(virtual_media_id=virtual_media_id):
                    return False

        url = 'https://%s:%s/redfish/v1/Managers/CIMC/VirtualMedia/%s/Actions/VirtualMedia.InsertMedia' % (self.endpoint_ip, self.endpoint_port, virtual_media_id)

        data = {}
        data['Image'] = iso_url
        data['WriteProtected'] = True
        data['TransferProtocolType'] = protocol
        data['TransferMethod'] = 'Stream'
        data['Inserted'] = True

        return self.post(url, data=data)

    def eject_media(self, virtual_media_id=0):
        url = 'https://%s:%s/redfish/v1/Managers/CIMC/VirtualMedia/%s/Actions/VirtualMedia.EjectMedia' % (self.endpoint_ip, self.endpoint_port, virtual_media_id)
        return self.post(url)

    def set_one_time_boot_source(self, target):
        system_id = self.get_system_id()
        url = 'https://%s:%s/redfish/v1/Systems/%s' % (self.endpoint_ip, self.endpoint_port, system_id)

        data = {}
        data['Boot'] = {}
        data['Boot']['BootSourceOverrideTarget'] = target
        data['Boot']['BootSourceOverrideEnabled'] = 'Once'

        return self.patch(url, data=data)

    def power_cycle(self):
        system_id = self.get_system_id()
        url = 'https://%s:%s/redfish/v1/Systems/%s/Actions/ComputerSystem.Reset' % (self.endpoint_ip, self.endpoint_port, system_id)

        data = {}
        data['ResetType'] = 'PowerCycle'

        return self.post(url, data=data)
