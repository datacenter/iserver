import sys
import click
from lib.workflow.ocp_cilium_registry import get


@click.command("registry")
@click.pass_obj
def get_ocp_cilium_registry_command(ctx):
    """Get isovalent registry settings"""

    params = {}
    success = get.run(
        params,
        log_id=ctx.run_id
    )
    if not success:
        sys.exit(1)