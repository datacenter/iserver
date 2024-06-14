import sys
import click

from lib import my_servers_helper


@click.command("delete")
@click.pass_obj
@click.argument("name", required=True, type=click.STRING)
def settings_groups_delete_command(ctx, name):
    """Delete servers group"""

    # iserver settings groups delete

    my_servers_handler = my_servers_helper.MyServers()

    if not my_servers_handler.del_group(name):
        ctx.my_output.error('Failed')
        sys.exit(1)

    ctx.my_output.default('Deleted')
