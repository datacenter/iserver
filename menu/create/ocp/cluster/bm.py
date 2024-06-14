import sys
import traceback
import click

from lib.workflow import ocp_bm_install

class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("bm")
@click.pass_obj
@click.option("--dir", "location", is_flag=False, show_default=False, default='', type=click.STRING, help="Cluster definition directory")
def create_ocp_cluster_bm_command(ctx, location):
    """Create bare metal OCP cluster"""

    try:
        success, user_settings, data, infra, manifests = ocp_bm_install.get_input_files(
            location,
            log_id=ctx.run_id
        )
        if not success:
            raise ErrorExit

        success = ocp_bm_install.run(
            user_settings,
            data,
            infra,
            manifests,
            log_id=ctx.run_id
        )
        if not success:
            raise ErrorExit

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
