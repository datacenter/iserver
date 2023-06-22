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


@click.command("fault")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--port", "controller_port", default=443, show_default=True, help="APIC Port")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--severity", "fault_severity", type=click.Choice(['any', 'critical', 'major', 'minor', 'warning'], case_sensitive=False), default='any', show_default=True, help="Filter by severity")
@click.option("--domain", "fault_domain", type=click.Choice(['any', 'access', 'apps', 'ext', 'fw', 'infra', 'mgmt', 'sec', 'tenant'], case_sensitive=False), default='any', show_default=True, help="Filter by domain")
@click.option("--type", "fault_type", type=click.Choice(['any', 'env', 'comm', 'config', 'oper'], case_sensitive=False), default='any', show_default=True, help="Filter by type")
@click.option("--code", "fault_code", default='', callback=validations.empty_string_to_none, help="Filter by code")
@click.option("--cause", "fault_cause", default='', callback=validations.empty_string_to_none, help="Filter by cause")
@click.option("--object", "fault_dn", default='', callback=validations.empty_string_to_none, help="Filter by object")
@click.option("--desc", "fault_description", default='', callback=validations.empty_string_to_none, help="Filter by description")
@click.option("--view", "-v", type=click.Choice(['summary', 'domain', 'type', 'verbose'], case_sensitive=False), multiple=False, default='summary', show_default=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--no-cache", "no_cache", is_flag=True, show_default=True, default=False, help="Disable cache")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_system_fault_command(
        ctx,
        controller,
        controller_ip,
        controller_port,
        controller_username,
        controller_password,
        fault_severity,
        fault_domain,
        fault_type,
        fault_code,
        fault_cause,
        fault_dn,
        fault_description,
        view,
        output,
        no_cache,
        devel
        ):
    """Get aci system fault"""

    # iserver get aci system fault

    ctx.developer = devel
    ctx.output = output

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

        system_fault_filter = []

        if fault_severity != 'any':
            system_fault_filter.append(
                'severity:%s' % (fault_severity)
            )

        if fault_domain != 'any':
            system_fault_filter.append(
                'domain:%s' % (fault_domain)
            )

        if fault_type != 'any':
            system_fault_filter.append(
                'type:%s' % (fault_type)
            )

        if fault_code is not None:
            system_fault_filter.append(
                'code:%s' % (fault_code)
            )

        if fault_cause is not None:
            system_fault_filter.append(
                'cause:%s' % (fault_cause)
            )

        if fault_dn is not None:
            system_fault_filter.append(
                'dn:%s' % (fault_dn)
            )

        if fault_description is not None:
            system_fault_filter.append(
                'description:%s' % (fault_description)
            )

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        if view == 'summary':
            faults = apic_handler.get_system_faults_summary(
                system_fault_filter=system_fault_filter
            )

        if view == 'domain':
            faults = apic_handler.get_system_faults_domain_count(
                system_fault_filter=system_fault_filter
            )

        if view == 'type':
            faults = apic_handler.get_system_faults_type_count(
                system_fault_filter=system_fault_filter
            )

        if view == 'verbose':
            faults = apic_handler.get_system_faults(
                system_fault_filter=system_fault_filter
            )

        ctx.busy = False

        if faults is None or len(faults) == 0:
            raise ErrorExit

        if output == 'json':
            ctx.log_prompt = False
            ctx.my_output.default(
                json.dumps(
                    faults,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(faults)

        if view == 'summary':
            aci_output_handler.print_system_faults_summary(
                faults,
                title=True
            )

        if view == 'domain':
            aci_output_handler.print_system_faults_domain_count(
                faults,
                title=True
            )

        if view == 'type':
            aci_output_handler.print_system_faults_type_count(
                faults,
                title=True
            )

        if view == 'verbose':
            aci_output_handler.print_system_faults(
                faults,
                title=True
            )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
