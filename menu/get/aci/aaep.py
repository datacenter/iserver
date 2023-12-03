import sys
import json
import threading
import traceback
import click

from menu import validations
from menu import progress

from lib.aci import output as aci_output


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("aaep")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--port", "controller_port", default=443, show_default=True, help="APIC Port")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--name", "aae_name", default='', callback=validations.empty_string_to_none, help="Filter by profile name")
@click.option("--fault", "fault", is_flag=True, show_default=True, default=False, help="Filter with faults")
@click.option("--severity", "fault_severity", type=click.Choice(['any', 'critical', 'major', 'minor', 'warning'], case_sensitive=False), default='any', show_default=True, help="Filter faults by severity")
@click.option("--when", "fault_when", default='7d', show_default=True, callback=validations.validate_timestamp_filter, help="Filter faults by timestamp")
@click.option("--view", "-v", default=['state'], help="[state|epg|node|intf|pol|fault|hfault|event|audit|diag|all]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--no-cache", "no_cache", is_flag=True, show_default=True, default=False, help="Disable cache")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_aaep_command(
        ctx,
        controller,
        controller_ip,
        controller_port,
        controller_username,
        controller_password,
        aae_name,
        fault,
        fault_severity,
        fault_when,
        view,
        output,
        no_cache,
        devel
        ):
    """Get aci aaep"""

    # iserver get aci aaep

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'state|epg|node|intf|pol|fault|hfault|event|audit|diag|all',
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

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        policy_global_aae_filter = []
        hfault_filter = []
        event_filter = []
        audit_filter = []

        if aae_name is not None:
            policy_global_aae_filter.append(
                'name:%s' % (aae_name)
            )

        if fault:
            policy_global_aae_filter.append(
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

        domain_info = False
        fault_info = False
        hfault_info = False
        event_info = False
        audit_info = False
        node_info = False

        if 'state' in view:
            domain_info = True

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

        aae = apic_handler.get_policy_global_aae(
            policy_global_aae_filter=policy_global_aae_filter,
            domain_info=domain_info,
            node_info=node_info,
            fault_info=fault_info,
            hfault_info=hfault_info,
            event_info=event_info,
            hfault_filter=hfault_filter,
            event_filter=event_filter,
            audit_info=audit_info,
            audit_filter=audit_filter
        )

        event = []
        fault_record = []
        fault_inst = []
        audit = []

        for item in aae:
            if 'eventLog' in item:
                if item['eventLog'] is not None:
                    event = event + item['eventLog']

            if 'faultRecord' in item:
                if item['faultRecord'] is not None:
                    fault_record = fault_record + item['faultRecord']

            if 'faultInst' in item:
                if item['faultInst'] is not None:
                    fault_inst = fault_inst + item['faultInst']

            if 'auditLog' in item:
                if item['auditLog'] is not None:
                    audit = audit + item['auditLog']

        ctx.busy = False

        if output == 'json':
            ctx.log_prompt = False
            ctx.my_output.default(
                json.dumps(
                    aae,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(aae)

        if 'state' in view:
            aci_output_handler.print_policies_global_aae(
                aae,
                title=True
            )

        if 'epg' in view:
            aci_output_handler.print_policies_global_aae_epg(
                aae,
                title=True
            )

        if 'pol' in view:
            aci_output_handler.print_policies_global_aae_reln(
                aae,
                title=True
            )

        if 'node' in view:
            aci_output_handler.print_policies_global_aae_node(
                aae,
                title=True
            )

        if 'intf' in view:
            aci_output_handler.print_policies_global_aae_interface(
                aae,
                title=True
            )

        if 'fault' in view:
            aci_output_handler.print_policies_global_aae_fault_inst(
                fault_inst,
                title=True
            )

        if 'hfault' in view:
            aci_output_handler.print_policies_global_aae_fault_record(
                fault_record,
                when=fault_when,
                title=True
            )

        if 'event' in view:
            aci_output_handler.print_policies_global_aae_event_logs(
                event,
                when=fault_when,
                title=True
            )

        if 'audit' in view:
            aci_output_handler.print_policies_global_aae_audit_logs(
                audit,
                when=fault_when,
                title=True
            )

        ctx.my_output.default('Filter: name, fault, severity, when', before_newline=True)
        ctx.my_output.default('View:   state (def), epg, node, intf, pol, fault, hfault, event, audit, diag, all')

        if aae is None or len(aae) == 0:
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
