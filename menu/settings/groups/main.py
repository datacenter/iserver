import click

from menu.settings.groups.get import settings_groups_get_command
from menu.settings.groups.clear import settings_groups_clear_command
from menu.settings.groups.delete import settings_groups_delete_command


@click.group("groups")
@click.pass_obj
def settings_groups_menu(ctx):
    """Servers groups"""


settings_groups_menu.add_command(settings_groups_get_command)
settings_groups_menu.add_command(settings_groups_clear_command)
settings_groups_menu.add_command(settings_groups_delete_command)
