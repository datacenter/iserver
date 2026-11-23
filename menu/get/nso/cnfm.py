import sys
import json
import threading
import traceback
import click

from lib.nso import output as nso_output

from menu import validations
from menu import progress


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("cnfm")
@click.pass_obj
@click.option("--ncs", "ncs_name", default='', callback=validations.validate_ncs_name, help="NSO name")
@click.option("--protocol", "ncs_protocol", type=click.Choice(['http', 'https'], case_sensitive=False), default='http', show_default=True, help="Protocol")
@click.option("--ip", "ncs_ip", default='', callback=validations.validate_ip, help="NSO IP")
@click.option("--port", "ncs_port", default=8080, help="NSO Port")
@click.option("--username", "ncs_username", default='', help="NSO Username")
@click.option("--password", "ncs_password", default='', help="NSO Password")
@click.option("--restconf_disabled", is_flag=True, show_default=True, default=False, help="Restconf")
@click.option("--name", "cnfm_name", default='', callback=validations.empty_string_to_none, help="Filter by cnfm name")
@click.option("--view", "-v", default=['state'], help="[state|cluster|all]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_nso_cnfm_command(
        ctx,
        ncs_name,
        ncs_protocol,
        ncs_ip,
        ncs_port,
        ncs_username,
        ncs_password,
        restconf_disabled,
        cnfm_name,
        view,
        output,
        devel
        ):
    """Get nso cnfm"""

    # iserver get nso cnfm

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'state|cluster|device|all',
        'state',
        []
    )
    if view is None:
        sys.exit(1)

    try:
        nso_output_handler = nso_output.NsoOutput(
            verbose=False,
            debug=devel,
            log_id=ctx.run_id
        )
        nso_handler = validations.validate_nso(
            ctx,
            ncs_name,
            ncs_protocol,
            ncs_ip,
            ncs_port,
            ncs_username,
            ncs_password,
            not restconf_disabled
        )
        if nso_handler is None:
            raise ErrorExit

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        object_filter = []

        if cnfm_name is not None:
            object_filter.append(
                'name:%s' % (cnfm_name)
            )

        cnfi_info = False
        device_info = False

        if 'state' in view:
            cnfi_info = True
            device_info = True

        if 'cluster' in view:
            cnfi_info = True

        devices = nso_handler.get_cnfm_devices(
            object_filter=object_filter,
            cnfi_info=cnfi_info,
            device_info=device_info
        )

        ctx.busy = False

        if devices is None:
            ctx.my_output.error('Failed to get cnfm device information')
            raise ErrorExit

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    devices,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(devices)

        if 'state' in view:
            nso_output_handler.print_cnfm_state(
                devices,
                title=True
            )

        if 'cluster' in view:
            nso_output_handler.print_cnfm_clusters(
                devices,
                title=True
            )

        ctx.my_output.default('Filter: name', before_newline=True)
        ctx.my_output.default('View:   state (def), cluster, all')

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
