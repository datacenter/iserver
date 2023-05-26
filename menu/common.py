from lib.intersight import compute_info
from lib.intersight import computes_info


def flags_fixup(ctx, silent, verbose, debug):
    if silent:
        debug = False
        verbose = False

    if debug:
        verbose = True

    ctx.my_output.set_flags(silent, verbose, debug)
    return (silent, verbose, debug)


def get_confirmation():
    answer = ""
    while answer not in ["y", "n"]:
        answer = input("Continue [Y/N]? ").lower()
    return answer == "y"


def get_no_match_definition():
    match_rules = {}
    match_rules['name'] = ''
    match_rules['ip'] = []
    match_rules['serials'] = []
    match_rules['model'] = ''
    match_rules['locator'] = False
    match_rules['power_off'] = False
    match_rules['alarms'] = False
    match_rules['ucsm'] = False
    match_rules['disconnected'] = False
    match_rules['standalone'] = False
    match_rules['cpu'] = ''
    match_rules['memory'] = ''
    match_rules['pci'] = ''
    match_rules['mac'] = ''
    match_rules['fan'] = False
    match_rules['psu'] = False
    return match_rules


def get_servers(ctx, iaccount, locator=True, server_setting_id=True, workflow=0, registration=True):
    settings = get_server_selection_settings(
        iaccount,
        workflow=workflow,
        action=server_setting_id,
        registration=registration
    )
    settings['locator'] = locator

    match_rules = get_no_match_definition()

    computes_handler = computes_info.ComputesInfo(iaccount, settings, log_id=ctx.run_id)
    servers = computes_handler.get(match_rules=match_rules)
    servers = sorted(servers, key=lambda i: i['Name'])
    ctx.busy = False

    return servers


def get_selected_servers(ctx, iaccount, group, serial_filter, name_filter, ip_filter, model_filter='', confirm=True, workflow=86400, registration=True, server_setting_id=True, locator=True, show_servers=True, allow_all=False):
    if len(group) == 0 and len(serial_filter) == 0 and name_filter == '' and len(ip_filter) == 0:
        if not allow_all:
            ctx.busy = False
            ctx.my_output.error('Select servers')
            return None

    settings = get_server_selection_settings(
        iaccount,
        workflow=workflow,
        action=server_setting_id,
        registration=registration
    )
    settings['locator'] = locator

    match_rules = {}
    match_rules['name'] = name_filter
    match_rules['model'] = model_filter
    match_rules['ip'] = ip_filter
    match_rules['serials'] = group + serial_filter
    match_rules['locator'] = False
    match_rules['power_off'] = False
    match_rules['alarms'] = False
    match_rules['ucsm'] = False
    match_rules['disconnected'] = False
    match_rules['standalone'] = False
    match_rules['cpu'] = ''
    match_rules['memory'] = ''
    match_rules['pci'] = ''
    match_rules['fan'] = False
    match_rules['psu'] = False

    computes_handler = computes_info.ComputesInfo(iaccount, settings, log_id=ctx.run_id)
    servers = computes_handler.get(match_rules=match_rules)
    servers = sorted(servers, key=lambda i: i['Name'])
    ctx.busy = False

    if servers is None or len(servers) == 0:
        ctx.my_output.error('No server found')
        return None

    if show_servers:
        computes_handler.print(servers, legend_on=False)
        if confirm:
            if not get_confirmation():
                return None
        else:
            ctx.my_output.default('Auto confirmation: Y')

    return servers


def get_server_selection_settings(iaccount, workflow=None, action=False, registration=False, enabled=[]):
    compute_info_handler = compute_info.ComputeInfo(iaccount)

    settings = compute_info_handler.get_default_settings()
    settings['registration'] = registration
    settings['server_setting_id'] = action
    settings['workflow'] = workflow

    for key in enabled:
        settings[key] = True

    return settings


def get_selected_server(ctx, iaccount, name_filter, ip_filter, serial_filter, workflow=None, action=False, include_object=False, confirm=False, show_servers=False, cache_enabled=False):
    if name_filter == '' and ip_filter == '' and serial_filter == '':
        ctx.my_output.error('Select server by name, ip or serial')
        return None

    settings = get_server_selection_settings(
        iaccount,
        workflow=workflow,
        action=action
    )
    match_rules = get_no_match_definition()

    if len(name_filter) > 0:
        match_rules['name'] = name_filter

    if len(ip_filter) > 0:
        match_rules['ip'] = [
            dict(
                type='address',
                value=ip_filter
            )
        ]

    if len(serial_filter) > 0:
        match_rules['serials'] = [serial_filter]

    computes_handler = computes_info.ComputesInfo(iaccount, settings, log_id=getattr(ctx, 'run_id', None))
    servers = computes_handler.get(
        match_rules=match_rules,
        include_object=include_object,
        inventory_cache_enabled=cache_enabled,
        parallel=False
    )
    if len(servers) == 0:
        ctx.busy = False
        ctx.my_output.error('Server not found')
        return None

    if len(servers) > 1:
        ctx.busy = False
        ctx.my_output.error('Multiple servers found. Be more precise to match single server')
        computes_handler.print(servers, legend_on=False, force_base_output=True)
        return None

    if show_servers:
        computes_handler.print(servers, legend_on=False)
        if confirm:
            if not get_confirmation():
                return None
        else:
            ctx.my_output.default('Auto confirmation: Y')

    return servers[0]


def print_servers(ctx, iaccount, servers):
    settings = get_server_selection_settings(
        iaccount,
        workflow=None,
        action=False,
        registration=False
    )

    computes_handler = computes_info.ComputesInfo(iaccount, settings, log_id=ctx.run_id)
    computes_handler.print(servers, legend_on=False)


def chassis_settings_fixup(settings):

    # Do not print summary header if any details section is enabled

    summary = True
    for key in ['power', 'fan', 'module', 'port', 'node']:
        if settings[key]['enabled']:
            summary = False

    settings['summary'] = {}
    settings['summary']['enabled'] = summary

    # Copy module selection to port module selection

    if settings['module']['enabled']:
        if settings['module']['path'] is not None:
            if settings['port']['enabled']:
                if settings['port']['module'] is None:
                    settings['port']['module'] = settings['module']['path'].lower()

        if settings['module']['id'] is not None:
            if settings['port']['enabled']:
                if settings['port']['module'] is None:
                    settings['port']['module'] = str(settings['module']['id'])

    # If port node is selected, enforce port type host

    if settings['port']['enabled']:
        if settings['port']['node'] is not None:
            settings['port']['type'] = 'host'

    return settings
