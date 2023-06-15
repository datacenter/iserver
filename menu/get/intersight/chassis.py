import json
import sys
import time
import traceback
import threading
import yaml
import click

from lib.intersight import chassiz_info
from lib.intersight import chassis_info

from menu import common
from menu import defaults
from menu import progress
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("chassis")
@click.pass_obj
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
@click.option("--name", "name_filter", default='', help="Name filter")
@click.option("--serial", "serial_filter", default='', help="Serial filter")
@click.option("--model", "model_filter", default='', help="Model filter")
@click.option("--module", "-m", "ifm_filter", default=None, callback=validations.validate_chassis_ifm_filter, help="IFM output control")
@click.option("--port", "-p", "port_filter", default=None, multiple=True, callback=validations.validate_chassis_port_filter, help="Port output control")
@click.option("--node", "node_filter", is_flag=True, default=False, callback=validations.validate_chassis_node_filter, help="Node output control")
@click.option("--fan", "fan_filter", is_flag=True, default=False, callback=validations.validate_chassis_fan_filter, help="Fan output control")
@click.option("--power", "power_filter", is_flag=True, default=False, callback=validations.validate_chassis_power_filter, help="Power output control")
@click.option("--output", "-o", type=click.Choice(['default', 'json', 'yaml'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_intersight_chassis_command(
        ctx,
        iaccount,
        name_filter,
        serial_filter,
        model_filter,
        ifm_filter,
        port_filter,
        node_filter,
        fan_filter,
        power_filter,
        output,
        devel
        ):
    """Get chassis details"""

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
        chassis_list = chassiz_info_handler.get(
            match_rules
        )

        if chassis_list is None:
            ctx.busy = False
            raise ErrorExit

        if len(chassis_list) == 0:
            ctx.busy = False
            ctx.my_output.default('No chassis found matching the selection criteria')
            return

        if len(chassis_list) > 1:
            ctx.busy = False
            ctx.my_output.error('Multiple chassis found matching the selection criteria.')
            chassiz_info_handler.print(
                chassis_list,
                legend_on=False,
                base_output=True
            )
            return

        settings = {}
        settings['power'] = power_filter
        settings['fan'] = fan_filter
        settings['module'] = ifm_filter
        settings['port'] = port_filter
        settings['node'] = node_filter
        settings = common.chassis_settings_fixup(settings)

        chassis_info_handler = chassis_info.ChassisInfo(iaccount, settings, log_id=ctx.run_id)
        chassis = chassis_info_handler.get(
            chassis=chassis_list[0],
            extra_attributes_enabled=True
        )

        if output == 'json':
            ctx.my_output.default(json.dumps(chassis, indent=4))
            ctx.log_prompt = False
            return

        if output == 'yaml':
            yaml_output = yaml.dump(
                chassis,
                default_flow_style=False
            )
            ctx.my_output.default(yaml_output)
            ctx.log_prompt = False
            return

        ctx.busy = False
        time.sleep(.5)
        chassis_info_handler.print()

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
