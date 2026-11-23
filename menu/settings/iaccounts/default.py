import sys
import click

from lib import iaccount_helper


@click.command("default")
@click.pass_obj
@click.argument("iaccount", required=True, type=click.STRING)
def settings_iaccount_default_command(ctx, iaccount):
    """Set Intersight Account as default"""

    # iserver settings iaccount default

    iaccount_handler = iaccount_helper.IntersightAccount()
    if not iaccount_handler.set_default_iaccount(iaccount):
        ctx.my_output.error('Failed')
        sys.exit(1)

    ctx.my_output.default('Set as default')
