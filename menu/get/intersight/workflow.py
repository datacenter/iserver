import json
import sys
import traceback
import yaml
import click

from lib.intersight import workflow_info

from menu import defaults
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("workflow")
@click.pass_obj
@click.argument("workflow_id", required=True, type=click.STRING)
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
@click.option("--output", "-o", type=click.Choice(['default', 'json', 'yaml'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_intersight_workflow_command(
        ctx,
        iaccount,
        workflow_id,
        output,
        devel
        ):
    """Get workflow"""

    # iserver get is workflow

    ctx.developer = devel

    try:
        if output == 'default':
            ctx.my_output.default('Get server workflow info...')

        workflow_info_handler = workflow_info.WorkflowInfo(iaccount, log_id=ctx.run_id)
        workflow_info_object = workflow_info_handler.get_workflow_info(workflow_id)
        if workflow_info_object is None:
            ctx.my_output.error('Workflow information collection failed')
            raise ErrorExit

        if output == 'json':
            ctx.my_output.default(json.dumps(workflow_info_object, indent=4))
            ctx.log_prompt = False
            return

        if output == 'yaml':
            yaml_output = yaml.dump(
                workflow_info_object,
                default_flow_style=False
            )
            ctx.my_output.default(yaml_output)
            ctx.log_prompt = False
            return

        workflow_info_handler.print_workflow_info(workflow_info_object)

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
