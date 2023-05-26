import sys
import click

from lib import settings_helper


@click.command("rfd")
@click.pass_obj
def settings_defaults_rfd_command(ctx):
    """Revert default settings to factory defaults"""

    # iwectl settings defaults rfd

    settings_handler = settings_helper.Settings()
    if not settings_handler.rfd_settings():
        ctx.my_output.error('Set settings failed')
        sys.exit(1)

    ctx.my_output.default('Done')
