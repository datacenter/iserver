import os

from progress.bar import Bar

from lib import ip_helper
from lib import log_helper
from lib import output_helper

from lib.endpoint_helper import EndpointSettings
from lib.redfish import endpoint


class RedfishEndpointSettings(EndpointSettings):
    def __init__(self, log_id=None):
        EndpointSettings.__init__(self, log_id=log_id)

        self.log_id = log_id
        self.log = log_helper.Log(log_id=log_id)
        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=False,
            debug=False
        )

        self.redfish_settings_filename = os.path.join(
            self.settings_dir,
            'redfish'
        )

    def get_redfish_endpoint_id(self, identity):
        return identity['SerialNumber']

    def is_redfish_endpoint(self, endpoint_id):
        if self.get_redfish_endpoint_settings(endpoint_id) is None:
            return False
        return True

    def get_redfish_endpoint_settings(self, endpoint_id):
        endpoint_settings = self.get_endpoint_settings(endpoint_id)
        if endpoint_settings is None:
            return None

        if 'redfish' in endpoint_settings:
            return endpoint_settings['redfish']

        return None

    def set_redfish_endpoint_settings(self, redfish_endpoint_configuration, redfish_endpoint_identity):
        endpoint_id = self.get_redfish_endpoint_id(
            redfish_endpoint_identity
        )

        endpoint_settings = self.get_endpoint_settings(
            endpoint_id
        )
        if endpoint_settings is None:
            endpoint_settings = {}
            endpoint_settings['endpoint_id'] = endpoint_id

        endpoint_settings['redfish'] = {}
        endpoint_settings['redfish']['endpoint_id'] = endpoint_id
        endpoint_settings['redfish']['identity'] = redfish_endpoint_identity
        endpoint_settings['redfish']['endpoint'] = redfish_endpoint_configuration

        return self.set_endpoint_settings(endpoint_id, endpoint_settings)

    def match_redfish_endpoint(self, redfish_endpoint, endpoint_type, endpoint_ip, serial_number):
        if len(endpoint_type) > 0 and endpoint_type != 'any':
            if redfish_endpoint['endpoint']['type'] != endpoint_type:
                return False

        if len(endpoint_ip) > 0:
            if ip_helper.is_valid_ipv4_address(endpoint_ip):
                if redfish_endpoint['endpoint']['ip'] != endpoint_ip:
                    return False

            if ip_helper.is_valid_ipv4_cidr(endpoint_ip):
                if not ip_helper.is_ipv4_in_cidr(redfish_endpoint['endpoint']['ip'], endpoint_ip):
                    return False

        if len(serial_number) > 0:
            if redfish_endpoint['identity']['SerialNumber'] != serial_number:
                return False

        return True

    def get_redfish_endpoints_settings(self, endpoint_type='', endpoint_ip='', serial_number=''):
        endpoint_ids = self.get_endpoint_ids()

        endpoints = []
        for endpoint_id in endpoint_ids:
            redfish_endpoint = self.get_redfish_endpoint_settings(endpoint_id)
            if redfish_endpoint is None:
                continue

            match = self.match_redfish_endpoint(
                redfish_endpoint,
                endpoint_type,
                endpoint_ip,
                serial_number
            )

            if not match:
                continue

            endpoints.append(
                redfish_endpoint
            )

        return endpoints

    def get_servers_redfish_settings(self, servers, verify=False, bar_enabled=False):
        redfish_endpoints_settings = self.get_redfish_endpoints_settings()
        if redfish_endpoints_settings is None:
            return None

        for server in servers:
            server['redfish_capable'] = server['Redfish']['Capable']
            server['redfish_enabled'] = False
            server['redfish_endpoint'] = None
            server['redfish_verified'] = ''
            if server['redfish_capable']:
                for redfish_endpoint in redfish_endpoints_settings:
                    if server['Serial'] == redfish_endpoint['identity']['SerialNumber']:
                        server['redfish_enabled'] = True
                        server['redfish_verified'] = False
                        server['redfish_endpoint_id'] = redfish_endpoint['endpoint_id']
                        for key in redfish_endpoint['endpoint']:
                            server['redfish_endpoint_%s' % (key)] = redfish_endpoint['endpoint'][key]

        if verify:
            if bar_enabled:
                bar_handler = Bar('Progress', max=len(servers))
                bar_handler.goto(0)

            for item in servers:
                if item['redfish_enabled']:
                    item['redfish_verified'] = self.verify_redfish_endpoint_authentication(
                        item['redfish_endpoint_id']
                    )
                if bar_enabled:
                    bar_handler.next()

            if bar_enabled:
                bar_handler.finish()

        return servers

    def get_servers_redfish_summary(self, servers, verify=False):
        summary = {}
        summary['count'] = len(servers)
        summary['capable'] = 0
        summary['enabled'] = 0
        if verify:
            summary['verified'] = 0
        summary['ucsc'] = 0
        summary['fi'] = 0
        summary['dell'] = 0
        summary['hpe'] = 0
        summary['standard'] = 0

        for server in servers:
            if server['Redfish']['Capable']:
                summary['capable'] = summary['capable'] + 1
            if server['redfish_enabled']:
                summary['enabled'] = summary['enabled'] + 1
                summary[server['redfish_endpoint_type']] = summary[server['redfish_endpoint_type']] + 1
                if verify:
                    if server['redfish_verified']:
                        summary['verified'] = summary['verified'] + 1

        return summary

    def delete_redfish_endpoint_settings(self, endpoint_id):
        endpoint_settings = self.get_endpoint_settings(endpoint_id)
        if 'redfish' in endpoint_settings:
            del endpoint_settings['redfish']

        return self.set_endpoint_settings(endpoint_id, endpoint_settings)

    def verify_redfish_endpoint_authentication(self, endpoint_id):
        endpoint_settings = self.get_redfish_endpoint_settings(endpoint_id)
        if endpoint_settings is None:
            return False

        redfish_handler = endpoint.RedfishEndpoint(
            endpoint_settings['endpoint']['type'],
            endpoint_settings['endpoint']['ip'],
            endpoint_settings['endpoint']['port'],
            endpoint_settings['endpoint']['username'],
            endpoint_settings['endpoint']['password'],
            log_id=self.log_id
        )

        if not redfish_handler.is_connected():
            return False

        return True

    def get_redfish_endpoint_template(self, endpoint_id, template_name):
        endpoint_settings = self.get_redfish_endpoint_settings(endpoint_id)
        if endpoint_settings is None:
            return None

        redfish_handler = endpoint.RedfishEndpoint(
            endpoint_settings['endpoint']['type'],
            endpoint_settings['endpoint']['ip'],
            endpoint_settings['endpoint']['port'],
            endpoint_settings['endpoint']['username'],
            endpoint_settings['endpoint']['password'],
            log_id=self.log_id
        )

        if not redfish_handler.is_connected():
            return None

        if endpoint_settings['endpoint']['type'] == 'fi':
            redfish_handler.endpoint_handler.set_inventory(
                endpoint_settings['endpoint']['inventory_type'],
                endpoint_settings['endpoint']['inventory_id']
            )

        return redfish_handler.endpoint_handler.get_template_properties(template_name)

    def print_redfish_endpoint_template(self, endpoint_id, template_name, template_properties):
        endpoint_settings = self.get_redfish_endpoint_settings(endpoint_id)
        if endpoint_settings is None:
            return

        redfish_handler = endpoint.RedfishEndpoint(
            endpoint_settings['endpoint']['type'],
            endpoint_settings['endpoint']['ip'],
            endpoint_settings['endpoint']['port'],
            endpoint_settings['endpoint']['username'],
            endpoint_settings['endpoint']['password'],
            auto_connect=False,
            log_id=self.log_id
        )

        if endpoint_settings['endpoint']['type'] == 'fi':
            redfish_handler.endpoint_handler.set_inventory(
                endpoint_settings['endpoint']['inventory_type'],
                endpoint_settings['endpoint']['inventory_id']
            )

        redfish_handler.endpoint_handler.print_template_properties(
            template_name,
            template_properties
        )

    def print_redfish_endpoint_settings(self, endpoints, verify=False, show_password=True):
        entries = []
        for item in endpoints:
            entry = item['endpoint']
            for key in ['Product', 'SerialNumber', 'HostName']:
                entry[key] = item['identity'][key]
            entries.append(entry)

        entries = sorted(entries, key=lambda k: (k['ip']))

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
            order.append('verified')
            headers.append('Authenticated')

        self.my_output.my_table(
            entries,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_servers_redfish(self, servers, verify=False, show_password=True):
        if not show_password:
            for item in servers:
                if item['redfish_enabled']:
                    item['redfish_endpoint_password'] = '******'

        order = [
            'Name',
            'Model',
            'Serial',
            'ManagementIp',
            'redfish_capable',
            'redfish_enabled',
            'redfish_endpoint_type',
            'redfish_endpoint_ip',
            'redfish_endpoint_port',
            'redfish_endpoint_username',
            'redfish_endpoint_password',
            'redfish_endpoint_inventory_type',
            'redfish_endpoint_inventory_id'
        ]

        headers = [
            'Name',
            'Model',
            'Serial',
            'IP',
            'Redfish Support',
            'Redfish Access',
            'Type',
            'IP',
            'Port',
            'Username',
            'Password',
            'Inventory Type',
            'Inventory ID'
        ]

        if verify:
            order.append('redfish_verified')
            headers.append('Authenticated')

        self.my_output.my_table(
            servers,
            order=order,
            headers=headers,
            table=True
        )

    def print_servers_redfish_summary(self, summary, verify=False):
        if verify:
            self.my_output.dictionary(
                summary,
                title='Intersight Servers - Redfish Access Summary',
                underline=True,
                prefix="- ",
                justify=True,
                keys=[
                    'count',
                    'capable',
                    'enabled',
                    'verified',
                    'standard',
                    'ucsc',
                    'fi',
                    'dell',
                    'hpe'
                ],
                title_keys=[
                    'Servers Count',
                    'Redfish Support',
                    'Redfish Configured',
                    'Redfish Access Verified',
                    'Endpoint Type - standard',
                    'Endpoint Type - ucsc',
                    'Endpoint Type - fi',
                    'Endpoint Type - dell',
                    'Endpoint Type - hpe'
                ]
            )
        else:
            self.my_output.dictionary(
                summary,
                title='Intersight Servers - Redfish Access Summary',
                underline=True,
                prefix="- ",
                justify=True,
                keys=[
                    'count',
                    'capable',
                    'enabled',
                    'standard',
                    'ucsc',
                    'fi',
                    'dell',
                    'hpe'
                ],
                title_keys=[
                    'Servers Count',
                    'Redfish Support',
                    'Redfish Configured',
                    'Endpoint Type - standard',
                    'Endpoint Type - ucsc',
                    'Endpoint Type - fi',
                    'Endpoint Type - dell',
                    'Endpoint Type - hpe'
                ]
            )
