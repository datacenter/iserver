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
@click.option("--fabric", is_flag=True, show_default=True, default=False, help="Fabric only mode")
def delete_ocp_cluster_bm_command(ctx, location, fabric):
    """Delete bare metal OCP cluster"""

    try:
        if fabric:
            success = ocp_installer.run(
                location,
                ctx.run_id,
                'none',
                'delete'
            )
        else:
            success = ocp_installer.run(
                location,
                ctx.run_id,
                'delete',
                'delete'
            )

        if not success:
            raise ErrorExit

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
