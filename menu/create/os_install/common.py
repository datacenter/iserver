import json

from progress.bar import IncrementalBar

from lib.intersight import os_install
from lib.intersight.lcm import common as lcm_server_common
from lib.intersight.lcm import power as lcm_server_power


def servers_power_cycle(ctx, iaccount, attributes, verbose):
    lcm_server_power_handler = lcm_server_power.LcmServerPower(
        iaccount,
        dry_run=False,
        wait=True,
        silent=False,
        verbose=verbose,
        debug=False,
        log_id=ctx.run_id
    )

    bar_handler = IncrementalBar('Power cycle the servers', max=len(attributes))
    bar_handler.goto(0)
    for attribute in attributes:
        if not lcm_server_power_handler.power_cycle([attribute['server']]):
            bar_handler.finish()
            ctx.my_output.error('Power cycle failed')
            ctx.my_output.debug(json.dumps(attribute, indent=4))
            return False

        bar_handler.next()

    bar_handler.finish()

    return True


def request_os_install(ctx, iaccount, attributes, dry_run, verbose):
    os_install_handler = os_install.OsInstall(
        iaccount,
        dry_run=dry_run,
        verbose=verbose,
        log_id=ctx.run_id
    )

    if not dry_run and not verbose:
        bar_handler = IncrementalBar('Request OS installation', max=len(attributes))
        bar_handler.goto(0)

    for attribute in attributes:
        response = os_install_handler.create_os_install(attribute)
        if not response['success']:
            if not dry_run and not verbose:
                bar_handler.finish()
            ctx.my_output.error('OS installation request failed')
            ctx.my_output.default(response['response'])
            ctx.my_output.debug(json.dumps(attribute, indent=4))
            return False

        if not dry_run and not verbose:
            bar_handler.next()

    if not dry_run and not verbose:
        bar_handler.finish()

    return True


def wait_workflows(ctx, iaccount, servers, verbose):
    lcm_handler = lcm_server_common.LcmServerCommon(
        iaccount,
        verbose=verbose,
        log_id=ctx.run_id
    )

    success = lcm_handler.wait_workflows(
        servers,
        'Operating System Install',
        max_start_time=180,
        max_complete_time=3600,
        summary=True
    )
    if not success:
        ctx.my_output.error('OS installation failed')
        return False

    ctx.my_output.default('OS installation successful')
    return True


def run(ctx, iaccount, attributes, dry_run=False, wait=True, verbose=False):
    if not dry_run:
        if not servers_power_cycle(ctx, iaccount, attributes, verbose):
            return False

    if not request_os_install(ctx, iaccount, attributes, dry_run, verbose):
        return False

    if dry_run:
        return True

    if wait:
        servers = []
        for attribute in attributes:
            servers.append(attribute['server'])
        return wait_workflows(ctx, iaccount, servers, verbose)

    return True
