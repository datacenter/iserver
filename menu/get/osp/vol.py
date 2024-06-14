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


@click.command("vol")
@click.pass_obj
@click.option("--cluster", default='', help="Openstack cluster name")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Filter by name")
@click.option("--tenant", default='', callback=validations.empty_string_to_none, help="Filter by tenant name")
@click.option("--hv", "hypervisor", default='', callback=validations.empty_string_to_none, help="Filter by hypervisor")
@click.option("--vm", "virtual_machine", default='', callback=validations.empty_string_to_none, help="Filter by virtual machine")
@click.option("--view", "-v", default=['state'], help="[state|id|all]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_osp_vol_command(
        ctx,
        cluster,
        name,
        tenant,
        hypervisor,
        virtual_machine,
        view,
        output,
        devel
        ):
    """Get osp volume"""

    # iserver get osp vol

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
        vm_info = False

        if 'state' in view:
            tenant_info = True
            vm_info = True

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

        if hypervisor is not None:
            vm_info = True
            object_filter.append(
                'hv:%s' % (hypervisor)
            )

        if virtual_machine is not None:
            vm_info = True
            object_filter.append(
                'vm_name:%s' % (virtual_machine)
            )

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        volumes = osp_handlers.get_volumes(
            object_filter=object_filter,
            tenant_info=tenant_info,
            vm_info=vm_info
        )

        ctx.busy = False

        if volumes is None:
            ctx.my_output.error(
                'Failed to get volumes'
            )
            raise ErrorExit

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    volumes,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(volumes)

        if 'state' in view:
            osp_output_handler.print_volumes(
                volumes,
                title=True
            )

        if 'id' in view:
            osp_output_handler.print_volumes_id(
                volumes,
                title=True
            )

        ctx.my_output.default('Filter: name, tenant, hv, vm', before_newline=True)
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
