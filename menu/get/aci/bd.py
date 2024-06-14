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
@click.option("--fault", "fault", is_flag=True, show_default=True, default=False, help="Filter with faults")
@click.option("--severity", "fault_severity", type=click.Choice(['any', 'critical', 'major', 'minor', 'warning'], case_sensitive=False), default='any', show_default=True, help="Filter faults by severity")
@click.option("--when", "fault_when", default='7d', show_default=True, callback=validations.validate_timestamp_filter, help="Filter faults by timestamp")
@click.option("--view", "-v", default=['state'], help="[state|l2|l3|mcast|vrf|node|intf|fault|hfault|event|audit|diag|all|verbose]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
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
        fault,
        fault_severity,
        fault_when,
        view,
        output,
        no_cache,
        devel
        ):
    """Get aci bridge domain"""

    # iserver get aci bd

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'state|l2|l3|mcast|vrf|node|intf|fault|hfault|event|audit|diag|all|verbose',
        'state',
        [
            'diag:fault,hfault,event,audit'
        ]
    )
    if view is None:
        sys.exit(1)

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

        bridge_domain_filter = []
        hfault_filter = []
        event_filter = []
        audit_filter = []

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

        if fault:
            bridge_domain_filter.append(
                'fault:any'
            )

        if fault_severity != 'any':
            hfault_filter.append(
                'severity:%s' % (fault_severity)
            )

        if fault_when is not None:
            hfault_filter.append(
                'timestamp:%s' % (fault_when)
            )
            event_filter.append(
                'timestamp:%s' % (fault_when)
            )
            audit_filter.append(
                'timestamp:%s' % (fault_when)
            )

        endpoint_info = True
        endpoint_vm_info = False
        endpoint_fabric_info = False
        snoop_info = False
        vrf_info = False
        epg_info = True
        node_info = False
        fault_info = False
        hfault_info = False
        event_info = False
        audit_info = False

        if 'vrf' in view:
            vrf_info = True
            epg_info = True

        if 'node' in view:
            node_info = True

        if 'intf' in view:
            node_info = True

        if 'fault' in view:
            fault_info = True

        if 'hfault' in view:
            hfault_info = True

        if 'event' in view:
            event_info = True

        if 'audit' in view:
            audit_info = True

        if 'verbose' in view:
            vrf_info = True
            epg_info = True
            endpoint_vm_info = True
            endpoint_fabric_info = True
            snoop_info = True

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        bridge_domains = apic_handler.get_bridge_domains(
            bridge_domain_filter=bridge_domain_filter,
            endpoint_info=endpoint_info,
            endpoint_vm_info=endpoint_vm_info,
            endpoint_fabric_info=endpoint_fabric_info,
            snoop_info=snoop_info,
            vrf_info=vrf_info,
            epg_info=epg_info,
            node_info=node_info,
            fault_info=fault_info,
            hfault_info=hfault_info,
            hfault_filter=hfault_filter,
            event_info=event_info,
            event_filter=event_filter,
            audit_info=audit_info,
            audit_filter=audit_filter
        )

        event = []
        fault_record = []
        fault_inst = []
        audit = []

        for bridge_domain in bridge_domains:
            if 'eventLog' in bridge_domain:
                if bridge_domain['eventLog'] is not None:
                    event = event + bridge_domain['eventLog']

            if 'faultRecord' in bridge_domain:
                if bridge_domain['faultRecord'] is not None:
                    fault_record = fault_record + bridge_domain['faultRecord']

            if 'faultInst' in bridge_domain:
                if bridge_domain['faultInst'] is not None:
                    fault_inst = fault_inst + bridge_domain['faultInst']

            if 'auditLog' in bridge_domain:
                if bridge_domain['auditLog'] is not None:
                    audit = audit + bridge_domain['auditLog']

        ctx.busy = False

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

        if 'state' in view:
            aci_output_handler.print_bridge_domains(
                bridge_domains,
                title=True
            )

        if 'l2' in view:
            aci_output_handler.print_bridge_domains_l2(
                bridge_domains,
                title=True
            )

        if 'l3' in view:
            aci_output_handler.print_bridge_domains_l3(
                bridge_domains,
                title=True
            )

        if 'mcast' in view:
            aci_output_handler.print_bridge_domains_mcast(
                bridge_domains,
                title=True
            )

        if 'vrf' in view:
            aci_output_handler.print_bridge_domains_vrf(
                bridge_domains,
                title=True
            )

        if 'node' in view:
            aci_output_handler.print_bridge_domains_node(
                bridge_domains,
                title=True
            )

        if 'intf' in view:
            aci_output_handler.print_bridge_domains_interface(
                bridge_domains,
                title=True
            )

        if 'fault' in view:
            aci_output_handler.print_bridge_domains_fault_inst(
                fault_inst,
                title=True
            )

        if 'hfault' in view:
            aci_output_handler.print_bridge_domains_fault_record(
                fault_record,
                when=fault_when,
                title=True
            )

        if 'event' in view:
            aci_output_handler.print_bridge_domains_event_logs(
                event,
                when=fault_when,
                title=True
            )

        if 'audit' in view:
            aci_output_handler.print_bridge_domains_audit_logs(
                audit,
                when=fault_when,
                title=True
            )

        if 'verbose' in view:
            aci_output_handler.print_bridge_domains(
                bridge_domains,
                title=True
            )
            for bridge_domain in bridge_domains:
                aci_output_handler.print_bridge_domain(bridge_domain)

        ctx.my_output.default('Filter: name, tenant, vrf, epg, address, subnet, l3out, fault, severity, when', before_newline=True)
        ctx.my_output.default('View:   state (def), l2, l3, mcast, vrf, node, intf, fault, hfault, event, audit, diag, all')

        if bridge_domains is None or len(bridge_domains) == 0:
            raise NoResultExit

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
