import sys
import json
import click

from lib import my_servers_helper


@click.command("get")
@click.pass_obj
@click.option("--name", type=click.STRING, default='', show_default=False)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
def settings_groups_get_command(ctx, name, output):
    """Show servers groups"""

    # iserver settings groups get

    my_servers_handler = my_servers_helper.MyServers()
    servers = my_servers_handler.get_my_servers()
    if servers is None:
        ctx.my_output.error('My servers not found')
        sys.exit(1)
    if len(servers) == 0:
        ctx.my_output.default('My servers not defined')
        return

    servers_list = []
    for group_name in servers:
        if len(name) > 0 and name != group_name:
            continue

        for group_server in servers[group_name]:
            server = {}
            server['Group'] = group_name
            for key in group_server:
                server[key] = group_server[key]
            servers_list.append(server)

    if output == 'json':
        ctx.my_output.default(json.dumps(servers_list, indent=4))
    else:
        ctx.my_output.my_table(
            servers_list,
            order=[
                'Group',
                'Name',
                'Serial',
                'Model',
                'ManagementIp'
            ],
            headers=[
                'Group',
                'Name',
                'Serial',
                'Model',
                'Management IP'
            ],
            table=True
        )
