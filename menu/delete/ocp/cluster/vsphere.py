import sys
import traceback
import click

from lib.ocp.lcm import main as ocp


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("vsphere")
@click.pass_obj
@click.option("--dir", "location", is_flag=False, show_default=False, default='', type=click.STRING, help="Cluster definition directory")
@click.option("--verbose", is_flag=True, show_default=True, default=False, help="Verbose mode")
@click.option("--debug", is_flag=True, show_default=True, default=False, help="Debug mode")
def delete_ocp_cluster_vshpere_command(ctx, location, verbose, debug):
    """Delete OCP vsphere cluster"""

    # iocp delete cluster

    try:
        if len(location) == 0:
            ctx.my_output.error('Cluster definition directory required')
            raise ErrorExit

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
