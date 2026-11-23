import sys
import click
from lib.linux import settings
from lib.linux import output as linux_output


@click.command("connector")
@click.pass_obj
@click.option("--show-password", is_flag=True, show_default=True, default=False, help="Show password")
@click.option("--view", "-v", default=['state'], help="[state|cache]", show_default=True, multiple=True)
def get_linux_connector_command(
        ctx,
        show_password,
        view
        ):
    """Get linux connectors"""

    linux_output_handler = linux_output.LinuxOutput(log_id=ctx.run_id)
    settings_handler = settings.LinuxSettings(log_id=ctx.run_id)

    servers = settings_handler.get_linux_servers()
    if servers is None:
        ctx.my_output.error('Failed to get linux servers')
        sys.exit(1)

    linux_output_handler.print_linux_servers(
        servers,
        show_password=show_password,
        show_cache='cache' in view
    )