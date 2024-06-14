import json
import sys
import csv
import traceback
import click

from lib.intersight import settings as intersight_settings
from lib.intersight import chassis
from lib.intersight import chassis_output

from menu import defaults
from menu import validations

from progress.bar import Bar


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
@click.option("--ttl", "user_cache_ttl", default=None, help="Cache TTL")
@click.option("--inventory", "inventory_filename", default=None, help="Inventory CSV filename")
@click.option("--view", "-v", default=['state'], help="[state|adv|alarm|contract|istate|node|fi|io|exp|port|fan|psu|psuc|hw|inv]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json', 'yaml'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_chassis_command(
        ctx,
        iaccount,
        name_filter,
        serial_filter,
        model_filter,
        user_cache_ttl,
        inventory_filename,
        view,
        output,
        devel
        ):
    """Get chassis details"""

    # iserver get is chassis

    ctx.developer = devel
    ctx.output = output
    if ctx.output == 'default':
        ctx.my_output.set_debug()

    view = validations.validate_view(
        ctx,
        view,
        'state|adv|alarm|contract|istate|node|fi|io|exp|port|net|fan|psu|psuc|hw|inv',
        'state',
        [
            'net:io,fi,port',
            'inv:node,io,exp,fan,psu,inventory',
            'hw:node,io,exp,fan,psu',
            'istate:adv,alarm,contract,state'
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
            try:
                cache_ttl = int(user_cache_ttl)
            except BaseException:
                cache_ttl = -1

            if cache_ttl < 0:
                ctx.my_output.error('Cache TTL must be gt 0')
                raise ErrorExit

        if output not in ['json', 'yaml']:
            if cache_ttl is None:
                ctx.my_output.default('iaccount %s (cache: off)' % (iaccount))
            else:
                if cache_ttl == 0:
                    ctx.my_output.default('iaccount %s (cache: any)' % (iaccount))
                if cache_ttl > 0:
                    ctx.my_output.default('iaccount %s (cache: %s seconds)' % (iaccount, cache_ttl))

            ctx.my_output.default('Select chassis...')

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

        if output not in ['json']:
            ctx.my_output.default('Selected chassis: %s' % (len(chassiz_mo)))

        # Collect chassis information

        settings = {}
        settings['advisory'] = 'adv' in view
        settings['alarm'] = 'alarm' in view
        settings['contract'] = 'contract' in view
        settings['profile'] = 'state' in view
        settings['fan'] = 'fan' in view
        settings['fan_control'] = 'fan' in view
        settings['psu'] = 'psu' in view
        settings['psu_control'] = 'psuc' in view
        settings['power_control'] = 'psuc' in view
        settings['io'] = 'io' in view or 'port' in view
        settings['expander_module'] = 'exp' in view
        settings['port'] = 'port' in view
        settings['node'] = 'node' in view or 'port' in view
        settings['fi'] = 'fi' in view

        if output not in ['json']:
            ctx.my_output.default('Collect chassis api objects...')

        chassis_handler.set_cache(
            chassiz_mo,
            settings,
            cache_ttl,
            ctx=ctx
        )

        bar_handler = None
        if output == 'default':
            bar_handler = Bar('Collect chassis information', max=len(chassiz_mo))
            bar_handler.goto(0)

        chassiz_info = chassis_handler.get_info(
            chassiz_mo,
            settings,
            match_rules,
            cache_ttl,
            prepare_cache=False,
            bar_handler=bar_handler
        )

        if output == 'default':
            bar_handler.finish()

        # Output section

        chassis_output_handler = chassis_output.ChassisOutput(log_id=ctx.run_id)

        if output == 'json':
            ctx.my_output.default(json.dumps(chassiz_info, indent=4))
            ctx.log_prompt = False
            return

        if 'inventory' in view:
            chassis_output_handler.print_inventory(
                chassiz_info,
                title=True
            )

            if inventory_filename is not None:
                fields = ['Server', 'Server Type', 'Inventory Type', 'Inventory Name', 'Inventory Model', 'Inventory Vendor', 'Inventory Serial', 'Inventory PID']
                rows = []

                for chassis_info in chassiz_info:
                    for inventory_info in chassis_info['Inventory']:
                        row = []
                        row.append(
                            chassis_info['Name']
                        )
                        row.append(
                            chassis_info['Type']
                        )
                        row.append(
                            inventory_info['Type']
                        )
                        row.append(
                            inventory_info['Name']
                        )
                        row.append(
                            inventory_info['Model']
                        )
                        row.append(
                            inventory_info['Vendor']
                        )
                        row.append(
                            inventory_info['Serial']
                        )
                        row.append(
                            inventory_info['Pid']
                        )
                        rows.append(
                            row
                        )

                with open(inventory_filename, 'w', newline='') as file_handler:
                    write = csv.writer(file_handler)
                    write.writerow(fields)
                    for row in rows:
                        write.writerow(row)

            return

        if 'state' in view:
            chassis_output_handler.print_state(
                chassiz_info,
                title=True
            )

        if 'adv' in view:
            chassis_output_handler.print_advisory(
                chassiz_info,
                title=True
            )

        if 'alarm' in view:
            chassis_output_handler.print_chassis_alarm(
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

        if 'exp' in view:
            chassis_output_handler.print_expander_module(
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

        if 'fi' in view:
            chassis_output_handler.print_domain(
                chassiz_info,
                title=True
            )

        if 'fan' in view:
            chassis_output_handler.print_fan(
                chassiz_info,
                title=True
            )

        if 'psuc' in view:
            chassis_output_handler.print_psu_control_state_info(
                chassiz_info,
                title=True
            )
            chassis_output_handler.print_power_control_state_info(
                chassiz_info,
                title=True
            )

        if 'psu' in view:
            chassis_output_handler.print_psu(
                chassiz_info,
                title=True
            )

        ctx.my_output.default('Filter: name, serial, model', before_newline=True)
        ctx.my_output.default('View:   state (def), adv, alarm, contract, istate, node, fi, io, exp, port, net, fan, psu, psuc, hw, inv')

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
