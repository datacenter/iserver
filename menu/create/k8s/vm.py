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


@click.command("vm")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', type=click.STRING, help="Cluster Name")
@click.option("--file", "vm_filename", is_flag=False, show_default=False, default='', type=click.STRING, help="VM Definition YAML")
@click.option("--report", is_flag=True, show_default=True, default=False, help="Enable report")
@click.option("--verbose", is_flag=True, show_default=True, default=False, help="Verbose mode")
@click.option("--debug", is_flag=True, show_default=True, default=False, help="Debug mode")
def create_k8s_vm_command(
        ctx,
        cluster_name,
        vm_filename,
        report,
        verbose,
        debug
        ):
    """Create virtual machine"""

    try:
        if debug:
            verbose = True
        ctx.my_output.set_flags(False, verbose, debug)

        if len(vm_filename) == 0:
            ctx.my_output.error('Define VM definition yaml location')
            raise ErrorExit

        settings = validations.validate_ocp_cluster_settings(ctx, cluster_name, silent=True)
        if settings is None:
            raise ErrorExit

        if settings['tools'] is None:
            ctx.my_output.error('Tools not defined for cluster %s' % (settings['name']))
            raise ErrorExit

        if settings['virtctl'] is None:
            ctx.my_output.error('Virtctl not defined for cluster %s' % (settings['name']))
            raise ErrorExit

        ctx.my_output.default('Validate vm deployment file')
        validated_input = validations.validate_ocp_vm_yaml_file(ctx, vm_filename)
        if validated_input is None:
            ctx.busy = False
            raise ErrorExit

        ctx.my_output.default('Validate ocp cluster')
        ocp_handler = validations.validate_ocp_cluster(
            ctx,
            cluster_name
        )
        if ocp_handler is None:
            raise ErrorExit

        if not ocp_handler.create_vm_deployment(validated_input, report=report):
            raise ErrorExit

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
