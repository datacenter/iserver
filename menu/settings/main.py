import click

from menu.settings.defaults.main import settings_defaults_menu
from menu.settings.groups.main import settings_groups_menu
from menu.settings.iaccounts.main import settings_iaccounts_menu


class Failure(Exception):
    pass


@click.group("settings")
@click.pass_obj
def settings_menu(ctx):
    """Settings"""


settings_menu.add_command(settings_defaults_menu)
settings_menu.add_command(settings_groups_menu)
settings_menu.add_command(settings_iaccounts_menu)
