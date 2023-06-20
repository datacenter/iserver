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


class NoResultExit(Exception):
    pass


@click.command("epg")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--port", "controller_port", default=443, show_default=True, help="APIC Port")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--tenant", "tenant_name", default='', callback=validations.empty_string_to_none, help="Filter by tenant name")
@click.option("--ap", "profile_name", default='', callback=validations.empty_string_to_none, help="Filter by application profile name")
@click.option("--name", "epg_name", default='', callback=validations.validate_apic_tenant_ap_name, help="Filter by epg name")
@click.option("--pctag", default='', callback=validations.empty_string_to_none, help="Filter by pcTag")
@click.option("--bd", "bd_name", default='', callback=validations.empty_string_to_none, help="Filter by bridge domain name")
@click.option("--subnet", "ip_subnet", default='', callback=validations.validate_ip_subnet, help="Filter by IP subnet")
@click.option("--address", "ip_address", default='', callback=validations.validate_ip, help="Filter by IP address")
@click.option("--contract", "contract_name", default='', callback=validations.empty_string_to_none, help="Filter by contract name")
@click.option("--node", "node_name", default='', callback=validations.empty_string_to_none, help="Filter by deployed node name")
@click.option("--domain", "domain_name", default='', callback=validations.empty_string_to_none, help="Filter by domain name")
@click.option("--member", "member_type", type=click.Choice(['any', 'dyn', 'st'], case_sensitive=False), default='any', show_default=True)
@click.option("--pg", "pg_name", default='', callback=validations.empty_string_to_none, help="Filter by policy group name")
@click.option("--view", "-v", type=click.Choice(['summary', 'prop', 'bd', 'contract', 'ep', 'node', 'stport', 'domain', 'member', 'all', 'verbose'], case_sensitive=False), default='summary', show_default=True)
@click.option("--pivot", is_flag=True, show_default=True, default=False, help="Pivot view")
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--no-cache", "no_cache", is_flag=True, show_default=True, default=False, help="Disable cache")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_epg_command(
        ctx,
        controller,
        controller_ip,
        controller_port,
        controller_username,
        controller_password,
        epg_name,
        tenant_name,
        profile_name,
        pctag,
        bd_name,
        ip_subnet,
        ip_address,
        node_name,
        contract_name,
        domain_name,
        member_type,
        pg_name,
        view,
        pivot,
        output,
        no_cache,
        devel
        ):
    """Get aci epg"""

    # iserver get aci aepg

    ctx.developer = devel
    ctx.output = output

    try:
        aci_output_handler = aci_output.ApicOutput(log_id=ctx.run_id)
        apic_handler = validations.validate_apic_controller(
            ctx,
            controller,
            controller_ip,
            controller_port,
            controller_username,
            controller_password,
            no_cache=no_cache
        )
        if apic_handler is None:
            raise ErrorExit

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        bd_info = False
        locale_info = False
        ifconn_info = False
        endpoint_info = False
        endpoint_vm_info = False
        endpoint_fabric_info = False
        contract_info = False
        vrf_info = False
        l3out_info = False

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
            locale_info = True
            epg_filter.append(
                'node:%s' % (node_name)
            )

        if bd_name is not None:
            bd_info = True
            epg_filter.append(
                'bd:%s' % (bd_name)
            )

        if contract_name is not None:
            contract_info = True
            epg_filter.append(
                'contract:%s' % (contract_name)
            )

        if pctag is not None:
            epg_filter.append(
                'pctag:%s' % (pctag)
            )

        if len(ip_subnet) > 0:
            bd_info = True
            epg_filter.append(
                'subnet:%s' % (ip_subnet)
            )

        if len(ip_address) > 0:
            bd_info = True
            epg_filter.append(
                'ip:%s' % (ip_address)
            )

        if domain_name is not None:
            epg_filter.append(
                'domain:%s' % (domain_name)
            )

        if member_type != 'any':
            ifconn_info = True
            epg_filter.append(
                'member_type:%s' % (member_type)
            )

        if pg_name is not None:
            ifconn_info = True
            epg_filter.append(
                'pg:%s' % (pg_name)
            )

        if view == 'summary':
            bd_info = True
            locale_info = True
            ifconn_info = True
            endpoint_info = True
            contract_info = True

        if view == 'ep':
            bd_info = True
            endpoint_info = True

        if view == 'bd':
            bd_info = True
            endpoint_info = True
            vrf_info = True

        if view == 'contract':
            contract_info = True

        if view == 'node':
            locale_info = True

        if view == 'stport':
            ifconn_info = True

        if view == 'domain':
            ifconn_info = True

        if view == 'member':
            ifconn_info = True

        if view in ['verbose', 'all']:
            pivot = False
            bd_info = True
            locale_info = True
            ifconn_info = True
            endpoint_info = True
            endpoint_vm_info = True
            endpoint_fabric_info = True
            contract_info = True
            vrf_info = True
            l3out_info = True

        epgs = apic_handler.get_epgs(
            epg_filter=epg_filter,
            bd_info=bd_info,
            locale_info=locale_info,
            ifconn_info=ifconn_info,
            endpoint_info=endpoint_info,
            endpoint_vm_info=endpoint_vm_info,
            endpoint_fabric_info=endpoint_fabric_info,
            contract_info=contract_info,
            vrf_info=vrf_info,
            l3out_info=l3out_info
        )

        ctx.busy = False

        if epgs is None or len(epgs) == 0:
            raise NoResultExit

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

        if view in ['summary', 'all']:
            aci_output_handler.print_epgs(
                epgs,
                title=True
            )

        if view in ['prop', 'all']:
            aci_output_handler.print_epgs_properties(
                epgs,
                title=True
            )

        if view in ['bd', 'all']:
            aci_output_handler.print_epgs_bridge_domain(
                epgs,
                title=True
            )

        if view in ['ep', 'all']:
            endpoints = []
            for epg in epgs:
                endpoints = endpoints + epg['fvCEp']

            aci_output_handler.print_epgs_endpoint(
                endpoints,
                title=True
            )

        if view in ['contract', 'all']:
            if not pivot:
                aci_output_handler.print_epgs_contract(
                    epgs,
                    title=True
                )

            if pivot:
                aci_output_handler.print_epgs_contract_pivot(
                    epgs,
                    title=True
                )

        if view in ['domain', 'all']:
            if not pivot:
                aci_output_handler.print_epgs_domain(
                    epgs,
                    title=True
                )

            if pivot:
                aci_output_handler.print_epgs_domain_pivot(
                    epgs,
                    title=True
                )

        if view in ['node', 'all']:
            if not pivot:
                aci_output_handler.print_epgs_node(
                    epgs,
                    title=True
                )

            if pivot:
                aci_output_handler.print_epgs_node_pivot(
                    epgs,
                    title=True
                )

        if view in ['member', 'all']:
            aci_output_handler.print_epgs_member(
                epgs,
                title=True
            )

        if view in ['stport', 'all']:
            aci_output_handler.print_epgs_static_port(
                epgs,
                title=True
            )

        if view == 'verbose':
            aci_output_handler.print_epgs(
                epgs,
                title=True
            )

            for epg in epgs:
                aci_output_handler.print_epg(
                    epg
                )

    except NoResultExit:
        ctx.busy = False
        sys.exit(666)

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
