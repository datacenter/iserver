from lib import ip_helper
from lib.redfish import endpoint_settings
from lib.redfish import endpoint


def set_endpoint(ctx, params):
    endpoint_settings_handler = endpoint_settings.RedfishEndpointSettings(
        log_id=ctx.run_id
    )

    redfish_endpoint_settings = {}
    redfish_endpoint_settings['type'] = params['handler_endpoint_type']
    redfish_endpoint_settings['ip'] = params['endpoint_ip']
    redfish_endpoint_settings['port'] = params['endpoint_port']
    redfish_endpoint_settings['username'] = params['username']
    redfish_endpoint_settings['password'] = params['password']
    redfish_endpoint_settings['inventory_type'] = params['inventory_type']
    redfish_endpoint_settings['inventory_id'] = params['inventory_id']

    if params['endpoint_id'] is None:
        params['endpoint_id'] = ip_helper.get_short_uuid()

    endpoint_settings_handler.set_redfish_endpoint_access(
        redfish_endpoint_settings,
        params['endpoint_id']
    )


def get_params_from_user(ctx, params):
    if len(params['username']) > 0:
        params['system_id'] = None
        params['handler_endpoint_type'] = params['endpoint_type']

    if len(params['username']) == 0:
        ctx.my_output.default('Endpoint not found in internal redfish database. Provide access details.')
        params['system_id'] = None

        params['endpoint_port'] = input('Redfish endpoint port [def. 443]: ')
        if len(params['endpoint_port']) == 0:
            params['endpoint_port'] = 443
        else:
            try:
                params['endpoint_port'] = int(params['endpoint_port'])
            except BaseException:
                ctx.my_output.error('Port (int) value expected')
                params['endpoint_port'] = None

        if params['endpoint_port'] is None:
            return None

        params['username'] = input('Redfish authentication username: ')
        if len(params['username']) == 0:
            return None

        params['password'] = input('Redfish authentication password: ')
        if len(params['password']) == 0:
            return None

        params['handler_endpoint_type'] = input('Endpoint type [ucsc, bmc, fi, dell, hp]: ')
        if len(params['handler_endpoint_type']) == 0 or params['handler_endpoint_type'] not in ['ucsc', 'bmc', 'fi', 'dell', 'hp']:
            return None

        if params['handler_endpoint_type'] == 'fi':
            params['inventory_type'] = input('Inventory type: ')
            if len(params['inventory_type']) == 0:
                return None

            params['inventory_id'] = input('Inventory id: ')
            if len(params['inventory_id']) == 0:
                return None

    return params


def get_params_from_cache(ctx, endpoint_settings_handler, params):
    redfish_settings = endpoint_settings_handler.get_redfish_endpoint_settings(params['endpoint_id'])
    if redfish_settings is None:
        ctx.my_output.default('Selected server in internal redfish database and is not configured with Redfish access')
        return None

    ctx.my_output.default('Endpoint found in internal redfish database.')

    if redfish_settings['endpoint']['type'] == 'generic':
        ctx.my_output.error(
            'Endpoint properties template not supported on generic endpoint type'
        )
        return None

    params['endpoint_type'] = redfish_settings['endpoint']['type']
    params['handler_endpoint_type'] = redfish_settings['endpoint']['type']
    params['system_id'] = None
    params['endpoint_ip'] = redfish_settings['endpoint']['ip']
    params['endpoint_port'] = redfish_settings['endpoint']['port']

    if len(params['username']) == 0:
        params['username'] = redfish_settings['endpoint']['username']

    if len(params['password']) == 0:
        params['password'] = redfish_settings['endpoint']['password']

    if params['endpoint_type'] == 'fi':
        if len(params['inventory_type']) == 0:
            params['inventory_type'] = input('Inventory type: ')
            if len(params['inventory_type']) == 0:
                return None

        if len(params['inventory_id']) == 0:
            params['inventory_id'] = input('Inventory id: ')
            if len(params['inventory_id']) == 0:
                return None

    return params


def input_params(ctx, params):
    if len(params['endpoint_ip']) == 0:
        params['endpoint_ip'] = input('Redfish endpoint IP address: ')
        if not ip_helper.is_valid_ipv4_address(params['endpoint_ip']):
            ctx.my_output.error('IPv4 address invalid')
            return None

    endpoint_settings_handler = endpoint_settings.RedfishEndpointSettings(
        log_id=ctx.run_id
    )

    params['endpoint_id'] = endpoint_settings_handler.get_endpoint_id_with_ip(
        params['endpoint_ip']
    )
    if params['endpoint_id'] is None:
        params = get_params_from_user(ctx, params)
    else:
        params = get_params_from_cache(ctx, endpoint_settings_handler, params)
    
    return params


def get_redfish_handler(ctx, params, get_timeout=10):
    if 'deep_search_exlusions' not in params:
        params['deep_search_exlusions'] = True

    if 'tree_max_execution_time' not in params:
        params['tree_max_execution_time'] = 120

    redfish_handler = endpoint.RedfishEndpoint(
        params['handler_endpoint_type'],
        params['endpoint_ip'],
        params['endpoint_port'],
        params['username'],
        params['password'],
        system_id=params['system_id'],
        get_timeout=get_timeout,
        auto_connect=True,
        ssl_verify=False,
        deep_search_exlusions=params['deep_search_exlusions'],
        tree_max_execution_time=params['tree_max_execution_time'],
        log_id=ctx.run_id
    )

    if params['endpoint_type'] == 'fi':
        redfish_handler.endpoint_handler.set_inventory(
            params['inventory_type'],
            params['inventory_id']
        )

    if not redfish_handler.is_connected():
        ctx.busy = False
        ctx.my_output.error(
            'Redfish access failed'
        )
        return None

    set_endpoint(ctx, params)
    return redfish_handler
