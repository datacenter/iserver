import sys
import traceback
import click

from lib.vc import virtual_machine_deployment_validator
from lib.vc import vcenter

from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("vm")
@click.pass_obj
@click.option("--vc", "vcenter_name", default='', callback=validations.validate_vc_name, help="vCenter name")
@click.option("--ip", "vcenter_ip", default='', callback=validations.validate_ip, help="vCenter IP")
@click.option("--username", "vcenter_username", default='', help="vCenter Username")
@click.option("--password", "vcenter_password", default='', help="vCenter Password")
@click.option("--name", "vm_name", is_flag=False, show_default=False, default='', type=click.STRING, help="VM name")
@click.option("--dir", "vm_directory", is_flag=False, show_default=False, default='', type=click.STRING, help="VM definition directory")
@click.option("--verbose", is_flag=True, show_default=True, default=False, help="Verbose mode")
@click.option("--debug", is_flag=True, show_default=True, default=False, help="Debug mode")
def delete_vc_vm_command(
        ctx,
        vcenter_name,
        vcenter_ip,
        vcenter_username,
        vcenter_password,
        vm_name,
        vm_directory,
        verbose,
        debug
        ):
    """Delete vCehter virtual machine"""

    try:
        if len(vm_directory) == 0 and len(vm_name) == 0:
            ctx.my_output.error(
                'Define vm by name or definition directory'
            )
            raise ErrorExit

        if len(vm_directory) > 0 and len(vm_name) > 0:
            ctx.my_output.error(
                'Define vm by name or definition directory'
            )
            raise ErrorExit

        if len(vm_name) > 0:
            vc_handler = validations.validate_vcenter(
                ctx,
                vcenter_name,
                vcenter_ip,
                vcenter_username,
                vcenter_password
            )
            if vc_handler is None:
                raise ErrorExit

            ctx.my_output.default('Delete virtual machine...')
            success = vc_handler.delete_vm(
                name=vm_name
            )
            if not success:
                raise ErrorExit

        if len(vm_directory) > 0:
            ctx.my_output.default('Validate virtual machine definition...')

            vm_input_validator_handler = virtual_machine_deployment_validator.VcVirtualMachineDeploymentValidator(
                log_id=ctx.run_id,
                verbose=verbose,
                debug=debug
            )
            vm_parameters = vm_input_validator_handler.validate_delete(vm_directory)
            if vm_parameters is None:
                raise ErrorExit

            vc_handler = vcenter.Vcenter(
                vm_parameters['vcenter']['ip'],
                vm_parameters['vcenter']['username'],
                vm_parameters['vcenter']['password'],
                port=vm_parameters['vcenter']['port'],
                log_id=ctx.run_id
            )
            if not vc_handler.is_vc_connected():
                ctx.my_output.error('Vcenter connection failed')
                raise ErrorExit

            ctx.my_output.default('Delete virtual machine deployment...')
            success = vc_handler.delete_vm_deployment(
                vm_parameters
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
