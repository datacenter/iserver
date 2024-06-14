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


@click.command("pnet")
@click.pass_obj
@click.option("--vc", "vcenter", default='', callback=validations.validate_vc_name, help="vCenter name")
@click.option("--ip", "vcenter_ip", default='', callback=validations.validate_ip, help="vCenter IP")
@click.option("--username", "vcenter_username", default='', help="vCenter Username")
@click.option("--password", "vcenter_password", default='', help="vCenter Password")
@click.option("--name", default='', help="Host name")
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_vc_host_pnet_command(
        ctx,
        vcenter,
        vcenter_ip,
        vcenter_username,
        vcenter_password,
        name,
        output,
        devel
        ):
    """Get vc host net"""

    # iserver get vc host net

    ctx.developer = devel
    ctx.output = output

    try:
        if len(name) == 0:
            ctx.my_output.error(
                'Define vcenter host name'
            )
            raise ErrorExit

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

        hosts_obj = vc_handler.get_hosts_by_name(name, strict=False)
        if len(hosts_obj) is None or len(hosts_obj) == 0:
            ctx.busy = False
            ctx.my_output.error(
                'Host not found'
            )
            raise ErrorExit

        if len(hosts_obj) > 1:
            ctx.busy = False
            ctx.my_output.error(
                'Be more precise...'
            )
            for host_obj in hosts_obj:
                ctx.my_output.default('- %s' % (host_obj.name))

            raise ErrorExit

        ctx.busy = False

        info = vc_handler.get_host_networking(
            hosts_obj[0]
        )

        if output == 'json':
            ctx.log_prompt = False
            ctx.my_output.default(
                json.dumps(
                    info,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(info)

        vc_handler.print_host_phy_networking(
            info
        )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
