import json
import click

from lib import iaccount_helper


@click.command("iaccount")
@click.pass_obj
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--show-key", is_flag=True, show_default=True, default=False, help="Show key")
def get_intersight_iaccount_command(ctx, output, show_key):
    """Get intersight accounts"""

    iaccount_handler = iaccount_helper.IntersightAccount()
    accounts = iaccount_handler.get_iaccounts()

    if not show_key:
        new_accounts = []
        for account in accounts:
            account['keyid'] = '*****'
            new_accounts.append(account)
        accounts = new_accounts

    if output == 'json':
        ctx.my_output.default(json.dumps(accounts, indent=4))
        return

    ctx.my_output.my_table(
        accounts,
        order=['name', 'keyfile', 'server', 'keyid'],
        headers=['iaccount', 'key file', 'server', 'key id'],
        table=True
    )
