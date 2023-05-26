import sys
import json
import traceback
import threading
import click

from menu import progress

from lib.ocp import settings
from lib.iwo.lcm import main as iwo


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("iwo")
@click.pass_obj
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_ocp_clusters_iwo_command(ctx, output, devel):
    """Get ocp clusters iwo addon"""

    # iserver get ocp clusters iwo

    ctx.developer = devel
    ctx.output = output

    try:
        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        settings_handler = settings.OcpSettings(log_id=ctx.run_id)

        clusters = settings_handler.get_ocp_clusters_iwo()
        if clusters is None:
            ctx.busy = False
            ctx.my_output.error('Failed to get OCP clusters')
            raise ErrorExit

        iwo_handler = iwo.IwoLcm(
            verbose=False,
            debug=False,
            log_id=ctx.run_id
        )
        for cluster in clusters:
            state = iwo_handler.get_lcm_state(cluster['iwo'])
            for key in state:
                cluster[key] = state[key]

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

        settings_handler.print_ocp_clusters_iwo(clusters)

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
