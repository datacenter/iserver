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


@click.command("snap")
@click.pass_obj
@click.option("--cluster", default='', help="Openstack cluster name")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Filter by snapshot name")
@click.option("--tenant", default='', callback=validations.empty_string_to_none, help="Filter by tenant name")
@click.option("--vol", default='', callback=validations.empty_string_to_none, help="Filter by volume name")
@click.option("--view", "-v", default=['state'], help="[state|id|all]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_osp_snap_command(
        ctx,
        cluster,
        name,
        tenant,
        vol,
        view,
        output,
        devel
        ):
    """Get osp snapshot"""

    # iserver get osp snap

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'state|id|all',
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

        tenant_info = False
        volume_info = False

        if 'state' in view:
            tenant_info = True
            volume_info = True

        object_filter = []

        if name is not None:
            object_filter.append(
                'name:%s' % (name)
            )

        if tenant is not None:
            tenant_info = True
            object_filter.append(
                'tenant_name:%s' % (tenant)
            )

        if vol is not None:
            volume_info = True
            object_filter.append(
                'volume_name:%s' % (vol)
            )

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        snapshots = osp_handlers.get_snapshots(
            object_filter=object_filter,
            tenant_info=tenant_info,
            volume_info=volume_info
        )

        ctx.busy = False

        if snapshots is None:
            ctx.my_output.error(
                'Failed to get snapshots'
            )
            raise ErrorExit

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    snapshots,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(snapshots)

        if 'state' in view:
            osp_output_handler.print_snapshots(
                snapshots,
                title=True
            )

        if 'id' in view:
            osp_output_handler.print_snapshots_id(
                snapshots,
                title=True
            )

        ctx.my_output.default('Filter: name, tenant, vol', before_newline=True)
        ctx.my_output.default('View:   state (def), id, all')

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
