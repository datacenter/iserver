import click

from menu.settings.iaccounts.add import settings_iaccount_add_command
from menu.settings.iaccounts.cache import settings_iaccount_cache_command
from menu.settings.iaccounts.get import settings_iaccount_get_command
from menu.settings.iaccounts.delete import settings_iaccount_delete_command
from menu.settings.iaccounts.default import settings_iaccount_default_command


@click.group("iaccounts")
@click.pass_obj
def settings_iaccounts_menu(ctx):
    """Intersight Accounts"""


settings_iaccounts_menu.add_command(settings_iaccount_add_command)
settings_iaccounts_menu.add_command(settings_iaccount_cache_command)
settings_iaccounts_menu.add_command(settings_iaccount_get_command)
settings_iaccounts_menu.add_command(settings_iaccount_delete_command)
settings_iaccounts_menu.add_command(settings_iaccount_default_command)
