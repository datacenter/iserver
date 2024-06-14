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


@click.command("flv")
@click.pass_obj
@click.option("--cluster", default='', help="Openstack cluster name")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Filter by flavor name")
@click.option("--vm", "virtual_machine", default='', callback=validations.empty_string_to_none, help="Filter by virtual machine name")
@click.option("--key", "key", default='', callback=validations.empty_string_to_none, help="Filter by key")
@click.option("--value", "value", default='', callback=validations.empty_string_to_none, help="Filter by value")
@click.option("--view", "-v", default=['state'], help="[state|key|vm|id|all]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_osp_flv_command(
        ctx,
        cluster,
        name,
        virtual_machine,
        key,
        value,
        view,
        output,
        devel
        ):
    """Get osp flavor"""

    # iserver get osp flv

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'state|key|vm|id|all',
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

        keys_info = False
        vm_info = False

        if 'key' in view:
            keys_info = True

        if 'vm' in view:
            vm_info = True

        object_filter = []

        if name is not None:
            object_filter.append(
                'name:%s' % (name)
            )

        if virtual_machine is not None:
            vm_info = True
            object_filter.append(
                'vm:%s' % (virtual_machine)
            )

        if key is not None:
            keys_info = True
            object_filter.append(
                'key:%s' % (key)
            )

        if value is not None:
            keys_info = True
            object_filter.append(
                'value:%s' % (value)
            )

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        flavors = osp_handlers.get_flavors(
            object_filter=object_filter,
            keys_info=keys_info,
            vm_info=vm_info
        )

        ctx.busy = False

        if flavors is None:
            ctx.my_output.error(
                'Failed to get flavors'
            )
            raise ErrorExit

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    flavors,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(flavors)

        if 'state' in view or 'key' in view:
            osp_output_handler.print_flavors(
                flavors,
                title=True
            )

        if 'id' in view:
            osp_output_handler.print_flavors_id(
                flavors,
                title=True
            )

        if 'vm' in view:
            osp_output_handler.print_flavors_vm(
                flavors,
                title=True
            )

        ctx.my_output.default('Filter: name, vm, key, value', before_newline=True)
        ctx.my_output.default('View:   state (def), id, key, vm, all')

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
