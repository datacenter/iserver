import json
import sys
import time
import threading
import traceback
import yaml
import click

from lib.intersight import computes_info
from lib import my_servers_helper

from menu import common
from menu import defaults
from menu import validations
from menu import progress


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("servers")
@click.pass_obj
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
@click.option("--group", default='', callback=validations.validate_group_serials, help="Group name")
@click.option("--column", "-c", default='default', help="Extra columns: contract,env,fan,fw,group,id,mac,pci,power,psu,storage,thermal")
@click.option("--loc", "locator", is_flag=True, default=False, help="Locator LED on")
@click.option("--rack", "rack", is_flag=True, default=False, help="Filter rack servers")
@click.option("--blade", "blade", is_flag=True, default=False, help="Filter blade servers")
@click.option("--off", "power_off", is_flag=True, default=False, help="Filter powered off")
@click.option("--health", is_flag=True, default=False, help="Filter unhealthy")
@click.option("--fan", is_flag=True, default=False, help="Filter unhealthy fans")
@click.option("--psu", is_flag=True, default=False, help="Filter unhealthy psu")
@click.option("--ucsm", is_flag=True, default=False, help="Filter UCSM managed")
@click.option("--disconnected", is_flag=True, default=False, help="Filter disconnected")
@click.option("--standalone", is_flag=True, default=False, help="Filter standalone servers")
@click.option("--ip", "ip_filter", default='', callback=validations.validate_filter_ip, help="Management IP address or subnet filter")
@click.option("--name", "name_filter", default='', help="Name loose match filter")
@click.option("--model", "model_filter", default='', help="Model loose match filter")
@click.option("--pci", "pci_filter", default='', help="Pci model loose match filter")
@click.option("--mac", "mac_filter", default='', help="MAC address loose match filter")
@click.option("--serial", "serial_filter", default='', callback=validations.validate_filter_serials, help="Serial strict match filter")
@click.option("--cpu", "cpu_filter", default='', callback=validations.validate_int_oper, help="CPU cores filter")
@click.option("--memory", "memory_filter", default='', callback=validations.validate_int_oper, help="Memory [GiB] filter")
@click.option("--set", "set_group", default='', callback=validations.validate_group_oper, help="Set as group")
@click.option("--no-cache", "cache_disabled", is_flag=True, show_default=True, default=False, help="Disable cache")
@click.option("--no-state", "state_disabled", is_flag=True, show_default=True, default=False, help="Disable state")
@click.option("--fast", "fast_mode", is_flag=True, show_default=True, default=False, help="Enable caching")
@click.option("--legend", "legend_on", is_flag=True, show_default=True, default=False, help="Show legend")
@click.option("--output", "-o", type=click.Choice(['default', 'json', 'yaml', 'influx'], case_sensitive=False), default='default', show_default=True)
@click.option("--verbose", is_flag=True, show_default=True, default=False, help="Verbose output")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_intersight_servers_command(
        ctx,
        iaccount,
        group,
        column,
        rack,
        blade,
        locator,
        power_off,
        health,
        fan,
        psu,
        ucsm,
        disconnected,
        standalone,
        ip_filter,
        name_filter,
        model_filter,
        pci_filter,
        mac_filter,
        serial_filter,
        cpu_filter,
        memory_filter,
        set_group,
        cache_disabled,
        state_disabled,
        fast_mode,
        legend_on,
        output,
        verbose,
        devel
        ):
    """Get servers list"""

    # iserver get is servers list

    # Ideas
    # - mac search
    # - fw >= <= == !=
    # - what about oper state like temp??? or cpu vendor?
    # - workflow/tasks as flag (?)

    ctx.developer = devel

    parallel = True
    inventory_cache_enabled = False
    if fast_mode:
        cache_disabled = False
        state_disabled = True
        inventory_cache_enabled = True

    try:
        if output not in ['json', 'yaml', 'influx']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx,)).start()

        # Selected columns for output

        if output == 'influx':
            # influx output is designed for power/env only using redfish or ucsm
            settings = common.get_server_selection_settings(
                iaccount,
                workflow=None,
                action=False,
                registration=False
            )
            settings['locator'] = False
            if rack:
                settings['blade'] = False
            if blade:
                settings['rack'] = False

            settings['power'] = True
            settings['thermal'] = True

        if output in ['json', 'yaml', 'default']:
            if state_disabled:
                settings = common.get_server_selection_settings(
                    iaccount,
                    workflow=None,
                    action=False,
                    registration=False
                )
                settings['locator'] = False
                if rack:
                    settings['blade'] = False
                if blade:
                    settings['rack'] = False
            else:
                settings = common.get_server_selection_settings(
                    iaccount,
                    workflow=86400,
                    action=False,
                    registration=True
                )
                settings['locator'] = True
                if rack:
                    settings['blade'] = False
                if blade:
                    settings['rack'] = False

            keys = [
                'contract'
                'cpu',
                'env',
                'id',
                'fan',
                'fw',
                'group',
                'mac',
                'memory',
                'pci',
                'power',
                'psu',
                'storage',
                'thermal'
            ]
            for key in keys:
                if key in column.split(','):
                    settings[key] = True

            if settings['env']:
                settings['power'] = True
                settings['thermal'] = True

            # Make sure that columns choice follows filtering choice

            if len(pci_filter) > 0:
                settings['pci'] = True
            if len(mac_filter) > 0:
                settings['mac'] = True
            if fan:
                settings['fan'] = True
            if psu:
                settings['psu'] = True

        # Server filtering options

        match_rules = {}
        match_rules['name'] = name_filter
        match_rules['model'] = model_filter
        match_rules['ip'] = ip_filter
        match_rules['serials'] = group
        if len(serial_filter) > 0:
            match_rules['serials'] = serial_filter
        match_rules['locator'] = locator
        match_rules['power_off'] = power_off
        match_rules['alarms'] = health
        match_rules['ucsm'] = ucsm
        match_rules['disconnected'] = disconnected
        match_rules['standalone'] = standalone
        match_rules['cpu'] = cpu_filter
        match_rules['memory'] = memory_filter
        match_rules['pci'] = pci_filter
        match_rules['mac'] = mac_filter
        match_rules['fan'] = fan
        match_rules['psu'] = psu

        computes_handler = computes_info.ComputesInfo(
            iaccount,
            settings,
            log_id=ctx.run_id
        )

        servers = computes_handler.get(
            match_rules=match_rules,
            parallel=parallel,
            inventory_cache_enabled=inventory_cache_enabled,
            cache_enabled=not cache_disabled,
            state_enabled=not state_disabled
        )
        ctx.my_output.json_output(servers)

        if output == 'json':
            ctx.my_output.default(json.dumps(servers, indent=4))
            ctx.log_prompt = False
            return

        if output == 'yaml':
            yaml_output = yaml.dump(
                servers,
                default_flow_style=False
            )
            ctx.my_output.default(yaml_output)
            ctx.log_prompt = False
            return

        if output == 'influx':
            computes_handler.print_influx(
                servers
            )

            ctx.log_prompt = False

            if verbose:
                ctx.log_prompt = True

                count = 0
                for server in servers:
                    if server['Power'] is not None:
                        count = count + 1

                print('Servers: %s' % (count))

            return

        ctx.busy = False
        time.sleep(.1)

        computes_handler.print(
            servers,
            state_enabled=not state_disabled,
            legend_on=legend_on
        )

        # Set group operation handling

        if set_group is not None:
            my_servers_handler = my_servers_helper.MyServers()
            if set_group['oper'] == 'add':
                if my_servers_handler.add_group_servers(set_group['group'], servers):
                    ctx.my_output.default('Servers added to group: %s' % (set_group['group']))
                    return

                ctx.my_output.error('Failed to add servers to group: %s' % (set_group['group']))
                raise ErrorExit

            if set_group['oper'] == 'del':
                if my_servers_handler.del_group_servers(set_group['group'], servers):
                    ctx.my_output.default('Servers removed from group: %s' % (set_group['group']))
                    return

                ctx.my_output.error('Failed to add servers to group: %s' % (set_group['group']))
                raise ErrorExit

            if my_servers_handler.set_group_servers(set_group['group'], servers):
                ctx.my_output.default('Group configured with selected servers: %s' % (set_group['group']))
                return

            ctx.my_output.error('Failed to configure group with selected servers: %s' % (set_group['group']))
            raise ErrorExit

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
