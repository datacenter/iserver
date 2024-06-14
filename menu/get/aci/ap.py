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


@click.command("ap")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--port", "controller_port", default=443, show_default=True, help="APIC Port")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--name", "ap_name", default='', callback=validations.validate_apic_tenant_name, help="Filter by application profile name")
@click.option("--tenant", "tenant_name", default='', callback=validations.empty_string_to_none, help="Filter by tenant name")
@click.option("--epg", "epg_name", default='', callback=validations.empty_string_to_none, help="Filter by epg name")
@click.option("--fault", "fault", is_flag=True, show_default=True, default=False, help="Filter with faults")
@click.option("--severity", "fault_severity", type=click.Choice(['any', 'critical', 'major', 'minor', 'warning'], case_sensitive=False), default='any', show_default=True, help="Filter faults by severity")
@click.option("--when", "fault_when", default='7d', show_default=True, callback=validations.validate_timestamp_filter, help="Filter faults by timestamp")
@click.option("--view", "-v", default=['state'], help="[state|node|intf|fault|hfault|event|audit|diag|all]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--no-cache", "no_cache", is_flag=True, show_default=True, default=False, help="Disable cache")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_ap_command(
        ctx,
        controller,
        controller_ip,
        controller_port,
        controller_username,
        controller_password,
        ap_name,
        tenant_name,
        epg_name,
        fault,
        fault_severity,
        fault_when,
        view,
        output,
        no_cache,
        devel
        ):
    """Get aci application profile"""

    # iserver get aci ap

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'state|node|intf|fault|hfault|event|audit|diag|all',
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

        application_profile_filter = []
        hfault_filter = []
        event_filter = []
        audit_filter = []

        tenant_filtered = False
        if ap_name is not None:
            application_profile_filter.append(
                'name:%s' % (ap_name['name'])
            )

            if ap_name['tenant'] is not None:
                tenant_filtered = True
                application_profile_filter.append(
                    'tenant:%s' % (ap_name['tenant'])
                )

        if tenant_name is not None:
            if tenant_filtered:
                ctx.my_output.error(
                    'Define tenant in one place'
                )
                raise ErrorExit

            application_profile_filter.append(
                'tenant:%s' % (tenant_name)
            )

        if epg_name is not None:
            application_profile_filter.append(
                'epg:%s' % (epg_name)
            )

        if fault:
            application_profile_filter.append(
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

        node_info = False
        fault_info = False
        hfault_info = False
        event_info = False
        audit_info = False

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

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        application_profiles = apic_handler.get_application_profiles(
            application_profile_filter=application_profile_filter,
            epg_info=True,
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

        for application_profile in application_profiles:
            if 'eventLog' in application_profile:
                if application_profile['eventLog'] is not None:
                    event = event + application_profile['eventLog']

            if 'faultRecord' in application_profile:
                if application_profile['faultRecord'] is not None:
                    fault_record = fault_record + application_profile['faultRecord']

            if 'faultInst' in application_profile:
                if application_profile['faultInst'] is not None:
                    fault_inst = fault_inst + application_profile['faultInst']

            if 'auditLog' in application_profile:
                if application_profile['auditLog'] is not None:
                    audit = audit + application_profile['auditLog']

        ctx.busy = False

        if output == 'json':
            ctx.log_prompt = False
            ctx.my_output.default(
                json.dumps(
                    application_profiles,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(application_profiles)

        if 'state' in view:
            aci_output_handler.print_application_profiles(
                application_profiles,
                title=True
            )

        if 'node' in view:
            aci_output_handler.print_application_profiles_node(
                application_profiles,
                title=True
            )

        if 'intf' in view:
            aci_output_handler.print_application_profiles_interface(
                application_profiles,
                title=True
            )

        if 'fault' in view:
            aci_output_handler.print_application_profiles_fault_inst(
                fault_inst,
                title=True
            )

        if 'hfault' in view:
            aci_output_handler.print_application_profiles_fault_record(
                fault_record,
                when=fault_when,
                title=True
            )

        if 'event' in view:
            aci_output_handler.print_application_profiles_event_logs(
                event,
                when=fault_when,
                title=True
            )

        if 'audit' in view:
            aci_output_handler.print_application_profiles_audit_logs(
                audit,
                when=fault_when,
                title=True
            )

        if application_profiles is None or len(application_profiles) == 0:
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
