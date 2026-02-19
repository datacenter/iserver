import sys
import traceback
import click

from lib.ocp import settings

from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("connector")
@click.pass_obj
@click.option("--cluster", "cluster_name", default='', callback=validations.empty_string_to_none, help="OCP cluster name")
def delete_ocp_connector(
        ctx,
        cluster_name
        ):
    """Delete ocp cluster connector"""

    ctx.developer = False

    try:
        if cluster_name is None:
            ctx.my_output.error('Define cluster name')
            raise ErrorExit
        
        settings_handler = settings.OcpSettings(log_id=ctx.run_id)

        if not settings_handler.is_ocp_cluster(cluster_name):
            ctx.my_output.error('Cluster not found: %s' % (cluster_name))
            raise ErrorExit
        
        if not settings_handler.delete_ocp_cluster(cluster_name):
            ctx.my_output.error('Cluster delete failed: %s' % (cluster_name))
            raise ErrorExit
        
        ctx.my_output.default('Cluster deleted: %s' % (cluster_name))
        
    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
