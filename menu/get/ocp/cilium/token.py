import sys
import click
from lib.workflow.ocp_cilium_registry import create_token


@click.command("token")
@click.pass_obj
def get_ocp_cilium_token_command(ctx):
    """Get isovalent registry access token"""

    params = {}
    success = create_token.run(
        params,
        log_id=ctx.run_id
    )
    if not success:
        sys.exit(1)