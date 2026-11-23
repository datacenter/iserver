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


@click.command("cnfd")
@click.pass_obj
@click.option("--ncs", "ncs_name", default='', callback=validations.validate_ncs_name, help="NSO name")
@click.option("--protocol", "ncs_protocol", type=click.Choice(['http', 'https'], case_sensitive=False), default='http', show_default=True, help="Protocol")
@click.option("--ip", "ncs_ip", default='', callback=validations.validate_ip, help="NSO IP")
@click.option("--port", "ncs_port", default=8080, help="NSO Port")
@click.option("--username", "ncs_username", default='', help="NSO Username")
@click.option("--password", "ncs_password", default='', help="NSO Password")
@click.option("--restconf_disabled", is_flag=True, show_default=True, default=False, help="Restconf")
@click.option("--name", "cnfd_name", default='', help="Filter by CNFD name")
@click.option("--chart", "chart_name", default='', help="Filter by chart name")
@click.option("--version", "chart_version", default='', help="Filter by chart version")
@click.option("--view", "-v", default=['state'], help="[state]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_nso_cnfd_command(
        ctx,
        ncs_name,
        ncs_protocol,
        ncs_ip,
        ncs_port,
        ncs_username,
        ncs_password,
        restconf_disabled,
        cnfd_name,
        chart_name,
        chart_version,
        view,
        output,
        devel
        ):
    """Get nso cnfd"""

    # iserver get cnfd

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'state',
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

        if cnfd_name is not None:
            object_filter.append(
                'name:%s' % (cnfd_name)
            )

        if chart_name is not None:
            object_filter.append(
                'chart:%s' % (chart_name)
            )

        if chart_version is not None:
            object_filter.append(
                'version:%s' % (chart_version)
            )

        cnfds = nso_handler.get_cnfm_cnfds(
            object_filter=object_filter,
            cnfi_info=True
        )

        ctx.busy = False

        if cnfds is None:
            ctx.my_output.error(
                'Failed to CNFD'
            )
            raise ErrorExit

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    cnfds,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(cnfds)

        if 'state' in view:
            nso_output_handler.print_cnfm_cnfds(
                cnfds,
                title=True
            )

        ctx.my_output.default('\nViews: state (def)')

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
