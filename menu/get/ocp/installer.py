import sys
import json
import traceback
import threading
import click

from menu import progress
from menu import validations

from lib.ocp.state.installer import main as ocp_installer


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("installer")
@click.pass_obj
@click.option("--name", "cluster_name", default='', callback=validations.empty_string_to_none, help="Filter by cluster name")
@click.option("--verify", is_flag=True, show_default=True, default=False, help="Verify SSH access")
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_ocp_installer_command(
        ctx,
        cluster_name,
        verify,
        output,
        devel
        ):
    """Get ocp installer"""

    # iserver get ocp installer

    ctx.developer = devel
    ctx.output = output

    try:
        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        ocp_installer_handler = ocp_installer.OcpInstaller(
            log_id=ctx.run_id
        )

        cluster_filter = []

        if cluster_name is not None:
            cluster_filter.append(
                'name:%s' % (cluster_name)
            )

        clusters = ocp_installer_handler.get_ocp_clusters_installer(
            cluster_filter=cluster_filter,
            validate_info=verify
        )
        if clusters is None:
            ctx.busy = False
            ctx.my_output.error('Failed to get OCP clusters')
            raise ErrorExit

        if output == 'json':
            ctx.busy = False
            ctx.log_prompt = False
            ctx.my_output.default(
                json.dumps(
                    clusters,
                    indent=4
                )
            )
            return

        ctx.busy = False
        ctx.my_output.json_output(clusters)

        ocp_installer_handler.print_ocp_clusters_installer(
            clusters
        )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
