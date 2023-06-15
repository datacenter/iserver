import sys
import json
import threading
import traceback
import click

from lib.aci import output as aci_output
from lib import context

from menu import validations
from menu import progress


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("ep")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_any_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--port", "controller_port", default=443, show_default=True, help="APIC Port")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--mac", "mac_address_filter", default='', callback=validations.empty_string_to_none, help="MAC filter")
@click.option("--address", "ip_address_filter", default='', callback=validations.validate_ip_subnet, help="IP address filter")
@click.option("--subnet", "ip_subnet_filter", default='', callback=validations.validate_ip_subnet, help="IP subnet filter")
@click.option("--tenant", "tenant_filter", default='', callback=validations.empty_string_to_none, help="Tenant filter")
@click.option("--bd", "bd_filter", default='', callback=validations.empty_string_to_none, help="Bridge Domain filter")
@click.option("--epg", "epg_filter", default='', callback=validations.empty_string_to_none, help="EPG filter")
@click.option("--ap", "ap_filter", default='', callback=validations.empty_string_to_none, help="App filter")
@click.option("--vrf", "vrf_filter", default='', callback=validations.empty_string_to_none, help="VRF filter")
@click.option("--node", "node_filter", multiple=True, help="Node filter")
@click.option("--vmm", "vmm_filter", default='', callback=validations.empty_string_to_none, help="VMM filter")
@click.option("--hv", "hv_filter", default='', callback=validations.empty_string_to_none, help="Hypevisor filter")
@click.option("--vm", "vm_filter", default='', callback=validations.empty_string_to_none, help="VM filter")
@click.option("--xd", "xd_filter", default='', callback=validations.validate_aci_xd, help="Cross domain filter")
@click.option("--view", "-v", type=click.Choice(['default', 'vm', 'fabric'], case_sensitive=False), multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--no-cache", "no_cache", is_flag=True, show_default=True, default=False, help="Disable cache")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_ep_command(
        ctx,
        controller,
        controller_ip,
        controller_port,
        controller_username,
        controller_password,
        mac_address_filter,
        ip_address_filter,
        ip_subnet_filter,
        tenant_filter,
        bd_filter,
        epg_filter,
        ap_filter,
        vrf_filter,
        node_filter,
        vmm_filter,
        hv_filter,
        vm_filter,
        xd_filter,
        view,
        output,
        no_cache,
        devel
        ):
    """Get aci endpoints"""

    # iserver get aci endpoints

    ctx.developer = devel
    ctx.output = output
    if len(view) == 0:
        view = ['default']

    try:
        aci_output_handler = aci_output.ApicOutput(log_id=ctx.run_id)
        apic_handlers = validations.validate_apic_controllers(
            ctx,
            controller,
            controller_ip,
            controller_port,
            controller_username,
            controller_password,
            no_cache=no_cache
        )
        if apic_handlers is None:
            raise ErrorExit

        if len(apic_handlers) == 1:
            aci_output_handler.set_apic_off()

        xd_mac, xd_interface = validations.resolve_aci_xd(
            ctx,
            xd_filter,
            output
        )

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        vm_info = False
        fabric_info = False

        if 'vm' in view:
            vm_info = True

        if 'fabric' in view:
            fabric_info = True

        endpoint_filter = []

        if xd_mac is not None:
            for item in xd_mac:
                endpoint_filter.append(
                    'mac:%s' % (item)
                )

        if mac_address_filter is not None:
            endpoint_filter.append(
                'mac:%s' % (mac_address_filter)
            )

        if len(ip_address_filter) > 0:
            endpoint_filter.append(
                'ip:%s' % (ip_address_filter)
            )

        if len(ip_subnet_filter) > 0:
            endpoint_filter.append(
                'subnet:%s' % (ip_subnet_filter)
            )

        if tenant_filter is not None:
            endpoint_filter.append(
                'tenant:%s' % (tenant_filter)
            )

        if bd_filter is not None:
            endpoint_filter.append(
                'bd:%s' % (bd_filter)
            )

        if epg_filter is not None:
            endpoint_filter.append(
                'epg:%s' % (epg_filter)
            )

        if ap_filter is not None:
            endpoint_filter.append(
                'ap:%s' % (ap_filter)
            )

        if vrf_filter is not None:
            endpoint_filter.append(
                'vrf:%s' % (vrf_filter)
            )

        if len(node_filter) > 0:
            fabric_info = True
            endpoint_filter.append(
                'node:%s' % (','.join(node_filter))
            )

        if vmm_filter is not None:
            vm_info = True
            endpoint_filter.append(
                'vmm:%s' % (vmm_filter)
            )

        if hv_filter is not None:
            vm_info = True
            endpoint_filter.append(
                'hv:%s' % (hv_filter)
            )

        if vm_filter is not None:
            vm_info = True
            endpoint_filter.append(
                'vm:%s' % (vm_filter)
            )

        if vm_info:
            endpoint_filter.append(
                'vm-info:enabled'
            )

        endpoints = []
        ep_context = {}
        ep_context['apic'] = []
        ep_context['node'] = {}
        ep_context['interface'] = {}

        for apic_handler in apic_handlers:
            apic_endpoints = apic_handler['handler'].get_endpoints(
                endpoint_filter=endpoint_filter,
                vm_info=vm_info,
                fabric_info=fabric_info
            )
            for apic_endpoint in apic_endpoints:
                apic_endpoint['apic'] = apic_handler['name']

            endpoints = endpoints + apic_endpoints

            if fabric_info:
                if len(apic_endpoints) > 0:
                    ep_context['apic'].append(
                        apic_handler['name']
                    )
                    ep_context['node'][apic_handler['name']] = []
                    ep_context['interface'][apic_handler['name']] = []

                for endpoint in apic_endpoints:
                    for ep_fabric in endpoint['fabric']:
                        node_name = apic_handler['handler'].get_node_name(ep_fabric['node_id'])
                        if node_name not in ep_context['node'][apic_handler['name']]:
                            ep_context['node'][apic_handler['name']].append(
                                node_name
                            )

                        interface_name = 'pod-%s:node-%s:%s' % (
                            ep_fabric['pod_id'],
                            ep_fabric['node_id'],
                            ep_fabric['port_id']
                        )
                        if interface_name not in ep_context['interface'][apic_handler['name']]:
                            ep_context['interface'][apic_handler['name']].append(
                                interface_name
                            )

        ctx.busy = False

        if len(endpoints) == 0:
            raise NoResultExit

        if output == 'json':
            ctx.log_prompt = False
            ctx.my_output.default(
                json.dumps(
                    endpoints,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(endpoints)

        if 'default' in view:
            aci_output_handler.print_endpoints(
                endpoints
            )

        if 'vm' in view:
            aci_output_handler.print_endpoints_vmm(
                endpoints
            )

        if 'fabric' in view:
            aci_output_handler.print_endpoints_fabric(
                endpoints
            )

            if len(endpoints) > 0:
                context_handler = context.Context(log_id=ctx.run_id)
                success = context_handler.set(
                    'ep',
                    ep_context
                )
                if not success:
                    ctx.my_output.error('Failed to set interface context')
                else:
                    ctx.my_output.default('Interface context: ep')

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
