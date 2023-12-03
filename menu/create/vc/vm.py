import sys
import threading
import traceback
import click

from menu import validations
from menu import progress


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("vm")
@click.pass_obj
@click.option("--vc", "vcenter", default='', callback=validations.validate_vc_name, help="vCenter name")
@click.option("--ip", "vcenter_ip", default='', callback=validations.validate_ip, help="vCenter IP")
@click.option("--username", "vcenter_username", default='', help="vCenter Username")
@click.option("--password", "vcenter_password", default='', help="vCenter Password")
@click.option("--yaml", "vm_filename", is_flag=False, show_default=False, default='', type=click.STRING, help="VM Definition YAML")
@click.option("--recreate", is_flag=True, show_default=True, default=False, help="Recreate")
@click.option("--dry-run", is_flag=True, show_default=True, default=False, help="Dry run")
@click.option("--verbose", is_flag=True, show_default=True, default=False, help="Verbose mode")
@click.option("--debug", is_flag=True, show_default=True, default=False, help="Debug mode")
def create_vc_vm_command(
        ctx,
        vcenter,
        vcenter_ip,
        vcenter_username,
        vcenter_password,
        vm_filename,
        recreate,
        dry_run,
        verbose,
        debug
        ):
    """Create vCehter virtual machine"""

    # iserver create vc vm

    try:
        vc_handler = validations.validate_vcenter(
            ctx,
            vcenter,
            vcenter_ip,
            vcenter_username,
            vcenter_password
        )
        if vc_handler is None:
            raise ErrorExit

        vm_definition = {}
        success = vc_handler.create(
            vm_definition,
            dry_run=dry_run
        )
        if not success:
            raise ErrorExit

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
