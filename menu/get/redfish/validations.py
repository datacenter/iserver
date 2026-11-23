from lib import ip_helper
from lib.redfish import endpoint_settings


def get_redfish_endpoint_ips(ctx):
    endpoints = []
    while True:
        endpoint_ip = input('Redfish endpoint IP address or range (empty to exit): ')
        if len(endpoint_ip) == 0:
            break

        if len(endpoint_ip.split('-')) == 1:
            if not ip_helper.is_valid_ipv4_address(endpoint_ip):
                ctx.my_output.error('IPv4 address invalid')
                return None
            endpoints.append(
                endpoint_ip
            )

        else:
            addresses = ip_helper.get_ipv4_addresses_in_range(
                endpoint_ip.split('-')[0],
                endpoint_ip.split('-')[1]
            )
            if addresses is None:
                ctx.my_output.error('IPv4 address rangeinvalid')
                return None

            endpoints = endpoints + addresses

    return endpoints


def get_redfish_endpoints(ctx, endpoint_ips, endpoint_port, username, password):
    endpoints = []

    endpoint_settings_handler = endpoint_settings.RedfishEndpointSettings(
        log_id=ctx.run_id
    )

    for endpoint_ip in endpoint_ips:
        endpoint_id = endpoint_settings_handler.get_endpoint_id_with_ip(
            endpoint_ip
        )
        if endpoint_id is None:
            ctx.my_output.default('Endpoint %s not found in internal redfish database. Provide full access details.' % (endpoint_ip))

            endpoint = {}
            endpoint['system_id'] = None
            endpoint['type'] = 'ucsc'
            endpoint['ip'] = endpoint_ip
            endpoint['port'] = endpoint_port

            if len(username) > 0:
                endpoint['username'] = username
            else:
                endpoint['username'] = input('Redfish authentication username: ')
                if len(endpoint['username']) == 0:
                    return None

            if len(password) > 0:
                endpoint['password'] = password
            else:
                endpoint['password'] = input('Redfish authentication password: ')
                if len(endpoint['password']) == 0:
                    return None

            endpoints.append(
                endpoint
            )

        else:
            redfish_settings = endpoint_settings_handler.get_redfish_endpoint_settings(endpoint_id)
            if redfish_settings is None:
                ctx.my_output.default('Selected server in internal redfish database and is not configured with Redfish access: %s' % (endpoint_ip))
                return None

            if redfish_settings['endpoint']['type'] != 'ucsc':
                ctx.my_output.error(
                    'Endpoint properties template not supported on generic endpoint type: %s' % (endpoint_ip)
                )
                return None

            endpoint = {}
            endpoint['system_id'] = endpoint_id
            endpoint['type'] = redfish_settings['endpoint']['type']
            endpoint['ip'] = endpoint_ip
            endpoint['port'] = redfish_settings['endpoint']['port']
            endpoint['username'] = redfish_settings['endpoint']['username']
            endpoint['password'] = redfish_settings['endpoint']['password']

            endpoints.append(
                endpoint
            )

    return endpoints
