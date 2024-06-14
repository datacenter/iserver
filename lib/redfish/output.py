import json
from lib import output_helper

from lib.redfish.dell.output import RedfishEndpointDellOutput
from lib.redfish.fi.output import RedfishEndpointFabricInterconnectOutput
from lib.redfish.hpe.output import RedfishEndpointHpeOutput
from lib.redfish.ucs_rack.output import RedfishEndpointUcsRackOutput


class RedfishOutput(
        RedfishEndpointDellOutput,
        RedfishEndpointFabricInterconnectOutput,
        RedfishEndpointHpeOutput,
        RedfishEndpointUcsRackOutput
        ):
    def __init__(self, verbose=False, debug=False, log_id=None):
        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=verbose,
            debug=debug
        )

        RedfishEndpointDellOutput.__init__(self)
        RedfishEndpointFabricInterconnectOutput.__init__(self)
        RedfishEndpointHpeOutput.__init__(self)
        RedfishEndpointUcsRackOutput.__init__(self)

    def print_redfish_endpoint_settings(self, endpoints, verify=False, show_password=True, title=False):
        if title:
            self.my_output.default(
                'RedFish Endpoint [#%s]' % (len(endpoints)),
                underline=True,
                before_newline=True
            )

        if len(endpoints) == 0:
            self.my_output.default('None')
            return

        entries = []
        for item in endpoints:
            entry = item['endpoint']
            entry['__Output'] = {}

            if 'verified' in entry:
                if entry['verified']:
                    entry['AuthenticatedTick'] = '\u2713'
                    entry['__Output']['AuthenticatedTick'] = 'Green'
                else:
                    entry['AuthenticatedTick'] = '\u2717'
                    entry['__Output']['AuthenticatedTick'] = 'Red'

            for key in ['Product', 'SerialNumber', 'HostName']:
                entry[key] = item['identity'][key]

            if len(entry['inventory_type']) == 0:
                entry['inventory_type'] = '--'

            if len(entry['inventory_id']) == 0:
                entry['inventory_id'] = '--'

            entries.append(entry)

        if not show_password:
            for item in entries:
                item['password'] = '******'

        order = [
            'SerialNumber',
            'Product',
            'HostName',
            'type',
            'ip',
            'port',
            'username',
            'password',
            'inventory_type',
            'inventory_id'
        ]

        headers = [
            'S/N',
            'Product',
            'Name',
            'Type',
            'IP',
            'Port',
            'Username',
            'Password',
            'FI Inventory Type',
            'FI Inventory ID'
        ]

        if verify:
            order.append('AuthenticatedTick')
            headers.append('Authenticated')

        self.my_output.my_table(
            entries,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_redfish_cache(self, info, title=False):
        if title:
            self.my_output.default(
                'RedFish Cache [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'CacheName',
            'Product',
            'SerialNumber',
            'Firmware',
            'PowerState',
            'EndpointType',
            'EndpointIp',
            'EndpointInventoryType',
            'EndpointInventoryId'
        ]

        headers = [
            'Cache Name',
            'Product',
            'S/N',
            'Firmware',
            'Power',
            'Type',
            'IP',
            'Inventory',
            'Id'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_children(self, path, children, deep, output):
        if output == 'default':
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

    def print_redfish_settings(self, settings):
        order = [
            'CacheEnabled',
            'CacheDirectory'
        ]

        headers = [
            'Cache Enabled',
            'Cache Directory'
        ]

        self.my_output.dictionary(
            settings,
            title='Redfish Settings',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )
