import sys
import traceback
import click
from lib.workflow.linux_disk import zap
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("disk")
@click.pass_obj
@click.option("--server", multiple=True, help="Linux server name")
@click.option("--device", multiple=True, help="Block device name")
@click.option("--mode", type=click.Choice(['zap'], case_sensitive=False), default='', show_default=True, help="Mode of operation")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_linux_disk_command(
        ctx,
        server,
        device,
        mode,
        no_confirm
        ):
    """Set linux disk"""

    ctx.developer = False
    ctx.output = 'default'

    try:
        linux_access = validations.get_linux_access_details(
            ctx,
            server
        )
        if linux_access is None:
            raise ErrorExit
        
        if mode == 'zap':
            device_list = []
            for item in device:
                device_list.append(item)

            params = {}
            params['server'] = linux_access
            params['device'] = device_list
            params['confirmation'] = not no_confirm

            success = zap.run(
                params,
                log_id=ctx.run_id
            )
            if not success:
                raise ErrorExit        
            
    except NoResultExit:
        ctx.busy = False
        sys.exit(666)

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
