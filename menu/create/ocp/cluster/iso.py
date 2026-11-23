import sys
import traceback
import click

from lib.workflow.ocp_bm_install import install as ocp_installer

class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("iso")
@click.pass_obj
@click.option("--source", "iso_source_filename", is_flag=False, show_default=False, default='', type=click.STRING, help="ISO source filename")
@click.option("--destination", "iso_destination_filename", is_flag=False, show_default=False, default='', type=click.STRING, help="ISO destination filename")
@click.option("--password", is_flag=False, show_default=False, default='', type=click.STRING, help="Core password")
@click.option("--exec", type=click.Choice(['podman', 'docker'], case_sensitive=False), help="Container exec mode")
@click.option("--image", is_flag=False, show_default=False, default='quay.io/coreos/coreos-installer:release', type=click.STRING, help="Container image")
def create_ocp_cluster_iso_command(ctx, iso_source_filename, iso_destination_filename, password, exec, image):
    """Create bare metal iso with core password"""

    if exec not in ['podman', 'docker']:
        ctx.my_output.error('Unsupported exec mode')
        sys.exit(1)

    try:
        success = ocp_installer.modify_boot_iso_locally(
            iso_source_filename, 
            image,
            exec,
            password,
            ctx.my_output,
            destination=iso_destination_filename
        )
        if not success:
            raise ErrorExit

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
