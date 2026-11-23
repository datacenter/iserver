import click

from menu.settings.defaults.get import settings_defaults_get_command
from menu.settings.defaults.rfd import settings_defaults_rfd_command


class Failure(Exception):
    pass


@click.group("defaults")
@click.pass_obj
def settings_defaults_menu(ctx):
    """Defaults"""


settings_defaults_menu.add_command(settings_defaults_get_command)
settings_defaults_menu.add_command(settings_defaults_rfd_command)
