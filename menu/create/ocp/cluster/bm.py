import sys
import traceback
import click

from lib.workflow.ocp_bm_install import main as ocp_installer

class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("bm")
@click.pass_obj
@click.option("--dir", "location", is_flag=False, show_default=False, default='', type=click.STRING, help="Cluster definition directory")
@click.option("--mode", type=click.Choice(['check', 'install'], case_sensitive=False), default='check', show_default=True, help="Install mode")
@click.option("--offline", is_flag=True, show_default=True, default=False, help="Offline mode")
def create_ocp_cluster_bm_command(ctx, location, mode, offline):
    """Create bare metal OCP cluster"""

    try:
        if mode == 'install':
            offline = False

        success = ocp_installer.run(
            location,
            ctx.run_id,
            mode,
            offline=offline
        )
        if not success:
            raise ErrorExit

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
