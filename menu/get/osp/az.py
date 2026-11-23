import sys
import json
import threading
import traceback
import click

from lib.osp import output as osp_output

from menu import validations
from menu import progress


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("az")
@click.pass_obj
@click.option("--cluster", default='', help="Openstack cluster name")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Filter by az name")
@click.option("--hv", "hypervisor", default='', callback=validations.empty_string_to_none, help="Filter by hypervisor")
@click.option("--view", "-v", default=['state'], help="[state|hv|all]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_osp_az_command(
        ctx,
        cluster,
        name,
        hypervisor,
        view,
        output,
        devel
        ):
    """Get osp availability zone"""

    # iserver get osp az

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'state|hv|all',
        'state',
        []
    )
    if view is None:
        sys.exit(1)

    try:
        osp_output_handler = osp_output.OspOutput(log_id=ctx.run_id)
        osp_handlers = validations.validate_osp_name(ctx, cluster)
        if osp_handlers is None:
            raise ErrorExit

        hv_info = False

        if 'hv' in view:
            hv_info = True

        object_filter = []

        if name is not None:
            object_filter.append(
                'name:%s' % (name)
            )

        if hypervisor is not None:
            object_filter.append(
                'hv:%s' % (hypervisor)
            )

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        availability_zones = osp_handlers.get_availability_zones(
            object_filter=object_filter,
            hv_info=hv_info
        )

        ctx.busy = False

        if availability_zones is None:
            ctx.my_output.error(
                'Failed to get availability zones'
            )
            raise ErrorExit

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    availability_zones,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(availability_zones)

        if 'state' in view:
            osp_output_handler.print_availability_zones(
                availability_zones,
                title=True
            )

        if 'hv' in view:
            osp_output_handler.print_availability_zones_hv(
                availability_zones,
                title=True
            )

        ctx.my_output.default('Filter: name, hv', before_newline=True)
        ctx.my_output.default('View:   state (def), hv, all')

    except NoResultExit:
        ctx.busy = False
        sys.exit(666)

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
