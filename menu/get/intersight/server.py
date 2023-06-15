import json
import sys
import time
import traceback
import yaml
import click

from lib.intersight import compute_info
from lib.xd import server2fabric

from menu import common
from menu import defaults
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("server")
@click.pass_obj
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
@click.option("--ip", "ip_filter", default='', callback=validations.validate_ip, help="Select by IP")
@click.option("--name", "name_filter", default='', help="Select by name")
@click.option("--serial", "serial_filter", default='', help="Select by serial")
@click.option("--advisory", is_flag=True, default=False, help="Show advisories")
@click.option("--alarm", is_flag=True, default=False, help="Show alarms")
@click.option("--bios", is_flag=True, default=False, help="Show bios settings")
@click.option("--board", is_flag=True, default=False, help="Show compute board info")
@click.option("--boot", is_flag=True, default=False, help="Show boot policy")
@click.option("--chassis", is_flag=True, default=False, help="Show chassis info")
@click.option("--connector", is_flag=True, default=False, help="Show device connector info")
@click.option("--contract", is_flag=True, default=False, help="Show contract info")
@click.option("--cpu", is_flag=True, default=False, help="Show processor units")
@click.option("--env", is_flag=True, default=False, help="Show environmental info")
@click.option("--fabric", is_flag=True, default=False, help="Show fabric connectivity")
@click.option("--fan", is_flag=True, default=False, help="Show fan units")
@click.option("--fw", "firmware", is_flag=True, default=False, help="Show fw info")
@click.option("--gpu", is_flag=True, default=False, help="Show gpu info")
@click.option("--hcl", is_flag=True, default=False, help="Show hcl info")
@click.option("--kvm", is_flag=True, default=False, help="Show management info")
@click.option("--license", "ilicense", is_flag=True, default=False, help="Show license info")
@click.option("--memory", is_flag=True, default=False, help="Show memory units")
@click.option("--mac", is_flag=True, default=False, help="Show mac addresses")
@click.option("--net", is_flag=True, default=False, help="Show networking info")
@click.option("--pci", is_flag=True, default=False, help="Show pci details")
@click.option("--pn", "partnumber", is_flag=True, default=False, help="Show part numbers")
@click.option("--power", is_flag=True, default=False, help="Show power consumption")
@click.option("--profile", is_flag=True, default=False, help="Show profile")
@click.option("--psu", is_flag=True, default=False, help="Show psu units")
@click.option("--storage", is_flag=True, default=False, help="Show storage details")
@click.option("--thermal", is_flag=True, default=False, help="Show thermal info")
@click.option("--tpm", is_flag=True, default=False, help="Show tpm info")
@click.option("--workflow", is_flag=True, default=False, help="Show workflow info")
@click.option("--days", default=7, type=click.INT, help="Last <n> days workflows")
@click.option("--all", "all_info", is_flag=True, default=False, help="Show all details")
@click.option("--no-cache", "cache_disabled", is_flag=True, show_default=True, default=False, help="Disable cache")
@click.option("--state", "state_enabled", is_flag=True, show_default=True, default=False, help="Enable state collection")
@click.option("--legend", "legend_on", is_flag=True, show_default=True, default=False, help="Show legend")
@click.option("--output", "-o", type=click.Choice(['default', 'json', 'yaml'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_intersight_server_command(
        ctx,
        iaccount,
        ip_filter,
        name_filter,
        serial_filter,
        advisory,
        alarm,
        bios,
        board,
        boot,
        chassis,
        connector,
        contract,
        cpu,
        env,
        fabric,
        fan,
        firmware,
        gpu,
        hcl,
        kvm,
        ilicense,
        memory,
        mac,
        net,
        partnumber,
        pci,
        power,
        profile,
        psu,
        storage,
        thermal,
        tpm,
        workflow,
        all_info,
        days,
        cache_disabled,
        state_enabled,
        legend_on,
        output,
        devel
        ):
    """Get server details"""

    # iserver get is server

    ctx.developer = devel

    try:
        if output not in ['json', 'yaml']:
            if state_enabled:
                ctx.my_output.default('Get base server info...')
            else:
                ctx.my_output.default('Get base server info from cache...')

            ctx.busy = True

        server = common.get_selected_server(
            ctx,
            iaccount,
            name_filter,
            ip_filter,
            serial_filter,
            workflow=None,
            action=False,
            include_object=True,
            cache_enabled=not state_enabled
        )
        if server is None:
            if not state_enabled:
                ctx.my_output.default('Cache miss and checking with Intersight...')
                server = common.get_selected_server(
                    ctx,
                    iaccount,
                    name_filter,
                    ip_filter,
                    serial_filter,
                    workflow=None,
                    action=False,
                    include_object=True,
                    cache_enabled=False
                )
                if server is None:
                    raise ErrorExit

        ctx.log.debug(
            'server',
            json.dumps(
                server,
                indent=4
            )
        )

        if env:
            power = True
            thermal = True

        seconds = 86400 * days
        if state_enabled:
            settings = common.get_server_selection_settings(
                iaccount,
                workflow=seconds,
                action=False,
                registration=True
            )
        else:
            settings = common.get_server_selection_settings(
                iaccount,
                workflow=None,
                action=False,
                registration=False
            )

        settings['locator'] = True
        settings['alarm'] = alarm or all_info
        settings['advisory'] = advisory or all_info
        settings['bios'] = bios or all_info
        settings['board'] = board or all_info
        settings['boot'] = boot or all_info
        settings['chassis'] = chassis or all_info
        settings['connector'] = connector or all_info
        settings['contract'] = contract or all_info
        settings['cpu'] = cpu or all_info
        settings['fabric'] = fabric or all_info
        settings['fan'] = fan or all_info
        settings['fw'] = firmware or all_info
        settings['gpu'] = gpu or all_info
        settings['hcl'] = hcl or all_info
        settings['kvm'] = kvm or all_info
        settings['license'] = ilicense or all_info
        settings['memory'] = memory or all_info
        settings['mac'] = fabric or mac or all_info
        settings['net'] = net or all_info
        settings['pn'] = partnumber or all_info
        settings['pci'] = pci or all_info
        settings['power'] = power or all_info
        settings['profile'] = profile or all_info
        settings['psu'] = psu or all_info
        settings['storage'] = storage or all_info
        settings['thermal'] = thermal or all_info
        settings['tpm'] = tpm or all_info

        if output not in ['json', 'yaml']:
            if cache_disabled:
                ctx.my_output.default('Get selected server details...')
            else:
                ctx.my_output.default('Get selected server details from cache...')

        compute_handler = compute_info.ComputeInfo(iaccount, settings=settings, log_id=ctx.run_id)
        server_info = compute_handler.get_server_info(
            server['IntersightObject'],
            state_enabled=state_enabled,
            cache_enabled=not cache_disabled
        )

        if fabric:
            server_info = server2fabric.add_server_fabric_info(
                iaccount,
                server_info,
                log_id=ctx.run_id,
                include_cdp=False
            )

        if output == 'json':
            ctx.my_output.default(json.dumps(server_info, indent=4))
            ctx.log_prompt = False
            return

        if output == 'yaml':
            yaml_output = yaml.dump(
                server_info,
                default_flow_style=False
            )
            ctx.my_output.default(yaml_output)
            ctx.log_prompt = False
            return

        ctx.busy = False
        time.sleep(.1)
        ctx.my_output.default('')

        ctx.my_output.json_output(server_info)

        workflow_count = 10
        if not workflow:
            workflow_count = 0

        compute_handler.print(
            server_info,
            legend_on=legend_on,
            workflow_count=workflow_count
        )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
