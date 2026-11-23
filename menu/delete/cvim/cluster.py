import sys
import traceback
import click

from lib.cvim import settings


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("cluster")
@click.pass_obj
@click.option("--cluster", "cluster_name", default='', help="K8s cluster name")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def delete_cvim_cluster(
        ctx,
        cluster_name,
        devel
        ):
    """Delete cvim cluster"""

    # iserver delete cvim cluster

    ctx.developer = devel

    try:
        settings_handler = settings.CvimSettings(log_id=ctx.run_id)
        cluster = settings_handler.get_cvim_cluster(cluster_name)

        if cluster is None:
            ctx.my_output.default('Cisco VIM cluster not defined')
            raise ErrorExit

        if not settings_handler.delete_cvim_cluster(cluster_name):
            ctx.my_output.default('Cisco VIM cluster delete failed')
            raise ErrorExit

        ctx.my_output.default('Cisco VIM cluster deleted')

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
