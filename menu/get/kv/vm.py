import sys
import json
import threading
import traceback
import click

from lib.kubevirt import output as kubevirt_output

from menu import validations
from menu import progress


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("vm")
@click.pass_obj
@click.option("--cluster", default='', help="Kubernetes cluster name")
@click.option("--namespace", default='', callback=validations.empty_string_to_none, help="Filter by namespace")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Filter by name")
@click.option("--view", "-v", default=['state'], help="[state]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'mo', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_kubevirt_vm_command(
        ctx,
        cluster,
        namespace,
        name,
        view,
        output,
        devel
        ):
    """Get kubevirt virtual machine"""

    # iserver get kv vm

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
        kubevirt_output_handler = kubevirt_output.KubevirtOutput(log_id=ctx.run_id)
        kubevirt_handlers = validations.validate_kubevirt_name(ctx, cluster)
        if kubevirt_handlers is None:
            raise ErrorExit

        object_filter = []

        if namespace is not None:
            object_filter.append(
                'namespace:%s' % (namespace)
            )

        if name is not None:
            object_filter.append(
                'name:%s' % (name)
            )

        if output not in ['json', 'mo']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        if output == 'mo':
            virtual_machines = kubevirt_handlers.get_virtual_machines(
                object_filter=object_filter,
                return_mo=True
            )
            ctx.my_output.default(
                json.dumps(
                    virtual_machines,
                    indent=4
                )
            )
            return

        virtual_machines = kubevirt_handlers.get_virtual_machines(
            object_filter=object_filter
        )

        ctx.busy = False

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    virtual_machines,
                    indent=4
                )
            )
            return

        if 'state' in view:
            kubevirt_output_handler.print_virtual_machines(
                virtual_machines,
                title=True
            )

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
