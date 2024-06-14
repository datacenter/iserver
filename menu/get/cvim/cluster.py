import sys
import threading
import traceback
import click

from lib.cvim import settings

from menu import progress


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("cluster")
@click.pass_obj
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_cvim_cluster(
        ctx,
        devel
        ):
    """Get cvim cluster settings"""

    # iserver get cvim cluster

    ctx.developer = devel

    try:
        settings_handler = settings.CvimSettings(log_id=ctx.run_id)
        clusters = settings_handler.get_cvim_clusters()

        if clusters is None or len(clusters) == 0:
            ctx.my_output.default('No cisco vim clusters defined')
            return

        default_cluster_name = settings_handler.get_default_cluster()
        if default_cluster_name is not None:
            for cluster in clusters:
                cluster['__Output'] = {}
                if cluster['name'] == default_cluster_name:
                    cluster['__Output']['defaultTick'] = 'Green'
                    cluster['defaultTick'] = '\u2713'

        order = [
            'name',
            'defaultTick',
            'openrc',
        ]

        headers = [
            'Cluster Name',
            'Default',
            'Openrc'
        ]

        ctx.my_output.my_table(
            clusters,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=False,
            table=True
        )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
