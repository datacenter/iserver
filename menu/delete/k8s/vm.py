import sys
import threading
import traceback
import click

from lib import file_helper

from menu import validations
from menu import progress


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("vm")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', type=click.STRING, help="Cluster Name")
@click.option("--file", "vm_filename", is_flag=False, show_default=False, default='', type=click.STRING, help="VM Definition YAML")
@click.option("--sriov", "include_sriov_policy", is_flag=True, show_default=True, default=False, help="Delete sriov policy")
@click.option("--image", "include_image", is_flag=True, show_default=True, default=False, help="Delete image")
@click.option("--verbose", is_flag=True, show_default=True, default=False, help="Verbose mode")
@click.option("--debug", is_flag=True, show_default=True, default=False, help="Debug mode")
def delete_k8s_vm_command(
        ctx,
        cluster_name,
        vm_filename,
        include_sriov_policy,
        include_image,
        verbose,
        debug
        ):
    """Delete OCP virtual machine"""

    # iocp delete ocp vm

    try:
        if debug:
            verbose = True
        ctx.my_output.set_flags(False, verbose, debug)

        ctx.busy = True
        threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        validated_input = validations.validate_ocp_vm_yaml_file(ctx, vm_filename)
        if validated_input is None:
            ctx.busy = False
            raise ErrorExit

        ocp_handler = validations.validate_ocp_cluster(
            ctx,
            cluster_name
        )
        if ocp_handler is None:
            raise ErrorExit

        ctx.busy = False

        if not ocp_handler.delete_vm_deployment(validated_input, include_sriov_policy=include_sriov_policy, include_image=include_image):
            raise ErrorExit

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
