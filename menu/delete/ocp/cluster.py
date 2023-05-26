import sys
import traceback
import click

from lib.ocp.lcm import main as ocp


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("cluster")
@click.pass_obj
@click.argument("location", required=True, type=click.STRING)
@click.option("--verbose", is_flag=True, show_default=True, default=False, help="Verbose mode")
@click.option("--debug", is_flag=True, show_default=True, default=False, help="Debug mode")
def delete_ocp_cluster_command(ctx, location, verbose, debug):
    """Delete OCP cluster"""

    # iocp delete cluster

    try:
        if debug:
            verbose = True
        ctx.my_output.set_flags(False, verbose, debug)

        ocp_handler = ocp.Ocp(verbose=verbose, debug=debug, log_id=ctx.run_id)
        if not ocp_handler.set_ocp_user_input(location):
            raise ErrorExit

        if not ocp_handler.delete():
            raise ErrorExit

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
