import sys
import traceback
import click

from menu import defaults
from menu import validations

from lib.ocp.lcm import main as ocp


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("cluster")
@click.pass_obj
@click.argument("location", required=True, type=click.STRING)
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
@click.option("--token", "token_filename", is_flag=False, show_default=False, default='', callback=validations.empty_string_to_none, help="Openshift API Token Filename")
@click.option("--organization", "organization_name", is_flag=False, show_default=False, default='', type=click.STRING, help="Organization Name")
@click.option("--verbose", is_flag=True, show_default=True, default=False, help="Verbose mode")
@click.option("--debug", is_flag=True, show_default=True, default=False, help="Debug mode")
def create_ocp_cluster_command(ctx, location, iaccount, organization_name, token_filename, verbose, debug):
    """Create OCP cluster"""

    # iocp create cluster

    try:
        if debug:
            verbose = True
        ctx.my_output.set_flags(False, verbose, debug)

        ocp_handler = ocp.Ocp(verbose=verbose, debug=debug, log_id=ctx.run_id)
        if not ocp_handler.set_ocp_user_input(location, token_filename=token_filename):
            raise ErrorExit

        if not ocp_handler.create():
            raise ErrorExit

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
