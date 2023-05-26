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


@click.command("bd")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--name", "bridge_domain_name", default='', callback=validations.validate_apic_tenant_name, help="Filter by bridge domain name")
@click.option("--tenant", "tenant_name", default='', callback=validations.empty_string_to_none, help="Filter by tenant name")
@click.option("--vrf", "vrf_name", default='', callback=validations.empty_string_to_none, help="Filter by vrf name")
@click.option("--epg", "epg_name", default='', callback=validations.empty_string_to_none, help="Filter by epg name")
@click.option("--ip", "ip_address", default='', callback=validations.validate_ip, help="Filter by subnet with IP")
@click.option("--subnet", "ip_subnet", default='', callback=validations.validate_ip_subnet, help="Filter by subnet within subnet")
@click.option("--l3out", "l3out_name", default='', callback=validations.empty_string_to_none, help="Filter by l3out name")
@click.option("--output", "-o", type=click.Choice(['default', 'json', 'verbose', 'l2', 'l3', 'mcast', 'vrf'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_bd_command(
        ctx,
        controller,
        controller_ip,
        controller_username,
        controller_password,
        bridge_domain_name,
        tenant_name,
        vrf_name,
        epg_name,
        ip_address,
        ip_subnet,
        l3out_name,
        output,
        devel
        ):
    """Get aci bridge domain"""

    # iserver get aci bd

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

        if output in ['default', 'json', 'l2', 'l3', 'mcast', 'epg']:
            bridge_domains = apic_handler.get_bridge_domains(
                bridge_domain_filter=bridge_domain_filter,
                endpoint_info=True,
                endpoint_vm_info=False,
                endpoint_fabric_info=False,
                snoop_info=False,
                vrf_info=False,
                epg_info=True
            )

        if output == 'vrf':
            bridge_domains = apic_handler.get_bridge_domains(
                bridge_domain_filter=bridge_domain_filter,
                endpoint_info=True,
                endpoint_vm_info=False,
                endpoint_fabric_info=False,
                snoop_info=False,
                vrf_info=True,
                epg_info=True
            )

        if output == 'verbose':
            bridge_domains = apic_handler.get_bridge_domains(
                bridge_domain_filter=bridge_domain_filter,
                endpoint_info=True,
                endpoint_vm_info=True,
                endpoint_fabric_info=True,
                snoop_info=True,
                vrf_info=True,
                epg_info=True
            )

        ctx.busy = False

        if bridge_domains is None:
            ctx.my_output.error('Failed to get bridge domains')
            raise ErrorExit

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

        if output == 'default':
            aci_output_handler.print_bridge_domains(
                bridge_domains
            )

        if output == 'verbose':
            aci_output_handler.print_bridge_domains(
                bridge_domains
            )
            for bridge_domain in bridge_domains:
                aci_output_handler.print_bridge_domain(bridge_domain)

        if output == 'vrf':
            aci_output_handler.print_bridge_domains_vrf(
                bridge_domains
            )

        if output == 'l2':
            aci_output_handler.print_bridge_domains_l2(
                bridge_domains
            )

        if output == 'l3':
            aci_output_handler.print_bridge_domains_l3(
                bridge_domains
            )

        if output == 'mcast':
            aci_output_handler.print_bridge_domains_mcast(
                bridge_domains
            )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
