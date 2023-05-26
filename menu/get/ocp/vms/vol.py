import sys
import json
import threading
import traceback
import click

from menu import validations
from menu import progress

from lib.kubevirt import main as kubevirt


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("vol")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', type=click.STRING, help="Cluster Name")
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_ocp_vms_vol_command(ctx, cluster_name, output, devel):
    """Get ocp virtual machines volumes"""

    # iserver get ocp vms vol

    ctx.developer = devel
    ctx.output = output

    try:
        ctx.my_output.default('tbd')

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
