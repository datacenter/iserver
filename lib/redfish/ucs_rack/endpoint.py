from lib.redfish.standard.endpoint import RedfishEndpointStandard
from lib.redfish.ucs_rack.template import RedfishEndpointUcsRackTemplate


class RedfishEndpointUcsRack(RedfishEndpointStandard, RedfishEndpointUcsRackTemplate):
    def __init__(self, endpoint_handler, endpoint_ip, endpoint_port, redfish_username, redfish_password, cache_filename=None, auto_connect=True, get_timeout=10, ssl_verify=False, deep_search_exlusions=True, log_id=None, verbose=False, debug=False):
        RedfishEndpointStandard.__init__(
            self,
            endpoint_handler,
            endpoint_ip,
            endpoint_port,
            redfish_username,
            redfish_password,
            cache_filename=cache_filename,
            auto_connect=auto_connect,
            get_timeout=get_timeout,
            ssl_verify=ssl_verify,
            deep_search_exlusions=deep_search_exlusions,
            log_id=log_id,
            verbose=verbose,
            debug=debug
        )
        RedfishEndpointUcsRackTemplate.__init__(
            self
        )

        self.endpoint_type = 'ucsc'
        self.default_chassis_uri = '/redfish/v1/Chassis/1'
        self.chassis_uri = None

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
