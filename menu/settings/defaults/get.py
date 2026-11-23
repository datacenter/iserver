import sys
import json
import click

from lib import settings_helper


@click.command("get")
@click.pass_obj
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
def settings_defaults_get_command(ctx, output):
    """Show Default Settings"""

    # iwectl settings defaults get

    settings_handler = settings_helper.Settings()
    values = settings_handler.get_settings()
    if values is None:
        ctx.my_output.error('Get settings failed')
        sys.exit(1)

    if output == 'json':
        ctx.my_output.default(json.dumps(values, indent=4))
        return

    ctx.my_output.dictionary(
        values,
        exclude=[],
        title='Default Settings',
        underline=True,
        prefix='- ',
        justify=True
    )
