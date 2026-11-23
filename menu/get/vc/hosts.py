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


@click.command("hosts")
@click.pass_obj
@click.option("--vc", "vcenter", default='', callback=validations.validate_vc_name, help="vCenter name")
@click.option("--ip", "vcenter_ip", default='', callback=validations.validate_ip, help="vCenter IP")
@click.option("--username", "vcenter_username", default='', help="vCenter Username")
@click.option("--password", "vcenter_password", default='', help="vCenter Password")
@click.option("--name", "host_name_filter", default='', help="Host name loose match filter")
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_vc_hosts_command(
        ctx,
        vcenter,
        vcenter_ip,
        vcenter_username,
        vcenter_password,
        host_name_filter,
        output,
        devel
        ):
    """Get vc hosts"""

    # iserver get vc hosts

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

        host_filter = []
        if len(host_name_filter) > 0:
            host_filter.append(
                'name:%s' % (host_name_filter)
            )

        hosts = vc_handler.get_hosts_summary(
            host_filter=host_filter
        )

        ctx.busy = False

        if output == 'json':
            ctx.log_prompt = False
            ctx.my_output.default(
                json.dumps(
                    hosts,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(hosts)

        vc_handler.print_hosts_summary(
            hosts,
            title=True
        )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
