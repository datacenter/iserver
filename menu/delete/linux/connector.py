import sys
import traceback
import click
from menu import validations
from lib.linux import settings
from lib.linux import output as linux_output


@click.command("connector")
@click.pass_obj
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Linux name")
def delete_linux_connector_command(
        ctx,
        name
        ):
    """Delete linux connector"""

    linux_output_handler = linux_output.LinuxOutput(log_id=ctx.run_id)
    settings_handler = settings.LinuxSettings(log_id=ctx.run_id)

    if name is None:
        servers = settings_handler.get_linux_servers()
        linux_output_handler.print_linux_servers(
            servers,
            show_password=False
        )
        name = ctx.my_output.get_input('Connector name: ', empty_to_none=True)
        if name is None:
            sys.exit(1)

    if settings_handler.get_linux_server(name) is None:
        ctx.my_output.error('Server %s not found' % (name))
        sys.exit(1)

    if not settings_handler.delete_linux_server(name):
        ctx.my_output.error('Server %s delete failed' % (name))
        sys.exit(1)

    ctx.my_output.default('Server %s deleted' % (name))

    servers = settings_handler.get_linux_servers()
    linux_output_handler.print_linux_servers(
        servers,
        show_password=False
    )