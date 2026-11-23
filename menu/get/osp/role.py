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


@click.command("role")
@click.pass_obj
@click.option("--cluster", default='', help="Openstack cluster name")
@click.option("--view", "-v", default=['state'], help="[state]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_osp_role_command(
        ctx,
        cluster,
        view,
        output,
        devel
        ):
    """Get osp role"""

    # iserver get osp role

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

        object_filter = []

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        roles = osp_handlers.get_roles(
            object_filter=object_filter
        )

        ctx.busy = False

        if roles is None:
            ctx.my_output.error(
                'Failed to get roles'
            )
            raise ErrorExit

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    roles,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(roles)

        if 'state' in view:
            osp_output_handler.print_roles(
                roles,
                title=True
            )

        ctx.my_output.default('Filter: --', before_newline=True)
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
