import json
import sys
import time
import traceback
import threading
import yaml
import click

from lib.intersight import settings as intersight_settings
from lib.intersight import chassis
from lib.intersight import chassis_output

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
@click.option("--name", "name_filter", multiple=True, help="Select by name")
@click.option("--serial", "serial_filter", multiple=True, help="Select by serial")
@click.option("--model", "model_filter", multiple=True, help="Select by model")
@click.option("--module", "-m", "ifm_filter", default=None, callback=validations.validate_chassis_ifm_filter, help="IFM output control")
@click.option("--port", "-p", "port_filter", default=None, multiple=True, callback=validations.validate_chassis_port_filter, help="Port output control")
@click.option("--node", "node_filter", is_flag=True, default=False, callback=validations.validate_chassis_node_filter, help="Node output control")
@click.option("--fan", "fan_filter", is_flag=True, default=False, callback=validations.validate_chassis_fan_filter, help="Fan output control")
@click.option("--power", "power_filter", is_flag=True, default=False, callback=validations.validate_chassis_power_filter, help="Power output control")
@click.option("--ttl", "user_cache_ttl", default=None, help="Cache TTL")
@click.option("--view", "-v", default=['brief'], help="[brief|state|alarm|profile|contract|istate|node|dom|io|port|net|fan|psu|inv]", show_default=True, multiple=True)
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
        user_cache_ttl,
        view,
        output,
        devel
        ):
    """Get chassis details"""

    # iserver get is chassis

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'brief|state|alarm|profile|contract|istate|node|dom|io|port|net|fan|psu|inv',
        'brief',
        [
            'net:dom,io,port',
            'inv:node,dom,io,fan,psu',
            'istate:profile,contract,alarm'
        ]
    )
    if view is None:
        sys.exit(1)

    try:
        settings_handler = intersight_settings.IntersightSettings(
            log_id=ctx.run_id
        )
        cache_ttl = settings_handler.get_intersight_cache_ttl()
        if user_cache_ttl is not None:
            cache_ttl = int(user_cache_ttl)

        if output not in ['json', 'yaml']:
            if cache_ttl is None:
                ctx.my_output.default('iaccount %s (cache: off)' % (iaccount))
            else:
                if cache_ttl == 0:
                    ctx.my_output.default('iaccount %s (cache: any)' % (iaccount))
                if cache_ttl > 0:
                    ctx.my_output.default('iaccount %s (cache: %s seconds)' % (iaccount, cache_ttl))

            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx,)).start()

        chassis_handler = chassis.Chassis(iaccount, log_id=ctx.run_id)

        match_rules = chassis_handler.get_mo_match_rules(
            name_filter=name_filter,
            serial_filter=serial_filter,
            model_filter=model_filter
        )

        chassiz_mo = chassis_handler.get_mo(
            match_rules=match_rules,
            cache_ttl=cache_ttl
        )

        settings = chassis_handler.get_default_settings()

        chassiz_info = chassis_handler.get_info(
            chassiz_mo,
            settings,
            match_rules,
            cache_ttl
        )

        ctx.busy = False

        chassis_output_handler = chassis_output.ChassisOutput(log_id=ctx.run_id)

        chassis_output_handler.print_summary(
            chassiz_info,
            title=True
        )

        if 'state' in view:
            chassis_output_handler.print_state(
                chassiz_info,
                title=True
            )

        if 'dom' in view:
            chassis_output_handler.print_domain(
                chassiz_info,
                title=True
            )

        if 'alarm' in view:
            chassis_output_handler.print_health(
                chassiz_info,
                title=True
            )

        if 'profile' in view:
            chassis_output_handler.print_profile(
                chassiz_info,
                title=True
            )

        if 'contract' in view:
            chassis_output_handler.print_contract(
                chassiz_info,
                title=True
            )

        if 'node' in view:
            chassis_output_handler.print_node(
                chassiz_info,
                title=True
            )

        if 'io' in view:
            chassis_output_handler.print_io_module(
                chassiz_info,
                title=True
            )

        if 'port' in view:
            chassis_output_handler.print_network_port(
                chassiz_info,
                title=True
            )

            chassis_output_handler.print_host_port(
                chassiz_info,
                title=True
            )

        if 'fan' in view:
            chassis_output_handler.print_fans(
                chassiz_info,
                title=True
            )

        if 'psu' in view:
            chassis_output_handler.print_psus(
                chassiz_info,
                title=True
            )

        # chassis_list = chassiz_info_handler.get(
        #     match_rules
        # )

        # if chassis_list is None:
        #     ctx.busy = False
        #     raise ErrorExit

        # if len(chassis_list) == 0:
        #     ctx.busy = False
        #     ctx.my_output.default('No chassis found matching the selection criteria')
        #     return

        # if len(chassis_list) > 1:
        #     ctx.busy = False
        #     ctx.my_output.error('Multiple chassis found matching the selection criteria.')
        #     chassiz_info_handler.print(
        #         chassis_list,
        #         legend_on=False,
        #         base_output=True
        #     )
        #     return

        # settings = {}
        # settings['power'] = power_filter
        # settings['fan'] = fan_filter
        # settings['module'] = ifm_filter
        # settings['port'] = port_filter
        # settings['node'] = node_filter
        # settings = common.chassis_settings_fixup(settings)

        # chassis_info_handler = chassis_info.ChassisInfo(iaccount, settings, log_id=ctx.run_id)
        # chassis = chassis_info_handler.get(
        #     chassis=chassis_list[0],
        #     extra_attributes_enabled=True
        # )

        # if output == 'json':
        #     ctx.my_output.default(json.dumps(chassis, indent=4))
        #     ctx.log_prompt = False
        #     return

        # if output == 'yaml':
        #     yaml_output = yaml.dump(
        #         chassis,
        #         default_flow_style=False
        #     )
        #     ctx.my_output.default(yaml_output)
        #     ctx.log_prompt = False
        #     return

        # ctx.busy = False
        # time.sleep(.5)

        # ctx.my_output.json_output(chassis)
        # chassis_info_handler.print()

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
