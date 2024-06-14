import json
import sys
import traceback
import click

from progress.bar import Bar

from lib.intersight import compute
from lib.intersight import computes_summary
from lib.intersight import compute_output
from lib.intersight import chassis
from lib.intersight import validations as intersight_validations
from lib.vc import vcenter
from lib.vc import settings as vc_settings
from lib import my_servers_helper
from lib import context

from menu import defaults
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("server")
@click.pass_obj
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
@click.option("--ip", "ip_filter", multiple=True, help="Select by IP or subnet")
@click.option("--name", "name_filter", multiple=True, callback=intersight_validations.name_filter, help="Select by name")
@click.option("--serial", "serial_filter", multiple=True, callback=intersight_validations.serial_filter, help="Select by serial")
@click.option("--model", "model_filter", multiple=True, callback=intersight_validations.model_filter, help="Select by model")
@click.option("--type", "type_filter", type=click.Choice(['any', 'blade', 'rack'], case_sensitive=False), default='any', show_default=True, help="Select by type")
@click.option("--group", "group_filter", default='', callback=validations.validate_group_serials, help="Select by group name")
@click.option("--tag", "tag_filter", multiple=True, callback=intersight_validations.tag_filter, help="Tag filter")
@click.option("--led", "locator_filter", type=click.Choice(['any', 'on', 'off'], case_sensitive=False), default='any', show_default=True, help="Filter by locator led state")
@click.option("--power", "power_filter", type=click.Choice(['any', 'on', 'off'], case_sensitive=False), default='any', show_default=True, help="Filter by power state")
@click.option("--alarm", "alarm_filter", type=click.Choice(['any', 'info', 'warn', 'crit'], case_sensitive=False), default='any', show_default=True, help="Filter by alarm severity")
@click.option("--mode", "mode_filter", type=click.Choice(['any', 'imm', 'ucsm'], case_sensitive=False), default='any', show_default=True, help="Filter by management mode")
@click.option("--disc", "disconnected", is_flag=True, default=False, help="Filter disconnected")
@click.option("--cname", "cname_filter", default='', help="Chassis name loose match filter")
@click.option("--cmodel", "cmodel_filter", default='', help="Chassis model loose match filter")
@click.option("--cserial", "cserial_filter", default='', callback=validations.validate_filter_serials, help="Chassis serial strict match filter")
@click.option("--cpu", "cpu_filter", multiple=True, callback=intersight_validations.cpu_filter, help="CPU filter")
@click.option("--gpu", "gpu_filter", multiple=True, callback=intersight_validations.gpu_filter, help="GPU filter")
@click.option("--mem", "memory_filter", multiple=True, callback=intersight_validations.memory_filter, help="Memory filter")
@click.option("--pci", "pci_filter", multiple=True, callback=intersight_validations.pci_filter, help="PCI filter")
@click.option("--mac", "mac_filter", multiple=True, help="MAC address filter")
@click.option("--sc", "sc_filter", multiple=True, callback=intersight_validations.sc_filter, help="Storage controller filter")
@click.option("--pd", "pd_filter", multiple=True, callback=intersight_validations.pd_filter, help="Physical disk filter")
@click.option("--vd", "vd_filter", multiple=True, callback=intersight_validations.vd_filter, help="Virtual drive filter")
@click.option("--fan", "fan_filter", multiple=True, callback=intersight_validations.fan_filter, help="Fan filter")
@click.option("--psu", "psu_filter", multiple=True, callback=intersight_validations.psu_filter, help="Psu filter")
@click.option("--vc", "vcenter_name", default='', help="vCenter name")
@click.option("--view", "-v", default=['state'], help="[state|adv|alarm|board|boot|connector|contract|cpu|env|fan|fanm|fw|gpu|hcl|hw|inv|istate|kvm|lic|mem|net|pci|power|profile|psu|sc|pd|vd|storage|sw|thermal|tpm|workflow|vc|summary]", show_default=True, multiple=True)
@click.option("--days", default=0, type=click.INT, help="Last <n> days workflows")
@click.option("--ttl", "user_cache_ttl", default=None, help="Cache TTL")
@click.option("--inventory", "inventory_filename", default=None, help="Inventory CSV filename")
@click.option("--set", "set_group", default='', callback=validations.validate_group_oper, help="Set as group")
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_server_command(
        ctx,
        iaccount,
        ip_filter,
        name_filter,
        serial_filter,
        model_filter,
        type_filter,
        group_filter,
        tag_filter,
        locator_filter,
        power_filter,
        alarm_filter,
        mode_filter,
        disconnected,
        cname_filter,
        cmodel_filter,
        cserial_filter,
        cpu_filter,
        gpu_filter,
        memory_filter,
        pci_filter,
        mac_filter,
        sc_filter,
        pd_filter,
        vd_filter,
        fan_filter,
        psu_filter,
        vcenter_name,
        view,
        days,
        user_cache_ttl,
        inventory_filename,
        set_group,
        output,
        devel
        ):
    """Get server details"""

    # iserver get is server

    ctx.developer = devel
    ctx.output = output
    if ctx.output == 'default':
        ctx.my_output.set_debug()

    view = validations.validate_view(
        ctx,
        view,
        'state|adv|alarm|board|boot|connector|contract|cpu|env|fan|fanm|fw|gpu|hcl|hw|inv|istate|kvm|lic|mem|net|pci|power|profile|psu|sc|pd|vd|storage|sw|thermal|tpm|workflow|vc|summary',
        'state',
        [
            'hw:state,board,cpu,fan,gpu,mem,pci,net,psu,storage,tpm',
            'inv:board,chassis,cpu,fan,gpu,mem,pci,net,psu,storage,tpm,inventory',
            'sw:fw,boot,kvm',
            'env:power,thermal',
            'istate:adv,alarm,connector,contract,hcl,lic,profile,workflow'
        ]
    )
    if view is None:
        sys.exit(1)

    if 'summary' in view and len(view) > 1:
        ctx.my_output.error(
            'Summary view should be the only view defined'
        )
        sys.exit(1)

    try:
        # default vs. user-defined cache_ttl
        cache_ttl = intersight_validations.validate_cache_ttl(user_cache_ttl, log_id=ctx.run_id)
        if cache_ttl is not None and cache_ttl < 0:
            ctx.my_output.error('Cache TTL must be gt 0')
            raise ErrorExit

        # Server details collection settings

        settings = {}
        settings['alarm'] = 'alarm' in view or alarm_filter != 'any'
        settings['advisory'] = 'adv' in view
        settings['board'] = 'board' in view or 'tpm' in view
        settings['boot'] = 'boot' in view
        settings['connector'] = 'connector' in view or 'state' in view
        settings['contract'] = 'contract' in view
        settings['cpu'] = 'cpu' in view or cpu_filter['info']
        settings['fan'] = 'fan' in view or 'fanm' in view or fan_filter['info']
        settings['fw'] = 'fw' in view
        settings['gpu'] = 'gpu' in view or gpu_filter['info']
        settings['hcl'] = 'hcl' in view
        settings['inventory'] = 'inventory' in view
        settings['locator'] = 'state' in view or locator_filter != 'any'
        settings['memory'] = 'mem' in view or memory_filter['info']
        settings['net'] = 'net' in view or len(mac_filter) > 0
        settings['pci'] = 'pci' in view or 'gpu' in view or pci_filter['info'] or gpu_filter['info']
        settings['power'] = 'power' in view
        settings['profile'] = 'profile' in view
        settings['psu'] = 'psu' in view or psu_filter['info']
        settings['state'] = 'state' in view or locator_filter != 'any' or power_filter != 'any'
        settings['storage'] = 'storage' in view or 'sc' in view or 'pd' in view or 'vd' in view or sc_filter['info'] or pd_filter['info'] or vd_filter['info']
        settings['thermal'] = 'thermal' in view
        settings['tpm'] = 'tpm' in view
        settings['workflow'] = None
        if 'workflow' in view or 'state' in view:
            if days > 0:
                settings['workflow'] = 86400 * days

        # Server filtering options incl. chassis filtering (early exit if no chassis matching criteria)

        match_rules = {}
        match_rules['locator'] = locator_filter
        match_rules['power'] = power_filter
        match_rules['alarms'] = alarm_filter
        match_rules['ucsm'] = False
        if mode_filter == 'ucsm':
            match_rules['ucsm'] = True
        match_rules['imm'] = False
        if mode_filter == 'imm':
            match_rules['imm'] = True
        match_rules['disconnected'] = disconnected
        match_rules['cpu'] = cpu_filter
        match_rules['gpu'] = gpu_filter
        match_rules['memory'] = memory_filter
        match_rules['pci'] = pci_filter
        match_rules['mac'] = mac_filter
        match_rules['sc'] = sc_filter
        match_rules['pd'] = pd_filter
        match_rules['vd'] = vd_filter
        match_rules['fan'] = fan_filter
        match_rules['psu'] = psu_filter
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
                ctx.my_output.error('No chassis found')
                return

            for chassis_mo in chassiz_mo:
                match_rules['ancestor'].append(
                    chassis_mo['Moid']
                )

        # Runtime information

        if output not in ['json']:
            if cache_ttl is None:
                ctx.my_output.default('iaccount %s (cache: off)' % (iaccount))
            else:
                if cache_ttl == 0:
                    ctx.my_output.default('iaccount %s (cache: any)' % (iaccount))
                if cache_ttl > 0:
                    ctx.my_output.default('iaccount %s (cache: %s seconds)' % (iaccount, cache_ttl))

            ctx.my_output.default('Select servers...')

        # Collect servers mo using basic filtering criteria and expansion based on settings. No cache used

        compute_handler = compute.Compute(iaccount, log_id=ctx.run_id)
        mo_match_rules = compute_handler.get_mo_match_rules(
            ip_filter=ip_filter,
            name_filter=name_filter,
            serial_filter=intersight_validations.add_group_filter(serial_filter, group_filter),
            model_filter=model_filter,
            tag_filter=tag_filter
        )

        include_rack = True
        include_blade = True
        if type_filter == 'rack':
            include_blade = False
        if type_filter == 'blade':
            include_rack = False

        rack_expand = []
        blade_expand = []
        if settings['pci']:
            rack_expand.append('PciDevices')
            blade_expand.append('PciDevices')
            blade_expand.append('PciNodes')
        if settings['psu']:
            rack_expand.append('Psus')
        if settings['fan']:
            rack_expand.append('Fanmodules')
        if settings['locator']:
            rack_expand.append('LocatorLed')
            blade_expand.append('LocatorLed')
        if settings['state']:
            rack_expand.append('RegisteredDevice')
            blade_expand.append('RegisteredDevice')

        servers_mo = compute_handler.get_mo(
            match_rules=mo_match_rules,
            include_rack=include_rack,
            rack_expand=rack_expand,
            include_blade=include_blade,
            blade_expand=blade_expand,
            cache_ttl=None
        )

        if output not in ['json']:
            ctx.my_output.default('Selected servers: %s' % (len(servers_mo)))

        if len(servers_mo) == 0:
            return

        # Collect chassis information. No cache used

        chassiz_info = None
        if 'chassis' in view:
            chassiz_moid = []
            for server_mo in servers_mo:
                if server_mo['ObjectType'] == 'compute.Blade':
                    if server_mo['EquipmentChassis']['Moid'] not in chassiz_moid:
                        chassiz_moid.append(
                            server_mo['EquipmentChassis']['Moid']
                        )

            chassiz_info = []
            if len(chassiz_moid) > 0:
                if output not in ['json']:
                    ctx.my_output.default('Collect chassis api objects...')

                chassis_handler = chassis.Chassis(iaccount, log_id=ctx.run_id)
                cmatch_rules = chassis_handler.get_mo_match_rules(
                    moid_filter=','.join(chassiz_moid)
                )
                chassiz_mo = chassis_handler.get_mo(
                    match_rules=cmatch_rules,
                    cache_ttl=None
                )
                if chassiz_mo is not None and len(chassiz_mo) > 0:
                    chassis_settings = {}
                    chassis_settings['node'] = True
                    chassis_settings['io'] = True
                    chassis_settings['expander_module'] = True
                    chassis_settings['fan'] = True
                    chassis_settings['psu'] = True

                    bar_handler = None
                    if output == 'default':
                        bar_handler = Bar('Collect chassis information', max=len(chassiz_mo))
                        bar_handler.goto(0)

                    chassiz_info = chassis_handler.get_info(
                        chassiz_mo,
                        chassis_settings,
                        [],
                        cache_ttl,
                        bar_handler=bar_handler
                    )

                    if output == 'default':
                        bar_handler.finish()

        # Collect server information

        if output not in ['json']:
            ctx.my_output.default('Collect server api objects...')

        compute_handler.set_cache(
            servers_mo,
            settings,
            cache_ttl,
            ctx=ctx
        )

        bar_handler = None
        if output == 'default':
            bar_handler = Bar('Collect server information', max=len(servers_mo))
            bar_handler.goto(0)

        servers_info = compute_handler.get_info(
            servers_mo,
            settings,
            match_rules,
            cache_ttl,
            prepare_cache=False,
            bar_handler=bar_handler
        )

        if output == 'default':
            bar_handler.finish()

        if len(vcenter_name) > 0:
            vc_settings_handler = vc_settings.VcSettings(log_id=ctx.run_id)
            vcenter_settings = vc_settings_handler.get_vc_instance(vcenter_name)
            if vcenter_settings is None:
                ctx.my_output.error('vcenter not found: %s' % (vcenter_name))
                raise ErrorExit

            vc_handler = vcenter.Vcenter(
                vcenter_settings['ip'],
                vcenter_settings['username'],
                vcenter_settings['password'],
                port=vcenter_settings['port'],
                log_id=ctx.run_id
            )

            ctx.my_output.default('Get vcenter hosts...')

            vc_hosts = vc_handler.get_hosts_summary()
            if vc_hosts is None:
                ctx.my_output.error('No vcenter hosts found')
                raise ErrorExit

            vc_vms = vc_handler.get_vms()
            if vc_vms is None:
                ctx.my_output.error('No vcenter virtual machines found')
                raise ErrorExit

        # Output section

        is_rack = False
        is_blade = False
        for server_info in servers_info:
            if server_info['Type'] == 'Blade':
                is_blade = True
            if server_info['Type'] == 'Rack':
                is_rack = True

        if 'summary' in view:
            summary_handler = computes_summary.ComputesSummary(settings, log_id=ctx.run_id)
            summary = summary_handler.get_summary(servers_info)
            if output == 'json':
                ctx.my_output.default(json.dumps(summary, indent=4))
                ctx.log_prompt = False
                return

            ctx.my_output.default('')
            ctx.my_output.json_output(summary)
            summary_handler.print_summary(summary)
            return

        if output == 'json':
            ctx.my_output.default(json.dumps(servers_info, indent=4))
            ctx.log_prompt = False
            return

        ctx.my_output.json_output(servers_info)

        ctx.my_output.default('')
        compute_output_handler = compute_output.ComputeOutput(log_id=ctx.run_id)

        if 'inventory' in view:
            compute_output_handler.print_inventory(
                servers_info,
                chassiz_info,
                title=True
            )

            if inventory_filename is not None:
                compute_output_handler.print_inventory_csv(
                    servers_info,
                    chassiz_info,
                    inventory_filename
                )

            return

        if 'state' in view:
            compute_output_handler.print_summary_table(
                servers_info,
                title=True
            )

        # hw:board,cpu,fan,gpu,mem,pci,net,psu,state,storage,tpm

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

        if 'mem' in view:
            compute_output_handler.print_memory(
                servers_info,
                title=True
            )

        if 'storage' in view or 'sc' in view:
            compute_output_handler.print_storage_controllers(
                servers_info,
                title=True
            )

        if 'storage' in view or 'pd' in view:
            compute_output_handler.print_physical_disks(
                servers_info,
                title=True
            )

        if 'storage' in view or 'vd' in view:
            compute_output_handler.print_virtual_drives(
                servers_info,
                title=True
            )

        if 'net' in view:
            if is_rack:
                compute_output_handler.print_cimc(
                    servers_info,
                    title=True
                )

            compute_output_handler.print_net(
                servers_info,
                title=True
            )

        if 'pci' in view:
            compute_output_handler.print_pci(
                servers_info,
                title=True
            )

            if is_blade:
                compute_output_handler.print_pci_node(
                    servers_info,
                    title=True
                )

        if 'fanm' in view:
            if is_rack:
                compute_output_handler.print_fan_module(
                    servers_info,
                    title=True
                )

        if 'fan' in view:
            if is_rack:
                compute_output_handler.print_fan(
                    servers_info,
                    title=True
                )

        if 'psu' in view:
            if is_rack:
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
            compute_output_handler.print_server_alarm(
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

        if 'vc' in view:
            compute_output_handler.print_vc_vms(
                servers_info,
                vc_hosts,
                vc_vms,
                title=True
            )

        # Set group operation handling

        if set_group is not None:
            my_servers_handler = my_servers_helper.MyServers()
            if set_group['oper'] == 'add':
                if my_servers_handler.add_group_servers(set_group['group'], servers_info):
                    ctx.my_output.default('Servers added to group: %s' % (set_group['group']))
                    return

                ctx.my_output.error('Failed to add servers to group: %s' % (set_group['group']))
                raise ErrorExit

            if set_group['oper'] == 'del':
                if my_servers_handler.del_group_servers(set_group['group'], servers_info):
                    ctx.my_output.default('Servers removed from group: %s' % (set_group['group']))
                    return

                ctx.my_output.error('Failed to add servers to group: %s' % (set_group['group']))
                raise ErrorExit

            if my_servers_handler.set_group_servers(set_group['group'], servers_info):
                ctx.my_output.default('Group configured with selected servers: %s' % (set_group['group']))
                return

            ctx.my_output.error('Failed to configure group with selected servers: %s' % (set_group['group']))
            raise ErrorExit

        context_handler = context.Context(log_id=ctx.run_id)
        context_handler.set(
            'mac',
            compute_handler.get_context_mac(servers_info)
        )
        context_handler.set(
            'ip',
            compute_handler.get_context_ip(servers_info)
        )

        ctx.my_output.default('Filter: ip, name, serial, model, type, group, led, power, alarm, mode', before_newline=True)
        ctx.my_output.default('        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu')
        ctx.my_output.default('View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate')
        ctx.my_output.default('        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary')
        ctx.my_output.default('Ctx:    ip, mac')

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
