import json
import sys
import traceback
import threading
import yaml
import click

from lib.intersight import chassiz_info

from menu import defaults
from menu import progress
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("chassiz")
@click.pass_obj
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
@click.option("--name", "name_filter", default='', help="Name filter")
@click.option("--serial", "serial_filter", default='', help="Serial filter")
@click.option("--model", "model_filter", default='', help="Model filter")
@click.option("--output", "-o", type=click.Choice(['default', 'json', 'yaml'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_intersight_chassiz_command(
        ctx,
        iaccount,
        name_filter,
        serial_filter,
        model_filter,
        output,
        devel
        ):
    """Get chassis list"""

    # iserver get is chassis

    ctx.developer = devel

    try:
        if output not in ['json', 'yaml']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx,)).start()

        chassiz_info_handler = chassiz_info.ChassizInfo(iaccount, log_id=ctx.run_id)

        match_rules = {}
        match_rules['name'] = name_filter
        match_rules['serial'] = serial_filter
        match_rules['model'] = model_filter
        chassis_list = chassiz_info_handler.get(match_rules)
        if chassis_list is None:
            ctx.busy = False
            raise ErrorExit

        if output == 'json':
            ctx.my_output.default(json.dumps(chassis_list, indent=4))
            ctx.log_prompt = False
            return

        if output == 'yaml':
            yaml_output = yaml.dump(
                chassis_list,
                default_flow_style=False
            )
            ctx.my_output.default(yaml_output)
            ctx.log_prompt = False
            return

        ctx.busy = False
        chassiz_info_handler.print(chassis_list)

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
