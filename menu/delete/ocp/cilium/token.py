import sys
import click
from lib.workflow.ocp_cilium_registry import delete_token
from menu import validations


@click.command("token")
@click.pass_obj
@click.option("--token-id", default='', callback=validations.empty_string_to_none, help="token id")
def delete_ocp_cilium_token_command(
        ctx, 
        token_id
    ):
    """Get isovalent registry access token"""

    params = {}
    params['token_id'] = token_id

    success = delete_token.run(
        params,
        log_id=ctx.run_id
    )
    if not success:
        sys.exit(1)