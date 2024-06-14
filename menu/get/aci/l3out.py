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


@click.command("l3out")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--port", "controller_port", default=443, show_default=True, help="APIC Port")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--name", "l3out_name", default='', callback=validations.validate_apic_tenant_name, help="Filter by l3out name")
@click.option("--tenant", "tenant_name", default='', callback=validations.empty_string_to_none, help="Filter by tenant name")
@click.option("--vrf", "vrf_name", default='', callback=validations.empty_string_to_none, help="Filter by vrf name")
@click.option("--domain", "domain_name", default='', callback=validations.empty_string_to_none, help="Filter by domain name")
@click.option("--node", "node_id", default='', callback=validations.empty_string_to_none, help="Filter by node id")
@click.option("--fault", "fault", is_flag=True, show_default=True, default=False, help="Filter with faults")
@click.option("--severity", "fault_severity", type=click.Choice(['any', 'critical', 'major', 'minor', 'warning'], case_sensitive=False), default='any', show_default=True, help="Filter faults by severity")
@click.option("--when", "fault_when", default='7d', show_default=True, callback=validations.validate_timestamp_filter, help="Filter faults by timestamp")
@click.option("--view", "-v", default=['state'], help="[state|epg|bgp|eigrp|mpls|ospf|pim|fault|hfault|event|audit|diag|all]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--no-cache", "no_cache", is_flag=True, show_default=True, default=False, help="Disable cache")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_l3out_command(
        ctx,
        controller,
        controller_ip,
        controller_port,
        controller_username,
        controller_password,
        l3out_name,
        tenant_name,
        vrf_name,
        domain_name,
        node_id,
        fault,
        fault_severity,
        fault_when,
        view,
        output,
        no_cache,
        devel
        ):
    """Get aci l3out"""

    # iserver get aci l3out

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'state|epg|node|bgp|eigrp|mpls|ospf|pim|fault|hfault|event|audit|diag|all',
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

        l3out_filter = []
        hfault_filter = []
        event_filter = []
        audit_filter = []

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

        if 'bgp' in view:
            l3out_filter.append(
                'bgp:enabled'
            )

        if 'eigrp' in view:
            l3out_filter.append(
                'eigrp:enabled'
            )

        if 'ospf' in view:
            l3out_filter.append(
                'ospf:enabled'
            )

        if 'mpls' in view:
            l3out_filter.append(
                'mpls:enabled'
            )

        if 'pim' in view:
            l3out_filter.append(
                'pim:enabled'
            )

        if node_id is not None:
            l3out_filter.append(
                'node:%s' % (node_id)
            )

        if fault:
            l3out_filter.append(
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

        fault_info = False
        hfault_info = False
        event_info = False
        audit_info = False

        if 'fault' in view:
            fault_info = True

        if 'hfault' in view:
            hfault_info = True

        if 'event' in view:
            event_info = True

        if 'audit' in view:
            audit_info = True

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        l3outs = apic_handler.get_l3outs(
            l3out_filter=l3out_filter,
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

        for l3out in l3outs:
            if 'eventLog' in l3out:
                if l3out['eventLog'] is not None:
                    event = event + l3out['eventLog']

            if 'faultRecord' in l3out:
                if l3out['faultRecord'] is not None:
                    fault_record = fault_record + l3out['faultRecord']

            if 'faultInst' in l3out:
                if l3out['faultInst'] is not None:
                    fault_inst = fault_inst + l3out['faultInst']

            if 'auditLog' in l3out:
                if l3out['auditLog'] is not None:
                    audit = audit + l3out['auditLog']

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

        if 'state' in view:
            aci_output_handler.print_l3outs(
                l3outs,
                title=True
            )

        if 'bgp' in view:
            aci_output_handler.print_l3outs_bgp(
                l3outs,
                title=True
            )

        if 'eigrp' in view:
            aci_output_handler.print_l3outs_eigrp(
                l3outs,
                title=True
            )

        if 'ospf' in view:
            aci_output_handler.print_l3outs_ospf(
                l3outs,
                title=True
            )

        if 'pim' in view:
            aci_output_handler.print_l3outs_pim(
                l3outs,
                title=True
            )

        if 'mpls' in view:
            aci_output_handler.print_l3outs_mpls(
                l3outs,
                title=True
            )

        if 'epg' in view:
            aci_output_handler.print_l3outs_epg(
                l3outs,
                title=True
            )

        if 'fault' in view:
            aci_output_handler.print_l3outs_fault_inst(
                fault_inst,
                title=True
            )

        if 'hfault' in view:
            aci_output_handler.print_l3outs_fault_record(
                fault_record,
                when=fault_when,
                title=True
            )

        if 'event' in view:
            aci_output_handler.print_l3outs_event_logs(
                event,
                when=fault_when,
                title=True
            )

        if 'audit' in view:
            aci_output_handler.print_l3outs_audit_logs(
                audit,
                when=fault_when,
                title=True
            )

        ctx.my_output.default('Filter: name, tenant, vrf, domain, node, fault, severity, when', before_newline=True)
        ctx.my_output.default('View:   state (def), epg, bgp, eigrp, ospf, pim, mpls, fault, hfault, event, audit, diag, all')

        if l3outs is None or len(l3outs) == 0:
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
