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


@click.command("l3out")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--name", "l3out_name", default='', callback=validations.validate_apic_tenant_name, help="Filter by l3out name")
@click.option("--tenant", "tenant_name", default='', callback=validations.empty_string_to_none, help="Filter by tenant name")
@click.option("--vrf", "vrf_name", default='', callback=validations.empty_string_to_none, help="Filter by vrf name")
@click.option("--domain", "domain_name", default='', callback=validations.empty_string_to_none, help="Filter by domain name")
@click.option("--node", "node_id", default='', callback=validations.empty_string_to_none, help="Filter by node id")
@click.option("--bgp", is_flag=True, show_default=True, default=False, help="Filter bgp protocol")
@click.option("--eigrp", is_flag=True, show_default=True, default=False, help="Filter eigrp protocol")
@click.option("--ospf", is_flag=True, show_default=True, default=False, help="Filter osfp protocol")
@click.option("--pim", is_flag=True, show_default=True, default=False, help="Filter pim enabled")
@click.option("--mpls", is_flag=True, show_default=True, default=False, help="Filter mpls enabled")
@click.option("--output", "-o", type=click.Choice(['default', 'json', 'epg', 'node'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_l3out_command(
        ctx,
        controller,
        controller_ip,
        controller_username,
        controller_password,
        l3out_name,
        tenant_name,
        vrf_name,
        domain_name,
        node_id,
        bgp,
        eigrp,
        ospf,
        pim,
        mpls,
        output,
        devel
        ):
    """Get aci l3out"""

    # iserver get aci l3out

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

        l3out_filter = []

        tenant_filtered = False
        if l3out_name is not None:
            l3out_filter.append(
                'name:%s' % (l3out_name['name'])
            )

            if l3out_name['tenant'] is not None:
                tenant_filtered = True
                l3out_filter.append(
                    'tenant:%s' % (l3out_name['tenant'])
                )

        if tenant_name is not None:
            if tenant_filtered:
                ctx.my_output.error(
                    'Define tenant in one place'
                )
                raise ErrorExit

            l3out_filter.append(
                'tenant:%s' % (tenant_name)
            )

        if vrf_name is not None:
            l3out_filter.append(
                'vrf:%s' % (vrf_name)
            )

        if domain_name is not None:
            l3out_filter.append(
                'domain:%s' % (domain_name)
            )

        if bgp:
            if output == 'default':
                output = 'bgp'
            l3out_filter.append(
                'bgp:enabled'
            )

        if eigrp:
            if output == 'default':
                output = 'eigrp'
            l3out_filter.append(
                'eigrp:enabled'
            )

        if ospf:
            if output == 'default':
                output = 'ospf'
            l3out_filter.append(
                'ospf:enabled'
            )

        if mpls:
            if output == 'default':
                output = 'mpls'
            l3out_filter.append(
                'mpls:enabled'
            )

        if pim:
            if output == 'default':
                output = 'pim'
            l3out_filter.append(
                'pim:enabled'
            )

        if node_id is not None:
            if output == 'default':
                output = 'node'
            l3out_filter.append(
                'node:%s' % (node_id)
            )

        l3outs = apic_handler.get_l3outs(
            l3out_filter=l3out_filter
        )

        ctx.busy = False

        if output == 'json':
            ctx.log_prompt = False
            ctx.my_output.default(
                json.dumps(
                    l3outs,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(l3outs)

        if output == 'default':
            aci_output_handler.print_l3outs(
                l3outs
            )

        if output == 'bgp':
            aci_output_handler.print_l3outs_bgp(
                l3outs
            )

        if output == 'eigrp':
            aci_output_handler.print_l3outs_eigrp(
                l3outs
            )

        if output == 'ospf':
            aci_output_handler.print_l3outs_ospf(
                l3outs
            )

        if output == 'pim':
            aci_output_handler.print_l3outs_pim(
                l3outs
            )

        if output == 'mpls':
            aci_output_handler.print_l3outs_mpls(
                l3outs
            )

        if output == 'epg':
            aci_output_handler.print_l3outs_epg(
                l3outs
            )

        if output == 'node':
            aci_output_handler.print_l3outs_node(
                l3outs
            )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
