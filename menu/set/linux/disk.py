import sys
import click
from lib.workflow.linux_disk import zap
from menu import validations


@click.command("disk")
@click.pass_obj
@click.option("--server", multiple=True, help="Linux server name")
@click.option("--device", multiple=True, help="Block device name")
@click.option("--fstype", multiple=True, help="Filesystem type")
@click.option("--mode", type=click.Choice(['zap'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--no-break", is_flag=True, show_default=True, default=False, help="Break-on-error mode")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_linux_disk_command(
        ctx,
        server,
        device,
        fstype,
        mode,
        no_break,
        no_confirm
        ):
    """Set linux disk"""

    linux_access = validations.get_linux_access_details(
        ctx,
        server
    )
    if linux_access is None:
        sys.exit(1)
        
    if mode == 'zap':
        params = {}
        params['server'] = linux_access
        params['device'] = device
        params['fstype'] = fstype
        params['break'] = not no_break
        params['confirmation'] = not no_confirm

        success = zap.run(
            params,
            log_id=ctx.run_id
        )
        if not success:
            sys.exit(1)