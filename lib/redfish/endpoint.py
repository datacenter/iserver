import json

from lib import output_helper
from lib.redfish.cache import RedfishCache
from lib.redfish.ucs_rack import endpoint as ucs_rack_endpoint
from lib.redfish.standard import endpoint as standard_endpoint
from lib.redfish.fi import endpoint as fi_endpoint
from lib.redfish.dell import endpoint as dell_endpoint
from lib.redfish.hpe import endpoint as hpe_endpoint
from lib.redfish import tree


class RedfishEndpoint(RedfishCache):
    def __init__(
        self,
        endpoint_type,
        endpoint_ip,
        endpoint_port,
        redfish_username,
        redfish_password,
        cache_name=None,
        get_timeout=10,
        auto_connect=True,
        ssl_verify=False,
        deep_search_exlusions=True,
        tree_max_execution_time=0,
        log_id=None,
        verbose=False,
        debug=False
        ):

        RedfishCache.__init__(self, log_id=log_id)

        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=verbose,
            debug=debug
        )

        self.tree_max_execution_time = tree_max_execution_time
        self.endpoint_handler = None

        endpoint_cache_filename = None
        endpoint_cache_entry = None
        if endpoint_type == 'cache':
            endpoint_cache_entry = self.get_redfish_cache_entry(cache_name)
            if endpoint_cache_entry is None:
                raise ValueError('Unknown cache entry: %s' % (cache_name))

            endpoint_cache_filename = self.get_cache_resources_filename(cache_name)
            if endpoint_cache_filename is None or len(endpoint_cache_filename) == 0:
                raise ValueError('Unknown cache filename: %s' % (cache_name))

            endpoint_type = endpoint_cache_entry['EndpointType']
            endpoint_ip = endpoint_cache_entry['EndpointType']
            redfish_username = None
            redfish_password = None

        if endpoint_type == 'standard':
            self.endpoint_handler = standard_endpoint.RedfishEndpointStandard(
                self,
                endpoint_ip,
                endpoint_port,
                redfish_username,
                redfish_password,
                cache_filename=endpoint_cache_filename,
                auto_connect=auto_connect,
                get_timeout=get_timeout,
                ssl_verify=ssl_verify,
                deep_search_exlusions=deep_search_exlusions,
                log_id=log_id,
                verbose=verbose,
                debug=debug
            )

        if endpoint_type == 'ucsc':
            self.endpoint_handler = ucs_rack_endpoint.RedfishEndpointUcsRack(
                self,
                endpoint_ip,
                endpoint_port,
                redfish_username,
                redfish_password,
                cache_filename=endpoint_cache_filename,
                auto_connect=auto_connect,
                get_timeout=get_timeout,
                ssl_verify=ssl_verify,
                deep_search_exlusions=deep_search_exlusions,
                log_id=log_id,
                verbose=verbose,
                debug=debug
            )

        if endpoint_type == 'fi':
            self.endpoint_handler = fi_endpoint.RedfishEndpointFabricInterconnect(
                self,
                endpoint_ip,
                endpoint_port,
                redfish_username,
                redfish_password,
                cache_filename=endpoint_cache_filename,
                auto_connect=auto_connect,
                get_timeout=get_timeout,
                ssl_verify=ssl_verify,
                deep_search_exlusions=deep_search_exlusions,
                log_id=log_id,
                verbose=verbose,
                debug=debug
            )

            if endpoint_cache_entry is not None:
                self.endpoint_handler.set_inventory(
                    endpoint_cache_entry['EndpointInventoryType'],
                    endpoint_cache_entry['EndpointInventoryId']
                )

        if endpoint_type == 'dell':
            self.endpoint_handler = dell_endpoint.RedfishEndpointDell(
                self,
                endpoint_ip,
                endpoint_port,
                redfish_username,
                redfish_password,
                cache_filename=endpoint_cache_filename,
                auto_connect=auto_connect,
                get_timeout=get_timeout,
                ssl_verify=ssl_verify,
                deep_search_exlusions=deep_search_exlusions,
                log_id=log_id,
                verbose=verbose,
                debug=debug
            )

        if endpoint_type == 'hpe':
            self.endpoint_handler = hpe_endpoint.RedfishEndpointHpe(
                self,
                endpoint_ip,
                endpoint_port,
                redfish_username,
                redfish_password,
                cache_filename=endpoint_cache_filename,
                auto_connect=auto_connect,
                get_timeout=get_timeout,
                ssl_verify=ssl_verify,
                deep_search_exlusions=deep_search_exlusions,
                log_id=log_id,
                verbose=verbose,
                debug=debug
            )

        if self.endpoint_handler is None:
            raise ValueError('Unsupported endpoint type: %s' % (endpoint_type))

        self.tree_handler = tree.RedfishTree(self.endpoint_handler)

    def is_connected(self):
        return self.endpoint_handler.is_connected()

    def get_properties(self, path, properties=[]):
        return self.endpoint_handler.get_properties(path, properties=properties)

    def get_tree(self, path):
        self.tree_handler.initialize_tree(
            path,
            True,
            self.tree_max_execution_time
        )
        success = self.tree_handler.get_tree()
        if not success:
            self.my_output.error('Max path walk time reached: %s seconds' % (self.tree_max_execution_time))
            return None

        my_tree = json.loads(
            json.dumps(
                self.tree_handler.tree,
                sort_keys=True
            )
        )

        return my_tree

    def print_tree(self, data, output):
        if data is None:
            return

        if output == 'json':
            self.my_output.default(
                json.dumps(
                    data,
                    indent=4
                )
            )

        if output == 'default':
            self.my_output.default('')
            for uri in data:
                self.my_output.default(uri, underline=True)
                if data[uri] is None:
                    self.my_output.default('No properties')
                    continue

                self.my_output.default(
                    json.dumps(
                        data[uri],
                        indent=4
                    )
                )

                self.my_output.default('')

    def filter_key(self, rules, path=None, data=None):
        if path is None and data is None:
            return None

        if data is None:
            data = self.get_properties(
                path,
                properties=[]
            )
            if data is None:
                return None

        filtered_data = self.endpoint_handler.filter_key(data, rules)
        return filtered_data

    def get_keys(self, path, deep, key_filter):
        keys = {}

        if deep:
            data = self.get_tree(
                path
            )
            if data is None:
                return None

            for uri in data:
                if data[uri] is None:
                    continue

                properties = self.filter_key(
                    key_filter,
                    data=data[uri]
                )

                if len(properties) > 0:
                    keys[uri] = properties

        if not deep:
            path = self.endpoint_handler.path_fixup(path)
            properties = self.filter_key(
                key_filter,
                path=path
            )

            if properties is not None and len(properties) > 0:
                keys[path] = properties

        return keys

    def filter_value(self, rules, path=None, data=None):
        if path is None and data is None:
            return None

        if data is None:
            data = self.get_properties(
                path,
                properties=[]
            )
            if data is None:
                return None

        filtered_data = self.endpoint_handler.filter_value(data, rules)
        return filtered_data

    def get_values(self, path, deep, value_filter):
        values = {}

        if deep:
            data = self.get_tree(
                path
            )
            if data is None:
                return None

            for uri in data:
                if data[uri] is None:
                    continue

                properties = self.filter_value(
                    value_filter,
                    data=data[uri]
                )

                if len(properties) > 0:
                    values[uri] = properties

        if not deep:
            path = self.endpoint_handler.path_fixup(path)
            properties = self.filter_value(
                value_filter,
                path=path
            )

            if len(properties) > 0:
                values[path] = properties

        return values

    def get_odata_ids(self, path):
        properties = self.get_properties(path)
        if properties is None:
            return None

        return self.tree_handler.find_odata_id(properties)

    def get_children(self, path, deep):
        self.tree_handler.initialize_tree(
            path,
            deep,
            self.tree_max_execution_time
        )
        success = self.tree_handler.get_tree()
        if not success:
            self.my_output.error('Max path walk time reached: %s' % (self.tree_max_execution_time))
            return None

        return sorted(self.tree_handler.tree.keys())

    def print_children(self, path, children, deep, output):
        if output == 'default':
            path = self.endpoint_handler.path_fixup(path)
            self.my_output.default('')
            if deep:
                self.my_output.default('Redfish resource references (recursively): %s' % (path), underline=True)
            else:
                self.my_output.default('Redfish resource references: %s' % (path), underline=True)

            for child in children:
                if child != path:
                    self.my_output.default(child)

        if output == 'json':
            self.my_output.default(json.dumps(children, indent=4))

    def get_descriptions(self, path, deep):
        redfish_properties = [
            '@odata.id',
            '@odata.type',
            '@odata.context',
            'Id',
            'Name',
            'Description'
        ]

        descriptions = {}

        if deep:
            data = self.get_tree(
                path
            )
            if data is None:
                return None

            for uri in data:
                if data[uri] is not None:
                    uri_description = {}
                    for key in redfish_properties:
                        if key in data[uri]:
                            uri_description[key] = data[uri][key]
                    descriptions[uri] = uri_description

        if not deep:
            path = self.endpoint_handler.path_fixup(path)
            properties = self.get_properties(
                path,
                redfish_properties
            )
            if properties is None:
                return None

            descriptions[path] = properties

        return descriptions

    def get_action(self, path, deep):
        key_filter = [
            'eq(Actions)'
        ]

        return self.get_keys(path, deep, key_filter)

    def get_oem(self, path, deep):
        key_filter = [
            'eq(Oem)'
        ]

        return self.get_keys(path, deep, key_filter)
