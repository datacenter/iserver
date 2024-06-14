import sys
import traceback
import click

from lib.vc import virtual_machine_deployment_validator

from menu import validations
from menu import common


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
@click.option("--dir", "vm_directory", is_flag=False, show_default=False, default='', type=click.STRING, help="VM definition directory")
@click.option("--dry-run", is_flag=True, show_default=True, default=False, help="Dry run")
@click.option("--verbose", is_flag=True, show_default=True, default=False, help="Verbose mode")
@click.option("--debug", is_flag=True, show_default=True, default=False, help="Debug mode")
def create_vc_vm_command(
        ctx,
        vcenter,
        vcenter_ip,
        vcenter_username,
        vcenter_password,
        vm_directory,
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

        ctx.my_output.default('Validate virtual machine deployment definition...')
        vm_input_validator_handler = virtual_machine_deployment_validator.VcVirtualMachineDeploymentValidator(
            log_id=ctx.run_id,
            verbose=verbose,
            debug=debug
        )
        vm_parameters = vm_input_validator_handler.validate_create(vm_directory)
        if vm_parameters is None:
            raise ErrorExit

        ctx.my_output.default('Creating virtual machine...')
        success = vc_handler.create_vm_deployment(
            vm_parameters,
            screen_base_directory=ctx.log.logs_directory,
            dry_run=dry_run
        )
        if not success:
            raise ErrorExit

        ctx.my_output.default('Done')

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
