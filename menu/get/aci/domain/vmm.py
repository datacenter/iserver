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
@click.option("--view", "-v", type=click.Choice(['default', 'prop', 'vc'], case_sensitive=False), multiple=True)
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
        view,
        output,
        no_cache,
        devel
        ):
    """Get aci domain vmm"""

    # iserver get aci domain vmm

    ctx.developer = devel
    ctx.output = output
    if len(view) == 0:
        view = ['default']

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
        if domain_name is not None:
            domain_filter.append(
                'name:%s' % (domain_name)
            )

        domains = apic_handler.get_domains_vmm(
            domain_filter=domain_filter,
            vlan_info=True
        )

        ctx.busy = False

        if domains is None or len(domains) == 0:
            raise NoResultExit

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

        if 'default' in view:
            aci_output_handler.print_domains_vmm(
                domains
            )

        if 'prop' in view:
            aci_output_handler.print_domains_vmm_prop(
                domains
            )

        if 'vc' in view:
            aci_output_handler.print_domains_vmm_vcenter(
                domains
            )

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
