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


def get_confirmation():
    answer = ""
    while answer not in ["y", "n"]:
        answer = input("Continue [Y/N]? ").lower()
    return answer == "y"


def get_servers_mo(ctx, iaccount, ip_filter, name_filter, serial_filter, show_progress=True, include_rack=True, include_blade=True):
    if show_progress:
        ctx.busy = True
        threading.Thread(target=progress.spinner_task, args=(ctx,)).start()

    compute_handler = compute.Compute(iaccount, log_id=ctx.run_id)
    match_rules = compute_handler.get_mo_match_rules(
        ip_filter=ip_filter,
        name_filter=name_filter,
        serial_filter=serial_filter
    )
    servers_mo = compute_handler.get_mo(
        match_rules=match_rules,
        include_rack=include_rack,
        include_blade=include_blade
    )

    ctx.busy = False

    return servers_mo


def get_servers_info(ctx, iaccount, ip_filter, name_filter, serial_filter, show_progress=True, include_rack=True, include_blade=True, settings={}, cache=True):
    if show_progress:
        ctx.busy = True
        threading.Thread(target=progress.spinner_task, args=(ctx,)).start()

    compute_handler = compute.Compute(iaccount, log_id=ctx.run_id)
    match_rules = compute_handler.get_mo_match_rules(
        ip_filter=ip_filter,
        name_filter=name_filter,
        serial_filter=serial_filter
    )
    servers_mo = compute_handler.get_mo(
        match_rules=match_rules,
        include_rack=include_rack,
        include_blade=include_blade
    )
    if servers_mo is None or len(servers_mo) == 0:
        ctx.busy = False
        return servers_mo

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


def print_servers_info(ctx, iaccount, ip_filter, name_filter, serial_filter, show_progress=True, include_rack=True, include_blade=True, settings={}, cache=True):
    servers_info = get_servers_info(
        ctx,
        iaccount,
        ip_filter,
        name_filter,
        serial_filter,
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
