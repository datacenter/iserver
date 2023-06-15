import sys
import threading
import traceback
import click

from menu import validations
from menu import progress


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("down")
@click.pass_obj
@click.option("--cluster", "cluster_name", default='', help="OCP cluster name")
@click.option("--name", "vm_name", default='', help="Virtual machine name")
@click.option("--namespace", is_flag=False, show_default=False, default='', type=click.STRING, help="Namespace")
@click.option("--no-wait", is_flag=True, show_default=True, default=False, help="No wait")
@click.option("--verbose", is_flag=True, show_default=True, default=False, help="Verbose output")
@click.option("--debug", is_flag=True, show_default=True, default=False, help="Debug output")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def set_ocp_vm_down(
        ctx,
        cluster_name,
        vm_name,
        namespace,
        no_wait,
        verbose,
        debug,
        devel
        ):
    """Set ocp cluster vm down"""

    # iserver set ocp vm down

    ctx.developer = devel

    try:
        if len(vm_name) == 0:
            ctx.my_output.error('Define VM name')
            raise ErrorExit

        ctx.busy = True
        threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        ocp_handler = validations.validate_ocp_cluster(
            ctx,
            cluster_name,
            verbose=verbose,
            debug=debug
        )
        if ocp_handler is None:
            raise ErrorExit

        namespace = validations.validate_ocp_vm_namespace(
            ctx,
            ocp_handler,
            namespace,
            vm_name
        )
        if namespace is None:
            raise ErrorExit

        if not ocp_handler.is_ocp_vmi_mo(namespace, vm_name):
            ctx.my_output.default('Virtual machine already down')
            return

        ctx.my_output.default('Stop virtual machine...')
        if not ocp_handler.stop_ocp_vm(namespace, vm_name):
            ctx.my_output.error('Virtual machine stop failed')
            raise ErrorExit

        ctx.my_output.default('Virtual machine stopped')

        if not no_wait:
            ctx.my_output.default('Wait for virtual machine stopped...')
            if not ocp_handler.wait_ocp_vm_stopped(namespace, vm_name):
                ctx.my_output.error('Timed out')
                raise ErrorExit

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
