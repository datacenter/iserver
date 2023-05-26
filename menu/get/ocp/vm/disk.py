import sys
import json
import threading
import traceback
import click

from menu import validations
from menu import progress

from lib.kubevirt import main as kubevirt


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("disk")
@click.pass_obj
@click.option("--cluster", "cluster_name", default='', help="OCP cluster name")
@click.option("--name", "vm_name", default='', help="Virtual machine name")
@click.option("--namespace", is_flag=False, show_default=False, default='', type=click.STRING, help="Namespace")
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--verbose", is_flag=True, show_default=True, default=False, help="Verbose output")
@click.option("--debug", is_flag=True, show_default=True, default=False, help="Debug output")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_ocp_vm_disk_command(
        ctx,
        cluster_name,
        vm_name,
        namespace,
        output,
        verbose,
        debug,
        devel
        ):
    """Get ocp virtual machine disks"""

    # iserver get ocp vm disks

    ctx.developer = devel
    ctx.output = output

    try:
        if len(vm_name) == 0:
            ctx.my_output.error('Define virtual machine name')
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

        if not ocp_handler.is_ocp_vm(namespace, vm_name):
            ctx.my_output.default('Virtual machine does not exist')
            raise ErrorExit

        info = ocp_handler.get_ocp_vm_disks_info(
            namespace,
            vm_name
        )
        ctx.busy = False

        if info is None:
            ctx.my_output.error(
                'Failed to get information'
            )
            raise ErrorExit

        if output == 'json':
            ctx.log_prompt = False
            ctx.my_output.default(
                json.dumps(
                    info,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(info)
        ocp_handler.print_ocp_vm_disks_info(
            info,
            show_vm_info=verbose
        )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
