import sys
import click
from menu import validations
from lib.workflow.ocp_cilium_registry import set


@click.command("registry")
@click.pass_obj
@click.option("--registry", default='https://registry.isovalent.com', callback=validations.empty_string_to_none, help="Registry base url: https://registry.isovalent.com")
@click.option("--token", default='', callback=validations.empty_string_to_none, help="Identity token value")
def set_ocp_registry_command(
        ctx, 
        registry,
        token
    ):
    """Set cilium registry access credentials"""

    params = {}
    params['registry'] = registry
    params['token'] = token

    success = set.run(
        params,
        log_id=ctx.run_id
    )
    if not success:
        sys.exit(1)