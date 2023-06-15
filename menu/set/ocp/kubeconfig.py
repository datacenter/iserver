import os
import sys
import traceback
import click

from lib.ocp import settings


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("kc")
@click.pass_obj
@click.option("--name", "cluster_name", default='', help="OCP cluster name")
@click.option("--kc", "kubeconfig_filename", default='', help="Kubeconfig filename")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def set_ocp_kubeconfig(
        ctx,
        cluster_name,
        kubeconfig_filename,
        devel
        ):
    """Set ocp cluster kubeconfig"""

    # iserver set ocp kc

    ctx.developer = devel

    try:
        if len(cluster_name) == 0:
            ctx.my_output.error('Define OCP cluster name')
            raise ErrorExit

        if len(kubeconfig_filename) == 0:
            ctx.my_output.error('Define OCP kubeconfig filename')
            raise ErrorExit

        if not os.path.isfile(kubeconfig_filename):
            ctx.my_output.error('Kubeconfig file not found')
            raise ErrorExit

        settings_handler = settings.OcpSettings(log_id=ctx.run_id)
        success = settings_handler.set_ocp_cluster(
            cluster_name,
            kubeconfig_filename
        )
        if not success:
            ctx.my_output.error('Failed to define ocp cluster kubeconfig')
            raise ErrorExit

        ctx.my_output.default('OCP cluster access created: %s' % (cluster_name))

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
