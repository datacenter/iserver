import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_cilium_cni import image

class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("image")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--url", default='', callback=validations.empty_string_to_none, help="Image url")
def set_ocp_cilium_image_command(ctx, cluster_name, url):
    """Set cilium cni image"""

    try:
        params = {}
        params['cluster'] = cluster_name
        params['url'] = url

        success = image.run(
            params,
            log_id=ctx.run_id
        )
        if not success:
            raise ErrorExit
            
    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
