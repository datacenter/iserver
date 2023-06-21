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


@click.command("bd")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--port", "controller_port", default=443, show_default=True, help="APIC Port")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--name", "bridge_domain_name", default='', callback=validations.validate_apic_tenant_name, help="Filter by bridge domain name")
@click.option("--tenant", "tenant_name", default='', callback=validations.empty_string_to_none, help="Filter by tenant name")
@click.option("--vrf", "vrf_name", default='', callback=validations.empty_string_to_none, help="Filter by vrf name")
@click.option("--epg", "epg_name", default='', callback=validations.empty_string_to_none, help="Filter by epg name")
@click.option("--address", "ip_address", default='', callback=validations.validate_ip, help="Filter by subnet with IP")
@click.option("--subnet", "ip_subnet", default='', callback=validations.validate_ip_subnet, help="Filter by subnet within subnet")
@click.option("--l3out", "l3out_name", default='', callback=validations.empty_string_to_none, help="Filter by l3out name")
@click.option("--view", "-v", type=click.Choice(['summary', 'l2', 'l3', 'mcast', 'vrf', 'all', 'verbose'], case_sensitive=False), default='summary', show_default=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json', ], case_sensitive=False), default='default', show_default=True)
@click.option("--no-cache", "no_cache", is_flag=True, show_default=True, default=False, help="Disable cache")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_bd_command(
        ctx,
        controller,
        controller_ip,
        controller_port,
        controller_username,
        controller_password,
        bridge_domain_name,
        tenant_name,
        vrf_name,
        epg_name,
        ip_address,
        ip_subnet,
        l3out_name,
        view,
        output,
        no_cache,
        devel
        ):
    """Get aci bridge domain"""

    # iserver get aci bd

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

        bridge_domain_filter = []

        tenant_filtered = False
        if bridge_domain_name is not None:
            bridge_domain_filter.append(
                'name:%s' % (bridge_domain_name['name'])
            )

            if bridge_domain_name['tenant'] is not None:
                tenant_filtered = True
                bridge_domain_filter.append(
                    'tenant:%s' % (bridge_domain_name['tenant'])
                )

        if tenant_name is not None:
            if tenant_filtered:
                ctx.my_output.error(
                    'Define tenant in one place'
                )
                raise ErrorExit

            bridge_domain_filter.append(
                'tenant:%s' % (tenant_name)
            )

        if vrf_name is not None:
            bridge_domain_filter.append(
                'vrf:%s' % (vrf_name)
            )

        if epg_name is not None:
            bridge_domain_filter.append(
                'epg:%s' % (epg_name)
            )

        if len(ip_subnet) > 0:
            bridge_domain_filter.append(
                'subnet:%s' % (ip_subnet)
            )

        if len(ip_address) > 0:
            bridge_domain_filter.append(
                'ip:%s' % (ip_address)
            )

        if l3out_name is not None:
            bridge_domain_filter.append(
                'l3out:%s' % (l3out_name)
            )

        endpoint_info = True
        endpoint_vm_info = False
        endpoint_fabric_info = False
        snoop_info = False
        vrf_info = False
        epg_info = True

        if view in ['vrf', 'all', 'verbose']:
            vrf_info = True
            epg_info = True

        if view == 'verbose':
            endpoint_vm_info = True
            endpoint_fabric_info = True
            snoop_info = True

        bridge_domains = apic_handler.get_bridge_domains(
            bridge_domain_filter=bridge_domain_filter,
            endpoint_info=endpoint_info,
            endpoint_vm_info=endpoint_vm_info,
            endpoint_fabric_info=endpoint_fabric_info,
            snoop_info=snoop_info,
            vrf_info=vrf_info,
            epg_info=epg_info
        )

        ctx.busy = False

        if bridge_domains is None or len(bridge_domains) == 0:
            raise NoResultExit

        if output == 'json':
            ctx.log_prompt = False
            ctx.my_output.default(
                json.dumps(
                    bridge_domains,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(bridge_domains)

        if view in ['summary', 'all']:
            aci_output_handler.print_bridge_domains(
                bridge_domains,
                title=True
            )

        if view in ['l2', 'all']:
            aci_output_handler.print_bridge_domains_l2(
                bridge_domains,
                title=True
            )

        if view in ['l3', 'all']:
            aci_output_handler.print_bridge_domains_l3(
                bridge_domains,
                title=True
            )

        if view in ['mcast', 'all']:
            aci_output_handler.print_bridge_domains_mcast(
                bridge_domains,
                title=True
            )

        if view in ['vrf', 'all']:
            aci_output_handler.print_bridge_domains_vrf(
                bridge_domains,
                title=True
            )

        if view == 'verbose':
            aci_output_handler.print_bridge_domains(
                bridge_domains
            )
            for bridge_domain in bridge_domains:
                aci_output_handler.print_bridge_domain(bridge_domain)

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
