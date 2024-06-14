import os
import sys
import traceback
import click

from lib.ocp import settings

from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("kc")
@click.pass_obj
@click.option("--cluster", "cluster_name", callback=validations.empty_string_to_none, help="OCP cluster name")
@click.option("--file", "kubeconfig_filename", callback=validations.empty_string_to_none, help="Kubeconfig filename")
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
        settings_handler = settings.OcpSettings(log_id=ctx.run_id)

        if cluster_name is None:
            cluster_name = settings_handler.get_default_cluster()
            if cluster_name is None:
                ctx.my_output.error('Define OCP cluster name')
            raise ErrorExit

        if kubeconfig_filename is None:
            ctx.my_output.error('Define OCP kubeconfig filename')
            raise ErrorExit

        if not os.path.isfile(kubeconfig_filename):
            ctx.my_output.error('Kubeconfig file not found')
            raise ErrorExit

        cluster_settings = settings_handler.get_ocp_cluster(cluster_name, strict_match=False)
        if cluster_settings is None:
            success = settings_handler.create_ocp_cluster(
                cluster_name,
                kubeconfig_filename
            )
            if not success:
                ctx.my_output.error('Failed to create ocp cluster kubeconfig')
                raise ErrorExit

            ctx.my_output.default('OCP cluster kubeconfig created: %s' % (cluster_name))

        else:
            success = settings_handler.set_ocp_cluster_kubeconfig(
                cluster_name,
                kubeconfig_filename
            )
            if not success:
                ctx.my_output.error('Failed to update ocp cluster kubeconfig')
                raise ErrorExit

            ctx.my_output.default('OCP cluster kubeconfig set: %s' % (cluster_name))

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
