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


@click.command("aaa")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--port", "controller_port", default=443, show_default=True, help="APIC Port")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--name", "domain_name", default='', callback=validations.empty_string_to_none, help="Filter by pool name")
@click.option("--fault", "fault", is_flag=True, show_default=True, default=False, help="Filter with faults")
@click.option("--severity", "fault_severity", type=click.Choice(['any', 'critical', 'major', 'minor', 'warning'], case_sensitive=False), default='any', show_default=True, help="Filter faults by severity")
@click.option("--when", "fault_when", default='7d', show_default=True, callback=validations.validate_timestamp_filter, help="Filter faults by timestamp")
@click.option("--view", "-v", default=['state'], help="[state|event|fault|diag|all]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--no-cache", "no_cache", is_flag=True, show_default=True, default=False, help="Disable cache")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_domain_aaa_command(
        ctx,
        controller,
        controller_ip,
        controller_port,
        controller_username,
        controller_password,
        domain_name,
        fault,
        fault_severity,
        fault_when,
        view,
        output,
        no_cache,
        devel
        ):
    """Get aci domain aaa"""

    # iserver get aci domain aaa

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'state|event|fault|diag|all',
        'state',
        [
            'diag:event,fault'
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

        domain_filter = []
        fault_filter = []
        event_filter = []

        if domain_name is not None:
            domain_filter.append(
                'name:%s' % (domain_name)
            )

        if fault:
            domain_filter.append(
                'fault:any'
            )

        if fault_severity != 'any':
            fault_filter.append(
                'severity:%s' % (fault_severity)
            )

        if fault_when is not None:
            fault_filter.append(
                'timestamp:%s' % (fault_when)
            )
            event_filter.append(
                'timestamp:%s' % (fault_when)
            )

        fault_info = False
        event_info = False
        if 'fault' in view:
            fault_info = True

        if 'event' in view:
            event_info = True

        domains = apic_handler.get_domains_aaa(
            domain_filter=domain_filter,
            fault_info=fault_info,
            event_info=event_info,
            fault_filter=fault_filter,
            event_filter=event_filter
        )

        event = []
        fault_record = []
        fault_inst = []

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
            aci_output_handler.print_domains_aaa(
                domains,
                title=True
            )

        if 'event' in view:
            aci_output_handler.print_domains_aaa_event_logs(
                event,
                when=fault_when,
                title=True
            )

        if 'fault' in view:
            aci_output_handler.print_domains_aaa_fault_inst(
                fault_inst,
                title=True
            )

            aci_output_handler.print_domains_aaa_fault_record(
                fault_record,
                when=fault_when,
                title=True
            )

        if domains is None or len(domains) == 0:
            raise ErrorExit

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
