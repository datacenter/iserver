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
@click.option("--pctag", default='', callback=validations.empty_string_to_none, help="Filter by pcTag")
@click.option("--vnid", default='', callback=validations.empty_string_to_none, help="Filter by vnid")
@click.option("--bd", "bd_name", default='', callback=validations.empty_string_to_none, help="Filter by bridge domain name")
@click.option("--epg", "epg_name", default='', callback=validations.empty_string_to_none, help="Filter by epg name")
@click.option("--address", "ip_address", default='', callback=validations.validate_ip, help="Filter by subnet with IP")
@click.option("--subnet", "ip_subnet", default='', callback=validations.validate_ip_subnet, help="Filter by subnet within subnet")
@click.option("--l3out", "l3out_name", default='', callback=validations.empty_string_to_none, help="Filter by l3out name")
@click.option("--fault", "fault", is_flag=True, show_default=True, default=False, help="Filter with faults")
@click.option("--severity", "fault_severity", type=click.Choice(['any', 'critical', 'major', 'minor', 'warning'], case_sensitive=False), default='any', show_default=True, help="Filter faults by severity")
@click.option("--when", "fault_when", default='7d', show_default=True, callback=validations.validate_timestamp_filter, help="Filter faults by timestamp")
@click.option("--view", "-v", default=['state'], help="[state|route|prop|node|intf|fault|hfault|event|audit|diag|all|verbose]", show_default=True, multiple=True)
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
        pctag,
        vnid,
        bd_name,
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
    """Get aci vrfs"""

    # iserver get aci vrfs

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'state|route|prop|node|intf|fault|hfault|event|audit|diag|all|verbose',
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

        vrf_filter = []
        hfault_filter = []
        event_filter = []
        audit_filter = []

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

        if pctag is not None:
            vrf_filter.append(
                'pctag:%s' % (pctag)
            )

        if vnid is not None:
            vrf_filter.append(
                'vnid:%s' % (vnid)
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

        if fault:
            vrf_filter.append(
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

        bridge_domain_info = True
        epg_info = True
        l3out_info = True
        route_info = False
        node_info = False
        fault_info = False
        hfault_info = False
        event_info = False
        audit_info = False

        if 'route' in view:
            route_info = True

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
            route_info = True

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        vrfs = apic_handler.get_vrfs(
            vrf_filter=vrf_filter,
            bridge_domain_info=bridge_domain_info,
            epg_info=epg_info,
            l3out_info=l3out_info,
            route_info=route_info,
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

        for vrf in vrfs:
            if 'eventLog' in vrf:
                if vrf['eventLog'] is not None:
                    event = event + vrf['eventLog']

            if 'faultRecord' in vrf:
                if vrf['faultRecord'] is not None:
                    fault_record = fault_record + vrf['faultRecord']

            if 'faultInst' in vrf:
                if vrf['faultInst'] is not None:
                    fault_inst = fault_inst + vrf['faultInst']

            if 'auditLog' in vrf:
                if vrf['auditLog'] is not None:
                    audit = audit + vrf['auditLog']

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

        if 'state' in view:
            aci_output_handler.print_vrfs(
                vrfs,
                title=True
            )

        if 'prop' in view:
            aci_output_handler.print_vrfs_properties(
                vrfs,
                title=True
            )

        if 'route' in view:
            for vrf in vrfs:
                aci_output_handler.print_vrf_v4_route(
                    vrf,
                    title=True
                )

        if 'node' in view:
            aci_output_handler.print_vrfs_node(
                vrfs,
                title=True
            )

        if 'intf' in view:
            aci_output_handler.print_vrfs_interface(
                vrfs,
                title=True
            )

        if 'fault' in view:
            aci_output_handler.print_vrfs_fault_inst(
                fault_inst,
                title=True
            )

        if 'hfault' in view:
            aci_output_handler.print_vrfs_fault_record(
                fault_record,
                when=fault_when,
                title=True
            )

        if 'event' in view:
            aci_output_handler.print_vrfs_event_logs(
                event,
                when=fault_when,
                title=True
            )

        if 'audit' in view:
            aci_output_handler.print_vrfs_audit_logs(
                audit,
                when=fault_when,
                title=True
            )

        if 'verbose' in view:
            aci_output_handler.print_vrfs(
                vrfs
            )
            for vrf in vrfs:
                aci_output_handler.print_vrf(vrf)

        if vrfs is None or len(vrfs) == 0:
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
