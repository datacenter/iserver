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


@click.command("vrf")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--name", "vrf_name", default='', callback=validations.validate_apic_tenant_name, help="VRF name")
@click.option("--tenant", "tenant_name", default='', callback=validations.empty_string_to_none, help="Tenant name")
@click.option("--bd", "bd_name", default='', callback=validations.empty_string_to_none, help="Filter by bridge domain name")
@click.option("--epg", "epg_name", default='', callback=validations.empty_string_to_none, help="Filter by epg name")
@click.option("--ip", "ip_address", default='', callback=validations.validate_ip, help="Filter by subnet with IP")
@click.option("--subnet", "ip_subnet", default='', callback=validations.validate_ip_subnet, help="Filter by subnet within subnet")
@click.option("--l3out", "l3out_name", default='', callback=validations.empty_string_to_none, help="Filter by l3out name")
@click.option("--output", "-o", type=click.Choice(['default', 'json', 'verbose', 'route', 'props', 'refs'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_vrf_command(
        ctx,
        controller,
        controller_ip,
        controller_username,
        controller_password,
        vrf_name,
        tenant_name,
        bd_name,
        epg_name,
        ip_address,
        ip_subnet,
        l3out_name,
        output,
        devel
        ):
    """Get aci vrfs"""

    # iserver get aci vrfs

    ctx.developer = devel
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

        vrf_filter = []

        tenant_filtered = False
        if vrf_name is not None:
            vrf_filter.append(
                'name:%s' % (vrf_name['name'])
            )

            if vrf_name['tenant'] is not None:
                tenant_filtered = True
                vrf_filter.append(
                    'tenant:%s' % (vrf_name['tenant'])
                )

        if tenant_name is not None:
            if tenant_filtered:
                ctx.my_output.error(
                    'Define tenant in one place'
                )
                raise ErrorExit

            vrf_filter.append(
                'tenant:%s' % (tenant_name)
            )

        if bd_name is not None:
            vrf_filter.append(
                'bd:%s' % (bd_name)
            )

        if epg_name is not None:
            vrf_filter.append(
                'epg:%s' % (epg_name)
            )

        if len(ip_subnet) > 0:
            vrf_filter.append(
                'subnet:%s' % (ip_subnet)
            )

        if len(ip_address) > 0:
            vrf_filter.append(
                'ip:%s' % (ip_address)
            )

        if l3out_name is not None:
            vrf_filter.append(
                'l3out:%s' % (l3out_name)
            )

        if output == 'verbose':
            vrfs = apic_handler.get_vrfs(
                vrf_filter=vrf_filter,
                bridge_domain_info=True,
                epg_info=True,
                l3out_info=True,
                route_info=False
            )

        if output == 'route':
            vrfs = apic_handler.get_vrfs(
                vrf_filter=vrf_filter,
                bridge_domain_info=True,
                epg_info=True,
                l3out_info=True,
                route_info=True
            )

        if output not in ['verbose', 'route']:
            vrfs = apic_handler.get_vrfs(
                vrf_filter=vrf_filter,
                bridge_domain_info=True,
                epg_info=True,
                l3out_info=True,
                route_info=False
            )

        ctx.busy = False

        if output == 'json':
            ctx.log_prompt = False
            ctx.my_output.default(
                json.dumps(
                    vrfs,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(vrfs)

        if output == 'default':
            aci_output_handler.print_vrfs(
                vrfs
            )

        if output == 'props':
            aci_output_handler.print_vrfs_properties(
                vrfs
            )

        if output == 'refs':
            aci_output_handler.print_vrfs_references(
                vrfs
            )

        if output == 'verbose':
            aci_output_handler.print_vrfs(
                vrfs
            )
            for vrf in vrfs:
                aci_output_handler.print_vrf(vrf)

        if output == 'route':
            for vrf in vrfs:
                aci_output_handler.print_vrf_v4_route(
                    vrf['v4route']
                )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
