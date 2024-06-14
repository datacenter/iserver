import sys
import copy
import json
import traceback
import click

from menu import common
from menu import defaults
from menu import validations
from menu import main as menu_main
from menu.create.os_install import validations as os_install_validations
from menu.create.os_install import common as os_install_common


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("batch")
@click.pass_obj
@click.argument("location", required=True, type=click.STRING)
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
@click.option("--dry-run", is_flag=True, show_default=True, default=False, help="Dry run")
@click.option("--one-by-one", is_flag=True, show_default=True, default=False, help="One by one")
@click.option("--no-wait", is_flag=True, show_default=True, default=False, help="Wait disabled")
@click.option("--verbose", is_flag=True, show_default=True, default=False, help="Verbose output")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def create_os_install_batch_command(ctx, iaccount, location, dry_run, one_by_one, no_wait, verbose, devel):
    """Batch OS installation"""

    # iserver create os-install batch

    silent = False
    debug = False
    common.flags_fixup(ctx, silent, verbose, debug)

    try:
        ctx.my_output.default('Check isctl version...')
        isctl_success, isctl_output = menu_main.check_isctl()
        if not isctl_success:
            ctx.my_output.error('isctl command execution failed')
            raise ErrorExit

        if not menu_main.check_isctl_version(isctl_output, '0.1.18'):
            ctx.my_output.error('Minimum isctl version 0.1.18 is required')
            raise ErrorExit

        ctx.my_output.default('Validate input parameters...')
        attributes = os_install_validations.get_batch_attributes(
            ctx,
            iaccount,
            location
        )
        if attributes is None:
            raise ErrorExit

        if len(attributes) == 0:
            ctx.my_output.error('No valid server defined')
            raise ErrorExit

        verbose_attributes = copy.deepcopy(attributes)
        for attribute in verbose_attributes:
            del attribute['server']
        ctx.my_output.info(json.dumps(verbose_attributes, indent=4))

        if one_by_one:
            no_wait = False
            for attribute in attributes:
                if not os_install_common.run(ctx, iaccount, [attribute], dry_run=dry_run, wait=not no_wait, verbose=verbose):
                    raise ErrorExit

        if not one_by_one:
            server_ids = []
            for attribute in attributes:
                if attribute['server']['Moid'] in server_ids:
                    ctx.my_output.error('Server cannot be defined more than once in parallel execution: %s' % (attribute['server']['Name']))
                    raise ErrorExit
                server_ids.append(attribute['server']['Moid'])

            if not os_install_common.run(ctx, iaccount, attributes, dry_run=dry_run, wait=not no_wait, verbose=verbose):
                raise ErrorExit

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
