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


@click.command("cnfi")
@click.pass_obj
@click.option("--ncs", "ncs_name", default='', callback=validations.validate_ncs_name, help="NSO name")
@click.option("--protocol", "ncs_protocol", type=click.Choice(['http', 'https'], case_sensitive=False), default='http', show_default=True, help="Protocol")
@click.option("--ip", "ncs_ip", default='', callback=validations.validate_ip, help="NSO IP")
@click.option("--port", "ncs_port", default=8080, help="NSO Port")
@click.option("--username", "ncs_username", default='', help="NSO Username")
@click.option("--password", "ncs_password", default='', help="NSO Password")
@click.option("--restconf_disabled", is_flag=True, show_default=True, default=False, help="Restconf")
@click.option("--name", "cnfi_name", default='', help="Filter by CNFI name")
@click.option("--view", "-v", default=['state'], help="[state|ready|plan|device|result|pod|dep|rs|svc|vmi|k8s|all]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_nso_cnfi_command(
        ctx,
        ncs_name,
        ncs_protocol,
        ncs_ip,
        ncs_port,
        ncs_username,
        ncs_password,
        restconf_disabled,
        cnfi_name,
        view,
        output,
        devel
        ):
    """Get nso cnfi"""

    # iserver get cnfi

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'state|ready|plan|device|result|pod|dep|rs|svc|vmi|k8s|all',
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

        if cnfi_name is not None:
            object_filter.append(
                'name:%s' % (cnfi_name)
            )

        plan_info = False
        device_info = False
        result_info = False

        if 'state' in view:
            plan_info = True
            device_info = True
            result_info = True

        if 'ready' in view:
            plan_info = True

        if 'plan' in view:
            plan_info = True

        if 'device' in view:
            device_info = True

        if 'result' in view:
            result_info = True

        if 'pod' in view:
            result_info = True

        if 'dep' in view:
            result_info = True

        if 'rs' in view:
            result_info = True

        if 'svc' in view:
            result_info = True

        if 'vmi' in view:
            result_info = True

        if 'k8s' in view:
            result_info = True

        cnfis = nso_handler.get_cnfm_cnfis(
            object_filter=object_filter,
            plan_info=plan_info,
            result_info=result_info,
            device_info=device_info
        )

        ctx.busy = False

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    cnfis,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(cnfis)

        if 'state' in view:
            nso_output_handler.print_cnfm_cnfis(
                cnfis,
                title=True
            )

        if 'ready' in view:
            nso_output_handler.print_cnfm_cnfis_ready(
                cnfis,
                title=True
            )

        if 'plan' in view:
            nso_output_handler.print_cnfm_cnfis_plan(
                cnfis,
                title=True
            )

        if 'result' in view:
            nso_output_handler.print_cnfm_cnfis_result(
                cnfis,
                title=True
            )

        if 'rs' in view or 'k8s' in view:
            nso_output_handler.print_cnfm_cnfis_rs(
                cnfis,
                title=True
            )

        if 'dep' in view or 'k8s' in view:
            nso_output_handler.print_cnfm_cnfis_dep(
                cnfis,
                title=True
            )

        if 'pod' in view or 'k8s' in view:
            nso_output_handler.print_cnfm_cnfis_pod(
                cnfis,
                title=True
            )

        if 'vmi' in view or 'k8s' in view:
            nso_output_handler.print_cnfm_cnfis_vmi(
                cnfis,
                title=True
            )

        if 'svc' in view or 'k8s' in view:
            nso_output_handler.print_cnfm_cnfis_svc(
                cnfis,
                title=True
            )

        if 'device' in view:
            nso_output_handler.print_cnfm_cnfis_device(
                cnfis,
                title=True
            )

        ctx.my_output.default('\nViews: state (def), ready, plan, device, result, pod, dep, rs, svc, vmi, k8s, all')

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
