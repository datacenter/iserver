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


@click.command("port")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--port", "controller_port", default=443, show_default=True, help="APIC Port")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Filter by name")
@click.option("--aaep", default='', callback=validations.empty_string_to_none, help="Filter by aaep")
@click.option("--policy", default='', callback=validations.empty_string_to_none, help="Filter by policy")
@click.option("--fault", "fault", is_flag=True, show_default=True, default=False, help="Filter with faults")
@click.option("--severity", "fault_severity", type=click.Choice(['any', 'critical', 'major', 'minor', 'warning'], case_sensitive=False), default='any', show_default=True, help="Filter faults by severity")
@click.option("--when", "fault_when", default='7d', show_default=True, callback=validations.validate_timestamp_filter, help="Filter faults by timestamp")
@click.option("--view", "-v", default=['state'], help="[state|aaep|node|intf|vlan|fault|hfault|event|audit|diag|all]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--no-cache", "no_cache", is_flag=True, show_default=True, default=False, help="Disable cache")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_pg_access_interface_port_command(
        ctx,
        controller,
        controller_ip,
        controller_port,
        controller_username,
        controller_password,
        name,
        aaep,
        policy,
        fault,
        fault_severity,
        fault_when,
        view,
        output,
        no_cache,
        devel
        ):
    """Get aci policy group interface port"""

    # iserver get aci pg intf port

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'state|aaep|node|intf|vlan|fault|hfault|event|audit|diag|all',
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

        policy_group_filter = []
        hfault_filter = []
        event_filter = []
        audit_filter = []

        if name is not None:
            policy_group_filter.append(
                'name:%s' % (name)
            )

        if aaep is not None:
            policy_group_filter.append(
                'aaep:%s' % (aaep)
            )

        if policy is not None:
            policy_group_filter.append(
                'policy:%s' % (policy)
            )

        if fault:
            policy_group_filter.append(
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

        aaep_info = False
        node_info = False
        vlan_info = False
        fault_info = False
        hfault_info = False
        event_info = False
        audit_info = False

        if 'aaep' in view:
            aaep_info = True

        if 'node' in view:
            aaep_info = True
            node_info = True

        if 'intf' in view:
            aaep_info = True
            node_info = True

        if 'vlan' in view:
            aaep_info = True
            node_info = True
            vlan_info = True

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
                ctx.my_output.default('[INFO] Requires per-group API call')
            if vlan_info:
                ctx.my_output.default('[INFO] Requires per-interface API call')

            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        policy_groups = apic_handler.get_policy_groups_access_interface_port(
            policy_group_filter=policy_group_filter,
            aaep_info=aaep_info,
            node_info=node_info,
            vlan_info=vlan_info,
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

        for policy_group in policy_groups:
            if 'eventLog' in policy_group:
                if policy_group['eventLog'] is not None:
                    event = event + policy_group['eventLog']

            if 'faultRecord' in policy_group:
                if policy_group['faultRecord'] is not None:
                    fault_record = fault_record + policy_group['faultRecord']

            if 'faultInst' in policy_group:
                if policy_group['faultInst'] is not None:
                    fault_inst = fault_inst + policy_group['faultInst']

            if 'auditLog' in policy_group:
                if policy_group['auditLog'] is not None:
                    audit = audit + policy_group['auditLog']

        ctx.busy = False

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    policy_groups,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(policy_groups)

        if 'state' in view:
            aci_output_handler.print_policy_groups_access_interface_port(
                policy_groups,
                title=True
            )

        if 'aaep' in view:
            aci_output_handler.print_policy_groups_access_interface_port_aaep(
                policy_groups,
                title=True
            )

        if 'node' in view:
            aci_output_handler.print_policy_groups_access_interface_port_node(
                policy_groups,
                title=True
            )

        if 'intf' in view:
            aci_output_handler.print_policy_groups_access_interface_port_interface(
                policy_groups,
                title=True
            )

        if 'vlan' in view:
            aci_output_handler.print_policy_groups_access_interface_port_vlan(
                policy_groups,
                title=True
            )

        if 'fault' in view:
            aci_output_handler.print_policy_groups_access_interface_port_fault_inst(
                fault_inst,
                title=True
            )

        if 'hfault' in view:
            aci_output_handler.print_policy_groups_access_interface_port_fault_record(
                fault_record,
                when=fault_when,
                title=True
            )

        if 'event' in view:
            aci_output_handler.print_policy_groups_access_interface_port_event_logs(
                event,
                when=fault_when,
                title=True
            )

        if 'audit' in view:
            aci_output_handler.print_policy_groups_access_interface_port_audit_logs(
                audit,
                when=fault_when,
                title=True
            )

        if policy_groups is None or len(policy_groups) == 0:
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
