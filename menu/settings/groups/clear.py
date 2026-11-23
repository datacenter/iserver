import sys
import click

from lib import my_servers_helper


@click.command("clear")
@click.pass_obj
def settings_groups_clear_command(ctx):
    """Clear servers groups settings"""

    # iserver settings groups clear

    my_servers_handler = my_servers_helper.MyServers()
    if not my_servers_handler.clear_my_servers():
        ctx.my_output.error('Failed')
        sys.exit(1)

    ctx.my_output.default('Cleared')
