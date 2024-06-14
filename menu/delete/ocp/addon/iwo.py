import sys
import traceback
import click

from menu import defaults
from menu import validations

from lib.iwo.lcm import main as iwo


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("iwo")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', type=click.STRING, help="Cluster Name")
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
@click.option("--verbose", is_flag=True, show_default=True, default=False, help="Verbose mode")
@click.option("--debug", is_flag=True, show_default=True, default=False, help="Debug mode")
def delete_ocp_addon_iwo_command(ctx, cluster_name, iaccount, verbose, debug):
    """Delete OCP IWO Addon"""

    # iocp delete ocp addon iwo

    try:
        if debug:
            verbose = True
        ctx.my_output.set_flags(False, verbose, debug)

        iwo_lcm_handler = iwo.IwoLcm(
            verbose=verbose,
            debug=debug,
            log_id=ctx.run_id
        )

        success = iwo_lcm_handler.delete(
            cluster_name,
            iaccount
        )
        if not success:
            raise ErrorExit

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
