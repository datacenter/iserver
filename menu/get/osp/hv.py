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


@click.command("hv")
@click.pass_obj
@click.option("--cluster", default='', help="Openstack cluster name")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Filter by name")
@click.option("--address", default='', callback=validations.validate_ip_subnet, help="Filter by ip address")
@click.option("--vm", "virtual_machine", default='', callback=validations.empty_string_to_none, help="Filter by virtual machine")
@click.option("--view", "-v", default=['state'], help="[state|vm|all]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_osp_hv_command(
        ctx,
        cluster,
        name,
        address,
        virtual_machine,
        view,
        output,
        devel
        ):
    """Get osp hypervisor"""

    # iserver get osp hv

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'state|vm|all',
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

        vm_info = False

        if 'vm' in view:
            vm_info = True

        object_filter = []

        if name is not None:
            object_filter.append('name:%s' % (name))

        if len(address) > 0:
            object_filter.append('address:%s' % (address))

        if virtual_machine is not None:
            vm_info = True
            object_filter.append('vm:%s' % (virtual_machine))

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        hvs = osp_handlers.get_hypervisors(
            object_filter=object_filter,
            vm_info=vm_info
        )

        ctx.busy = False

        if hvs is None:
            ctx.my_output.error(
                'Failed to get hypervisors'
            )
            raise ErrorExit

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    hvs,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(hvs)

        if 'state' in view:
            osp_output_handler.print_hypervisors(
                hvs,
                title=True
            )

        if 'vm' in view:
            osp_output_handler.print_hypervisors_vm(
                hvs,
                title=True
            )

        ctx.my_output.default('Filter: name, address, vm', before_newline=True)
        ctx.my_output.default('View:   state (def), vm, all')

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
