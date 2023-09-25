import json
import sys
import time
import platform
import threading
import traceback
import yaml
import click

from lib.intersight import compute
from lib.intersight import compute_output
from lib.intersight import settings as intersight_settings
from lib.intersight import chassis

from menu import defaults
from menu import validations
from menu import progress


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("server")
@click.pass_obj
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
@click.option("--ip", "ip_filter", multiple=True, help="Select by IP or subnet")
@click.option("--name", "name_filter", multiple=True, help="Select by name")
@click.option("--serial", "serial_filter", multiple=True, help="Select by serial")
@click.option("--model", "model_filter", multiple=True, help="Select by model")
@click.option("--type", "type_filter", type=click.Choice(['any', 'blade', 'rack'], case_sensitive=False), default='any', show_default=True, help="Select by type")
@click.option("--group", "group_filter", default='', callback=validations.validate_group_serials, help="Select by group name")
@click.option("--loc", "locator", is_flag=True, default=False, help="Filter locator LED on")
@click.option("--off", "power_off", is_flag=True, default=False, help="Filter powered off")
@click.option("--health", is_flag=True, default=False, help="Filter unhealthy")
@click.option("--fan", is_flag=True, default=False, help="Filter unhealthy fans")
@click.option("--psu", is_flag=True, default=False, help="Filter unhealthy psu")
@click.option("--ucsm", is_flag=True, default=False, help="Filter UCSM managed")
@click.option("--disconnected", is_flag=True, default=False, help="Filter disconnected")
@click.option("--standalone", is_flag=True, default=False, help="Filter standalone servers")
@click.option("--cname", "cname_filter", default='', help="Chassis name loose match filter")
@click.option("--cmodel", "cmodel_filter", default='', help="Chassis model loose match filter")
@click.option("--cserial", "cserial_filter", default='', callback=validations.validate_filter_serials, help="Chassis serial strict match filter")
@click.option("--pci", "pci_filter", default='', help="Pci model loose match filter")
@click.option("--mac", "mac_filter", default='', help="MAC address loose match filter")
@click.option("--cpu", "cpu_filter", default='', callback=validations.validate_int_oper, help="CPU cores filter")
@click.option("--memory", "memory_filter", default='', callback=validations.validate_int_oper, help="Memory [GiB] filter")
@click.option("--view", "-v", default=['brief'], help="[brief|adv|alarm|board|boot|connector|contract|cpu|env|fan|fw|gpu|hcl|hw|istate|kvm|lic|memory|net|pci|power|profile|psu|state|storage|sw|thermal|tpm|workflow|all]", show_default=True, multiple=True)
@click.option("--days", default=7, type=click.INT, help="Last <n> days workflows")
@click.option("--ttl", "user_cache_ttl", default=None, help="Cache TTL")
@click.option("--output", "-o", type=click.Choice(['default', 'json', 'yaml'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_intersight_server_command(
        ctx,
        iaccount,
        ip_filter,
        name_filter,
        serial_filter,
        model_filter,
        type_filter,
        group_filter,
        locator,
        power_off,
        health,
        fan,
        psu,
        ucsm,
        disconnected,
        standalone,
        cname_filter,
        cmodel_filter,
        cserial_filter,
        pci_filter,
        mac_filter,
        cpu_filter,
        memory_filter,
        view,
        days,
        user_cache_ttl,
        output,
        devel
        ):
    """Get server details"""

    # iserver get is server

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'brief|adv|alarm|board|boot|connector|contract|cpu|env|fan|fw|gpu|hcl|hw|istate|kvm|lic|memory|net|pci|power|profile|psu|state|storage|sw|thermal|tpm|workflow|all',
        'brief',
        [
            'hw:board,cpu,fan,gpu,memory,pci,net,psu,storage,tpm',
            'sw:fw,boot,kvm',
            'env:power,thermal',
            'istate:adv,alarm,connector,contract,hcl,lic,profile,workflow'
        ]
    )
    if view is None:
        sys.exit(1)

    try:
        # cache should be enhanced
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
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        if output not in ['json', 'yaml']:
            ctx.busy = True

        compute_handler = compute.Compute(iaccount, log_id=ctx.run_id)

        new_serial_filter = []
        for item in group_filter:
            new_serial_filter.append(item)
        for item in serial_filter:
            new_serial_filter.append(item)

        match_rules = compute_handler.get_mo_match_rules(
            ip_filter=ip_filter,
            name_filter=name_filter,
            serial_filter=new_serial_filter,
            model_filter=model_filter
        )

        include_rack = True
        include_blade = True
        if type_filter == 'rack':
            include_blade = False
        if type_filter == 'blade':
            include_rack = False

        servers_mo = compute_handler.get_mo(
            match_rules=match_rules,
            include_rack=include_rack,
            include_blade=include_blade,
            cache_ttl=cache_ttl
        )

        if output not in ['json', 'yaml']:
            ctx.my_output.default('Selected servers: %s' % (len(servers_mo)))

        settings = {}
        settings['alarm'] = 'alarm' in view
        settings['advisory'] = 'adv' in view
        settings['board'] = 'board' in view or 'tpm' in view
        settings['boot'] = 'boot' in view
        settings['connector'] = 'connector' in view or 'state' in view
        settings['contract'] = 'contract' in view
        settings['cpu'] = 'cpu' in view
        settings['fan'] = 'fan' in view
        settings['fw'] = 'fw' in view
        settings['gpu'] = 'gpu' in view
        settings['hcl'] = 'hcl' in view
        settings['locator'] = 'state' in view
        settings['memory'] = 'memory' in view
        settings['mac'] = False
        settings['net'] = 'net' in view
        settings['pci'] = 'pci' in view or 'gpu' in view
        settings['power'] = 'power' in view
        settings['profile'] = 'profile' in view
        settings['psu'] = 'psu' in view or psu
        settings['state'] = 'state' in view
        settings['storage'] = 'storage' in view
        settings['thermal'] = 'thermal' in view
        settings['tpm'] = 'tpm' in view
        settings['workflow'] = None
        if 'workflow' in view or 'state' in view:
            settings['workflow'] = 86400 * days

        # Server filtering options

        match_rules = {}
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
        match_rules['ancestor'] = []
        if len(cname_filter) > 0 or len(cserial_filter) > 0 or len(cmodel_filter) > 0:
            cmatch_rules = {}
            cmatch_rules['name'] = cname_filter
            cmatch_rules['serial'] = ','.join(cserial_filter)
            cmatch_rules['model'] = cmodel_filter

            chassis_handler = chassis.Chassis(iaccount, log_id=ctx.run_id)

            chassiz_mo = chassis_handler.get_mo(
                match_rules=cmatch_rules,
                cache_ttl=cache_ttl
            )
            if chassiz_mo is None or len(chassiz_mo) == 0:
                ctx.busy = False
                ctx.my_output.error('No chassis found')
                return

            for chassis_mo in chassiz_mo:
                match_rules['ancestor'].append(
                    chassis_mo['Moid']
                )

        parallel = True
        if platform.system() == 'Windows':
            parallel = False

        servers_info = compute_handler.get_info(
            servers_mo,
            settings,
            match_rules,
            cache_ttl,
            parallel=parallel
        )
        ctx.busy = False
        time.sleep(.1)

        if output == 'json':
            ctx.my_output.default(json.dumps(servers_info, indent=4))
            ctx.log_prompt = False
            return

        if output == 'yaml':
            yaml_output = yaml.dump(
                servers_info,
                default_flow_style=False
            )
            ctx.my_output.default(yaml_output)
            ctx.log_prompt = False
            return

        ctx.my_output.default('')
        ctx.my_output.json_output(servers_info)

        compute_output_handler = compute_output.ComputeOutput(log_id=ctx.run_id)

        compute_output_handler.print_summary_table(
            servers_info,
            title=True
        )

        # hw:board,cpu,fan,gpu,memory,pci,net,psu,state,storage,tpm

        if 'board' in view:
            compute_output_handler.print_board(
                servers_info,
                title=True
            )

        if 'cpu' in view:
            compute_output_handler.print_cpu(
                servers_info,
                title=True
            )

        if 'gpu' in view:
            compute_output_handler.print_gpu(
                servers_info,
                title=True
            )

        if 'memory' in view:
            compute_output_handler.print_memory(
                servers_info,
                title=True
            )

        if 'storage' in view:
            compute_output_handler.print_storage_controllers(
                servers_info,
                title=True
            )
            compute_output_handler.print_physical_disks(
                servers_info,
                title=True
            )
            compute_output_handler.print_virtual_drives(
                servers_info,
                title=True
            )

        if 'net' in view:
            compute_output_handler.print_net(
                servers_info,
                title=True
            )

        if 'pci' in view:
            compute_output_handler.print_pci(
                servers_info,
                title=True
            )

        if 'fan' in view:
            compute_output_handler.print_fan(
                servers_info,
                title=True
            )

        if 'psu' in view:
            compute_output_handler.print_psu(
                servers_info,
                title=True
            )

        if 'tpm' in view:
            compute_output_handler.print_tpm(
                servers_info,
                title=True
            )

        # sw:fw,boot,kvm

        if 'fw' in view:
            compute_output_handler.print_firmware(
                servers_info,
                title=True
            )

        if 'boot' in view:
            compute_output_handler.print_boot(
                servers_info,
                title=True
            )

        if 'kvm' in view:
            compute_output_handler.print_kvm(
                servers_info,
                title=True
            )

        # env:power,thermal

        if 'power' in view:
            compute_output_handler.print_power(
                servers_info,
                title=True
            )

        if 'thermal' in view:
            compute_output_handler.print_thermal(
                servers_info,
                title=True
            )

        # istate:adv,alarm,connector,contract,hcl,lic,profile,workflow

        if 'adv' in view:
            compute_output_handler.print_advisory(
                servers_info,
                title=True
            )

        if 'alarm' in view:
            compute_output_handler.print_alarm(
                servers_info,
                title=True
            )

        if 'connector' in view:
            compute_output_handler.print_connector(
                servers_info,
                title=True
            )

        if 'contract' in view:
            compute_output_handler.print_contract(
                servers_info,
                title=True
            )

        if 'hcl' in view:
            compute_output_handler.print_hcl(
                servers_info,
                title=True
            )

        if 'lic' in view:
            compute_output_handler.print_license(
                servers_info,
                title=True
            )

        if 'profile' in view:
            compute_output_handler.print_profile(
                servers_info,
                title=True
            )

        if 'workflow' in view:
            compute_output_handler.print_workflows(
                servers_info,
                title=True
            )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
