import sys
import json
import threading
import traceback
import click

from lib.xd import vc2fabric

from menu import validations
from menu import progress


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("vms")
@click.pass_obj
@click.option("--vc", "vcenter", default='', callback=validations.validate_vc_name, help="vCenter name")
@click.option("--ip", "vcenter_ip", default='', callback=validations.validate_ip, help="vCenter IP")
@click.option("--username", "vcenter_username", default='', help="vCenter Username")
@click.option("--password", "vcenter_password", default='', help="vCenter Password")
@click.option("--name", "vm_name_filter", default='', help="VM name loose match filter")
@click.option("--host", "host_filter", default='', help="Host loose match filter")
@click.option("--net", is_flag=True, show_default=True, default=False, help="Show network details")
@click.option("--fabric", is_flag=True, show_default=True, default=False, help="Show fabric details")
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_vc_vms_command(
        ctx,
        vcenter,
        vcenter_ip,
        vcenter_username,
        vcenter_password,
        vm_name_filter,
        host_filter,
        net,
        fabric,
        output,
        devel
        ):
    """Get vc vms"""

    # iserver get vc vms

    ctx.developer = devel
    ctx.output = output
    if fabric:
        net = False

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

        if fabric:
            vms = vc2fabric.add_vms_fabric_connections(
                vms,
                log_id=ctx.run_id
            )

        ctx.busy = False

        if output == 'json':
            ctx.log_prompt = False
            ctx.my_output.default(
                json.dumps(
                    vms,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(vms)

        if fabric:
            vc_handler.print_vms_fabric(
                vms
            )

        if net:
            vc_handler.print_vms_net(
                vms
            )

        if not fabric and not net:
            vc_handler.print_vms(
                vms,
                title=True
            )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
