import sys
import click

from lib import iaccount_helper


@click.command("delete")
@click.pass_obj
@click.argument("iaccount", required=True, type=click.STRING)
def settings_iaccount_delete_command(ctx, iaccount):
    """Delete Intersight Account"""

    # iwectl settings iaccount delete

    iaccount_handler = iaccount_helper.IntersightAccount()
    success, reason = iaccount_handler.delete_iaccount(iaccount)
    if not success:
        ctx.my_output.error(reason)
        sys.exit(1)

    ctx.my_output.default('Deleted')
