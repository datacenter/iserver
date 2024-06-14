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


@click.command("vmm")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--port", "controller_port", default=443, show_default=True, help="APIC Port")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--name", "domain_name", default='', callback=validations.empty_string_to_none, help="Filter by domain name")
@click.option("--aaep", "aaep_name", default='', callback=validations.empty_string_to_none, help="Filter by aaep name")
@click.option("--pool", "pool_name", default='', callback=validations.empty_string_to_none, help="Filter by vlan pool name")
@click.option("--vlan", "vlan_id", default=-1, help="Filter by vlan id")
@click.option("--fault", "fault", is_flag=True, show_default=True, default=False, help="Filter with faults")
@click.option("--severity", "fault_severity", type=click.Choice(['any', 'critical', 'major', 'minor', 'warning'], case_sensitive=False), default='any', show_default=True, help="Filter faults by severity")
@click.option("--when", "fault_when", default='7d', show_default=True, callback=validations.validate_timestamp_filter, help="Filter faults by timestamp")
@click.option("--view", "-v", default=['state'], help="[state|prop|vc|epg|node|intf|vlan|reln|fault|hfault|event|audit|diag|all]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--no-cache", "no_cache", is_flag=True, show_default=True, default=False, help="Disable cache")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_domain_vmm_command(
        ctx,
        controller,
        controller_ip,
        controller_port,
        controller_username,
        controller_password,
        domain_name,
        aaep_name,
        pool_name,
        vlan_id,
        fault,
        fault_severity,
        fault_when,
        view,
        output,
        no_cache,
        devel
        ):
    """Get aci domain vmm"""

    # iserver get aci domain vmm

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'state|prop|vc|epg|node|intf|vlan|reln|fault|hfault|event|audit|diag|all',
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

        domain_filter = []
        hfault_filter = []
        event_filter = []
        audit_filter = []

        if domain_name is not None:
            domain_filter.append(
                'name:%s' % (domain_name)
            )

        if aaep_name is not None:
            domain_filter.append(
                'aaep:%s' % (aaep_name)
            )

        if pool_name is not None:
            domain_filter.append(
                'pool:%s' % (pool_name)
            )

        if vlan_id > 0:
            domain_filter.append(
                'vlan:%s' % (vlan_id)
            )

        if fault:
            domain_filter.append(
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

        vlan_info = False
        vlan_usage_info = False
        fault_info = False
        hfault_info = False
        event_info = False
        audit_info = False
        node_info = False
        intf_vlan_info = False
        controller_info = False

        if 'state' in view:
            vlan_info = True

        if 'epg' in view:
            vlan_info = True

        if 'node' in view:
            node_info = True

        if 'intf' in view:
            node_info = True

        if 'vlan' in view:
            vlan_info = True
            node_info = True
            intf_vlan_info = True

        if 'vc' in view:
            controller_info = True

        if 'fault' in view:
            fault_info = True

        if 'hfault' in view:
            hfault_info = True

        if 'event' in view:
            event_info = True

        if 'audit' in view:
            audit_info = True

        if output not in ['json']:
            if node_info:
                ctx.my_output.default(
                    '[INFO] Requires per-domain api call'
                )

            if intf_vlan_info:
                ctx.my_output.default(
                    '[INFO] Requires per-interface api call'
                )

            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        domains = apic_handler.get_domains_vmm(
            domain_filter=domain_filter,
            vlan_info=vlan_info,
            vlan_usage_info=vlan_usage_info,
            node_info=node_info,
            intf_vlan_info=intf_vlan_info,
            controller_info=controller_info,
            fault_info=fault_info,
            hfault_info=hfault_info,
            event_info=event_info,
            audit_info=audit_info,
            hfault_filter=hfault_filter,
            event_filter=event_filter,
            audit_filter=audit_filter
        )

        event = []
        fault_record = []
        fault_inst = []
        audit = []

        for domain in domains:
            if 'eventLog' in domain:
                if domain['eventLog'] is not None:
                    event = event + domain['eventLog']

            if 'faultRecord' in domain:
                if domain['faultRecord'] is not None:
                    fault_record = fault_record + domain['faultRecord']

            if 'faultInst' in domain:
                if domain['faultInst'] is not None:
                    fault_inst = fault_inst + domain['faultInst']

            if 'auditLog' in domain:
                if domain['auditLog'] is not None:
                    audit = audit + domain['auditLog']

        ctx.busy = False

        if output == 'json':
            ctx.log_prompt = False
            ctx.my_output.default(
                json.dumps(
                    domains,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(domains)

        if 'state' in view:
            aci_output_handler.print_domains_vmm(
                domains,
                title=True
            )

        if 'prop' in view:
            aci_output_handler.print_domains_vmm_prop(
                domains,
                title=True
            )

        if 'vc' in view:
            aci_output_handler.print_domains_vmm_vcenter(
                domains,
                title=True
            )

        if 'epg' in view:
            aci_output_handler.print_domains_vmm_epg(
                domains,
                title=True
            )

        if 'node' in view:
            aci_output_handler.print_domains_vmm_node(
                domains,
                title=True
            )

        if 'intf' in view:
            aci_output_handler.print_domains_vmm_interface(
                domains,
                title=True
            )

        if 'vlan' in view:
            aci_output_handler.print_domains_vmm_vlan(
                domains,
                title=True
            )

        if 'reln' in view:
            aci_output_handler.print_domains_vmm_reln(
                domains,
                title=True
            )

        if 'fault' in view:
            aci_output_handler.print_domains_vmm_fault_inst(
                fault_inst,
                title=True
            )

        if 'hfault' in view:
            aci_output_handler.print_domains_vmm_fault_record(
                fault_record,
                when=fault_when,
                title=True
            )

        if 'event' in view:
            aci_output_handler.print_domains_vmm_event_logs(
                event,
                when=fault_when,
                title=True
            )

        if 'audit' in view:
            aci_output_handler.print_domains_vmm_audit_logs(
                audit,
                when=fault_when,
                title=True
            )

        if domains is None or len(domains) == 0:
            raise ErrorExit

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
