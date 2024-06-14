import sys
import threading
import traceback
import click

from lib.osp import output as osp_output

from menu import validations
from menu import progress
from progress.bar import Bar


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("vm")
@click.pass_obj
@click.option("--cluster", default='', help="OpenStack cluster name")
@click.option("--tenant", default='', callback=validations.empty_string_to_none, help="Filter by tenant")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Filter by name")
@click.option("--no-confirm", "no_confirm", is_flag=True, show_default=True, default=False, help="No confirmation mode")
def delete_osp_vm_command(
        ctx,
        cluster,
        tenant,
        name,
        no_confirm
        ):
    """Delete osp vm"""

    # iserver delete osp vm

    ctx.developer = False
    ctx.output = 'default'

    try:
        osp_output_handler = osp_output.OspOutput(log_id=ctx.run_id)
        osp_handlers = validations.validate_osp_name(ctx, cluster)
        if osp_handlers is None:
            raise ErrorExit

        object_filter = []

        if name is None and tenant is None:
            vms = osp_handlers.get_virtual_machines(
                tenant_info=True,
                flavor_info=True,
                image_info=True,
                volume_info=True,
                network_info=True,
                subnet_info=True
            )
            if vms is None or len(vms) == 0:
                ctx.my_output.default('No virtual machine found')
                raise ErrorExit

            selected_vm = osp_output_handler.select_virtual_machine(vms)
            if selected_vm is None:
                raise ErrorExit

            success = osp_handlers.delete_virtual_machine(selected_vm['id'])
            if not success:
                ctx.my_output.error('Virtual machine delete failed')
                raise ErrorExit

            ctx.my_output.default('Virtual machine deleted')
            return

        if tenant is not None:
            object_filter.append(
                'tenant:%s' % (tenant)
            )

        if name is not None:
            object_filter.append(
                'name:%s' % (name)
            )

        ctx.busy = True
        threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        vms = osp_handlers.get_virtual_machines(
            object_filter=object_filter,
            tenant_info=True,
            flavor_info=True,
            image_info=True,
            volume_info=True
        )

        if vms is None:
            ctx.my_output.error(
                'Failed to get virtual machines'
            )
            raise ErrorExit

        ctx.busy = False

        if len(vms) == 0:
            ctx.my_output.default('No virtual machines found')
            return

        osp_output_handler.print_virtual_machines(
            vms,
            title=True
        )

        if not no_confirm:
            value = input('Confirm (Y/N) ')
            if value.lower() != 'y':
                return

        bar_handler = Bar('Delete objects', max=len(vms))
        bar_handler.goto(0)

        success = True
        for vm_info in vms:
            success = success and osp_handlers.delete_virtual_machine(vm_info['id'])
            bar_handler.next()

        bar_handler.finish()

        if not success:
            ctx.my_output.error('Some delete api calls failed')
            raise ErrorExit

        ctx.my_output.default('Done')

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
