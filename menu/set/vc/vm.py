import sys
import threading
import traceback
import click

from menu.common import get_confirmation
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
@click.option("--name", "vm_name_filter", default='', help="VM name loose match filter")
@click.option("--host", "host_filter", default='', help="Host loose match filter")
@click.option("--state", "-s", type=click.Choice(['none', 'on', 'off'], case_sensitive=False), default='none', show_default=True)
@click.option("--output", "-o", type=click.Choice(['default'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def set_vc_vm_command(
        ctx,
        vcenter,
        vcenter_ip,
        vcenter_username,
        vcenter_password,
        vm_name_filter,
        host_filter,
        state,
        output,
        devel
        ):
    """Set vc vm"""

    ctx.developer = devel
    ctx.output = output

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

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        vm_filter = []
        if len(vm_name_filter) > 0:
            vm_filter.append(
                'name:%s' % (vm_name_filter)
            )

        if len(host_filter) > 0:
            vm_filter.append(
                'host:%s' % (host_filter)
            )

        vms = vc_handler.get_vms(
            vm_filter=vm_filter
        )

        ctx.busy = False

        ctx.my_output.json_output(vms)

        vc_handler.print_vms(
            vms,
            title=True
        )

        if get_confirmation():
            if state == 'on':
                for vm in vms:
                    if vm['powerState'] == 'poweredOff':
                        ctx.my_output.default('Power on: %s' % (vm['name']))
                        if not vc_handler.power_on_vm(vm['name']):
                            ctx.my_output.error('Failed')

                    else:
                        ctx.my_output.default('Skipping power on %s [%s]' % (vm['name'], vm['powerState']))

            if state == 'off':
                for vm in vms:
                    if vm['powerState'] != 'poweredOff':
                        ctx.my_output.default('Power off: %s' % (vm['name']))
                        if not vc_handler.power_off_vm(vm['name']):
                            ctx.my_output.error('Failed')

                    else:
                        ctx.my_output.default('Skipping power off %s [%s]' % (vm['name'], vm['powerState']))

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
