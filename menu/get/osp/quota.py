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


@click.command("quota")
@click.pass_obj
@click.option("--cluster", default='', help="Openstack cluster name")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Filter by tenant name")
@click.option("--view", "-v", default=['state'], help="[state]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_osp_quota_command(
        ctx,
        cluster,
        name,
        view,
        output,
        devel
        ):
    """Get osp quota"""

    # iserver get osp quota

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
        osp_output_handler = osp_output.OspOutput(log_id=ctx.run_id)
        osp_handlers = validations.validate_osp_name(ctx, cluster)
        if osp_handlers is None:
            raise ErrorExit

        tenant_info = False

        if 'state' in view:
            tenant_info = True

        object_filter = []

        if name is not None:
            tenant_info = True
            object_filter.append(
                'tenant_name:%s' % (name)
            )

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        quotas = osp_handlers.get_quotas(
            object_filter=object_filter,
            tenant_info=tenant_info
        )

        ctx.busy = False

        if quotas is None:
            ctx.my_output.error(
                'Failed to get quotas'
            )
            raise ErrorExit

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    quotas,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(quotas)

        if 'state' in view:
            osp_output_handler.print_quotas(
                quotas,
                title=True
            )

        ctx.my_output.default('Filter: name', before_newline=True)
        ctx.my_output.default('View:   state (def)')

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
