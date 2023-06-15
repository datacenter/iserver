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


@click.command("vrf")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--port", "controller_port", default=443, show_default=True, help="APIC Port")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--name", "vrf_name", default='', callback=validations.validate_apic_tenant_name, help="VRF name")
@click.option("--tenant", "tenant_name", default='', callback=validations.empty_string_to_none, help="Tenant name")
@click.option("--bd", "bd_name", default='', callback=validations.empty_string_to_none, help="Filter by bridge domain name")
@click.option("--epg", "epg_name", default='', callback=validations.empty_string_to_none, help="Filter by epg name")
@click.option("--address", "ip_address", default='', callback=validations.validate_ip, help="Filter by subnet with IP")
@click.option("--subnet", "ip_subnet", default='', callback=validations.validate_ip_subnet, help="Filter by subnet within subnet")
@click.option("--l3out", "l3out_name", default='', callback=validations.empty_string_to_none, help="Filter by l3out name")
@click.option("--view", "-v", type=click.Choice(['default', 'route', 'prop', 'ref', 'verbose'], case_sensitive=False), multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--no-cache", "no_cache", is_flag=True, show_default=True, default=False, help="Disable cache")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_vrf_command(
        ctx,
        controller,
        controller_ip,
        controller_port,
        controller_username,
        controller_password,
        vrf_name,
        tenant_name,
        bd_name,
        epg_name,
        ip_address,
        ip_subnet,
        l3out_name,
        view,
        output,
        no_cache,
        devel
        ):
    """Get aci vrfs"""

    # iserver get aci vrfs

    ctx.developer = devel
    ctx.output = output
    if len(view) == 0:
        view = ['default']

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

        if 'verbose' in view:
            vrfs = apic_handler.get_vrfs(
                vrf_filter=vrf_filter,
                bridge_domain_info=True,
                epg_info=True,
                l3out_info=True,
                route_info=False
            )

        if 'route' in view:
            vrfs = apic_handler.get_vrfs(
                vrf_filter=vrf_filter,
                bridge_domain_info=True,
                epg_info=True,
                l3out_info=True,
                route_info=True
            )

        if 'verbose' not in view and 'route' not in view:
            vrfs = apic_handler.get_vrfs(
                vrf_filter=vrf_filter,
                bridge_domain_info=True,
                epg_info=True,
                l3out_info=True,
                route_info=False
            )

        ctx.busy = False

        if vrfs is None or len(vrfs) == 0:
            raise NoResultExit

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

        if 'default' in view:
            aci_output_handler.print_vrfs(
                vrfs
            )

        if 'prop' in view:
            aci_output_handler.print_vrfs_properties(
                vrfs
            )

        if 'ref' in view:
            aci_output_handler.print_vrfs_references(
                vrfs
            )

        if 'verbose' in view:
            aci_output_handler.print_vrfs(
                vrfs
            )
            for vrf in vrfs:
                aci_output_handler.print_vrf(vrf)

        if 'route' in view:
            for vrf in vrfs:
                aci_output_handler.print_vrf_v4_route(
                    vrf['v4route']
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
