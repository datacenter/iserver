import sys
import click

from lib import iaccount_helper


@click.command("set")
@click.pass_obj
@click.argument("iaccount", required=True, type=click.STRING)
@click.option("--account", default='', help="Account")
@click.option("--role", default='', help="Role")
@click.option("--domain", default='', help="Domain")
def settings_iaccount_set_command(ctx, iaccount, account, role, domain):
    """Set Intersight Account Metadata"""

    iaccount_handler = iaccount_helper.IntersightAccount()
    if not iaccount_handler.is_iaccount(iaccount):
        ctx.my_output.error('iaccount not found')
        sys.exit(1)

    description = iaccount_handler.get_iaccount_description(iaccount)
    if description is None:
        description = {}

    if len(account) > 0:
        description['account'] = account

    if len(role) > 0:
        description['role'] = role

    if len(domain) > 0:
        description['domain'] = domain

    if not iaccount_handler.set_iaccount_description(iaccount, description):
        ctx.my_output.error('iaccount metadata set failed')
        sys.exit(1)

    ctx.my_output.default('Metadata updated')
