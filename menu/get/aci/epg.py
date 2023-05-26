import sys
import json
import threading
import traceback
import click

from lib.aci import output as aci_output

from menu import validations
from menu import progress


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("epg")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--name", "epg_name", default='', callback=validations.validate_apic_tenant_ap_name, help="Filter by epg name")
@click.option("--tenant", "tenant_name", default='', callback=validations.empty_string_to_none, help="Filter by tenant name")
@click.option("--app", "profile_name", default='', callback=validations.empty_string_to_none, help="Filter by application profile name")
@click.option("--bd", "bd_name", default='', callback=validations.empty_string_to_none, help="Filter by bridge domain name")
@click.option("--subnet", "ip_subnet", default='', callback=validations.validate_ip_subnet, help="Filter by IP subnet")
@click.option("--ip", "ip_address", default='', callback=validations.validate_ip, help="Filter by IP address")
@click.option("--node", "node_name", default='', callback=validations.empty_string_to_none, help="Filter by deployed node name")
@click.option("--contract", "contract_name", default='', callback=validations.empty_string_to_none, help="Filter by contract name")
@click.option("--output", "-o", type=click.Choice(['default', 'prop', 'bd', 'contract', 'node', 'json', 'verbose'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_epg_command(
        ctx,
        controller,
        controller_ip,
        controller_username,
        controller_password,
        epg_name,
        tenant_name,
        profile_name,
        bd_name,
        ip_subnet,
        ip_address,
        node_name,
        contract_name,
        output,
        devel
        ):
    """Get aci epg"""

    # iserver get aci aepg

    ctx.developer = devel
    if output == 'json':
        ctx.output = 'json'
    else:
        ctx.output = 'default'

    try:
        aci_output_handler = aci_output.ApicOutput(log_id=ctx.run_id)
        apic_handler = validations.validate_apic_controller(
            ctx,
            controller,
            controller_ip,
            controller_username,
            controller_password
        )
        if apic_handler is None:
            raise ErrorExit

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        epg_filter = []

        tenant_filtered = False
        ap_filtered = False
        if epg_name is not None:
            epg_filter.append(
                'name:%s' % (epg_name['name'])
            )

            if epg_name['tenant'] is not None:
                tenant_filtered = True
                epg_filter.append(
                    'tenant:%s' % (epg_name['tenant'])
                )

            if epg_name['ap'] is not None:
                ap_filtered = True
                epg_filter.append(
                    'profile:%s' % (epg_name['ap'])
                )

        if tenant_name is not None:
            if tenant_filtered:
                ctx.my_output.error(
                    'Define tenant in one place'
                )
                raise ErrorExit

            epg_filter.append(
                'tenant:%s' % (tenant_name)
            )

        if profile_name is not None:
            if ap_filtered:
                ctx.my_output.error(
                    'Define profile in one place'
                )
                raise ErrorExit

            epg_filter.append(
                'profile:%s' % (profile_name)
            )

        if node_name is not None:
            epg_filter.append(
                'node:%s' % (node_name)
            )

        if bd_name is not None:
            epg_filter.append(
                'bd:%s' % (bd_name)
            )

        if contract_name is not None:
            epg_filter.append(
                'contract:%s' % (contract_name)
            )

        if len(ip_subnet) > 0:
            epg_filter.append(
                'subnet:%s' % (ip_subnet)
            )

        if len(ip_address) > 0:
            epg_filter.append(
                'ip:%s' % (ip_address)
            )

        if output == 'verbose':
            epgs = apic_handler.get_epgs(
                epg_filter=epg_filter,
                deployed_leaves_info=True,
                endpoint_info=True,
                endpoint_vm_info=False,
                endpoint_fabric_info=True,
                contract_info=True,
                vrf_info=True,
                l3out_info=True
            )

        if output != 'verbose':
            epgs = apic_handler.get_epgs(
                epg_filter=epg_filter,
                deployed_leaves_info=True,
                endpoint_info=True,
                endpoint_vm_info=False,
                endpoint_fabric_info=False,
                contract_info=False,
                vrf_info=False,
                l3out_info=False
            )

        if output in 'contract':
            contracts = None
            contract_filter = apic_handler.get_epgs_contract_filter(
                epgs
            )
            if contract_filter != '':
                contracts = apic_handler.get_contracts(
                    contract_filter=contract_filter
                )

        ctx.busy = False

        if output == 'json':
            ctx.log_prompt = False
            ctx.my_output.default(
                json.dumps(
                    epgs,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(epgs)

        if output == 'default':
            aci_output_handler.print_epgs(
                epgs
            )

        if output == 'verbose':
            aci_output_handler.print_epgs(
                epgs
            )
            for epg in epgs:
                aci_output_handler.print_epg(
                    epg
                )

        if output == 'prop':
            aci_output_handler.print_epgs_properties(
                epgs
            )

        if output == 'bd':
            aci_output_handler.print_epgs_bridge_domain(
                epgs
            )

        if output == 'contract':
            aci_output_handler.print_epgs_contract(
                epgs
            )

            if contracts is not None:
                aci_output_handler.print_contracts(
                    contracts,
                    show_contract_filters=True
                )

        if output == 'node':
            aci_output_handler.print_epgs_node(
                epgs
            )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
