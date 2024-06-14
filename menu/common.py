import threading

from menu import progress
from lib.intersight import compute
from lib.intersight import compute_output


def flags_fixup(ctx, silent, verbose, debug):
    if silent:
        debug = False
        verbose = False

    if debug:
        verbose = True

    ctx.my_output.set_flags(silent, verbose, debug)
    return (silent, verbose, debug)


def get_confirmation(title=True, before_newline=False, after_newline=False):
    if before_newline:
        print('\n')

    answer = ""
    while answer not in ["y", "n"]:
        if title:
            answer = input("Continue [Y/N]? ").lower()
        else:
            answer = input("[Y/N]? ").lower()

    if after_newline:
        print('\n')

    return answer == "y"


def get_value_from_list(title, values, before_newline=False, after_newline=False):
    if before_newline:
        print('\n')

    print(title)
    for item in values:
        print('- %s' % (item))
    answer = None
    while answer not in values:
        answer = input('Selected: ')
        if len(answer) == 0:
            return None

    if after_newline:
        print('\n')

    return answer


def get_integer(title, before_newline=False, after_newline=False):
    if before_newline:
        print('\n')

    while True:
        answer = input(title)
        try:
            value = int(answer)
        except BaseException:
            value = None
        if value is not None:
            if after_newline:
                print('\n')
            return value


def get_servers_mo(
        ctx,
        iaccount,
        ip_filter=None,
        name_filter=None,
        model_filter=None,
        serial_filter=None,
        tag_filter=None,
        show_progress=True,
        include_rack=True,
        include_blade=True,
        rack_expand=[],
        blade_expand=[]
    ):
    if show_progress:
        ctx.busy = True
        threading.Thread(target=progress.spinner_task, args=(ctx,)).start()

    try:
        compute_handler = compute.Compute(iaccount, log_id=ctx.run_id)
        match_rules = compute_handler.get_mo_match_rules(
            ip_filter=ip_filter,
            name_filter=name_filter,
            model_filter=model_filter,
            serial_filter=serial_filter,
            tag_filter=tag_filter
        )
        servers_mo = compute_handler.get_mo(
            match_rules=match_rules,
            include_rack=include_rack,
            rack_expand=rack_expand,
            include_blade=include_blade,
            blade_expand=blade_expand,
        )
    except BaseException:
        servers_mo = None

    ctx.busy = False

    return servers_mo


def get_servers_info(ctx, iaccount, ip_filter=None, name_filter=None, serial_filter=None, show_progress=True, include_rack=True, include_blade=True, settings={}, state=True, cache=True):
    if show_progress:
        ctx.busy = True
        threading.Thread(target=progress.spinner_task, args=(ctx,)).start()

    compute_handler = compute.Compute(iaccount, log_id=ctx.run_id)
    match_rules = compute_handler.get_mo_match_rules(
        ip_filter=ip_filter,
        name_filter=name_filter,
        serial_filter=serial_filter
    )

    rack_expand = []
    blade_expand = []
    if state:
        rack_expand.append('LocatorLed')
        rack_expand.append('RegisteredDevice')
        blade_expand.append('LocatorLed')
        blade_expand.append('RegisteredDevice')

    servers_mo = compute_handler.get_mo(
        match_rules=match_rules,
        rack_expand=rack_expand,
        blade_expand=blade_expand,
        include_rack=include_rack,
        include_blade=include_blade
    )
    if servers_mo is None or len(servers_mo) == 0:
        ctx.busy = False
        return servers_mo

    if state:
        settings['state'] = True
        settings['connector'] = True
        settings['locator'] = True
        settings['server_setting_id'] = True
        settings['workflow'] = 3600

    if cache:
        servers_info = compute_handler.get_info(
            servers_mo,
            settings,
            None,
            0
        )
    else:
        servers_info = compute_handler.get_info(
            servers_mo,
            settings,
            None,
            1
        )

    ctx.busy = False

    return servers_info


def print_servers_info(ctx, iaccount, ip_filter=None, name_filter=None, serial_filter=None, show_progress=True, include_rack=True, include_blade=True, settings={}, cache=True):
    servers_info = get_servers_info(
        ctx,
        iaccount,
        ip_filter=ip_filter,
        name_filter=name_filter,
        serial_filter=serial_filter,
        show_progress=show_progress,
        include_rack=include_rack,
        include_blade=include_blade,
        settings=settings,
        cache=cache
    )

    compute_output_handler = compute_output.ComputeOutput(log_id=ctx.run_id)
    compute_output_handler.print_summary_table(
        servers_info,
        title=True
    )


def print_servers_mo_info(ctx, iaccount, servers_mo, show_progress=True, settings={}, cache=True, title=True):
    if show_progress:
        ctx.busy = True
        threading.Thread(target=progress.spinner_task, args=(ctx,)).start()

    compute_handler = compute.Compute(iaccount, log_id=ctx.run_id)

    if cache:
        servers_info = compute_handler.get_info(
            servers_mo,
            settings,
            None,
            0
        )
    else:
        servers_info = compute_handler.get_info(
            servers_mo,
            settings,
            None,
            1
        )

    ctx.busy = False

    compute_output_handler = compute_output.ComputeOutput(log_id=ctx.run_id)
    compute_output_handler.print_summary_table(
        servers_info,
        title=title
    )
