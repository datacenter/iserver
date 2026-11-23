import sys
import json
import click
from lib.openshift import helper
from lib.openshift import console
from lib.openshift import output as openshift_output


@click.command("version")
@click.pass_obj
@click.option("--type", "support_type", type=click.Choice(['latest', 'production', 'beta', 'maintenance', 'end-of-life'], case_sensitive=False), default='latest', show_default=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
def get_openshift_ai_version_command(
        ctx,
        support_type,
        output
        ):
    """Get openshift assisted installer supported versions"""

    ctx.developer = False
    ctx.output = output

    success = helper.check_openshift_authentication(
        my_output=ctx.my_output,
        log_id=ctx.run_id
    )
    if not success:
        sys.exit(1)

    console_handler = console.Console(log_id=ctx.run_id)

    support = support_type
    if support_type == 'latest':
        support='production'

    versions = console_handler.get_assisted_install_openshift_versions_info(
        support=support
    )
    if versions is None:
        ctx.my_output.error('Failed to get openshift versions')
        sys.exit(1)

    if support_type == 'latest':
        versions = versions[:1]

    if output == 'json':
        ctx.my_output.default(
            json.dumps(
                versions,
                indent=4
            )
        )
        return

    ctx.my_output.json_output(versions)

    openshift_output_handler = openshift_output.OpenshiftOutput(log_id=ctx.run_id)
    openshift_output_handler.print_assisted_install_openshift_versions(
        versions
    )

    ctx.my_output.default('Support level filter (--type): latest (def), production, beta, maintenance, end-of-life', before_newline=True)